# Dosya bağlantısını kullanıcıya sağlama
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from io import StringIO



#region Data Preprocessing

myEscDf = pd.read_csv("Data Preparation/LastSets/MyESC.csv")
myEscDf["Edition"] = myEscDf["Year"].astype(str) + " " + myEscDf["Stage"]
myEscDf.to_csv("Data Preparation/Datasets/MyESC.csv")
#endregion


#region Scaling
scaler = MinMaxScaler()

myEscDf['Score'] = myEscDf.groupby('Edition')['Score'].transform(lambda x: scaler.fit_transform(x.values.reshape(-1,1)).flatten())
myEscDf.columns
myEscDf.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'], inplace=True)
myEscDf.to_csv("Data Preparation/LastSets/MyESC.csv")

#endregion

#region Poll Preprocessing
# Her yıl için ilgili dataset'i yükleme
polls_2016 = pd.read_csv("Data Preparation/Datasets/polls/2016_poll_results.csv")
polls_2017 = pd.read_csv("Data Preparation/Datasets/polls/2017_poll_results.csv")
polls_2018 = pd.read_csv("Data Preparation/Datasets/polls/2018_poll_results.csv")
polls_2019 = pd.read_csv("Data Preparation/Datasets/polls/2019_poll_results.csv")
polls_2021 = pd.read_csv("Data Preparation/Datasets/polls/2021_poll_results.csv")
polls_2022 = pd.read_csv("Data Preparation/Datasets/polls/2022_poll_results.csv")
polls_2023 = pd.read_csv("Data Preparation/Datasets/polls/2023_poll_results.csv")

# 'year' kolonunu her bir dataset'e ekleme
polls_2016['year'] = 2016
polls_2017['year'] = 2017
polls_2018['year'] = 2018
polls_2019['year'] = 2019
polls_2021['year'] = 2021
polls_2022['year'] = 2022
polls_2023['year'] = 2023

# Dataset'leri birleştirme
all_polls = pd.concat([polls_2016, polls_2017, polls_2018, polls_2019,
                       polls_2021, polls_2022, polls_2023], ignore_index=True)


all_polls = all_polls[["Contestant", "eurovision_world_points", "year"]]

all_polls.replace("Netherlands", "The Netherlands", inplace=True)

all_polls.to_csv("Data Preparation/Datasets/LastSets/all_polls.csv")

df = pd.read_csv("Data Preparation/LastSets/all_polls.csv")

scaler = MinMaxScaler()

df['eurovision_world_points'] = df.groupby('year')['eurovision_world_points'].transform(
    lambda x: scaler.fit_transform(x.values.reshape(-1, 1)).flatten()
)

df = df.drop(columns=['Unnamed: 0'])
df.to_csv("Data Preparation/LastSets/all_polls.csv")

data2025 = """,Contestant,eurovision_world_points,year
321,Sweden,14573,2025
322,Austria,13972,2025
323,Finland,5227,2025
324,Israel,5141,2025
325,Albania,4428,2025
326,France,3701,2025
327,Netherlands,3368,2025
328,Malta,2775,2025
329,Estonia,2671,2025
330,Norway,2276,2025
331,Greece,1836,2025
332,Poland,1673,2025
333,Spain,1546,2025
334,Italy,1351,2025
335,Lithuania,1318,2025
336,Germany,1307,2025
337,Ukraine,1242,2025
338,Czechia,1108,2025
339,San Marino,1097,2025
340,Australia,1027,2025
341,Cyprus,956,2025
342,Switzerland,912,2025
343,Luxembourg,859,2025
344,Belgium,770,2025
345,Portugal,768,2025
346,United Kingdom,749,2025
347,Montenegro,730,2025
348,Iceland,692,2025
349,Ireland,657,2025
350,Latvia,641,2025
351,Denmark,640,2025
352,Serbia,406,2025
353,Croatia,398,2025
354,Azerbaijan,380,2025
355,Armenia,362,2025
356,Slovenia,217,2025
357,Georgia,203,2025
"""

df2025 = pd.read_csv(StringIO(data2025))

# Eski df ile birleştir
df_combined = pd.concat([df, df2025], ignore_index=True)
df_combined = df_combined.drop(columns=['Unnamed: 0'])
df_combined['eurovision_world_points'] = df_combined.groupby('year')['eurovision_world_points'].transform(
    lambda x: scaler.fit_transform(x.values.reshape(-1, 1)).flatten()
)
df_combined.to_csv("Data Preparation/LastSets/all_polls.csv")


#endregion