# model.py

# region 📦 Kütüphane ve Ayarlar
import pandas as pd
import numpy as np
import warnings
from io import StringIO


from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    mean_squared_error, r2_score
)
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import table


warnings.simplefilter(action='ignore', category=Warning)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# endregion

# region 📥 Veri Yükleme

df = pd.read_csv("Data Preparation/eurovision_master_clean.csv")
# endregion


# region 🔍 İlk Model: Sınıflandırma ile Finale Kalma Tahmini

df_train = df[(df["Year"] < 2025) & (df["Stage"].isin(["sf1", "sf2"]))].copy()
df_test = df[(df["Year"] == 2025) & (df["Stage"].isin(["sf1", "sf2"]))].copy()

features = [
    "Score_MyESC", "Rank_MyESC", "Odds_Rank",
    "PageRank_Score", "Weighted_Influence", "Scaled_Influence"
]

for col in features:
    mean_value = df_train[col].mean()
    df_train[col].fillna(mean_value, inplace=True)
    df_test[col].fillna(mean_value, inplace=True)

X_train = df_train[features]
y_train = df_train["Final_Qual"]
X_test = df_test[features]

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

df_test["Final_Qual_Pred"] = model.predict(X_test)
df_test["Final_Qual_Prob"] = model.predict_proba(X_test)[:, 1]

sf1_finalists = df_test[df_test["Stage"] == "sf1"].nlargest(10, "Final_Qual_Prob")
sf2_finalists = df_test[df_test["Stage"] == "sf2"].nlargest(10, "Final_Qual_Prob")

finalists_2025 = pd.concat([sf1_finalists, sf2_finalists]).sort_values(by="Stage")
print(finalists_2025[["Country", "Stage", "Final_Qual_Pred", "Final_Qual_Prob"]])

# Eğitim seti içi başarıyı görmek için:
y_test_pred = model.predict(X_train)
print("🎯 Confusion Matrix:")
print(confusion_matrix(y_train, y_test_pred))
print("\n📊 Classification Report:")
print(classification_report(y_train, y_test_pred))

# endregion

# region 🔁 Yıl Bazlı Cross-Test (LOYO)
years = df["Year"].unique()
years = years[years < 2025]
scores = []

for year in years:
    print(f"\n📅 Test yılı: {year}")

    test = df[(df["Year"] == year) & (df["Stage"].isin(["sf1", "sf2"]))].copy()
    X_test = test[features]
    y_test = test["Final_Qual"]

    train = df[(df["Year"] != year) & (df["Year"] < 2025) & (df["Stage"].isin(["sf1", "sf2"]))].copy()
    X_train = train[features]
    y_train = train["Final_Qual"]

    for col in features:
        mean_val = X_train[col].mean()
        X_train[col].fillna(mean_val, inplace=True)
        X_test[col].fillna(mean_val, inplace=True)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    scores.append(acc)
    print(classification_report(y_test, y_pred))

print(f"\n🚀 Ortalama Doğruluk: {np.mean(scores):.2f}")
# endregion

# region ⚙️ Feature Engineering

def grab_col_names(dataframe, cat_th=10, car_th=20):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtype == 'O']
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtype != 'O']
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and dataframe[col].dtype == 'O']

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in dataframe.columns if dataframe[col].dtype != 'O']
    num_cols = [col for col in num_cols if col not in num_but_cat]

    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)
for col in num_cols:
    df[col].fillna(df[col].mean(), inplace=True)

df_train = df[df["Year"] < 2025].copy()
df_test = df[df["Year"] == 2025].copy()

for dataset in [df_train, df_test]:
    dataset["Fan_Odds_Agreement"] = dataset["Score_MyESC"] * dataset["Odds_Rank"]
    dataset["Politik_Guc"] = dataset["Weighted_Influence"] * dataset["PageRank_Score"]
    dataset["Relative_Fan_Score"] = dataset["Score_MyESC"] / df_train["Score_MyESC"].max()
    dataset["Odds_Confidence"] = dataset["Odds_Rank"] - df_train["Odds_Rank"].mean()
    dataset["Composite_Influence"] = (dataset["Scaled_Influence"] + dataset["Odds_Rank"]) / 2
    dataset["Cluster_Country_Count"] = dataset.groupby(["Year", "Stage", "Cluster"])["Country"].transform("count")
    dataset["Cluster_Support_Count"] = dataset["Cluster_Country_Count"] - 1
    dataset["Countries_Per_Stage"] = dataset.groupby(["Year", "Stage"])["Country"].transform("count")
    dataset["Cluster_Support_Ratio"] = dataset["Cluster_Support_Count"] / dataset["Countries_Per_Stage"]

historical_features = df_train.copy()

historical_features["Final_Qual_Ratio_3y"] = historical_features.groupby("Country")["Final_Qual"].transform(lambda x: x.shift(1).rolling(3, min_periods=1).mean())
historical_features["ESC_Score_3y_avg"] = historical_features.groupby("Country")["ESC_Score"].transform(lambda x: x.shift(1).rolling(3, min_periods=1).mean())
historical_features["Odds_Delta"] = historical_features["Odds_Rank"] - historical_features.groupby("Country")["Odds_Rank"].shift(1)
historical_features["Fan_Momentum"] = historical_features["Score_MyESC"] - historical_features.groupby("Country")["Score_MyESC"].shift(1)
historical_features["Fan_ESC_Disagreement"] = historical_features["Rank_MyESC"] - historical_features["ESC_Rank"]

wins = historical_features[historical_features["ESC_Rank"] == 1].groupby("Country").size()
historical_features["Past_ESC_Wins"] = historical_features["Country"].map(wins).fillna(0)

top5_counts = historical_features[historical_features["ESC_Rank"] <= 5].groupby("Country").size()
historical_features["Past_Top5"] = historical_features["Country"].map(top5_counts).fillna(0)

historical_features = historical_features[[
    "Year", "Country", "Final_Qual_Ratio_3y", "ESC_Score_3y_avg",
    "Odds_Delta", "Fan_Momentum", "Fan_ESC_Disagreement",
    "Past_ESC_Wins", "Past_Top5"
]]

df_train = df_train.merge(historical_features, on=["Year", "Country"], how="left")
df_test = df_test.merge(historical_features.groupby("Country").last().reset_index(), on="Country", how="left")

df_train.fillna(0, inplace=True)
df_test.fillna(0, inplace=True)

cols_to_remove = ["Year", "Final_Qual", "ESC_Score", "ESC_Rank"]
num_cols = [col for col in num_cols if col not in cols_to_remove]

final_features = num_cols + [
    "Fan_Odds_Agreement", "Politik_Guc", "Relative_Fan_Score",
    "Odds_Confidence", "Composite_Influence", "Cluster_Support_Ratio",
    "Final_Qual_Ratio_3y", "ESC_Score_3y_avg", "Odds_Delta",
    "Fan_ESC_Disagreement", "Fan_Momentum", "Past_ESC_Wins", "Past_Top5"
]
# endregion

# region 🌟 Regresyon Modeli ile ESC Skoru Tahmini & Finalist Seçimi

X_train = df_train[final_features]
y_train_reg = df_train["ESC_Score"]
X_test = df_test[final_features]

reg_model = RandomForestRegressor(random_state=42)
reg_model.fit(X_train, y_train_reg)

train_preds = reg_model.predict(X_train)
r2 = r2_score(y_train_reg, train_preds)
rmse = mean_squared_error(y_train_reg, train_preds) ** 0.5
print(f"R2 Score: {r2:.2f}")
print(f"RMSE: {rmse:.2f}")

df_test["Predicted_ESC_Score"] = reg_model.predict(X_test)

# Normalize işlemi (Eurovision puan kuralları gereği)
sf1_n = df_test[df_test["Stage"] == "sf1"].shape[0]
sf2_n = df_test[df_test["Stage"] == "sf2"].shape[0]
sf1_total = sf1_n * 58
sf2_total = sf2_n * 58

sf1_sum = df_test[df_test["Stage"] == "sf1"]["Predicted_ESC_Score"].sum()
sf2_sum = df_test[df_test["Stage"] == "sf2"]["Predicted_ESC_Score"].sum()

df_test["Normalized_ESC_Score"] = df_test.apply(
    lambda row: row["Predicted_ESC_Score"] * (sf1_total / sf1_sum) if row["Stage"] == "sf1"
    else row["Predicted_ESC_Score"] * (sf2_total / sf2_sum), axis=1
)

# Integer puanlar & sıralama & finalist flag'ı

df_test["Normalized_ESC_Score"] = df_test["Normalized_ESC_Score"].round().astype(int)

sf1_result = df_test[df_test["Stage"] == "sf1"].copy().sort_values(by="Normalized_ESC_Score", ascending=False)
sf1_result["Rank"] = range(1, len(sf1_result) + 1)
sf1_result["Qualified"] = sf1_result["Rank"].apply(lambda x: 1 if x <= 10 else 0)

sf2_result = df_test[df_test["Stage"] == "sf2"].copy().sort_values(by="Normalized_ESC_Score", ascending=False)
sf2_result["Rank"] = range(1, len(sf2_result) + 1)
sf2_result["Qualified"] = sf2_result["Rank"].apply(lambda x: 1 if x <= 10 else 0)

print("\n📍 SF1 Tahmini Sonuçları:")
print(sf1_result[["Rank", "Country", "Normalized_ESC_Score", "Qualified"]])
print("\n📍 SF2 Tahmini Sonuçları:")
print(sf2_result[["Rank", "Country", "Normalized_ESC_Score", "Qualified"]])

sf1_qualifiers = sf1_result[["Rank", "Country", "Normalized_ESC_Score", "Qualified"]].nlargest(10, "Qualified")

sf2_qualifiers = sf2_result[["Rank", "Country", "Normalized_ESC_Score", "Qualified"]].nlargest(10, "Qualified")

# endregion

# region Yıl Bazlı Cross Test
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 2015-2024 yıllarını al
years_range = df[(df["Year"] < 2025)]["Year"].unique()

results = []

for year in years_range:
    # Test verisi (sadece o yıl ve Stage == 'f')
    test = df[(df["Year"] == year) & (df["Stage"] == "f")].copy()
    train = df[(df["Year"] != year) & (df["Year"] < 2025) & (df["Stage"] == "f")].copy()

    # Kullanılacak featurelar (target: ESC_Score)
    features = [
        "Score_MyESC", "Rank_MyESC", "Odds_Rank", "PageRank_Score",
        "Weighted_Influence", "Scaled_Influence"
    ]

    # Eksikleri doldur
    for col in features:
        mean_val = train[col].mean()
        train[col].fillna(mean_val, inplace=True)
        test[col].fillna(mean_val, inplace=True)

    X_train = train[features]
    y_train = train["ESC_Score"]
    X_test = test[features]
    y_test = test["ESC_Score"]

    # Model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5

    results.append({
        "Year": year,
        "RMSE": round(rmse, 2)
    })

results_df = pd.DataFrame(results)

print(f"LOYO Scores \n {results_df} \n Mean of RMSE: {results_df['RMSE'].mean():.2f}")

#endregion

#region Visualization


def show_table(data, title="Tablo", max_rows=15):
    fig, ax = plt.subplots(figsize=(10, 0.5 * len(data.head(max_rows))))
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_frame_on(False)
    table(ax, data.head(max_rows), loc='center')
    plt.title(title)
    plt.tight_layout()
    plt.show()

# Örnek kullanım:
show_table(sf1_result[["Rank", "Country", "Normalized_ESC_Score", "Qualified"]], "SF1 Tahmini Sonuçları")
show_table(sf2_result[["Rank", "Country", "Normalized_ESC_Score", "Qualified"]], "SF2 Tahmini Sonuçları")

#endregion


#region Data PreProcessing
df.to_csv("Data Preparation/eurovision_master_clean.csv")
df.tail(50)
df = df.iloc[:-20]

df.drop(columns=["Unnamed: 0"], inplace=True)
df.to_csv("Data Preparation/eurovision_master_clean.csv")

finalists_2025 = """,Unnamed: 0,Year,Stage,Country,Edition,Final_Qual,ESC_Score,ESC_Rank,Score_MyESC,Rank_MyESC,Odds_Rank,Cluster,Cluster_Name,PageRank_Score,Weighted_Influence,Scaled_Influence,Poll_Score_y
578,428,2025,f,Austria,2025f,,,,1.000000,1.0,0.998992,0.0,Western Core,0.020510,416.528993,0.624812,0.958177
579,429,2025,f,Finland,2025f,,,,0.861865,3.0,0.943548,1.0,Nordic & Baltic Bloc,0.020786,404.550154,0.599933,0.349617
580,430,2025,f,Israel,2025f,,,,0.067041,20.0,0.967742,0.0,Western Core,0.026724,530.771927,0.862083,0.343633
581,431,2025,f,Greece,2025f,,,,0.516603,7.0,0.967742,2.0,South-East Europe,0.022719,426.119195,0.647877,0.220864
582,432,2025,f,Malta,2025f,,,,0.633643,5.0,0.967742,0.0,Western Core,0.019820,343.721007,0.472909,0.137694
583,433,2025,f,Luxembourg,2025f,,,,0.048484,22.0,0.201613,0.0,Western Core,0.011746,202.220562,0.179716,0.045651
584,434,2025,f,Latvia,2025f,,,,0.060913,21.0,0.201613,1.0,Nordic & Baltic Bloc,0.019335,397.822557,0.585961,0.030480
585,435,2025,f,Armenia,2025f,,,,0.082231,16.0,0.201613,2.0,South-East Europe,0.017222,308.861401,0.401254,0.062578
586,436,2025,f,Australia,2025f,,,,0.285727,13.0,0.741935,1.0,Other,0.021047,422.180980,0.638560,0.171037
587,437,2025,f,Denmark,2025f,,,,0.099898,17.0,0.604839,1.0,Nordic & Baltic Bloc,0.015682,287.733302,0.360965,0.048613
588,438,2025,f,Sweden,2025f,,,,0.794214,4.0,0.985887,1.0,Nordic & Baltic Bloc,0.021985,439.105143,0.669429,0.361164
589,439,2025,f,Albania,2025f,,,,0.516603,7.0,0.414516,2.0,South-East Europe,0.015789,280.148420,0.351616,0.067280
590,440,2025,f,The Netherlands,2025f,,,,0.625929,6.0,0.967742,0.0,Western Core,0.022469,438.792622,0.668875,0.214505
591,441,2025,f,Ukraine,2025f,,,,0.285727,13.0,0.822581,1.0,Balkan & East,0.020053,365.871849,0.517692,0.080294
592,442,2025,f,Estonia,2025f,,,,0.550251,11.0,0.915323,1.0,Nordic & Baltic Bloc,0.018587,342.137911,0.468495,0.087004
593,443,2025,f,Cyprus,2025f,,,,0.157869,18.0,0.250000,2.0,South-East Europe,0.015083,276.491134,0.339780,0.028892
594,444,2025,f,Norway,2025f,,,,0.082231,16.0,0.750000,1.0,Nordic & Baltic Bloc,0.018268,319.864027,0.424432,0.036302
595,445,2025,f,Portugal,2025f,,,,0.070718,19.0,0.274194,2.0,South-East Europe,0.016871,299.679296,0.382611,0.027054
596,446,2025,f,Azerbaijan,2025f,,,,0.099898,17.0,0.233871,1.0,Balkan & East,0.015228,250.470140,0.293555,0.054707
597,447,2025,f,Belgium,2025f,,,,0.060913,21.0,0.750000,0.0,Western Core,0.016144,289.371975,0.364107,0.062460"""
finalistsdf2025 = pd.read_csv(StringIO(finalists_2025))
finalistsdf2025.drop(columns=["Unnamed: 0", "Unnamed: 0.1"], inplace=True)
df = pd.concat([df, finalistsdf2025], ignore_index=True)
df.to_csv("Data Preparation/eurovision_master_clean.csv")

columns_to_null = [
    "Final_Qual", "ESC_Score", "ESC_Rank",
    "Score_MyESC", "Rank_MyESC", "Odds_Rank", "Poll_Score_y"
]

# Şartlı olarak sadece 2025 final (f) verileri için null yap
df.loc[(df["Year"] == 2025) & (df["Stage"] == "f"), columns_to_null] = np.nan

# Tüm sütun adlarındaki boşlukları temizle
scaler = MinMaxScaler()
datamyesc2025 = """Year,Stage,Country,Scoreboard_Points
2025,f,Austria,232582
2025,f,Sweden,220041
2025,f,Finland,206231
2025,f,Albania,188547
2025,f,Malta,147672
2025,f,Norway,140565
2025,f,Greece,120533
2025,f,France,119222
2025,f,Poland,118817
2025,f,The Netherlands,115506
2025,f,Germany,113627
2025,f,Switzerland,81929
2025,f,Czechia,78142
2025,f,Spain,75582
2025,f,Lithuania,71865
2025,f,Australia,65888
2025,f,Estonia,64028
2025,f,Denmark,62247
2025,f,Ukraine,58520
2025,f,Belgium,56278
2025,f,Italy,54764
2025,f,Israel,54608
2025,f,Latvia,53439
2025,f,Luxembourg,51068
2025,f,San Marino,41819
2025,f,Cyprus,36759
2025,f,Iceland,33161
2025,f,Ireland,31754
2025,f,Portugal,29169
2025,f,Armenia,27496
2025,f,Azerbaijan,26747
2025,f,Montenegro,25982
2025,f,United Kingdom,24874
2025,f,Croatia,13264
2025,f,Slovenia,11794
2025,f,Serbia,8036
2025,f,Georgia,4780"""
data2025myesc_df = pd.read_csv(StringIO(datamyesc2025))
data2025myesc_df["Scoreboard_Points"] = scaler.fit_transform(data2025myesc_df[["Scoreboard_Points"]])
data2025myesc_df = data2025myesc_df.drop(columns=["Year", "Stage"])

data2025 = """Country,Year,Stage,Edition,Odd
Sweden,2025,f,2025 Final,3.0
Austria,2025,f,2025 Final,3.25
France,2025,f,2025 Final,6.5
Israel,2025,f,2025 Final,11.0
Netherlands,2025,f,2025 Final,15.0
Finland,2025,f,2025 Final,17.0
Estonia,2025,f,2025 Final,21.0
Belgium,2025,f,2025 Final,21.0
Albania,2025,f,2025 Final,34.0
Ukraine,2025,f,2025 Final,41.0
Malta,2025,f,2025 Final,41.0
Italy,2025,f,2025 Final,67.0
United Kingdom,2025,f,2025 Final,41.0
Czechia,2025,f,2025 Final,67.0
San Marino,2025,f,2025 Final,51.0
Lithuania,2025,f,2025 Final,81.0
Australia,2025,f,2025 Final,81.0
Greece,2025,f,2025 Final,67.0
Cyprus,2025,f,2025 Final,41.0
Ireland,2025,f,2025 Final,81.0
Germany,2025,f,2025 Final,101.0
Switzerland,2025,f,2025 Final,101.0
Poland,2025,f,2025 Final,101.0
Norway,2025,f,2025 Final,101.0
Slovenia,2025,f,2025 Final,101.0
Denmark,2025,f,2025 Final,201.0
Azerbaijan,2025,f,2025 Final,201.0
Spain,2025,f,2025 Final,101.0
Portugal,2025,f,2025 Final,251.0
Georgia,2025,f,2025 Final,251.0
Latvia,2025,f,2025 Final,201.0
Armenia,2025,f,2025 Final,251.0
Luxembourg,2025,f,2025 Final,201.0
Serbia,2025,f,2025 Final,251.0
Croatia,2025,f,2025 Final,251.0
Iceland,2025,f,2025 Final,251.0
Montenegro,2025,f,2025 Final,251.0
Sweden,2025,SF1,2025 Semi1,1.44
Estonia,2025,SF1,2025 Semi1,6.8
Netherlands,2025,SF1,2025 Semi1,8.6
Ukraine,2025,SF1,2025 Semi1,9.0
Poland,2025,SF1,2025 Semi1,14.0
Albania,2025,SF1,2025 Semi1,14.0
Belgium,2025,SF1,2025 Semi1,21.0
Cyprus,2025,SF1,2025 Semi1,14.0
Norway,2025,SF1,2025 Semi1,21.0
San Marino,2025,SF1,2025 Semi1,15.0
Croatia,2025,SF1,2025 Semi1,40.0
Azerbaijan,2025,SF1,2025 Semi1,4.0
Slovenia,2025,SF1,2025 Semi1,4.0
Iceland,2025,SF1,2025 Semi1,4.0
Portugal,2025,SF1,2025 Semi1,4.0
Israel,2025,SF2,2025 Semi2,1.71
Austria,2025,SF2,2025 Semi2,2.44
Finland,2025,SF2,2025 Semi2,3.25
Malta,2025,SF2,2025 Semi2,19.0
Greece,2025,SF2,2025 Semi2,20.0
Australia,2025,SF2,2025 Semi2,40.0
Czechia,2025,SF2,2025 Semi2,16.0
Lithuania,2025,SF2,2025 Semi2,32.0
Latvia,2025,SF2,2025 Semi2,3.0
Denmark,2025,SF2,2025 Semi2,20.0
Ireland,2025,SF2,2025 Semi2,30.0
Luxembourg,2025,SF2,2025 Semi2,81.0
Armenia,2025,SF2,2025 Semi2,50.0
Montenegro,2025,SF2,2025 Semi2,101.0
Serbia,2025,SF2,2025 Semi2,101.0
Georgia,2025,SF2,2025 Semi2,251.0
"""
data2025_df = pd.read_csv(StringIO(data2025))
df2025_final = data2025_df[data2025_df["Edition"] == "2025 Final"]
df2025_final = df2025_final.drop(columns=["Edition", "Year", "Stage"])
df2025_final["Odd"] = 1 - scaler.fit_transform(df2025_final[["Odd"]])

polldata2025 = """
Index, Country, Year, Score
361,Sweden,2025,1.0
362,Austria,2025,0.9581767571329158
363,Finland,2025,0.3496172581767571
364,Israel,2025,0.3436325678496869
365,Albania,2025,0.2940153096729297
366,France,2025,0.2434237995824635
367,Netherlands,2025,0.220250521920668
368,Malta,2025,0.1789839944328462
369,Estonia,2025,0.1717466945024356
370,Norway,2025,0.144258872651357
371,Greece,2025,0.1136395267919276
372,Poland,2025,0.1022964509394572
373,Spain,2025,0.0934585942936673
374,Italy,2025,0.0798886569241475
375,Lithuania,2025,0.0775922059846903
376,Germany,2025,0.0768267223382045
377,Ukraine,2025,0.0723034098816979
378,Czechia,2025,0.0629784272790535
379,San Marino,2025,0.0622129436325678
380,Australia,2025,0.0573416840640222
381,Cyprus,2025,0.0524008350730689
382,Switzerland,2025,0.0493389004871259
383,Luxembourg,2025,0.0456506610995128
384,Belgium,2025,0.0394572025052192
385,Portugal,2025,0.0393180236604036
386,United Kingdom,2025,0.0379958246346555
387,Montenegro,2025,0.0366736256089074
388,Iceland,2025,0.0340292275574112
389,Ireland,2025,0.0315935977731384
390,Latvia,2025,0.0304801670146137
391,Denmark,2025,0.0304105775922059
392,Serbia,2025,0.0141266527487821
393,Croatia,2025,0.0135699373695198
394,Azerbaijan,2025,0.0123173277661795
395,Armenia,2025,0.0110647181628392
396,Slovenia,2025,0.0009742519137091
397,Georgia,2025,0.0"""
poll2025df = pd.read_csv(StringIO(polldata2025))
poll2025df.columns
poll2025df = poll2025df.drop(columns=[" Year"])

# Öncelikle: veri eşleştirmesi için ülke isimleri normalize edilmeli
# (örneğin: "The Netherlands" ve "Netherlands")

poll2025df.columns = poll2025df.columns.str.strip()
df2025_final.columns = df2025_final.columns.str.strip()
data2025myesc_df.columns = data2025myesc_df.columns.str.strip()
# Score_MyESC & Rank_MyESC
myscore_map = data2025myesc_df.set_index("Country")["Scoreboard_Points"]
df.loc[(df["Year"] == 2025) & (df["Stage"] == "f"), "Score_MyESC"] = df.loc[
    (df["Year"] == 2025) & (df["Stage"] == "f"), "Country"
].map(myscore_map)

# Rank_MyESC hesapla: Score_MyESC'ye göre sıralama
rank_series = df.loc[(df["Year"] == 2025) & (df["Stage"] == "f")].sort_values(
    "Score_MyESC", ascending=False
).reset_index()

rank_map = {
    row["Country"]: rank + 1 for rank, row in rank_series.iterrows()
}
df.loc[(df["Year"] == 2025) & (df["Stage"] == "f"), "Rank_MyESC"] = df.loc[
    (df["Year"] == 2025) & (df["Stage"] == "f"), "Country"
].map(rank_map)

# Poll_Score_y
poll_map = poll2025df.set_index("Country")["Score"]
df.loc[(df["Year"] == 2025) & (df["Stage"] == "f"), "Poll_Score_y"] = df.loc[
    (df["Year"] == 2025) & (df["Stage"] == "f"), "Country"
].map(poll_map)

# Odds_Rank
odds_map = df2025_final.set_index("Country")["Odd"]
df.loc[(df["Year"] == 2025) & (df["Stage"] == "f"), "Odds_Rank"] = df.loc[
    (df["Year"] == 2025) & (df["Stage"] == "f"), "Country"
].map(odds_map)




#endregion



#region  🌟 Regresyon Modeli ile ESC Final Skoru Tahmini

def grab_col_names(dataframe, cat_th=10, car_th=20):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtype == 'O']
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtype != 'O']
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and dataframe[col].dtype == 'O']

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in dataframe.columns if dataframe[col].dtype != 'O']
    num_cols = [col for col in num_cols if col not in num_but_cat]

    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)
for col in num_cols:
    df[col].fillna(df[col].mean(), inplace=True)

# 2️⃣ EĞİTİM ve TEST AYIRIMI
df_train = df[df["Year"] < 2025].copy()
df_test = df[df["Year"] == 2025].copy()

# 3️⃣ FEATURE ENGINEERING
for dataset in [df_train, df_test]:
    dataset["Fan_Odds_Agreement"] = dataset["Score_MyESC"] * dataset["Odds_Rank"]
    dataset["Politik_Guc"] = dataset["Weighted_Influence"] * dataset["PageRank_Score"]
    dataset["Relative_Fan_Score"] = dataset["Score_MyESC"] / df_train["Score_MyESC"].max()
    dataset["Odds_Confidence"] = dataset["Odds_Rank"] - df_train["Odds_Rank"].mean()
    dataset["Composite_Influence"] = (dataset["Scaled_Influence"] + dataset["Odds_Rank"]) / 2
    dataset["Cluster_Country_Count"] = dataset.groupby(["Year", "Stage", "Cluster"])["Country"].transform("count")
    dataset["Cluster_Support_Count"] = dataset["Cluster_Country_Count"] - 1
    dataset["Countries_Per_Stage"] = dataset.groupby(["Year", "Stage"])["Country"].transform("count")
    dataset["Cluster_Support_Ratio"] = dataset["Cluster_Support_Count"] / dataset["Countries_Per_Stage"]

# 4️⃣ GEÇMİŞ BAŞARI ve MOMENTUM
historical_features = df_train.copy()
historical_features["Final_Qual_Ratio_3y"] = historical_features.groupby("Country")["Final_Qual"].transform(lambda x: x.shift(1).rolling(3, min_periods=1).mean())
historical_features["ESC_Score_3y_avg"] = historical_features.groupby("Country")["ESC_Score"].transform(lambda x: x.shift(1).rolling(3, min_periods=1).mean())
historical_features["Odds_Delta"] = historical_features["Odds_Rank"] - historical_features.groupby("Country")["Odds_Rank"].shift(1)
historical_features["Fan_Momentum"] = historical_features["Score_MyESC"] - historical_features.groupby("Country")["Score_MyESC"].shift(1)
historical_features["Fan_ESC_Disagreement"] = historical_features["Rank_MyESC"] - historical_features["ESC_Rank"]

# 5️⃣ GEÇMİŞ BAŞARI SAYILARI
wins = historical_features[historical_features["ESC_Rank"] == 1].groupby("Country").size()
historical_features["Past_ESC_Wins"] = historical_features["Country"].map(wins).fillna(0)
top5_counts = historical_features[historical_features["ESC_Rank"] <= 5].groupby("Country").size()
historical_features["Past_Top5"] = historical_features["Country"].map(top5_counts).fillna(0)

# Sadece gerekli kolonlar
historical_features = historical_features[[
    "Year", "Country", "Final_Qual_Ratio_3y", "ESC_Score_3y_avg",
    "Odds_Delta", "Fan_Momentum", "Fan_ESC_Disagreement",
    "Past_ESC_Wins", "Past_Top5"
]]

# Merge
df_train = df_train.merge(historical_features, on=["Year", "Country"], how="left")
df_test = df_test.merge(historical_features.groupby("Country").last().reset_index(), on="Country", how="left")
df_train.fillna(0, inplace=True)
df_test.fillna(0, inplace=True)

# 6️⃣ JÜRI ve HALK MODELİ

jury_features = [
    "Odds_Rank", "PageRank_Score", "Weighted_Influence",
    "Politik_Guc", "Composite_Influence",
    "Past_ESC_Wins", "ESC_Score_3y_avg"
]

televote_features = [
    "Score_MyESC", "Rank_MyESC", "Fan_Odds_Agreement",
    "Fan_Momentum", "Fan_ESC_Disagreement",
    "Relative_Fan_Score", "Cluster_Support_Ratio"
]

df_final = df_test[df_test["Stage"] == "f"].copy()
df_final[jury_features + televote_features] = df_final[jury_features + televote_features].fillna(0)

# 🎯 Jüri Modeli
jury_model = RandomForestRegressor(random_state=42)
jury_model.fit(df_train[jury_features], df_train["ESC_Score"])
df_final["Jury_Score"] = jury_model.predict(df_final[jury_features])

# 🎯 Televote Modeli
tel_model = RandomForestRegressor(random_state=42)
tel_model.fit(df_train[televote_features], df_train["ESC_Score"])
df_final["Televote_Score"] = tel_model.predict(df_final[televote_features])

# 🔗 ESC Score & Rank
df_final["ESC_Score"] = 0.5 * df_final["Jury_Score"] + 0.5 * df_final["Televote_Score"]
df_final = df_final.sort_values("ESC_Score", ascending=False).reset_index(drop=True)
df_final["Predicted_Rank"] = df_final.index + 1


# Finaldeki ülke sayısı
n_countries = len(df_final)
total_points = n_countries * 58

# Normalize etmek için toplam puanlara göre oranla
jury_sum = df_final["Jury_Score"].sum()
tel_sum = df_final["Televote_Score"].sum()

df_final["Jury_Score_Scaled"] = df_final["Jury_Score"] * (total_points / jury_sum)
df_final["Televote_Score_Scaled"] = df_final["Televote_Score"] * (total_points / tel_sum)

# Final ESC skoru (ortalama)
df_final["ESC_Score"] = (df_final["Jury_Score_Scaled"] + df_final["Televote_Score_Scaled"]).astype(int)
df_final["ESC_Score"] = df_final["ESC_Score"].round(2)

# Sıralama
df_final = df_final.sort_values("ESC_Score", ascending=False).reset_index(drop=True)
df_final["Predicted_Rank"] = df_final.index + 1

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 8))
sns.barplot(data=df_final.sort_values("ESC_Score", ascending=True),
            x="ESC_Score", y="Country", palette="viridis")
plt.title("🇪🇺 Eurovision 2025 – Tahmini Final Sıralaması (ESC Skoru)")
plt.xlabel("Toplam ESC Skoru")
plt.ylabel("Ülke")
plt.tight_layout()
plt.show()

# Son tabloyu göster
final_table = df_final[[
    "Predicted_Rank", "Country",
    "ESC_Score", "Jury_Score_Scaled", "Televote_Score_Scaled"
]]
print(final_table.to_string(index=False))
#endregion

