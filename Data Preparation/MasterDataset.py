import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from io import StringIO

#region Data Loading
results = pd.read_csv("Data Preparation/LastSets/Results.csv")
myesc = pd.read_csv("Data Preparation/LastSets/MyESC.csv")
odds = pd.read_csv("Data Preparation/LastSets/OddDatas.csv")
polls = pd.read_csv("Data Preparation/LastSets/all_polls.csv")
clusters = pd.read_csv("Data Preparation/LastSets/final_network_clusters_named.csv")
#endregion

#region Data Preparation
polls

polls.drop(columns=['Unnamed: 0'], inplace=True)
polls.to_csv("Data Preparation/LastSets/all_polls.csv")
polls["Eurovision_World_Points_Scaled"] = polls.groupby("Year")["Eurovision_World_Points"].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)
polls.drop(columns=["Eurovision_World_Points"], inplace=True)
polls.to_csv("Data Preparation/LastSets/all_polls.csv")

results

myesc
myesc.sort_values(by="Year", ascending=False)
myesc2024data = """,Year,Stage,Rank,Country,Score,Edition
484,2024,f,1,Switzerland,39834,2024f
485,2024,f,2,Croatia,37061,2024f
486,2024,f,3,Ukraine,32102,2024f
487,2024,f,4,Ireland,28228,2024f
488,2024,f,5,Italy,25290,2024f
489,2024,f,6,France,21409,2024f
490,2024,f,7,Greece,17406,2024f
491,2024,f,8,Lithuania,16770,2024f
492,2024,f,9,Norway,14184,2024f
493,2024,f,10,Austria,12608,2024f
494,2024,f,11,Georgia,12564,2024f
495,2024,f,12,Israel,12461,2024f
496,2024,f,13,Spain,10750,2024f
497,2024,f,14,Sweden,10382,2024f
498,2024,f,15,Portugal,9958,2024f
499,2024,f,16,Armenia,9724,2024f
500,2024,f,17,Slovenia,8582,2024f
501,2024,f,18,United Kingdom,6667,2024f
502,2024,f,19,Luxembourg,6240,2024f
503,2024,f,20,Cyprus,6166,2024f
504,2024,f,21,Serbia,5889,2024f
505,2024,f,22,Estonia,5850,2024f
506,2024,f,23,Finland,5522,2024f
507,2024,f,24,Germany,4321,2024f
508,2024,f,25,Latvia,2931,2024f
509,2024,sf1,1,Ukraine,64807,2024sf1
510,2024,sf1,2,Croatia,63303,2024sf1
511,2024,sf1,3,Lithuania,53970,2024sf1
512,2024,sf1,4,Ireland,47442,2024sf1
513,2024,sf1,5,Slovenia,33934,2024sf1
514,2024,sf1,6,Serbia,32250,2024sf1
515,2024,sf1,7,Portugal,31828,2024sf1
516,2024,sf1,8,Cyprus,30165,2024sf1
517,2024,sf1,9,Luxembourg,28942,2024sf1
518,2024,sf1,10,Poland,22927,2024sf1
519,2024,sf1,11,Finland,20044,2024sf1
520,2024,sf1,12,Australia,15281,2024sf1
521,2024,sf1,13,Azerbaijan,12158,2024sf1
522,2024,sf1,14,Moldova,7404,2024sf1
523,2024,sf1,15,Iceland,6853,2024sf1
524,2024,sf2,1,Switzerland,64550,2024sf2
525,2024,sf2,2,Netherlands,46810,2024sf2
526,2024,sf2,3,Greece,42926,2024sf2
527,2024,sf2,4,Austria,40824,2024sf2
528,2024,sf2,5,Norway,40110,2024sf2
529,2024,sf2,6,Georgia,33321,2024sf2
530,2024,sf2,7,Belgium,32641,2024sf2
531,2024,sf2,8,Armenia,29919,2024sf2
532,2024,sf2,9,Israel,24753,2024sf2
533,2024,sf2,10,Malta,21448,2024sf2
534,2024,sf2,11,Czechia,20688,2024sf2
535,2024,sf2,12,Denmark,19156,2024sf2
536,2024,sf2,13,Estonia,18086,2024sf2
537,2024,sf2,14,Latvia,10915,2024sf2
538,2024,sf2,15,San Marino,10679,2024sf2
539,2024,sf2,16,Albania,7058,2024sf2
"""
myesc2024df = pd.read_csv(StringIO(myesc2024data))
myesc2024df["Score"] = myesc2024df.groupby("Edition")["Score"].transform(lambda x: (x - x.min()) / (x.max() - x.min()))
myesc2025data = """Index,Year,Stage,Rank,Country,Score,Edition
540,2025,sf1,1,Sweden,220041,2025sf1
541,2025,sf1,2,Albania,188547,2025sf1
542,2025,sf1,3,Norway,140565,2025sf1
543,2025,sf1,4,Poland,118817,2025sf1
544,2025,sf1,5,Netherlands,115506,2025sf1
545,2025,sf1,6,Belgium,56278,2025sf1
546,2025,sf1,7,Estonia,64028,2025sf1
547,2025,sf1,8,Ukraine,58520,2025sf1
548,2025,sf1,9,Portugal,29169,2025sf1
549,2025,sf1,10,Azerbaijan,26747,2025sf1
550,2025,sf1,11,San Marino,41819,2025sf1
551,2025,sf1,12,Iceland,33161,2025sf1
552,2025,sf1,13,Croatia,13264,2025sf1
553,2025,sf1,14,Slovenia,11794,2025sf1
554,2025,sf1,15,Cyprus,36759,2025sf1
555,2025,sf2,1,Austria,232582,2025sf2
556,2025,sf2,2,Finland,206231,2025sf2
557,2025,sf2,3,Malta,147672,2025sf2
558,2025,sf2,4,Greece,120533,2025sf2
559,2025,sf2,5,Lithuania,71865,2025sf2
560,2025,sf2,6,Australia,65888,2025sf2
561,2025,sf2,7,Denmark,62247,2025sf2
562,2025,sf2,8,Israel,54608,2025sf2
563,2025,sf2,9,Latvia,53439,2025sf2
564,2025,sf2,10,Luxembourg,51068,2025sf2
565,2025,sf2,11,Czechia,78142,2025sf2
566,2025,sf2,12,Armenia,27496,2025sf2
567,2025,sf2,13,Ireland,31754,2025sf2
568,2025,sf2,14,Montenegro,25982,2025sf2
569,2025,sf2,15,Serbia,8036,2025sf2
570,2025,sf2,16,Georgia,4780,2025sf2
571,2025,f,1,France,119222,2025f
572,2025,f,2,Germany,113627,2025f
573,2025,f,3,Italy,54764,2025f
574,2025,f,4,Spain,75582,2025f
575,2025,f,5,United Kingdom,24874,2025f
576,2025,f,6,Switzerland,81929,2025f
577,2025,f,,,,2025f
578,2025,f,,,,2025f
579,2025,f,,,,2025f
580,2025,f,,,,2025f
581,2025,f,,,,2025f
582,2025,f,,,,2025f
583,2025,f,,,,2025f
584,2025,f,,,,2025f
585,2025,f,,,,2025f
586,2025,f,,,,2025f
587,2025,f,,,,2025f
588,2025,f,,,,2025f
589,2025,f,,,,2025f
590,2025,f,,,,2025f
591,2025,f,,,,2025f
592,2025,f,,,,2025f
593,2025,f,,,,2025f
594,2025,f,,,,2025f
595,2025,f,,,,2025f
596,2025,f,,,,2025f
"""
myesc2025df = pd.read_csv(StringIO(myesc2025data))
myesc2025df["Score"] = myesc2025df.groupby("Edition")["Score"].transform(lambda x: (x - x.min()) / (x.max() - x.min()))

myesc20242025df = pd.concat([myesc2024df, myesc2025df])
myesc = pd.concat([myesc, myesc20242025df])
myesc.reset_index(drop=True, inplace=True)
myesc.drop(columns=["Unnamed: 0"], inplace=True)
myesc.drop(columns=["Index"], inplace=True)
myesc.to_csv("Data Preparation/LastSets/MyESC.csv")

polls.drop(columns=["Unnamed: 0"], inplace=True)
polls.to_csv("Data Preparation/LastSets/all_polls.csv")
clusters.drop(columns=["Unnamed: 0"], inplace=True)
clusters.to_csv("Data Preparation/LastSets/final_network_clusters_named.csv")
#endregion

#region Master Dataset

df = results.copy()

df["Final_Qual"] = df.apply(
    lambda row: 1 if (row["Stage"] in ["sf1", "sf2"] and row["Rank"] <= 10) or (row["Stage"] == "f") else 0,
    axis=1
)
df.head(50)

df["key"] = df["Country"].astype(str) + "_" + df["Edition"]
myesc["key"] = myesc["Country"].astype(str) + "_" + myesc["Edition"]
odds["key"] = odds["Country"].astype(str) + "_" + odds["Edition"]
polls["key"] = polls["Country"].astype(str) + "_" + polls["Year"].astype(str)  # çünkü onda Edition yok
clusters["key"] = clusters["Country"]  # çünkü yıl/sahne yok → sadece ülkeye göre sabit

df = df.merge(myesc[["key", "Score", "Rank"]], on="key", how="left", suffixes=('', '_MyESC'))
df = df.merge(odds[["key", "Odd"]], on="key", how="left")
myesc["key"] = myesc["Country"].astype(str) + "_" + myesc["Edition"]

df = df.merge(clusters.drop(columns=["Unnamed: 0"]), on="Country", how="left")
df["key"] = df["Country"].astype(str) + "_" + df["Edition"]


# 1. MyESC
myesc["key"] = myesc["Country"].astype(str) + "_" + myesc["Edition"]
df = df.merge(
    myesc[["key", "Score", "Rank"]],
    on="key", how="left"
)
df.rename(columns={"Score": "MyESC_Score", "Rank": "MyESC_Rank"}, inplace=True)

# 2. Odds
odds["key"] = odds["Country"].astype(str) + "_" + odds["Edition"]
df = df.merge(
    odds[["key", "Odd"]],
    on="key", how="left"
)
df.rename(columns={"Odd": "Odds_Rank"}, inplace=True)

# 3. all_polls
polls["key"] = polls["Country"].astype(str) + "_" + polls["Year"].astype(str)
df = df.merge(
    polls[["key", "EurovisionWorld_Points"]],
    on="key", how="left"
)
df.rename(columns={"EurovisionWorld_Points": "Poll_Score"}, inplace=True)

# 4. Clusters (sadece Country ile)
if "Unnamed: 0" in clusters.columns:
    clusters.drop(columns=["Unnamed: 0"], inplace=True)
df = df.merge(
    clusters,
    on="Country", how="left"
)

df.to_csv("Data Preparation/eurovision_master_clean.csv", index=False)



df_clean = df[[
    "Year", "Stage", "Country", "Edition", "Final_Qual",
    "Score_x", "Rank_x",  # Orijinal Eurovision sonuçları
    "Score_MyESC", "Rank_MyESC",  # MyESC
    "Odds_Rank",  # Odds
    "EurovisionWorld_Points_y",  # Fan oylaması
    "Cluster", "Cluster_Name", "PageRank_Score",
    "Weighted_Influence", "Scaled_Influence"
]].copy()

# Kolon adlarını daha sade hale getir
df_clean.rename(columns={
    "Score_x": "ESC_Score",
    "Rank_x": "ESC_Rank",
    "EurovisionWorld_Points_y": "Poll_Score"
}, inplace=True)


df_clean.to_csv("Data Preparation/eurovision_master_clean.csv", index=False)
df_clean = df_clean.drop(columns=["Score_MyESC.1", "Rank_MyESC.1"])
df_clean.to_csv("Data Preparation/eurovision_master_clean.csv", index=False)
df_clean.drop(columns=["Score_MyESC.1", "Rank_MyESC.1"], inplace=True)
df_clean = df_clean.loc[:, ~df_clean.columns.duplicated()]
df_clean.to_csv("Data Preparation/eurovision_master_clean.csv", index=False)





