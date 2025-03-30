# model.py

# region 📦 Kütüphane ve Ayarlar
import pandas as pd
import numpy as np
import warnings

from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    mean_squared_error, r2_score
)
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

# endregion

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

