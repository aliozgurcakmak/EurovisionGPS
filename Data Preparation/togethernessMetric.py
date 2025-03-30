import pandas as pd
import numpy as np
pd.options.display.max_columns = 50
from sklearn.cluster import KMeans
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import community as community_louvain
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler

pd.set_option('display.expand_frame_repr', False)




#region Base Functions
def load_data(file_path):
    df = pd.read_excel(file_path)
    df.rename(columns={"Points      ": "Points"}, inplace=True)
    return df
def separate_votes(df):
    semi_final_votes = df[df['(semi-) final'] == 'sf']
    final_votes = df[df['(semi-) final'] == 'f']
    return semi_final_votes, final_votes
def country_points(df, country):
    country_points_all_years = df[df['To country'] == country].copy()
    return country_points_all_years
def top_voting_countries(df, country, round_type='f'):
    votes = df[(df['To country'] == country) & (df['(semi-) final'] == round_type)].copy()

    top_countries = (
        votes.groupby("From country", as_index=False)
        .agg({"Points": "sum"})
        .rename(columns={"Points": "Total Points"})
        .sort_values("Total Points", ascending=False)
    )

    top_countries['Years Together'] = top_countries['From country'].apply(
        lambda c: len(
            set(df[(df['From country'] == c) & (df['(semi-) final'] == round_type)]['Year']) &
            set(df[(df['To country'] == country) & (df['(semi-) final'] == round_type)]['Year'])
        )
    )

    top_countries["Points per Year"] = top_countries["Total Points"] / top_countries["Years Together"]

    top_countries['Adjusted Togetherness Score'] = (
            (top_countries['Total Points'] / top_countries['Years Together']) *
            np.log(top_countries['Years Together'] + 1)
    )

    top_countries = top_countries.sort_values(by="Adjusted Togetherness Score", ascending=False).reset_index(drop=True)
    return top_countries
def country_voting(df, country):
    votes_given = df[df['From country'] == country].copy()

    top_voted_countries = (
        votes_given.groupby('To country', as_index=False)
        .agg({'Points': 'sum'})
        .rename(columns={'Points': 'Total Points'})
        .sort_values(by='Total Points', ascending=False)
    )

    top_voted_countries['Years Together'] = top_voted_countries['To country'].apply(
        lambda c: len(
            set(df[(df['To country'] == c) & (df['(semi-) final'] == 'f')]['Year']) &
            set(df[(df['From country'] == country) & (df['(semi-) final'] == 'f')]['Year'])
        )
    )

    top_voted_countries["Points per Year"] = top_voted_countries["Total Points"] / top_voted_countries["Years Together"]

    top_voted_countries['Adjusted Togetherness Score'] = (
            (top_voted_countries['Total Points'] / top_voted_countries['Years Together']) *
            np.log(top_voted_countries['Years Together'] + 1)
    )

    top_voted_countries = top_voted_countries.sort_values(by="Adjusted Togetherness Score",
                                                          ascending=False).reset_index(drop=True)
    return top_voted_countries
def best_friend_of_country(df, country):
    top_voters = top_voting_countries(df, country)
    top_voted = country_voting(df, country)

    togetherness = pd.merge(
        top_voters[['From country', 'Adjusted Togetherness Score']],
        top_voted[['To country', 'Adjusted Togetherness Score']],
        left_on='From country',
        right_on='To country',
        how='outer'
    )

    togetherness.columns = ['Country', 'Score_From_Others', 'Country_2', 'Score_From_Country']
    togetherness = togetherness.drop('Country_2', axis=1)
    togetherness = togetherness.fillna(0)

    togetherness['Relationship_Score'] = np.sqrt(togetherness['Score_From_Others'] * togetherness['Score_From_Country'])
    togetherness = togetherness.sort_values('Relationship_Score', ascending=False).reset_index(drop=True)

    return togetherness

df = load_data("Data Preparation/Datasets/eurovision_song_contest_1975_2024.xlsx")
unwanted_countries = ['Andorra', 'Morocco', 'Slovakia', 'O']
df = df[
    ~df['From country'].isin(unwanted_countries) &  # From country için filtreleme
    ~df['To country'].isin(unwanted_countries)  # To country için filtreleme
    ]

df = df.dropna()

replace_map = {
    'The Netherands': 'The Netherlands',
    'Netherlands': 'The Netherlands',
    'Macedonia': 'North Macedonia'
}
df['From country'] = df['From country'].replace(replace_map)
df['To country'] = df['To country'].replace(replace_map)

print(df.head())
best_friend_of_country(df, 'Australia').head(5)

def calculate_all_togetherness_scores(df):
    countries = df["From country"].unique()
    results = []

    for country in countries:
        temp_df = best_friend_of_country(df, country)
        temp_df["To Country"] = country
        results.append(temp_df)

    full_togetherness_df = pd.concat(results, ignore_index=True)
    return full_togetherness_df
full_togetherness_df = calculate_all_togetherness_scores(df)
full_togetherness_df.to_csv("Data Preparation/Datasets/full_togetherness_df.csv")
full_togetherness_df["Relationship_Score"].max()
general_togetherness = full_togetherness_df.groupby("Country")["Relationship_Score"].mean().reset_index()
df = full_togetherness_df

def outlier_thresholds(dataframe, col_name, q1=0.05, q3=0.95):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit
def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False
def replace_with_thresholds(dataframe, variable, q1=0.01, q3=0.99):
    low_limit, up_limit = outlier_thresholds(dataframe, variable, q1, q3)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

check_outlier(full_togetherness_df, "Relationship_Score")

replace_with_thresholds(full_togetherness_df, "Relationship_Score")



#endregion



#region KNN Analysis

df = full_togetherness_df
df = df[df['Country'] != 0]

X = df[["Score_From_Others", "Score_From_Country", "Relationship_Score"]].copy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []
silhouette_scores = []
k_values = range(2, 10)  # Küme sayısını belirle

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)  # Küme içi hata kareler toplamı
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Elbow grafiği: Dirseğe göre ideal küme sayısı.
plt.figure(figsize=(10, 5))
plt.plot(k_values, wcss, marker="o", linestyle="-")
plt.xlabel("Küme Sayısı (k)")
plt.ylabel("WCSS (Küme İçi Hata Kareler Toplamı)")
plt.title("Elbow Yöntemi ile En İyi K Değerini Belirleme")
plt.show()

#endregion


#region Network

# Louvain için grafiği oluştur
G = nx.Graph()
for index, row in df.iterrows():
    G.add_edge(row["Country"], row["To Country"], weight=row["Relationship_Score"])

# Louvain algoritmasını uygula
partition = community_louvain.best_partition(G, weight="weight", resolution=1.05)


# Sonuçları dataframe'e aktar
df_clusters = pd.DataFrame(list(partition.items()), columns=["Country", "Cluster"])

# Küme dağılımını göster
print(df_clusters["Cluster"].value_counts())

# Grafiği görselleştir
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=list(partition.values()), cmap=plt.cm.Set1, node_size=50, with_labels=True)
plt.show()
# Her kümedeki ülkeleri listele
clustered_countries = df_clusters.groupby("Cluster")["Country"].apply(list)

# Sonuçları göster
for cluster_id, countries in clustered_countries.items():
    print(f"Küme {cluster_id}: {countries}")
    print("-" * 40)

#endregion

#region Name
# Küme isimleri sözlüğü
cluster_names = {
    0: "Western Core",
    1: "Nordic & Baltic Bloc",
    2: "Eastern European Bloc",
    3: "Balkan Brotherhood"
}

# DataFrame'e ekleyelim
df_clusters["Cluster_Name"] = df_clusters["Cluster"].map(cluster_names)

# Sonuçları CSV olarak kaydet
df_clusters.to_csv("final_network_clusters_named.csv", index=False)
#endregion

#region Network Member Types

# PageRank hesapla
pagerank_scores = nx.pagerank(G, weight="weight")

df_clusters["PageRank_Score"] = df_clusters["Country"].map(pagerank_scores)
df_clusters.sort_values(by=["Cluster_Name", "PageRank_Score"], ascending=[True, False])


df_clusters["Weighted_Influence"] = df_clusters["Country"].map(
    lambda x: df[df["Country"] == x]["Relationship_Score"].sum()
)

df_clusters.sort_values(by=["Weighted_Influence"], ascending=[ False])

df_clusters.to_excel("Data Preparation/Datasets/final_network_clusters_named.xlsx")

df_clusters = pd.read_excel("Data Preparation/LastSets/final_network_clusters_named.xlsx")

scaler = MinMaxScaler()
df_clusters["Scaled_Influence"] = scaler.fit_transform(df_clusters["Weighted_Influence"].values.reshape(-1, 1))

df_clusters.to_csv("Data Preparation/LastSets/final_network_clusters_named.csv", index=False)

