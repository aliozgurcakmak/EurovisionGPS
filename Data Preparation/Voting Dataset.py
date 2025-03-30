import pandas as pd
import numpy as np
import openpyxl
import pandas as pd
from io import StringIO




def add_data_to_df(existing_df, new_data):
    """
    Verilen bir DataFrame'e yeni veriyi (CSV formatında bir string) ekler.

    Args:
        existing_df (pd.DataFrame): Var olan DataFrame.
        new_data (str): Yeni veri (CSV formatında string).

    Returns:
        pd.DataFrame: Yeni veri ile birleştirilmiş DataFrame.
    """
    # Yeni veriyle bir DataFrame yarat
    new_df = pd.read_csv(StringIO(new_data))

    # Mevcut DataFrame ile birleştir
    updated_df = pd.concat([existing_df, new_df], ignore_index=True)

    return updated_df


df75_21 = pd.read_csv("Data Preparation/Datasets/eurovision_song_contest_1975_2021.csv")

df75_21.columns

data22 = """Year,(semi-) final,Edition,Jury or Televoting,From country,To country,Points
2022,sf1,2022sf1,t,Albania,Bulgaria,12
2022,sf1,2022sf1,t,Albania,Greece,10
2022,sf1,2022sf1,t,Albania,Ukraine,8
2022,sf1,2022sf1,t,Albania,Armenia,7
2022,sf1,2022sf1,t,Albania,Croatia,6
2022,sf1,2022sf1,t,Albania,Portugal,5
2022,sf1,2022sf1,t,Albania,Austria,4
2022,sf1,2022sf1,t,Albania,Netherlands,3
2022,sf1,2022sf1,t,Albania,Norway,2
2022,sf1,2022sf1,t,Albania,Lithuania,1
2022,sf1,2022sf1,j,Albania,Ukraine,12
2022,sf1,2022sf1,j,Albania,Netherlands,10
2022,sf1,2022sf1,j,Albania,Greece,8
2022,sf1,2022sf1,j,Albania,Armenia,7
2022,sf1,2022sf1,j,Albania,Switzerland,6
2022,sf1,2022sf1,j,Albania,Iceland,5
2022,sf1,2022sf1,j,Albania,Portugal,4
2022,sf1,2022sf1,j,Albania,Croatia,3
2022,sf1,2022sf1,j,Albania,Norway,2
2022,sf1,2022sf1,j,Albania,Bulgaria,1
2022,sf1,2022sf1,t,Armenia,Ukraine,12
2022,sf1,2022sf1,t,Armenia,Greece,10
2022,sf1,2022sf1,t,Armenia,Portugal,8
2022,sf1,2022sf1,t,Armenia,Lithuania,7
2022,sf1,2022sf1,t,Armenia,Moldova,6
2022,sf1,2022sf1,t,Armenia,Austria,5
2022,sf1,2022sf1,t,Armenia,Netherlands,4
2022,sf1,2022sf1,t,Armenia,Norway,3
2022,sf1,2022sf1,t,Armenia,Albania,2
2022,sf1,2022sf1,t,Armenia,Switzerland,1
2022,sf1,2022sf1,j,Armenia,Netherlands,12
2022,sf1,2022sf1,j,Armenia,Portugal,10
2022,sf1,2022sf1,j,Armenia,Greece,8
2022,sf1,2022sf1,j,Armenia,Ukraine,7
2022,sf1,2022sf1,j,Armenia,Norway,6
2022,sf1,2022sf1,j,Armenia,Switzerland,5
2022,sf1,2022sf1,j,Armenia,Croatia,4
2022,sf1,2022sf1,j,Armenia,Iceland,3
2022,sf1,2022sf1,j,Armenia,Latvia,2
2022,sf1,2022sf1,j,Armenia,Moldova,1
2022,sf1,2022sf1,t,Austria,Ukraine,12
2022,sf1,2022sf1,t,Austria,Moldova,10
2022,sf1,2022sf1,t,Austria,Armenia,8
2022,sf1,2022sf1,t,Austria,Norway,7
2022,sf1,2022sf1,t,Austria,Croatia,6
2022,sf1,2022sf1,t,Austria,Netherlands,5
2022,sf1,2022sf1,t,Austria,Lithuania,4
2022,sf1,2022sf1,t,Austria,Switzerland,3
2022,sf1,2022sf1,t,Austria,Albania,2
2022,sf1,2022sf1,t,Austria,Portugal,1
2022,sf1,2022sf1,j,Austria,Armenia,12
2022,sf1,2022sf1,j,Austria,Portugal,10
2022,sf1,2022sf1,j,Austria,Netherlands,8
2022,sf1,2022sf1,j,Austria,Switzerland,7
2022,sf1,2022sf1,j,Austria,Greece,6
2022,sf1,2022sf1,j,Austria,Denmark,5
2022,sf1,2022sf1,j,Austria,Norway,4
2022,sf1,2022sf1,j,Austria,Croatia,3
2022,sf1,2022sf1,j,Austria,Iceland,2
2022,sf1,2022sf1,j,Austria,Latvia,1
2022,sf1,2022sf1,t,Bulgaria,Ukraine,12
2022,sf1,2022sf1,t,Bulgaria,Armenia,10
2022,sf1,2022sf1,t,Bulgaria,Moldova,8
2022,sf1,2022sf1,t,Bulgaria,Greece,7
2022,sf1,2022sf1,t,Bulgaria,Portugal,6
2022,sf1,2022sf1,t,Bulgaria,Lithuania,5
2022,sf1,2022sf1,t,Bulgaria,Norway,4
2022,sf1,2022sf1,t,Bulgaria,Netherlands,3
2022,sf1,2022sf1,t,Bulgaria,Croatia,2
2022,sf1,2022sf1,t,Bulgaria,Albania,1
2022,sf1,2022sf1,j,Bulgaria,Switzerland,12
2022,sf1,2022sf1,j,Bulgaria,Greece,10
2022,sf1,2022sf1,j,Bulgaria,Armenia,8
2022,sf1,2022sf1,j,Bulgaria,Norway,7
2022,sf1,2022sf1,j,Bulgaria,Croatia,6
2022,sf1,2022sf1,j,Bulgaria,Portugal,5
2022,sf1,2022sf1,j,Bulgaria,Netherlands,4
2022,sf1,2022sf1,j,Bulgaria,Latvia,3
2022,sf1,2022sf1,j,Bulgaria,Denmark,2
2022,sf1,2022sf1,j,Bulgaria,Moldova,1
2022,sf1,2022sf1,t,Croatia,Ukraine,12
2022,sf1,2022sf1,t,Croatia,Moldova,10
2022,sf1,2022sf1,t,Croatia,Slovenia,8
2022,sf1,2022sf1,t,Croatia,Norway,7
2022,sf1,2022sf1,t,Croatia,Lithuania,6
2022,sf1,2022sf1,t,Croatia,Armenia,5
2022,sf1,2022sf1,t,Croatia,Austria,4
2022,sf1,2022sf1,t,Croatia,Netherlands,3
2022,sf1,2022sf1,t,Croatia,Albania,2
2022,sf1,2022sf1,t,Croatia,Portugal,1
2022,sf1,2022sf1,j,Croatia,Portugal,12
2022,sf1,2022sf1,j,Croatia,Lithuania,10
2022,sf1,2022sf1,j,Croatia,Greece,8
2022,sf1,2022sf1,j,Croatia,Ukraine,7
2022,sf1,2022sf1,j,Croatia,Switzerland,6
2022,sf1,2022sf1,j,Croatia,Slovenia,5
2022,sf1,2022sf1,j,Croatia,Iceland,4
2022,sf1,2022sf1,j,Croatia,Denmark,3
2022,sf1,2022sf1,j,Croatia,Netherlands,2
2022,sf1,2022sf1,j,Croatia,Armenia,1
2022,sf1,2022sf1,t,Denmark,Ukraine,12
2022,sf1,2022sf1,t,Denmark,Norway,10
2022,sf1,2022sf1,t,Denmark,Lithuania,8
2022,sf1,2022sf1,t,Denmark,Iceland,7
2022,sf1,2022sf1,t,Denmark,Moldova,6
2022,sf1,2022sf1,t,Denmark,Armenia,5
2022,sf1,2022sf1,t,Denmark,Netherlands,4
2022,sf1,2022sf1,t,Denmark,Portugal,3
2022,sf1,2022sf1,t,Denmark,Austria,2
2022,sf1,2022sf1,t,Denmark,Switzerland,1
2022,sf1,2022sf1,j,Denmark,Netherlands,12
2022,sf1,2022sf1,j,Denmark,Greece,10
2022,sf1,2022sf1,j,Denmark,Portugal,8
2022,sf1,2022sf1,j,Denmark,Ukraine,7
2022,sf1,2022sf1,j,Denmark,Switzerland,6
2022,sf1,2022sf1,j,Denmark,Lithuania,5
2022,sf1,2022sf1,j,Denmark,Iceland,4
2022,sf1,2022sf1,j,Denmark,Norway,3
2022,sf1,2022sf1,j,Denmark,Armenia,2
2022,sf1,2022sf1,j,Denmark,Latvia,1
2022,sf1,2022sf1,t,France,Armenia,12
2022,sf1,2022sf1,t,France,Ukraine,10
2022,sf1,2022sf1,t,France,Portugal,8
2022,sf1,2022sf1,t,France,Moldova,7
2022,sf1,2022sf1,t,France,Lithuania,6
2022,sf1,2022sf1,t,France,Albania,5
2022,sf1,2022sf1,t,France,Netherlands,4
2022,sf1,2022sf1,t,France,Iceland,3
2022,sf1,2022sf1,t,France,Norway,2
2022,sf1,2022sf1,t,France,Greece,1
2022,sf1,2022sf1,j,France,Greece,12
2022,sf1,2022sf1,j,France,Ukraine,10
2022,sf1,2022sf1,j,France,Netherlands,8
2022,sf1,2022sf1,j,France,Armenia,7
2022,sf1,2022sf1,j,France,Portugal,6
2022,sf1,2022sf1,j,France,Switzerland,5
2022,sf1,2022sf1,j,France,Iceland,4
2022,sf1,2022sf1,j,France,Norway,3
2022,sf1,2022sf1,j,France,Lithuania,2
2022,sf1,2022sf1,j,France,Austria,1
2022,sf1,2022sf1,t,Greece,Albania,12
2022,sf1,2022sf1,t,Greece,Ukraine,10
2022,sf1,2022sf1,t,Greece,Armenia,8
2022,sf1,2022sf1,t,Greece,Norway,7
2022,sf1,2022sf1,t,Greece,Moldova,6
2022,sf1,2022sf1,t,Greece,Lithuania,5
2022,sf1,2022sf1,t,Greece,Netherlands,4
2022,sf1,2022sf1,t,Greece,Portugal,3
2022,sf1,2022sf1,t,Greece,Austria,2
2022,sf1,2022sf1,t,Greece,Bulgaria,1
2022,sf1,2022sf1,j,Greece,Albania,12
2022,sf1,2022sf1,j,Greece,Bulgaria,10
2022,sf1,2022sf1,j,Greece,Croatia,8
2022,sf1,2022sf1,j,Greece,Moldova,7
2022,sf1,2022sf1,j,Greece,Netherlands,6
2022,sf1,2022sf1,j,Greece,Portugal,5
2022,sf1,2022sf1,j,Greece,Latvia,4
2022,sf1,2022sf1,j,Greece,Ukraine,3
2022,sf1,2022sf1,j,Greece,Austria,2
2022,sf1,2022sf1,j,Greece,Norway,1
2022,sf1,2022sf1,t,Iceland,Ukraine,12
2022,sf1,2022sf1,t,Iceland,Norway,10
2022,sf1,2022sf1,t,Iceland,Netherlands,8
2022,sf1,2022sf1,t,Iceland,Moldova,7
2022,sf1,2022sf1,t,Iceland,Denmark,6
2022,sf1,2022sf1,t,Iceland,Lithuania,5
2022,sf1,2022sf1,t,Iceland,Austria,4
2022,sf1,2022sf1,t,Iceland,Armenia,3
2022,sf1,2022sf1,t,Iceland,Portugal,2
2022,sf1,2022sf1,t,Iceland,Switzerland,1
2022,sf1,2022sf1,j,Iceland,Norway,12
2022,sf1,2022sf1,j,Iceland,Ukraine,10
2022,sf1,2022sf1,j,Iceland,Lithuania,8
2022,sf1,2022sf1,j,Iceland,Netherlands,7
2022,sf1,2022sf1,j,Iceland,Portugal,6
2022,sf1,2022sf1,j,Iceland,Switzerland,5
2022,sf1,2022sf1,j,Iceland,Latvia,4
2022,sf1,2022sf1,j,Iceland,Armenia,3
2022,sf1,2022sf1,j,Iceland,Greece,2
2022,sf1,2022sf1,j,Iceland,Denmark,1
2022,sf1,2022sf1,t,Italy,Ukraine,12
2022,sf1,2022sf1,t,Italy,Moldova,10
2022,sf1,2022sf1,t,Italy,Albania,8
2022,sf1,2022sf1,t,Italy,Armenia,7
2022,sf1,2022sf1,t,Italy,Portugal,6
2022,sf1,2022sf1,t,Italy,Norway,5
2022,sf1,2022sf1,t,Italy,Netherlands,4
2022,sf1,2022sf1,t,Italy,Greece,3
2022,sf1,2022sf1,t,Italy,Austria,2
2022,sf1,2022sf1,t,Italy,Lithuania,1
2022,sf1,2022sf1,j,Italy,Greece,12
2022,sf1,2022sf1,j,Italy,Netherlands,10
2022,sf1,2022sf1,j,Italy,Armenia,8
2022,sf1,2022sf1,j,Italy,Ukraine,7
2022,sf1,2022sf1,j,Italy,Switzerland,6
2022,sf1,2022sf1,j,Italy,Moldova,5
2022,sf1,2022sf1,j,Italy,Croatia,4
2022,sf1,2022sf1,j,Italy,Austria,3
2022,sf1,2022sf1,j,Italy,Lithuania,2
2022,sf1,2022sf1,j,Italy,Latvia,1
2022,sf1,2022sf1,t,Latvia,Ukraine,12
2022,sf1,2022sf1,t,Latvia,Lithuania,10
2022,sf1,2022sf1,t,Latvia,Moldova,8
2022,sf1,2022sf1,t,Latvia,Norway,7
2022,sf1,2022sf1,t,Latvia,Portugal,6
2022,sf1,2022sf1,t,Latvia,Iceland,5
2022,sf1,2022sf1,t,Latvia,Armenia,4
2022,sf1,2022sf1,t,Latvia,Netherlands,3
2022,sf1,2022sf1,t,Latvia,Denmark,2
2022,sf1,2022sf1,t,Latvia,Austria,1
2022,sf1,2022sf1,j,Latvia,Ukraine,12
2022,sf1,2022sf1,j,Latvia,Greece,10
2022,sf1,2022sf1,j,Latvia,Iceland,8
2022,sf1,2022sf1,j,Latvia,Norway,7
2022,sf1,2022sf1,j,Latvia,Denmark,6
2022,sf1,2022sf1,j,Latvia,Portugal,5
2022,sf1,2022sf1,j,Latvia,Switzerland,4
2022,sf1,2022sf1,j,Latvia,Netherlands,3
2022,sf1,2022sf1,j,Latvia,Armenia,2
2022,sf1,2022sf1,j,Latvia,Lithuania,1
2022,sf1,2022sf1,t,Lithuania,Ukraine,12
2022,sf1,2022sf1,t,Lithuania,Latvia,10
2022,sf1,2022sf1,t,Lithuania,Portugal,8
2022,sf1,2022sf1,t,Lithuania,Moldova,7
2022,sf1,2022sf1,t,Lithuania,Netherlands,6
2022,sf1,2022sf1,t,Lithuania,Norway,5
2022,sf1,2022sf1,t,Lithuania,Armenia,4
2022,sf1,2022sf1,t,Lithuania,Switzerland,3
2022,sf1,2022sf1,t,Lithuania,Iceland,2
2022,sf1,2022sf1,t,Lithuania,Denmark,1
2022,sf1,2022sf1,j,Lithuania,Ukraine,12
2022,sf1,2022sf1,j,Lithuania,Switzerland,10
2022,sf1,2022sf1,j,Lithuania,Netherlands,8
2022,sf1,2022sf1,j,Lithuania,Portugal,7
2022,sf1,2022sf1,j,Lithuania,Greece,6
2022,sf1,2022sf1,j,Lithuania,Denmark,5
2022,sf1,2022sf1,j,Lithuania,Iceland,4
2022,sf1,2022sf1,j,Lithuania,Norway,3
2022,sf1,2022sf1,j,Lithuania,Latvia,2
2022,sf1,2022sf1,j,Lithuania,Moldova,1
2022,sf1,2022sf1,t,Moldova,Ukraine,12
2022,sf1,2022sf1,t,Moldova,Norway,10
2022,sf1,2022sf1,t,Moldova,Netherlands,8
2022,sf1,2022sf1,t,Moldova,Armenia,7
2022,sf1,2022sf1,t,Moldova,Lithuania,6
2022,sf1,2022sf1,t,Moldova,Bulgaria,5
2022,sf1,2022sf1,t,Moldova,Portugal,4
2022,sf1,2022sf1,t,Moldova,Denmark,3
2022,sf1,2022sf1,t,Moldova,Austria,2
2022,sf1,2022sf1,t,Moldova,Greece,1
2022,sf1,2022sf1,j,Moldova,Ukraine,12
2022,sf1,2022sf1,j,Moldova,Switzerland,10
2022,sf1,2022sf1,j,Moldova,Greece,8
2022,sf1,2022sf1,j,Moldova,Norway,7
2022,sf1,2022sf1,j,Moldova,Armenia,6
2022,sf1,2022sf1,j,Moldova,Portugal,5
2022,sf1,2022sf1,j,Moldova,Latvia,4
2022,sf1,2022sf1,j,Moldova,Iceland,3
2022,sf1,2022sf1,j,Moldova,Netherlands,2
2022,sf1,2022sf1,j,Moldova,Slovenia,1
2022,sf1,2022sf1,t,Netherlands,Ukraine,12
2022,sf1,2022sf1,t,Netherlands,Moldova,10
2022,sf1,2022sf1,t,Netherlands,Armenia,8
2022,sf1,2022sf1,t,Netherlands,Norway,7
2022,sf1,2022sf1,t,Netherlands,Portugal,6
2022,sf1,2022sf1,t,Netherlands,Lithuania,5
2022,sf1,2022sf1,t,Netherlands,Iceland,4
2022,sf1,2022sf1,t,Netherlands,Greece,3
2022,sf1,2022sf1,t,Netherlands,Switzerland,2
2022,sf1,2022sf1,t,Netherlands,Latvia,1
2022,sf1,2022sf1,j,Netherlands,Greece,12
2022,sf1,2022sf1,j,Netherlands,Portugal,10
2022,sf1,2022sf1,j,Netherlands,Ukraine,8
2022,sf1,2022sf1,j,Netherlands,Switzerland,7
2022,sf1,2022sf1,j,Netherlands,Norway,6
2022,sf1,2022sf1,j,Netherlands,Iceland,5
2022,sf1,2022sf1,j,Netherlands,Armenia,4
2022,sf1,2022sf1,j,Netherlands,Croatia,3
2022,sf1,2022sf1,j,Netherlands,Lithuania,2
2022,sf1,2022sf1,j,Netherlands,Slovenia,1
2022,sf1,2022sf1,t,Norway,Greece,12
2022,sf1,2022sf1,t,Norway,Ukraine,10
2022,sf1,2022sf1,t,Norway,Lithuania,8
2022,sf1,2022sf1,t,Norway,Iceland,7
2022,sf1,2022sf1,t,Norway,Moldova,6
2022,sf1,2022sf1,t,Norway,Armenia,5
2022,sf1,2022sf1,t,Norway,Denmark,4
2022,sf1,2022sf1,t,Norway,Austria,3
2022,sf1,2022sf1,t,Norway,Portugal,2
2022,sf1,2022sf1,t,Norway,Netherlands,1
2022,sf1,2022sf1,j,Norway,Greece,12
2022,sf1,2022sf1,j,Norway,Portugal,10
2022,sf1,2022sf1,j,Norway,Netherlands,8
2022,sf1,2022sf1,j,Norway,Armenia,7
2022,sf1,2022sf1,j,Norway,Ukraine,6
2022,sf1,2022sf1,j,Norway,Lithuania,5
2022,sf1,2022sf1,j,Norway,Switzerland,4
2022,sf1,2022sf1,j,Norway,Denmark,3
2022,sf1,2022sf1,j,Norway,Iceland,2
2022,sf1,2022sf1,j,Norway,Moldova,1
2022,sf1,2022sf1,t,Portugal,Ukraine,12
2022,sf1,2022sf1,t,Portugal,Moldova,10
2022,sf1,2022sf1,t,Portugal,Netherlands,8
2022,sf1,2022sf1,t,Portugal,Norway,7
2022,sf1,2022sf1,t,Portugal,Lithuania,6
2022,sf1,2022sf1,t,Portugal,Armenia,5
2022,sf1,2022sf1,t,Portugal,Greece,4
2022,sf1,2022sf1,t,Portugal,Denmark,3
2022,sf1,2022sf1,t,Portugal,Iceland,2
2022,sf1,2022sf1,t,Portugal,Croatia,1
2022,sf1,2022sf1,j,Portugal,Latvia,12
2022,sf1,2022sf1,j,Portugal,Iceland,10
2022,sf1,2022sf1,j,Portugal,Netherlands,8
2022,sf1,2022sf1,j,Portugal,Ukraine,7
2022,sf1,2022sf1,j,Portugal,Lithuania,6
2022,sf1,2022sf1,j,Portugal,Greece,5
2022,sf1,2022sf1,j,Portugal,Switzerland,4
2022,sf1,2022sf1,j,Portugal,Armenia,3
2022,sf1,2022sf1,j,Portugal,Norway,2
2022,sf1,2022sf1,j,Portugal,Moldova,1
2022,sf1,2022sf1,t,Slovenia,Croatia,12
2022,sf1,2022sf1,t,Slovenia,Ukraine,10
2022,sf1,2022sf1,t,Slovenia,Greece,8
2022,sf1,2022sf1,t,Slovenia,Moldova,7
2022,sf1,2022sf1,t,Slovenia,Albania,6
2022,sf1,2022sf1,t,Slovenia,Lithuania,5
2022,sf1,2022sf1,t,Slovenia,Norway,4
2022,sf1,2022sf1,t,Slovenia,Netherlands,3
2022,sf1,2022sf1,t,Slovenia,Portugal,2
2022,sf1,2022sf1,t,Slovenia,Denmark,1
2022,sf1,2022sf1,j,Slovenia,Lithuania,12
2022,sf1,2022sf1,j,Slovenia,Netherlands,10
2022,sf1,2022sf1,j,Slovenia,Croatia,8
2022,sf1,2022sf1,j,Slovenia,Ukraine,7
2022,sf1,2022sf1,j,Slovenia,Portugal,6
2022,sf1,2022sf1,j,Slovenia,Greece,5
2022,sf1,2022sf1,j,Slovenia,Switzerland,4
2022,sf1,2022sf1,j,Slovenia,Latvia,3
2022,sf1,2022sf1,j,Slovenia,Norway,2
2022,sf1,2022sf1,j,Slovenia,Armenia,1
2022,sf1,2022sf1,t,Switzerland,Portugal,12
2022,sf1,2022sf1,t,Switzerland,Ukraine,10
2022,sf1,2022sf1,t,Switzerland,Albania,8
2022,sf1,2022sf1,t,Switzerland,Moldova,7
2022,sf1,2022sf1,t,Switzerland,Croatia,6
2022,sf1,2022sf1,t,Switzerland,Armenia,5
2022,sf1,2022sf1,t,Switzerland,Austria,4
2022,sf1,2022sf1,t,Switzerland,Lithuania,3
2022,sf1,2022sf1,t,Switzerland,Netherlands,2
2022,sf1,2022sf1,t,Switzerland,Iceland,1
2022,sf1,2022sf1,j,Switzerland,Netherlands,12
2022,sf1,2022sf1,j,Switzerland,Greece,10
2022,sf1,2022sf1,j,Switzerland,Ukraine,8
2022,sf1,2022sf1,j,Switzerland,Norway,7
2022,sf1,2022sf1,j,Switzerland,Iceland,6
2022,sf1,2022sf1,j,Switzerland,Denmark,5
2022,sf1,2022sf1,j,Switzerland,Portugal,4
2022,sf1,2022sf1,j,Switzerland,Lithuania,3
2022,sf1,2022sf1,j,Switzerland,Latvia,2
2022,sf1,2022sf1,j,Switzerland,Armenia,1
2022,sf1,2022sf1,t,Ukraine,Lithuania,12
2022,sf1,2022sf1,t,Ukraine,Moldova,10
2022,sf1,2022sf1,t,Ukraine,Iceland,8
2022,sf1,2022sf1,t,Ukraine,Norway,7
2022,sf1,2022sf1,t,Ukraine,Netherlands,6
2022,sf1,2022sf1,t,Ukraine,Latvia,5
2022,sf1,2022sf1,t,Ukraine,Portugal,4
2022,sf1,2022sf1,t,Ukraine,Austria,3
2022,sf1,2022sf1,t,Ukraine,Armenia,2
2022,sf1,2022sf1,t,Ukraine,Greece,1
2022,sf1,2022sf1,j,Ukraine,Netherlands,12
2022,sf1,2022sf1,j,Ukraine,Armenia,10
2022,sf1,2022sf1,j,Ukraine,Portugal,8
2022,sf1,2022sf1,j,Ukraine,Greece,7
2022,sf1,2022sf1,j,Ukraine,Switzerland,6
2022,sf1,2022sf1,j,Ukraine,Denmark,5
2022,sf1,2022sf1,j,Ukraine,Iceland,4
2022,sf1,2022sf1,j,Ukraine,Croatia,3
2022,sf1,2022sf1,j,Ukraine,Moldova,2
2022,sf1,2022sf1,j,Ukraine,Norway,1
2022,sf2,2022sf2,t,Australia,Serbia,12
2022,sf2,2022sf2,t,Australia,Sweden,10
2022,sf2,2022sf2,t,Australia,Ireland,8
2022,sf2,2022sf2,t,Australia,Czechia,7
2022,sf2,2022sf2,t,Australia,Poland,6
2022,sf2,2022sf2,t,Australia,San Marino,5
2022,sf2,2022sf2,t,Australia,Romania,4
2022,sf2,2022sf2,t,Australia,Estonia,3
2022,sf2,2022sf2,t,Australia,Finland,2
2022,sf2,2022sf2,t,Australia,Georgia,1
2022,sf2,2022sf2,j,Australia,Sweden,12
2022,sf2,2022sf2,j,Australia,Israel,10
2022,sf2,2022sf2,j,Australia,Belgium,8
2022,sf2,2022sf2,j,Australia,North Macedonia,7
2022,sf2,2022sf2,j,Australia,Ireland,6
2022,sf2,2022sf2,j,Australia,Estonia,5
2022,sf2,2022sf2,j,Australia,Serbia,4
2022,sf2,2022sf2,j,Australia,Azerbaijan,3
2022,sf2,2022sf2,j,Australia,Czechia,2
2022,sf2,2022sf2,j,Australia,Georgia,1
2022,sf2,2022sf2,t,Azerbaijan,Cyprus,12
2022,sf2,2022sf2,t,Azerbaijan,Israel,10
2022,sf2,2022sf2,t,Azerbaijan,Sweden,8
2022,sf2,2022sf2,t,Azerbaijan,Australia,7
2022,sf2,2022sf2,t,Azerbaijan,Romania,6
2022,sf2,2022sf2,t,Azerbaijan,Finland,5
2022,sf2,2022sf2,t,Azerbaijan,Belgium,4
2022,sf2,2022sf2,t,Azerbaijan,Malta,3
2022,sf2,2022sf2,t,Azerbaijan,Czechia,2
2022,sf2,2022sf2,t,Azerbaijan,Poland,1
2022,sf2,2022sf2,j,Azerbaijan,Sweden,12
2022,sf2,2022sf2,j,Azerbaijan,Australia,10
2022,sf2,2022sf2,j,Azerbaijan,Poland,8
2022,sf2,2022sf2,j,Azerbaijan,Estonia,7
2022,sf2,2022sf2,j,Azerbaijan,Czechia,6
2022,sf2,2022sf2,j,Azerbaijan,Belgium,5
2022,sf2,2022sf2,j,Azerbaijan,Finland,4
2022,sf2,2022sf2,j,Azerbaijan,Serbia,3
2022,sf2,2022sf2,j,Azerbaijan,Malta,2
2022,sf2,2022sf2,j,Azerbaijan,Israel,1
2022,sf2,2022sf2,t,Belgium,Poland,12
2022,sf2,2022sf2,t,Belgium,Sweden,10
2022,sf2,2022sf2,t,Belgium,Romania,8
2022,sf2,2022sf2,t,Belgium,Estonia,7
2022,sf2,2022sf2,t,Belgium,Serbia,6
2022,sf2,2022sf2,t,Belgium,Czechia,5
2022,sf2,2022sf2,t,Belgium,Finland,4
2022,sf2,2022sf2,t,Belgium,Australia,3
2022,sf2,2022sf2,t,Belgium,Malta,2
2022,sf2,2022sf2,t,Belgium,Ireland,1
2022,sf2,2022sf2,j,Belgium,San Marino,12
2022,sf2,2022sf2,j,Belgium,Sweden,10
2022,sf2,2022sf2,j,Belgium,Australia,8
2022,sf2,2022sf2,j,Belgium,Israel,7
2022,sf2,2022sf2,j,Belgium,Poland,6
2022,sf2,2022sf2,j,Belgium,Finland,5
2022,sf2,2022sf2,j,Belgium,Czechia,4
2022,sf2,2022sf2,j,Belgium,Azerbaijan,3
2022,sf2,2022sf2,j,Belgium,Serbia,2
2022,sf2,2022sf2,j,Belgium,Ireland,1
2022,sf2,2022sf2,t,Cyprus,Serbia,12
2022,sf2,2022sf2,t,Cyprus,Romania,10
2022,sf2,2022sf2,t,Cyprus,Poland,8
2022,sf2,2022sf2,t,Cyprus,Sweden,7
2022,sf2,2022sf2,t,Cyprus,Belgium,6
2022,sf2,2022sf2,t,Cyprus,Czechia,5
2022,sf2,2022sf2,t,Cyprus,Australia,4
2022,sf2,2022sf2,t,Cyprus,Estonia,3
2022,sf2,2022sf2,t,Cyprus,Finland,2
2022,sf2,2022sf2,t,Cyprus,Malta,1
2022,sf2,2022sf2,j,Cyprus,Sweden,12
2022,sf2,2022sf2,j,Cyprus,Australia,10
2022,sf2,2022sf2,j,Cyprus,Poland,8
2022,sf2,2022sf2,j,Cyprus,Estonia,7
2022,sf2,2022sf2,j,Cyprus,Azerbaijan,6
2022,sf2,2022sf2,j,Cyprus,Serbia,5
2022,sf2,2022sf2,j,Cyprus,Czechia,4
2022,sf2,2022sf2,j,Cyprus,Belgium,3
2022,sf2,2022sf2,j,Cyprus,Finland,2
2022,sf2,2022sf2,j,Cyprus,Ireland,1
2022,sf2,2022sf2,t,Czechia,Serbia,12
2022,sf2,2022sf2,t,Czechia,Finland,10
2022,sf2,2022sf2,t,Czechia,Estonia,8
2022,sf2,2022sf2,t,Czechia,Poland,7
2022,sf2,2022sf2,t,Czechia,Sweden,6
2022,sf2,2022sf2,t,Czechia,Australia,5
2022,sf2,2022sf2,t,Czechia,Romania,4
2022,sf2,2022sf2,t,Czechia,Israel,3
2022,sf2,2022sf2,t,Czechia,North Macedonia,2
2022,sf2,2022sf2,t,Czechia,Ireland,1
2022,sf2,2022sf2,j,Czechia,Sweden,12
2022,sf2,2022sf2,j,Czechia,North Macedonia,10
2022,sf2,2022sf2,j,Czechia,Australia,8
2022,sf2,2022sf2,j,Czechia,Estonia,7
2022,sf2,2022sf2,j,Czechia,Belgium,6
2022,sf2,2022sf2,j,Czechia,Georgia,5
2022,sf2,2022sf2,j,Czechia,Azerbaijan,4
2022,sf2,2022sf2,j,Czechia,Poland,3
2022,sf2,2022sf2,j,Czechia,Finland,2
2022,sf2,2022sf2,j,Czechia,Malta,1
2022,sf2,2022sf2,t,Estonia,Finland,12
2022,sf2,2022sf2,t,Estonia,Sweden,10
2022,sf2,2022sf2,t,Estonia,Czechia,8
2022,sf2,2022sf2,t,Estonia,Belgium,7
2022,sf2,2022sf2,t,Estonia,Poland,6
2022,sf2,2022sf2,t,Estonia,Australia,5
2022,sf2,2022sf2,t,Estonia,Serbia,4
2022,sf2,2022sf2,t,Estonia,Malta,3
2022,sf2,2022sf2,t,Estonia,Romania,2
2022,sf2,2022sf2,t,Estonia,Georgia,1
2022,sf2,2022sf2,j,Estonia,Sweden,12
2022,sf2,2022sf2,j,Estonia,Australia,10
2022,sf2,2022sf2,j,Estonia,Finland,8
2022,sf2,2022sf2,j,Estonia,Czechia,7
2022,sf2,2022sf2,j,Estonia,Azerbaijan,6
2022,sf2,2022sf2,j,Estonia,Belgium,5
2022,sf2,2022sf2,j,Estonia,Ireland,4
2022,sf2,2022sf2,j,Estonia,Georgia,3
2022,sf2,2022sf2,j,Estonia,Romania,2
2022,sf2,2022sf2,j,Estonia,Malta,1
2022,sf2,2022sf2,t,Finland,Estonia,12
2022,sf2,2022sf2,t,Finland,Sweden,10
2022,sf2,2022sf2,t,Finland,Serbia,8
2022,sf2,2022sf2,t,Finland,Czechia,7
2022,sf2,2022sf2,t,Finland,Australia,6
2022,sf2,2022sf2,t,Finland,Poland,5
2022,sf2,2022sf2,t,Finland,San Marino,4
2022,sf2,2022sf2,t,Finland,Romania,3
2022,sf2,2022sf2,t,Finland,Georgia,2
2022,sf2,2022sf2,t,Finland,Belgium,1
2022,sf2,2022sf2,j,Finland,Sweden,12
2022,sf2,2022sf2,j,Finland,Australia,10
2022,sf2,2022sf2,j,Finland,Serbia,8
2022,sf2,2022sf2,j,Finland,Azerbaijan,7
2022,sf2,2022sf2,j,Finland,Czechia,6
2022,sf2,2022sf2,j,Finland,San Marino,5
2022,sf2,2022sf2,j,Finland,Estonia,4
2022,sf2,2022sf2,j,Finland,Cyprus,3
2022,sf2,2022sf2,j,Finland,North Macedonia,2
2022,sf2,2022sf2,j,Finland,Poland,1
2022,sf2,2022sf2,t,Georgia,Serbia,12
2022,sf2,2022sf2,t,Georgia,Israel,10
2022,sf2,2022sf2,t,Georgia,Sweden,8
2022,sf2,2022sf2,t,Georgia,Estonia,7
2022,sf2,2022sf2,t,Georgia,Finland,6
2022,sf2,2022sf2,t,Georgia,Romania,5
2022,sf2,2022sf2,t,Georgia,Czechia,4
2022,sf2,2022sf2,t,Georgia,Poland,3
2022,sf2,2022sf2,t,Georgia,Australia,2
2022,sf2,2022sf2,t,Georgia,Cyprus,1
2022,sf2,2022sf2,j,Georgia,Sweden,12
2022,sf2,2022sf2,j,Georgia,Australia,10
2022,sf2,2022sf2,j,Georgia,Poland,8
2022,sf2,2022sf2,j,Georgia,Estonia,7
2022,sf2,2022sf2,j,Georgia,Czechia,6
2022,sf2,2022sf2,j,Georgia,Belgium,5
2022,sf2,2022sf2,j,Georgia,Azerbaijan,4
2022,sf2,2022sf2,j,Georgia,Finland,3
2022,sf2,2022sf2,j,Georgia,Serbia,2
2022,sf2,2022sf2,j,Georgia,Malta,1
2022,sf2,2022sf2,t,Germany,Poland,12
2022,sf2,2022sf2,t,Germany,Serbia,10
2022,sf2,2022sf2,t,Germany,Sweden,8
2022,sf2,2022sf2,t,Germany,Finland,7
2022,sf2,2022sf2,t,Germany,Czechia,6
2022,sf2,2022sf2,t,Germany,Romania,5
2022,sf2,2022sf2,t,Germany,Estonia,4
2022,sf2,2022sf2,t,Germany,Australia,3
2022,sf2,2022sf2,t,Germany,Israel,2
2022,sf2,2022sf2,t,Germany,Belgium,1
2022,sf2,2022sf2,j,Germany,North Macedonia,12
2022,sf2,2022sf2,j,Germany,Azerbaijan,10
2022,sf2,2022sf2,j,Germany,Romania,8
2022,sf2,2022sf2,j,Germany,Sweden,7
2022,sf2,2022sf2,j,Germany,Australia,6
2022,sf2,2022sf2,j,Germany,Belgium,5
2022,sf2,2022sf2,j,Germany,Estonia,4
2022,sf2,2022sf2,j,Germany,Georgia,3
2022,sf2,2022sf2,j,Germany,Israel,2
2022,sf2,2022sf2,j,Germany,Finland,1
2022,sf2,2022sf2,t,Ireland,Poland,12
2022,sf2,2022sf2,t,Ireland,Sweden,10
2022,sf2,2022sf2,t,Ireland,Czechia,8
2022,sf2,2022sf2,t,Ireland,Australia,7
2022,sf2,2022sf2,t,Ireland,Estonia,6
2022,sf2,2022sf2,t,Ireland,Romania,5
2022,sf2,2022sf2,t,Ireland,Serbia,4
2022,sf2,2022sf2,t,Ireland,Malta,3
2022,sf2,2022sf2,t,Ireland,Belgium,2
2022,sf2,2022sf2,t,Ireland,Finland,1
2022,sf2,2022sf2,j,Ireland,Sweden,12
2022,sf2,2022sf2,j,Ireland,Czechia,10
2022,sf2,2022sf2,j,Ireland,Estonia,8
2022,sf2,2022sf2,j,Ireland,Serbia,7
2022,sf2,2022sf2,j,Ireland,Malta,6
2022,sf2,2022sf2,j,Ireland,Australia,5
2022,sf2,2022sf2,j,Ireland,Cyprus,4
2022,sf2,2022sf2,j,Ireland,Israel,3
2022,sf2,2022sf2,j,Ireland,Belgium,2
2022,sf2,2022sf2,j,Ireland,North Macedonia,1
2022,sf2,2022sf2,t,Israel,Sweden,12
2022,sf2,2022sf2,t,Israel,Czechia,10
2022,sf2,2022sf2,t,Israel,Serbia,8
2022,sf2,2022sf2,t,Israel,Poland,7
2022,sf2,2022sf2,t,Israel,Australia,6
2022,sf2,2022sf2,t,Israel,Georgia,5
2022,sf2,2022sf2,t,Israel,Estonia,4
2022,sf2,2022sf2,t,Israel,Ireland,3
2022,sf2,2022sf2,t,Israel,Romania,2
2022,sf2,2022sf2,t,Israel,Belgium,1
2022,sf2,2022sf2,j,Israel,Sweden,12
2022,sf2,2022sf2,j,Israel,Australia,10
2022,sf2,2022sf2,j,Israel,Poland,8
2022,sf2,2022sf2,j,Israel,Belgium,7
2022,sf2,2022sf2,j,Israel,Czechia,6
2022,sf2,2022sf2,j,Israel,Finland,5
2022,sf2,2022sf2,j,Israel,Romania,4
2022,sf2,2022sf2,j,Israel,Estonia,3
2022,sf2,2022sf2,j,Israel,Malta,2
2022,sf2,2022sf2,j,Israel,Serbia,1
2022,sf2,2022sf2,t,Malta,Serbia,12
2022,sf2,2022sf2,t,Malta,Sweden,10
2022,sf2,2022sf2,t,Malta,San Marino,8
2022,sf2,2022sf2,t,Malta,Australia,7
2022,sf2,2022sf2,t,Malta,Finland,6
2022,sf2,2022sf2,t,Malta,Romania,5
2022,sf2,2022sf2,t,Malta,Poland,4
2022,sf2,2022sf2,t,Malta,Ireland,3
2022,sf2,2022sf2,t,Malta,Czechia,2
2022,sf2,2022sf2,t,Malta,Cyprus,1
2022,sf2,2022sf2,j,Malta,Sweden,12
2022,sf2,2022sf2,j,Malta,Australia,10
2022,sf2,2022sf2,j,Malta,Estonia,8
2022,sf2,2022sf2,j,Malta,Czechia,7
2022,sf2,2022sf2,j,Malta,Poland,6
2022,sf2,2022sf2,j,Malta,North Macedonia,5
2022,sf2,2022sf2,j,Malta,Azerbaijan,4
2022,sf2,2022sf2,j,Malta,Finland,3
2022,sf2,2022sf2,j,Malta,Israel,2
2022,sf2,2022sf2,j,Malta,Georgia,1
2022,sf2,2022sf2,t,Montenegro,Serbia,12
2022,sf2,2022sf2,t,Montenegro,North Macedonia,10
2022,sf2,2022sf2,t,Montenegro,Cyprus,8
2022,sf2,2022sf2,t,Montenegro,Estonia,7
2022,sf2,2022sf2,t,Montenegro,Sweden,6
2022,sf2,2022sf2,t,Montenegro,Belgium,5
2022,sf2,2022sf2,t,Montenegro,Czechia,4
2022,sf2,2022sf2,t,Montenegro,Australia,3
2022,sf2,2022sf2,t,Montenegro,Poland,2
2022,sf2,2022sf2,t,Montenegro,Malta,1
2022,sf2,2022sf2,j,Montenegro,Sweden,12
2022,sf2,2022sf2,j,Montenegro,Australia,10
2022,sf2,2022sf2,j,Montenegro,Belgium,8
2022,sf2,2022sf2,j,Montenegro,Serbia,7
2022,sf2,2022sf2,j,Montenegro,Estonia,6
2022,sf2,2022sf2,j,Montenegro,Azerbaijan,5
2022,sf2,2022sf2,j,Montenegro,Finland,4
2022,sf2,2022sf2,j,Montenegro,Poland,3
2022,sf2,2022sf2,j,Montenegro,Czechia,2
2022,sf2,2022sf2,j,Montenegro,North Macedonia,1
2022,sf2,2022sf2,t,North Macedonia,Serbia,12
2022,sf2,2022sf2,t,North Macedonia,Montenegro,10
2022,sf2,2022sf2,t,North Macedonia,Finland,8
2022,sf2,2022sf2,t,North Macedonia,Sweden,7
2022,sf2,2022sf2,t,North Macedonia,Czechia,6
2022,sf2,2022sf2,t,North Macedonia,Cyprus,5
2022,sf2,2022sf2,t,North Macedonia,Belgium,4
2022,sf2,2022sf2,t,North Macedonia,Malta,3
2022,sf2,2022sf2,t,North Macedonia,Poland,2
2022,sf2,2022sf2,t,North Macedonia,Estonia,1
2022,sf2,2022sf2,j,North Macedonia,Serbia,12
2022,sf2,2022sf2,j,North Macedonia,Belgium,10
2022,sf2,2022sf2,j,North Macedonia,Poland,8
2022,sf2,2022sf2,j,North Macedonia,Sweden,7
2022,sf2,2022sf2,j,North Macedonia,Malta,6
2022,sf2,2022sf2,j,North Macedonia,Australia,5
2022,sf2,2022sf2,j,North Macedonia,Finland,4
2022,sf2,2022sf2,j,North Macedonia,Montenegro,3
2022,sf2,2022sf2,j,North Macedonia,Estonia,2
2022,sf2,2022sf2,j,North Macedonia,Azerbaijan,1
2022,sf2,2022sf2,t,Poland,Sweden,12
2022,sf2,2022sf2,t,Poland,Estonia,10
2022,sf2,2022sf2,t,Poland,Czechia,8
2022,sf2,2022sf2,t,Poland,Serbia,7
2022,sf2,2022sf2,t,Poland,Finland,6
2022,sf2,2022sf2,t,Poland,Romania,5
2022,sf2,2022sf2,t,Poland,San Marino,4
2022,sf2,2022sf2,t,Poland,Cyprus,3
2022,sf2,2022sf2,t,Poland,Australia,2
2022,sf2,2022sf2,t,Poland,Belgium,1
2022,sf2,2022sf2,j,Poland,Sweden,12
2022,sf2,2022sf2,j,Poland,Australia,10
2022,sf2,2022sf2,j,Poland,Czechia,8
2022,sf2,2022sf2,j,Poland,Estonia,7
2022,sf2,2022sf2,j,Poland,Belgium,6
2022,sf2,2022sf2,j,Poland,North Macedonia,5
2022,sf2,2022sf2,j,Poland,Finland,4
2022,sf2,2022sf2,j,Poland,Azerbaijan,3
2022,sf2,2022sf2,j,Poland,San Marino,2
2022,sf2,2022sf2,j,Poland,Israel,1
2022,sf2,2022sf2,t,Romania,Sweden,12
2022,sf2,2022sf2,t,Romania,Serbia,10
2022,sf2,2022sf2,t,Romania,Estonia,8
2022,sf2,2022sf2,t,Romania,Cyprus,7
2022,sf2,2022sf2,t,Romania,Czechia,6
2022,sf2,2022sf2,t,Romania,Belgium,5
2022,sf2,2022sf2,t,Romania,Finland,4
2022,sf2,2022sf2,t,Romania,Australia,3
2022,sf2,2022sf2,t,Romania,San Marino,2
2022,sf2,2022sf2,t,Romania,Poland,1
2022,sf2,2022sf2,j,Romania,Sweden,12
2022,sf2,2022sf2,j,Romania,Australia,10
2022,sf2,2022sf2,j,Romania,Czechia,8
2022,sf2,2022sf2,j,Romania,Estonia,7
2022,sf2,2022sf2,j,Romania,Belgium,6
2022,sf2,2022sf2,j,Romania,North Macedonia,5
2022,sf2,2022sf2,j,Romania,Finland,4
2022,sf2,2022sf2,j,Romania,Azerbaijan,3
2022,sf2,2022sf2,j,Romania,San Marino,2
2022,sf2,2022sf2,j,Romania,Israel,1
2022,sf2,2022sf2,t,San Marino,Serbia,12
2022,sf2,2022sf2,t,San Marino,Sweden,10
2022,sf2,2022sf2,t,San Marino,Romania,8
2022,sf2,2022sf2,t,San Marino,Australia,7
2022,sf2,2022sf2,t,San Marino,Czechia,6
2022,sf2,2022sf2,t,San Marino,Poland,5
2022,sf2,2022sf2,t,San Marino,Cyprus,4
2022,sf2,2022sf2,t,San Marino,Finland,3
2022,sf2,2022sf2,t,San Marino,Israel,2
2022,sf2,2022sf2,t,San Marino,Belgium,1
2022,sf2,2022sf2,j,San Marino,Sweden,12
2022,sf2,2022sf2,j,San Marino,Australia,10
2022,sf2,2022sf2,j,San Marino,Poland,8
2022,sf2,2022sf2,j,San Marino,Estonia,7
2022,sf2,2022sf2,j,San Marino,Czechia,6
2022,sf2,2022sf2,j,San Marino,Belgium,5
2022,sf2,2022sf2,j,San Marino,Azerbaijan,4
2022,sf2,2022sf2,j,San Marino,Finland,3
2022,sf2,2022sf2,j,San Marino,Serbia,2
2022,sf2,2022sf2,j,San Marino,Malta,1
2022,sf2,2022sf2,t,Serbia,Montenegro,12
2022,sf2,2022sf2,t,Serbia,Cyprus,10
2022,sf2,2022sf2,t,Serbia,North Macedonia,8
2022,sf2,2022sf2,t,Serbia,Czechia,7
2022,sf2,2022sf2,t,Serbia,Romania,6
2022,sf2,2022sf2,t,Serbia,Sweden,5
2022,sf2,2022sf2,t,Serbia,Estonia,4
2022,sf2,2022sf2,t,Serbia,Belgium,3
2022,sf2,2022sf2,t,Serbia,Malta,2
2022,sf2,2022sf2,t,Serbia,Finland,1
2022,sf2,2022sf2,j,Serbia,Sweden,12
2022,sf2,2022sf2,j,Serbia,Estonia,10
2022,sf2,2022sf2,j,Serbia,Azerbaijan,8
2022,sf2,2022sf2,j,Serbia,Montenegro,7
2022,sf2,2022sf2,j,Serbia,Belgium,6
2022,sf2,2022sf2,j,Serbia,Finland,5
2022,sf2,2022sf2,j,Serbia,Czechia,4
2022,sf2,2022sf2,j,Serbia,Poland,3
2022,sf2,2022sf2,j,Serbia,Australia,2
2022,sf2,2022sf2,j,Serbia,North Macedonia,1
2022,sf2,2022sf2,t,Spain,Romania,12
2022,sf2,2022sf2,t,Spain,Czechia,10
2022,sf2,2022sf2,t,Spain,Sweden,8
2022,sf2,2022sf2,t,Spain,Ireland,7
2022,sf2,2022sf2,t,Spain,Finland,6
2022,sf2,2022sf2,t,Spain,Serbia,5
2022,sf2,2022sf2,t,Spain,Poland,4
2022,sf2,2022sf2,t,Spain,San Marino,3
2022,sf2,2022sf2,t,Spain,Estonia,2
2022,sf2,2022sf2,t,Spain,Cyprus,1
2022,sf2,2022sf2,j,Spain,Azerbaijan,12
2022,sf2,2022sf2,j,Spain,Australia,10
2022,sf2,2022sf2,j,Spain,Belgium,8
2022,sf2,2022sf2,j,Spain,Poland,7
2022,sf2,2022sf2,j,Spain,Sweden,6
2022,sf2,2022sf2,j,Spain,Serbia,5
2022,sf2,2022sf2,j,Spain,Romania,4
2022,sf2,2022sf2,j,Spain,Israel,3
2022,sf2,2022sf2,j,Spain,Finland,2
2022,sf2,2022sf2,j,Spain,Montenegro,1
2022,sf2,2022sf2,t,Sweden,Finland,12
2022,sf2,2022sf2,t,Sweden,Serbia,10
2022,sf2,2022sf2,t,Sweden,Estonia,8
2022,sf2,2022sf2,t,Sweden,Poland,7
2022,sf2,2022sf2,t,Sweden,Czechia,6
2022,sf2,2022sf2,t,Sweden,Belgium,5
2022,sf2,2022sf2,t,Sweden,Australia,4
2022,sf2,2022sf2,t,Sweden,Romania,3
2022,sf2,2022sf2,t,Sweden,Malta,2
2022,sf2,2022sf2,t,Sweden,Cyprus,1
2022,sf2,2022sf2,j,Sweden,Australia,12
2022,sf2,2022sf2,j,Sweden,Estonia,10
2022,sf2,2022sf2,j,Sweden,Belgium,8
2022,sf2,2022sf2,j,Sweden,Malta,7
2022,sf2,2022sf2,j,Sweden,Czechia,6
2022,sf2,2022sf2,j,Sweden,Azerbaijan,5
2022,sf2,2022sf2,j,Sweden,Finland,4
2022,sf2,2022sf2,j,Sweden,Israel,3
2022,sf2,2022sf2,j,Sweden,Cyprus,2
2022,sf2,2022sf2,j,Sweden,Poland,1
2022,sf2,2022sf2,t,United Kingdom,Ireland,12
2022,sf2,2022sf2,t,United Kingdom,Poland,10
2022,sf2,2022sf2,t,United Kingdom,Czechia,8
2022,sf2,2022sf2,t,United Kingdom,Romania,7
2022,sf2,2022sf2,t,United Kingdom,Serbia,6
2022,sf2,2022sf2,t,United Kingdom,Sweden,5
2022,sf2,2022sf2,t,United Kingdom,Finland,4
2022,sf2,2022sf2,t,United Kingdom,San Marino,3
2022,sf2,2022sf2,t,United Kingdom,Estonia,2
2022,sf2,2022sf2,t,United Kingdom,Cyprus,1
2022,sf2,2022sf2,j,United Kingdom,Sweden,12
2022,sf2,2022sf2,j,United Kingdom,Czechia,10
2022,sf2,2022sf2,j,United Kingdom,Azerbaijan,8
2022,sf2,2022sf2,j,United Kingdom,North Macedonia,7
2022,sf2,2022sf2,j,United Kingdom,Poland,6
2022,sf2,2022sf2,j,United Kingdom,Serbia,5
2022,sf2,2022sf2,j,United Kingdom,Estonia,4
2022,sf2,2022sf2,j,United Kingdom,Australia,3
2022,sf2,2022sf2,j,United Kingdom,Belgium,2
2022,sf2,2022sf2,j,United Kingdom,Israel,1
2022,f,2022f,t,Albania,Greece,12
2022,f,2022f,t,Albania,Ukraine,10
2022,f,2022f,t,Albania,Italy,8
2022,f,2022f,t,Albania,Spain,7
2022,f,2022f,t,Albania,Netherlands,6
2022,f,2022f,t,Albania,Estonia,5
2022,f,2022f,t,Albania,United Kingdom,4
2022,f,2022f,t,Albania,Serbia,3
2022,f,2022f,t,Albania,Finland,2
2022,f,2022f,t,Albania,Moldova,1
2022,f,2022f,j,Albania,Italy,12
2022,f,2022f,j,Albania,United Kingdom,10
2022,f,2022f,j,Albania,Sweden,8
2022,f,2022f,j,Albania,Ukraine,7
2022,f,2022f,j,Albania,Netherlands,6
2022,f,2022f,j,Albania,Spain,5
2022,f,2022f,j,Albania,Armenia,4
2022,f,2022f,j,Albania,Azerbaijan,3
2022,f,2022f,j,Albania,Belgium,2
2022,f,2022f,j,Albania,Portugal,1
2022,f,2022f,t,Armenia,Estonia,12
2022,f,2022f,t,Armenia,Ukraine,10
2022,f,2022f,t,Armenia,Spain,8
2022,f,2022f,t,Armenia,Sweden,7
2022,f,2022f,t,Armenia,Serbia,6
2022,f,2022f,t,Armenia,Moldova,5
2022,f,2022f,t,Armenia,Portugal,4
2022,f,2022f,t,Armenia,Greece,3
2022,f,2022f,t,Armenia,Lithuania,2
2022,f,2022f,t,Armenia,United Kingdom,1
2022,f,2022f,j,Armenia,Spain,12
2022,f,2022f,j,Armenia,Italy,10
2022,f,2022f,j,Armenia,Portugal,8
2022,f,2022f,j,Armenia,France,7
2022,f,2022f,j,Armenia,Ukraine,6
2022,f,2022f,j,Armenia,Sweden,5
2022,f,2022f,j,Armenia,Netherlands,4
2022,f,2022f,j,Armenia,Estonia,3
2022,f,2022f,j,Armenia,Greece,2
2022,f,2022f,j,Armenia,Moldova,1
2022,f,2022f,t,Australia,Ukraine,12
2022,f,2022f,t,Australia,Norway,10
2022,f,2022f,t,Australia,Serbia,8
2022,f,2022f,t,Australia,United Kingdom,7
2022,f,2022f,t,Australia,Spain,6
2022,f,2022f,t,Australia,Sweden,5
2022,f,2022f,t,Australia,Moldova,4
2022,f,2022f,t,Australia,Poland,3
2022,f,2022f,t,Australia,Lithuania,2
2022,f,2022f,t,Australia,Italy,1
2022,f,2022f,j,Australia,Spain,12
2022,f,2022f,j,Australia,Sweden,10
2022,f,2022f,j,Australia,Serbia,8
2022,f,2022f,j,Australia,Ukraine,7
2022,f,2022f,j,Australia,Portugal,6
2022,f,2022f,j,Australia,Belgium,5
2022,f,2022f,j,Australia,Czechia,4
2022,f,2022f,j,Australia,Italy,3
2022,f,2022f,j,Australia,Azerbaijan,2
2022,f,2022f,j,Australia,Estonia,1
2022,f,2022f,t,Azerbaijan,Ukraine,12
2022,f,2022f,t,Azerbaijan,Spain,10
2022,f,2022f,t,Azerbaijan,United Kingdom,8
2022,f,2022f,t,Azerbaijan,Norway,7
2022,f,2022f,t,Azerbaijan,Serbia,6
2022,f,2022f,t,Azerbaijan,Italy,5
2022,f,2022f,t,Azerbaijan,Sweden,4
2022,f,2022f,t,Azerbaijan,Greece,3
2022,f,2022f,t,Azerbaijan,Australia,2
2022,f,2022f,t,Azerbaijan,Poland,1
2022,f,2022f,j,Azerbaijan,United Kingdom,12
2022,f,2022f,j,Azerbaijan,Italy,10
2022,f,2022f,j,Azerbaijan,Sweden,8
2022,f,2022f,j,Azerbaijan,Portugal,7
2022,f,2022f,j,Azerbaijan,Ukraine,6
2022,f,2022f,j,Azerbaijan,Spain,5
2022,f,2022f,j,Azerbaijan,Netherlands,4
2022,f,2022f,j,Azerbaijan,Greece,3
2022,f,2022f,j,Azerbaijan,Poland,2
2022,f,2022f,j,Azerbaijan,France,1
2022,f,2022f,t,Belgium,Ukraine,12
2022,f,2022f,t,Belgium,Netherlands,10
2022,f,2022f,t,Belgium,Moldova,8
2022,f,2022f,t,Belgium,Poland,7
2022,f,2022f,t,Belgium,Spain,6
2022,f,2022f,t,Belgium,Sweden,5
2022,f,2022f,t,Belgium,Italy,4
2022,f,2022f,t,Belgium,United Kingdom,3
2022,f,2022f,t,Belgium,Serbia,2
2022,f,2022f,t,Belgium,Portugal,1
2022,f,2022f,j,Belgium,United Kingdom,12
2022,f,2022f,j,Belgium,Spain,10
2022,f,2022f,j,Belgium,Italy,8
2022,f,2022f,j,Belgium,Sweden,7
2022,f,2022f,j,Belgium,Ukraine,6
2022,f,2022f,j,Belgium,Portugal,5
2022,f,2022f,j,Belgium,Serbia,4
2022,f,2022f,j,Belgium,Azerbaijan,3
2022,f,2022f,j,Belgium,Czechia,2
2022,f,2022f,j,Belgium,Australia,1
2022,f,2022f,t,Croatia,Serbia,12
2022,f,2022f,t,Croatia,Ukraine,10
2022,f,2022f,t,Croatia,Moldova,8
2022,f,2022f,t,Croatia,Spain,7
2022,f,2022f,t,Croatia,Italy,6
2022,f,2022f,t,Croatia,Norway,5
2022,f,2022f,t,Croatia,Sweden,4
2022,f,2022f,t,Croatia,Lithuania,3
2022,f,2022f,t,Croatia,Estonia,2
2022,f,2022f,t,Croatia,France,1
2022,f,2022f,j,Croatia,Serbia,12
2022,f,2022f,j,Croatia,Portugal,10
2022,f,2022f,j,Croatia,Ukraine,8
2022,f,2022f,j,Croatia,Lithuania,7
2022,f,2022f,j,Croatia,Spain,6
2022,f,2022f,j,Croatia,Sweden,5
2022,f,2022f,j,Croatia,Italy,4
2022,f,2022f,j,Croatia,Greece,3
2022,f,2022f,j,Croatia,Netherlands,2
2022,f,2022f,j,Croatia,Switzerland,1
2022,f,2022f,t,Cyprus,Ukraine,12
2022,f,2022f,t,Cyprus,Greece,10
2022,f,2022f,t,Cyprus,Spain,8
2022,f,2022f,t,Cyprus,Serbia,7
2022,f,2022f,t,Cyprus,United Kingdom,6
2022,f,2022f,t,Cyprus,Italy,5
2022,f,2022f,t,Cyprus,Romania,4
2022,f,2022f,t,Cyprus,Poland,3
2022,f,2022f,t,Cyprus,Lithuania,2
2022,f,2022f,t,Cyprus,Armenia,1
2022,f,2022f,j,Cyprus,Greece,12
2022,f,2022f,j,Cyprus,Azerbaijan,10
2022,f,2022f,j,Cyprus,Australia,8
2022,f,2022f,j,Cyprus,Ukraine,7
2022,f,2022f,j,Cyprus,Spain,6
2022,f,2022f,j,Cyprus,Sweden,5
2022,f,2022f,j,Cyprus,Serbia,4
2022,f,2022f,j,Cyprus,United Kingdom,3
2022,f,2022f,j,Cyprus,Belgium,2
2022,f,2022f,j,Cyprus,Italy,1
2022,f,2022f,t,Czechia,Ukraine,12
2022,f,2022f,t,Czechia,Serbia,10
2022,f,2022f,t,Czechia,Moldova,8
2022,f,2022f,t,Czechia,Poland,7
2022,f,2022f,t,Czechia,Spain,6
2022,f,2022f,t,Czechia,Sweden,5
2022,f,2022f,t,Czechia,Estonia,4
2022,f,2022f,t,Czechia,Norway,3
2022,f,2022f,t,Czechia,United Kingdom,2
2022,f,2022f,t,Czechia,Finland,1
2022,f,2022f,j,Czechia,United Kingdom,12
2022,f,2022f,j,Czechia,Sweden,10
2022,f,2022f,j,Czechia,Estonia,8
2022,f,2022f,j,Czechia,Spain,7
2022,f,2022f,j,Czechia,Switzerland,6
2022,f,2022f,j,Czechia,Portugal,5
2022,f,2022f,j,Czechia,Ukraine,4
2022,f,2022f,j,Czechia,Greece,3
2022,f,2022f,j,Czechia,Norway,2
2022,f,2022f,j,Czechia,Australia,1
2022,f,2022f,t,Denmark,Ukraine,12
2022,f,2022f,t,Denmark,Sweden,10
2022,f,2022f,t,Denmark,Norway,8
2022,f,2022f,t,Denmark,Lithuania,7
2022,f,2022f,t,Denmark,United Kingdom,6
2022,f,2022f,t,Denmark,Moldova,5
2022,f,2022f,t,Denmark,Poland,4
2022,f,2022f,t,Denmark,Estonia,3
2022,f,2022f,t,Denmark,Iceland,2
2022,f,2022f,t,Denmark,Spain,1
2022,f,2022f,j,Denmark,Greece,12
2022,f,2022f,j,Denmark,Netherlands,10
2022,f,2022f,j,Denmark,Portugal,8
2022,f,2022f,j,Denmark,Sweden,7
2022,f,2022f,j,Denmark,United Kingdom,6
2022,f,2022f,j,Denmark,Ukraine,5
2022,f,2022f,j,Denmark,Spain,4
2022,f,2022f,j,Denmark,Lithuania,3
2022,f,2022f,j,Denmark,Switzerland,2
2022,f,2022f,j,Denmark,Iceland,1
2022,f,2022f,t,Estonia,Ukraine,12
2022,f,2022f,t,Estonia,Sweden,10
2022,f,2022f,t,Estonia,Finland,8
2022,f,2022f,t,Estonia,Lithuania,7
2022,f,2022f,t,Estonia,Moldova,6
2022,f,2022f,t,Estonia,United Kingdom,5
2022,f,2022f,t,Estonia,Norway,4
2022,f,2022f,t,Estonia,Netherlands,3
2022,f,2022f,t,Estonia,Germany,2
2022,f,2022f,t,Estonia,Spain,1
2022,f,2022f,j,Estonia,Sweden,12
2022,f,2022f,j,Estonia,Italy,10
2022,f,2022f,j,Estonia,Australia,8
2022,f,2022f,j,Estonia,Portugal,7
2022,f,2022f,j,Estonia,Greece,6
2022,f,2022f,j,Estonia,Finland,5
2022,f,2022f,j,Estonia,United Kingdom,4
2022,f,2022f,j,Estonia,Azerbaijan,3
2022,f,2022f,j,Estonia,Lithuania,2
2022,f,2022f,j,Estonia,Netherlands,1
2022,f,2022f,t,Finland,Ukraine,12
2022,f,2022f,t,Finland,Estonia,10
2022,f,2022f,t,Finland,Sweden,8
2022,f,2022f,t,Finland,Serbia,7
2022,f,2022f,t,Finland,Norway,6
2022,f,2022f,t,Finland,Moldova,5
2022,f,2022f,t,Finland,United Kingdom,4
2022,f,2022f,t,Finland,Spain,3
2022,f,2022f,t,Finland,Lithuania,2
2022,f,2022f,t,Finland,France,1
2022,f,2022f,j,Finland,Sweden,12
2022,f,2022f,j,Finland,United Kingdom,10
2022,f,2022f,j,Finland,Australia,8
2022,f,2022f,j,Finland,Serbia,7
2022,f,2022f,j,Finland,Greece,6
2022,f,2022f,j,Finland,Netherlands,5
2022,f,2022f,j,Finland,Norway,4
2022,f,2022f,j,Finland,Azerbaijan,3
2022,f,2022f,j,Finland,Italy,2
2022,f,2022f,j,Finland,Armenia,1
2022,f,2022f,t,France,Ukraine,12
2022,f,2022f,t,France,Moldova,10
2022,f,2022f,t,France,Serbia,8
2022,f,2022f,t,France,Spain,7
2022,f,2022f,t,France,Portugal,6
2022,f,2022f,t,France,Armenia,5
2022,f,2022f,t,France,Poland,4
2022,f,2022f,t,France,Italy,3
2022,f,2022f,t,France,United Kingdom,2
2022,f,2022f,t,France,Romania,1
2022,f,2022f,j,France,United Kingdom,12
2022,f,2022f,j,France,Ukraine,10
2022,f,2022f,j,France,Poland,8
2022,f,2022f,j,France,Armenia,7
2022,f,2022f,j,France,Belgium,6
2022,f,2022f,j,France,Spain,5
2022,f,2022f,j,France,Netherlands,4
2022,f,2022f,j,France,Greece,3
2022,f,2022f,j,France,Czechia,2
2022,f,2022f,j,France,Portugal,1
2022,f,2022f,t,Georgia,Ukraine,12
2022,f,2022f,t,Georgia,Armenia,10
2022,f,2022f,t,Georgia,Moldova,8
2022,f,2022f,t,Georgia,Serbia,7
2022,f,2022f,t,Georgia,Spain,6
2022,f,2022f,t,Georgia,Lithuania,5
2022,f,2022f,t,Georgia,United Kingdom,4
2022,f,2022f,t,Georgia,Azerbaijan,3
2022,f,2022f,t,Georgia,Finland,2
2022,f,2022f,t,Georgia,Greece,1
2022,f,2022f,j,Georgia,United Kingdom,12
2022,f,2022f,j,Georgia,Italy,10
2022,f,2022f,j,Georgia,Sweden,8
2022,f,2022f,j,Georgia,Portugal,7
2022,f,2022f,j,Georgia,Ukraine,6
2022,f,2022f,j,Georgia,Spain,5
2022,f,2022f,j,Georgia,Netherlands,4
2022,f,2022f,j,Georgia,Greece,3
2022,f,2022f,j,Georgia,Poland,2
2022,f,2022f,j,Georgia,France,1
2022,f,2022f,t,Germany,Ukraine,12
2022,f,2022f,t,Germany,Moldova,10
2022,f,2022f,t,Germany,Poland,8
2022,f,2022f,t,Germany,Serbia,7
2022,f,2022f,t,Germany,United Kingdom,6
2022,f,2022f,t,Germany,Sweden,5
2022,f,2022f,t,Germany,Netherlands,4
2022,f,2022f,t,Germany,Italy,3
2022,f,2022f,t,Germany,Spain,2
2022,f,2022f,t,Germany,Norway,1
2022,f,2022f,j,Germany,United Kingdom,12
2022,f,2022f,j,Germany,Ukraine,10
2022,f,2022f,j,Germany,Spain,8
2022,f,2022f,j,Germany,Sweden,7
2022,f,2022f,j,Germany,Azerbaijan,6
2022,f,2022f,j,Germany,Australia,5
2022,f,2022f,j,Germany,Netherlands,4
2022,f,2022f,j,Germany,Norway,3
2022,f,2022f,j,Germany,Switzerland,2
2022,f,2022f,j,Germany,Romania,1
2022,f,2022f,t,Greece,Spain,12
2022,f,2022f,t,Greece,Ukraine,10
2022,f,2022f,t,Greece,Serbia,8
2022,f,2022f,t,Greece,Italy,7
2022,f,2022f,t,Greece,Norway,6
2022,f,2022f,t,Greece,United Kingdom,5
2022,f,2022f,t,Greece,Sweden,4
2022,f,2022f,t,Greece,Moldova,3
2022,f,2022f,t,Greece,Romania,2
2022,f,2022f,t,Greece,France,1
2022,f,2022f,j,Greece,Azerbaijan,12
2022,f,2022f,j,Greece,Poland,10
2022,f,2022f,j,Greece,Australia,8
2022,f,2022f,j,Greece,Romania,7
2022,f,2022f,j,Greece,Moldova,6
2022,f,2022f,j,Greece,Spain,5
2022,f,2022f,j,Greece,Netherlands,4
2022,f,2022f,j,Greece,Portugal,3
2022,f,2022f,j,Greece,Czechia,2
2022,f,2022f,j,Greece,Italy,1
2022,f,2022f,t,Iceland,Ukraine,12
2022,f,2022f,t,Iceland,Norway,10
2022,f,2022f,t,Iceland,Sweden,8
2022,f,2022f,t,Iceland,United Kingdom,7
2022,f,2022f,t,Iceland,Moldova,6
2022,f,2022f,t,Iceland,Netherlands,5
2022,f,2022f,t,Iceland,Poland,4
2022,f,2022f,t,Iceland,Spain,3
2022,f,2022f,t,Iceland,Lithuania,2
2022,f,2022f,t,Iceland,Serbia,1
2022,f,2022f,j,Iceland,Sweden,12
2022,f,2022f,j,Iceland,Ukraine,10
2022,f,2022f,j,Iceland,Norway,8
2022,f,2022f,j,Iceland,United Kingdom,7
2022,f,2022f,j,Iceland,Italy,6
2022,f,2022f,j,Iceland,Portugal,5
2022,f,2022f,j,Iceland,Netherlands,4
2022,f,2022f,j,Iceland,Spain,3
2022,f,2022f,j,Iceland,Czechia,2
2022,f,2022f,j,Iceland,Lithuania,1
2022,f,2022f,t,Ireland,Ukraine,12
2022,f,2022f,t,Ireland,Poland,10
2022,f,2022f,t,Ireland,Lithuania,8
2022,f,2022f,t,Ireland,Moldova,7
2022,f,2022f,t,Ireland,United Kingdom,6
2022,f,2022f,t,Ireland,Spain,5
2022,f,2022f,t,Ireland,Norway,4
2022,f,2022f,t,Ireland,Sweden,3
2022,f,2022f,t,Ireland,Romania,2
2022,f,2022f,t,Ireland,Serbia,1
2022,f,2022f,j,Ireland,Spain,12
2022,f,2022f,j,Ireland,Sweden,10
2022,f,2022f,j,Ireland,United Kingdom,8
2022,f,2022f,j,Ireland,Czechia,7
2022,f,2022f,j,Ireland,Italy,6
2022,f,2022f,j,Ireland,Serbia,5
2022,f,2022f,j,Ireland,Portugal,4
2022,f,2022f,j,Ireland,Ukraine,3
2022,f,2022f,j,Ireland,Australia,2
2022,f,2022f,j,Ireland,Iceland,1
2022,f,2022f,t,Israel,Ukraine,12
2022,f,2022f,t,Israel,United Kingdom,10
2022,f,2022f,t,Israel,Spain,8
2022,f,2022f,t,Israel,Serbia,7
2022,f,2022f,t,Israel,Moldova,6
2022,f,2022f,t,Israel,Sweden,5
2022,f,2022f,t,Israel,Norway,4
2022,f,2022f,t,Israel,Italy,3
2022,f,2022f,t,Israel,Netherlands,2
2022,f,2022f,t,Israel,Poland,1
2022,f,2022f,j,Israel,Sweden,12
2022,f,2022f,j,Israel,United Kingdom,10
2022,f,2022f,j,Israel,Italy,8
2022,f,2022f,j,Israel,Ukraine,7
2022,f,2022f,j,Israel,Poland,6
2022,f,2022f,j,Israel,Australia,5
2022,f,2022f,j,Israel,Belgium,4
2022,f,2022f,j,Israel,Spain,3
2022,f,2022f,j,Israel,Czechia,2
2022,f,2022f,j,Israel,Netherlands,1
2022,f,2022f,t,Italy,Ukraine,12
2022,f,2022f,t,Italy,Moldova,10
2022,f,2022f,t,Italy,Romania,8
2022,f,2022f,t,Italy,Serbia,7
2022,f,2022f,t,Italy,United Kingdom,6
2022,f,2022f,t,Italy,Sweden,5
2022,f,2022f,t,Italy,Norway,4
2022,f,2022f,t,Italy,Poland,3
2022,f,2022f,t,Italy,Netherlands,2
2022,f,2022f,t,Italy,Portugal,1
2022,f,2022f,j,Italy,Netherlands,12
2022,f,2022f,j,Italy,Greece,10
2022,f,2022f,j,Italy,Armenia,8
2022,f,2022f,j,Italy,Belgium,7
2022,f,2022f,j,Italy,United Kingdom,6
2022,f,2022f,j,Italy,Moldova,5
2022,f,2022f,j,Italy,Serbia,4
2022,f,2022f,j,Italy,Switzerland,3
2022,f,2022f,j,Italy,Australia,2
2022,f,2022f,j,Italy,Finland,1
2022,f,2022f,t,Latvia,Ukraine,12
2022,f,2022f,t,Latvia,Lithuania,10
2022,f,2022f,t,Latvia,Estonia,8
2022,f,2022f,t,Latvia,Moldova,7
2022,f,2022f,t,Latvia,Sweden,6
2022,f,2022f,t,Latvia,Norway,5
2022,f,2022f,t,Latvia,Spain,4
2022,f,2022f,t,Latvia,United Kingdom,3
2022,f,2022f,t,Latvia,Serbia,2
2022,f,2022f,t,Latvia,Finland,1
2022,f,2022f,j,Latvia,Ukraine,12
2022,f,2022f,j,Latvia,Sweden,10
2022,f,2022f,j,Latvia,United Kingdom,8
2022,f,2022f,j,Latvia,Greece,7
2022,f,2022f,j,Latvia,Portugal,6
2022,f,2022f,j,Latvia,Norway,5
2022,f,2022f,j,Latvia,Netherlands,4
2022,f,2022f,j,Latvia,Switzerland,3
2022,f,2022f,j,Latvia,Australia,2
2022,f,2022f,j,Latvia,Lithuania,1
2022,f,2022f,t,Lithuania,Ukraine,12
2022,f,2022f,t,Lithuania,Sweden,10
2022,f,2022f,t,Lithuania,Estonia,8
2022,f,2022f,t,Lithuania,Portugal,7
2022,f,2022f,t,Lithuania,Spain,6
2022,f,2022f,t,Lithuania,Moldova,5
2022,f,2022f,t,Lithuania,United Kingdom,4
2022,f,2022f,t,Lithuania,Italy,3
2022,f,2022f,t,Lithuania,Norway,2
2022,f,2022f,t,Lithuania,Netherlands,1
2022,f,2022f,j,Lithuania,Ukraine,12
2022,f,2022f,j,Lithuania,United Kingdom,10
2022,f,2022f,j,Lithuania,Portugal,8
2022,f,2022f,j,Lithuania,Switzerland,7
2022,f,2022f,j,Lithuania,Netherlands,6
2022,f,2022f,j,Lithuania,Spain,5
2022,f,2022f,j,Lithuania,Italy,4
2022,f,2022f,j,Lithuania,Sweden,3
2022,f,2022f,j,Lithuania,Iceland,2
2022,f,2022f,j,Lithuania,Serbia,1
2022,f,2022f,t,Malta,United Kingdom,12
2022,f,2022f,t,Malta,Italy,10
2022,f,2022f,t,Malta,Ukraine,8
2022,f,2022f,t,Malta,Spain,7
2022,f,2022f,t,Malta,Serbia,6
2022,f,2022f,t,Malta,Sweden,5
2022,f,2022f,t,Malta,Norway,4
2022,f,2022f,t,Malta,Romania,3
2022,f,2022f,t,Malta,Poland,2
2022,f,2022f,t,Malta,Finland,1
2022,f,2022f,j,Malta,Spain,12
2022,f,2022f,j,Malta,Sweden,10
2022,f,2022f,j,Malta,United Kingdom,8
2022,f,2022f,j,Malta,Italy,7
2022,f,2022f,j,Malta,Australia,6
2022,f,2022f,j,Malta,Estonia,5
2022,f,2022f,j,Malta,Poland,4
2022,f,2022f,j,Malta,Czechia,3
2022,f,2022f,j,Malta,Azerbaijan,2
2022,f,2022f,j,Malta,Greece,1
2022,f,2022f,t,Moldova,Ukraine,12
2022,f,2022f,t,Moldova,Romania,10
2022,f,2022f,t,Moldova,Spain,8
2022,f,2022f,t,Moldova,Estonia,7
2022,f,2022f,t,Moldova,Norway,6
2022,f,2022f,t,Moldova,Sweden,5
2022,f,2022f,t,Moldova,Lithuania,4
2022,f,2022f,t,Moldova,United Kingdom,3
2022,f,2022f,t,Moldova,France,2
2022,f,2022f,t,Moldova,Belgium,1
2022,f,2022f,j,Moldova,Ukraine,12
2022,f,2022f,j,Moldova,United Kingdom,10
2022,f,2022f,j,Moldova,Sweden,8
2022,f,2022f,j,Moldova,Switzerland,7
2022,f,2022f,j,Moldova,Australia,6
2022,f,2022f,j,Moldova,Estonia,5
2022,f,2022f,j,Moldova,Belgium,4
2022,f,2022f,j,Moldova,Spain,3
2022,f,2022f,j,Moldova,Portugal,2
2022,f,2022f,j,Moldova,Azerbaijan,1
2022,f,2022f,t,Montenegro,Serbia,12
2022,f,2022f,t,Montenegro,Ukraine,10
2022,f,2022f,t,Montenegro,Spain,8
2022,f,2022f,t,Montenegro,Moldova,7
2022,f,2022f,t,Montenegro,Italy,6
2022,f,2022f,t,Montenegro,Portugal,5
2022,f,2022f,t,Montenegro,Poland,4
2022,f,2022f,t,Montenegro,Estonia,3
2022,f,2022f,t,Montenegro,Norway,2
2022,f,2022f,t,Montenegro,Sweden,1
2022,f,2022f,j,Montenegro,Serbia,12
2022,f,2022f,j,Montenegro,Italy,10
2022,f,2022f,j,Montenegro,Spain,8
2022,f,2022f,j,Montenegro,Sweden,7
2022,f,2022f,j,Montenegro,Ukraine,6
2022,f,2022f,j,Montenegro,United Kingdom,5
2022,f,2022f,j,Montenegro,Portugal,4
2022,f,2022f,j,Montenegro,Netherlands,3
2022,f,2022f,j,Montenegro,Lithuania,2
2022,f,2022f,j,Montenegro,Azerbaijan,1
2022,f,2022f,t,Netherlands,Ukraine,12
2022,f,2022f,t,Netherlands,Moldova,10
2022,f,2022f,t,Netherlands,United Kingdom,8
2022,f,2022f,t,Netherlands,Spain,7
2022,f,2022f,t,Netherlands,Poland,6
2022,f,2022f,t,Netherlands,Norway,5
2022,f,2022f,t,Netherlands,Belgium,4
2022,f,2022f,t,Netherlands,Serbia,3
2022,f,2022f,t,Netherlands,Sweden,2
2022,f,2022f,t,Netherlands,Estonia,1
2022,f,2022f,j,Netherlands,Greece,12
2022,f,2022f,j,Netherlands,Switzerland,10
2022,f,2022f,j,Netherlands,Portugal,8
2022,f,2022f,j,Netherlands,Australia,7
2022,f,2022f,j,Netherlands,Belgium,6
2022,f,2022f,j,Netherlands,Spain,5
2022,f,2022f,j,Netherlands,United Kingdom,4
2022,f,2022f,j,Netherlands,Norway,3
2022,f,2022f,j,Netherlands,Moldova,2
2022,f,2022f,j,Netherlands,Sweden,1
2022,f,2022f,t,North Macedonia,Serbia,12
2022,f,2022f,t,North Macedonia,Spain,10
2022,f,2022f,t,North Macedonia,Ukraine,8
2022,f,2022f,t,North Macedonia,Moldova,7
2022,f,2022f,t,North Macedonia,Italy,6
2022,f,2022f,t,North Macedonia,Czechia,5
2022,f,2022f,t,North Macedonia,Sweden,4
2022,f,2022f,t,North Macedonia,Estonia,3
2022,f,2022f,t,North Macedonia,Norway,2
2022,f,2022f,t,North Macedonia,Lithuania,1
2022,f,2022f,j,North Macedonia,Spain,12
2022,f,2022f,j,North Macedonia,Serbia,10
2022,f,2022f,j,North Macedonia,United Kingdom,8
2022,f,2022f,j,North Macedonia,Italy,7
2022,f,2022f,j,North Macedonia,Sweden,6
2022,f,2022f,j,North Macedonia,Australia,5
2022,f,2022f,j,North Macedonia,Azerbaijan,4
2022,f,2022f,j,North Macedonia,Belgium,3
2022,f,2022f,j,North Macedonia,Poland,2
2022,f,2022f,j,North Macedonia,Switzerland,1
2022,f,2022f,t,Norway,Ukraine,12
2022,f,2022f,t,Norway,Lithuania,10
2022,f,2022f,t,Norway,Sweden,8
2022,f,2022f,t,Norway,Greece,7
2022,f,2022f,t,Norway,United Kingdom,6
2022,f,2022f,t,Norway,Poland,5
2022,f,2022f,t,Norway,Moldova,4
2022,f,2022f,t,Norway,Serbia,3
2022,f,2022f,t,Norway,Estonia,2
2022,f,2022f,t,Norway,Spain,1
2022,f,2022f,j,Norway,Greece,12
2022,f,2022f,j,Norway,Portugal,10
2022,f,2022f,j,Norway,Sweden,8
2022,f,2022f,j,Norway,Spain,7
2022,f,2022f,j,Norway,United Kingdom,6
2022,f,2022f,j,Norway,Netherlands,5
2022,f,2022f,j,Norway,Armenia,4
2022,f,2022f,j,Norway,Ukraine,3
2022,f,2022f,j,Norway,Lithuania,2
2022,f,2022f,j,Norway,Switzerland,1
2022,f,2022f,t,Poland,Ukraine,12
2022,f,2022f,t,Poland,Sweden,10
2022,f,2022f,t,Poland,Estonia,8
2022,f,2022f,t,Poland,Moldova,7
2022,f,2022f,t,Poland,Spain,6
2022,f,2022f,t,Poland,Serbia,5
2022,f,2022f,t,Poland,Norway,4
2022,f,2022f,t,Poland,United Kingdom,3
2022,f,2022f,t,Poland,Lithuania,2
2022,f,2022f,t,Poland,Portugal,1
2022,f,2022f,j,Poland,Ukraine,12
2022,f,2022f,j,Poland,Sweden,10
2022,f,2022f,j,Poland,United Kingdom,8
2022,f,2022f,j,Poland,Portugal,7
2022,f,2022f,j,Poland,Australia,6
2022,f,2022f,j,Poland,Switzerland,5
2022,f,2022f,j,Poland,Italy,4
2022,f,2022f,j,Poland,Netherlands,3
2022,f,2022f,j,Poland,Greece,2
2022,f,2022f,j,Poland,Spain,1
2022,f,2022f,t,Portugal,Ukraine,12
2022,f,2022f,t,Portugal,Spain,10
2022,f,2022f,t,Portugal,Moldova,8
2022,f,2022f,t,Portugal,Sweden,7
2022,f,2022f,t,Portugal,United Kingdom,6
2022,f,2022f,t,Portugal,Serbia,5
2022,f,2022f,t,Portugal,Netherlands,4
2022,f,2022f,t,Portugal,Italy,3
2022,f,2022f,t,Portugal,Norway,2
2022,f,2022f,t,Portugal,Lithuania,1
2022,f,2022f,j,Portugal,Spain,12
2022,f,2022f,j,Portugal,United Kingdom,10
2022,f,2022f,j,Portugal,Ukraine,8
2022,f,2022f,j,Portugal,Netherlands,7
2022,f,2022f,j,Portugal,Iceland,6
2022,f,2022f,j,Portugal,Lithuania,5
2022,f,2022f,j,Portugal,Greece,4
2022,f,2022f,j,Portugal,Serbia,3
2022,f,2022f,j,Portugal,Switzerland,2
2022,f,2022f,j,Portugal,Armenia,1
2022,f,2022f,t,Romania,Moldova,12
2022,f,2022f,t,Romania,Ukraine,10
2022,f,2022f,t,Romania,Spain,8
2022,f,2022f,t,Romania,Serbia,7
2022,f,2022f,t,Romania,Sweden,6
2022,f,2022f,t,Romania,Estonia,5
2022,f,2022f,t,Romania,Italy,4
2022,f,2022f,t,Romania,United Kingdom,3
2022,f,2022f,t,Romania,Norway,2
2022,f,2022f,t,Romania,France,1
2022,f,2022f,j,Romania,Ukraine,12
2022,f,2022f,j,Romania,Sweden,10
2022,f,2022f,j,Romania,United Kingdom,8
2022,f,2022f,j,Romania,Portugal,7
2022,f,2022f,j,Romania,Australia,6
2022,f,2022f,j,Romania,Switzerland,5
2022,f,2022f,j,Romania,Italy,4
2022,f,2022f,j,Romania,Netherlands,3
2022,f,2022f,j,Romania,Greece,2
2022,f,2022f,j,Romania,Spain,1
2022,f,2022f,t,San Marino,Ukraine,12
2022,f,2022f,t,San Marino,Spain,10
2022,f,2022f,t,San Marino,Serbia,8
2022,f,2022f,t,San Marino,Greece,7
2022,f,2022f,t,San Marino,United Kingdom,6
2022,f,2022f,t,San Marino,Italy,5
2022,f,2022f,t,San Marino,Moldova,4
2022,f,2022f,t,San Marino,Sweden,3
2022,f,2022f,t,San Marino,Norway,2
2022,f,2022f,t,San Marino,Romania,1
2022,f,2022f,j,San Marino,Spain,12
2022,f,2022f,j,San Marino,Greece,10
2022,f,2022f,j,San Marino,United Kingdom,8
2022,f,2022f,j,San Marino,Azerbaijan,7
2022,f,2022f,j,San Marino,Australia,6
2022,f,2022f,j,San Marino,Sweden,5
2022,f,2022f,j,San Marino,Poland,4
2022,f,2022f,j,San Marino,Italy,3
2022,f,2022f,j,San Marino,Ukraine,2
2022,f,2022f,j,San Marino,Switzerland,1
2022,f,2022f,t,Serbia,Moldova,12
2022,f,2022f,t,Serbia,Spain,10
2022,f,2022f,t,Serbia,Norway,8
2022,f,2022f,t,Serbia,Ukraine,7
2022,f,2022f,t,Serbia,Estonia,6
2022,f,2022f,t,Serbia,Romania,5
2022,f,2022f,t,Serbia,Italy,4
2022,f,2022f,t,Serbia,Lithuania,3
2022,f,2022f,t,Serbia,France,2
2022,f,2022f,t,Serbia,Sweden,1
2022,f,2022f,j,Serbia,Azerbaijan,12
2022,f,2022f,j,Serbia,Estonia,10
2022,f,2022f,j,Serbia,Belgium,8
2022,f,2022f,j,Serbia,Portugal,7
2022,f,2022f,j,Serbia,Finland,6
2022,f,2022f,j,Serbia,Sweden,5
2022,f,2022f,j,Serbia,Spain,4
2022,f,2022f,j,Serbia,Czechia,3
2022,f,2022f,j,Serbia,Lithuania,2
2022,f,2022f,j,Serbia,United Kingdom,1
2022,f,2022f,t,Slovenia,Serbia,12
2022,f,2022f,t,Slovenia,Ukraine,10
2022,f,2022f,t,Slovenia,Greece,8
2022,f,2022f,t,Slovenia,Moldova,7
2022,f,2022f,t,Slovenia,Italy,6
2022,f,2022f,t,Slovenia,Sweden,5
2022,f,2022f,t,Slovenia,Spain,4
2022,f,2022f,t,Slovenia,Norway,3
2022,f,2022f,t,Slovenia,Lithuania,2
2022,f,2022f,t,Slovenia,Netherlands,1
2022,f,2022f,j,Slovenia,Italy,12
2022,f,2022f,j,Slovenia,Lithuania,10
2022,f,2022f,j,Slovenia,Ukraine,8
2022,f,2022f,j,Slovenia,Netherlands,7
2022,f,2022f,j,Slovenia,Serbia,6
2022,f,2022f,j,Slovenia,Switzerland,5
2022,f,2022f,j,Slovenia,Greece,4
2022,f,2022f,j,Slovenia,Portugal,3
2022,f,2022f,j,Slovenia,United Kingdom,2
2022,f,2022f,j,Slovenia,Spain,1
2022,f,2022f,t,Spain,Ukraine,12
2022,f,2022f,t,Spain,Romania,10
2022,f,2022f,t,Spain,United Kingdom,8
2022,f,2022f,t,Spain,Moldova,7
2022,f,2022f,t,Spain,Sweden,6
2022,f,2022f,t,Spain,Italy,5
2022,f,2022f,t,Spain,Portugal,4
2022,f,2022f,t,Spain,Norway,3
2022,f,2022f,t,Spain,Serbia,2
2022,f,2022f,t,Spain,Poland,1
2022,f,2022f,j,Spain,Azerbaijan,12
2022,f,2022f,j,Spain,Italy,10
2022,f,2022f,j,Spain,Australia,8
2022,f,2022f,j,Spain,Sweden,7
2022,f,2022f,j,Spain,Serbia,6
2022,f,2022f,j,Spain,Belgium,5
2022,f,2022f,j,Spain,Romania,4
2022,f,2022f,j,Spain,United Kingdom,3
2022,f,2022f,j,Spain,Greece,2
2022,f,2022f,j,Spain,Switzerland,1
2022,f,2022f,t,Sweden,Ukraine,12
2022,f,2022f,t,Sweden,Norway,10
2022,f,2022f,t,Sweden,Serbia,8
2022,f,2022f,t,Sweden,Finland,7
2022,f,2022f,t,Sweden,United Kingdom,6
2022,f,2022f,t,Sweden,Poland,5
2022,f,2022f,t,Sweden,Estonia,4
2022,f,2022f,t,Sweden,Lithuania,3
2022,f,2022f,t,Sweden,Spain,2
2022,f,2022f,t,Sweden,Netherlands,1
2022,f,2022f,j,Sweden,Spain,12
2022,f,2022f,j,Sweden,Australia,10
2022,f,2022f,j,Sweden,United Kingdom,8
2022,f,2022f,j,Sweden,Azerbaijan,7
2022,f,2022f,j,Sweden,Estonia,6
2022,f,2022f,j,Sweden,Czechia,5
2022,f,2022f,j,Sweden,Serbia,4
2022,f,2022f,j,Sweden,Norway,3
2022,f,2022f,j,Sweden,Armenia,2
2022,f,2022f,j,Sweden,Belgium,1
2022,f,2022f,t,Switzerland,Serbia,12
2022,f,2022f,t,Switzerland,Ukraine,10
2022,f,2022f,t,Switzerland,Italy,8
2022,f,2022f,t,Switzerland,Portugal,7
2022,f,2022f,t,Switzerland,Spain,6
2022,f,2022f,t,Switzerland,United Kingdom,5
2022,f,2022f,t,Switzerland,Moldova,4
2022,f,2022f,t,Switzerland,Sweden,3
2022,f,2022f,t,Switzerland,Germany,2
2022,f,2022f,t,Switzerland,Poland,1
2022,f,2022f,j,Switzerland,Greece,12
2022,f,2022f,j,Switzerland,Netherlands,10
2022,f,2022f,j,Switzerland,Spain,8
2022,f,2022f,j,Switzerland,Sweden,7
2022,f,2022f,j,Switzerland,United Kingdom,6
2022,f,2022f,j,Switzerland,Portugal,5
2022,f,2022f,j,Switzerland,Australia,4
2022,f,2022f,j,Switzerland,Ukraine,3
2022,f,2022f,j,Switzerland,Italy,2
2022,f,2022f,j,Switzerland,Norway,1
2022,f,2022f,t,Ukraine,Poland,12
2022,f,2022f,t,Ukraine,Lithuania,10
2022,f,2022f,t,Ukraine,Iceland,8
2022,f,2022f,t,Ukraine,United Kingdom,7
2022,f,2022f,t,Ukraine,Moldova,6
2022,f,2022f,t,Ukraine,Estonia,5
2022,f,2022f,t,Ukraine,Finland,4
2022,f,2022f,t,Ukraine,Netherlands,3
2022,f,2022f,t,Ukraine,Norway,2
2022,f,2022f,t,Ukraine,Spain,1
2022,f,2022f,j,Ukraine,United Kingdom,12
2022,f,2022f,j,Ukraine,Portugal,10
2022,f,2022f,j,Ukraine,Netherlands,8
2022,f,2022f,j,Ukraine,Greece,7
2022,f,2022f,j,Ukraine,Switzerland,6
2022,f,2022f,j,Ukraine,Azerbaijan,5
2022,f,2022f,j,Ukraine,Sweden,4
2022,f,2022f,j,Ukraine,Australia,3
2022,f,2022f,j,Ukraine,Armenia,2
2022,f,2022f,j,Ukraine,Czechia,1
2022,f,2022f,t,United Kingdom,Ukraine,12
2022,f,2022f,t,United Kingdom,Poland,10
2022,f,2022f,t,United Kingdom,Moldova,8
2022,f,2022f,t,United Kingdom,Lithuania,7
2022,f,2022f,t,United Kingdom,Norway,6
2022,f,2022f,t,United Kingdom,Spain,5
2022,f,2022f,t,United Kingdom,Sweden,4
2022,f,2022f,t,United Kingdom,Romania,3
2022,f,2022f,t,United Kingdom,Estonia,2
2022,f,2022f,t,United Kingdom,Serbia,1
2022,f,2022f,j,United Kingdom,Sweden,12
2022,f,2022f,j,United Kingdom,Spain,10
2022,f,2022f,j,United Kingdom,Poland,8
2022,f,2022f,j,United Kingdom,Azerbaijan,7
2022,f,2022f,j,United Kingdom,Australia,6
2022,f,2022f,j,United Kingdom,Estonia,5
2022,f,2022f,j,United Kingdom,Greece,4
2022,f,2022f,j,United Kingdom,Portugal,3
2022,f,2022f,j,United Kingdom,Switzerland,2
2022,f,2022f,j,United Kingdom,Serbia,1"""

data22 = StringIO(data22)
df_22 = pd.read_csv(data22)
df75_22 = pd.concat([df75_21, df_22], ignore_index=True)

df75_22.to_csv("Data Preparation/Datasets/eurovision_song_contest_1975_2022.csv")
df75_22.to_excel("Data Preparation/Datasets/eurovision_song_contest_1975_2022.xlsx")

data24 = """Year,(semi-) final,Edition,Jury or Televoting,From country,To country,Points
2024,sf1,2024sf1,t,Australia,Croatia,12
2024,sf1,2024sf1,t,Australia,Ireland,10
2024,sf1,2024sf1,t,Australia,Ukraine,8
2024,sf1,2024sf1,t,Australia,Cyprus,7
2024,sf1,2024sf1,t,Australia,Lithuania,6
2024,sf1,2024sf1,t,Australia,Finland,5
2024,sf1,2024sf1,t,Australia,Luxembourg,4
2024,sf1,2024sf1,t,Australia,Slovenia,3
2024,sf1,2024sf1,t,Australia,Portugal,2
2024,sf1,2024sf1,t,Australia,Poland,1
2024,sf1,2024sf1,t,Azerbaijan,Cyprus,12
2024,sf1,2024sf1,t,Azerbaijan,Ukraine,10
2024,sf1,2024sf1,t,Azerbaijan,Luxembourg,8
2024,sf1,2024sf1,t,Azerbaijan,Croatia,7
2024,sf1,2024sf1,t,Azerbaijan,Ireland,6
2024,sf1,2024sf1,t,Azerbaijan,Serbia,5
2024,sf1,2024sf1,t,Azerbaijan,Portugal,4
2024,sf1,2024sf1,t,Azerbaijan,Lithuania,3
2024,sf1,2024sf1,t,Azerbaijan,Moldova,2
2024,sf1,2024sf1,t,Azerbaijan,Slovenia,1
2024,sf1,2024sf1,t,Croatia,Serbia,12
2024,sf1,2024sf1,t,Croatia,Slovenia,10
2024,sf1,2024sf1,t,Croatia,Ukraine,8
2024,sf1,2024sf1,t,Croatia,Luxembourg,7
2024,sf1,2024sf1,t,Croatia,Ireland,6
2024,sf1,2024sf1,t,Croatia,Finland,5
2024,sf1,2024sf1,t,Croatia,Cyprus,4
2024,sf1,2024sf1,t,Croatia,Lithuania,3
2024,sf1,2024sf1,t,Croatia,Portugal,2
2024,sf1,2024sf1,t,Croatia,Moldova,1
2024,sf1,2024sf1,t,Cyprus,Ukraine,12
2024,sf1,2024sf1,t,Cyprus,Lithuania,10
2024,sf1,2024sf1,t,Cyprus,Luxembourg,8
2024,sf1,2024sf1,t,Cyprus,Croatia,7
2024,sf1,2024sf1,t,Cyprus,Ireland,6
2024,sf1,2024sf1,t,Cyprus,Serbia,5
2024,sf1,2024sf1,t,Cyprus,Portugal,4
2024,sf1,2024sf1,t,Cyprus,Moldova,3
2024,sf1,2024sf1,t,Cyprus,Slovenia,2
2024,sf1,2024sf1,t,Cyprus,Iceland,1
2024,sf1,2024sf1,t,Finland,Croatia,12
2024,sf1,2024sf1,t,Finland,Ukraine,10
2024,sf1,2024sf1,t,Finland,Ireland,8
2024,sf1,2024sf1,t,Finland,Lithuania,7
2024,sf1,2024sf1,t,Finland,Luxembourg,6
2024,sf1,2024sf1,t,Finland,Australia,5
2024,sf1,2024sf1,t,Finland,Portugal,4
2024,sf1,2024sf1,t,Finland,Slovenia,3
2024,sf1,2024sf1,t,Finland,Cyprus,2
2024,sf1,2024sf1,t,Finland,Azerbaijan,1
2024,sf1,2024sf1,t,Germany,Croatia,12
2024,sf1,2024sf1,t,Germany,Ukraine,10
2024,sf1,2024sf1,t,Germany,Lithuania,8
2024,sf1,2024sf1,t,Germany,Luxembourg,7
2024,sf1,2024sf1,t,Germany,Ireland,6
2024,sf1,2024sf1,t,Germany,Serbia,5
2024,sf1,2024sf1,t,Germany,Australia,4
2024,sf1,2024sf1,t,Germany,Finland,3
2024,sf1,2024sf1,t,Germany,Poland,2
2024,sf1,2024sf1,t,Germany,Portugal,1
2024,sf1,2024sf1,t,Iceland,Croatia,12
2024,sf1,2024sf1,t,Iceland,Ukraine,10
2024,sf1,2024sf1,t,Iceland,Poland,8
2024,sf1,2024sf1,t,Iceland,Lithuania,7
2024,sf1,2024sf1,t,Iceland,Finland,6
2024,sf1,2024sf1,t,Iceland,Luxembourg,5
2024,sf1,2024sf1,t,Iceland,Cyprus,4
2024,sf1,2024sf1,t,Iceland,Ireland,3
2024,sf1,2024sf1,t,Iceland,Australia,2
2024,sf1,2024sf1,t,Iceland,Portugal,1
2024,sf1,2024sf1,t,Ireland,Lithuania,12
2024,sf1,2024sf1,t,Ireland,Croatia,10
2024,sf1,2024sf1,t,Ireland,Ukraine,8
2024,sf1,2024sf1,t,Ireland,Poland,7
2024,sf1,2024sf1,t,Ireland,Luxembourg,6
2024,sf1,2024sf1,t,Ireland,Finland,5
2024,sf1,2024sf1,t,Ireland,Australia,4
2024,sf1,2024sf1,t,Ireland,Portugal,3
2024,sf1,2024sf1,t,Ireland,Moldova,2
2024,sf1,2024sf1,t,Ireland,Cyprus,1
2024,sf1,2024sf1,t,Lithuania,Ukraine,12
2024,sf1,2024sf1,t,Lithuania,Croatia,10
2024,sf1,2024sf1,t,Lithuania,Ireland,8
2024,sf1,2024sf1,t,Lithuania,Luxembourg,7
2024,sf1,2024sf1,t,Lithuania,Finland,6
2024,sf1,2024sf1,t,Lithuania,Portugal,5
2024,sf1,2024sf1,t,Lithuania,Poland,4
2024,sf1,2024sf1,t,Lithuania,Slovenia,3
2024,sf1,2024sf1,t,Lithuania,Australia,2
2024,sf1,2024sf1,t,Lithuania,Azerbaijan,1
2024,sf1,2024sf1,t,Luxembourg,Portugal,12
2024,sf1,2024sf1,t,Luxembourg,Lithuania,10
2024,sf1,2024sf1,t,Luxembourg,Ukraine,8
2024,sf1,2024sf1,t,Luxembourg,Croatia,7
2024,sf1,2024sf1,t,Luxembourg,Ireland,6
2024,sf1,2024sf1,t,Luxembourg,Serbia,5
2024,sf1,2024sf1,t,Luxembourg,Cyprus,4
2024,sf1,2024sf1,t,Luxembourg,Australia,3
2024,sf1,2024sf1,t,Luxembourg,Finland,2
2024,sf1,2024sf1,t,Luxembourg,Slovenia,1
2024,sf1,2024sf1,t,Moldova,Cyprus,12
2024,sf1,2024sf1,t,Moldova,Ukraine,10
2024,sf1,2024sf1,t,Moldova,Croatia,8
2024,sf1,2024sf1,t,Moldova,Luxembourg,7
2024,sf1,2024sf1,t,Moldova,Azerbaijan,6
2024,sf1,2024sf1,t,Moldova,Ireland,5
2024,sf1,2024sf1,t,Moldova,Slovenia,4
2024,sf1,2024sf1,t,Moldova,Portugal,3
2024,sf1,2024sf1,t,Moldova,Lithuania,2
2024,sf1,2024sf1,t,Moldova,Australia,1
2024,sf1,2024sf1,t,Poland,Ukraine,12
2024,sf1,2024sf1,t,Poland,Croatia,10
2024,sf1,2024sf1,t,Poland,Ireland,8
2024,sf1,2024sf1,t,Poland,Lithuania,7
2024,sf1,2024sf1,t,Poland,Luxembourg,6
2024,sf1,2024sf1,t,Poland,Finland,5
2024,sf1,2024sf1,t,Poland,Slovenia,4
2024,sf1,2024sf1,t,Poland,Portugal,3
2024,sf1,2024sf1,t,Poland,Australia,2
2024,sf1,2024sf1,t,Poland,Azerbaijan,1
2024,sf1,2024sf1,t,Portugal,Ukraine,12
2024,sf1,2024sf1,t,Portugal,Luxembourg,10
2024,sf1,2024sf1,t,Portugal,Cyprus,8
2024,sf1,2024sf1,t,Portugal,Ireland,7
2024,sf1,2024sf1,t,Portugal,Croatia,6
2024,sf1,2024sf1,t,Portugal,Moldova,5
2024,sf1,2024sf1,t,Portugal,Lithuania,4
2024,sf1,2024sf1,t,Portugal,Slovenia,3
2024,sf1,2024sf1,t,Portugal,Australia,2
2024,sf1,2024sf1,t,Portugal,Serbia,1
2024,sf1,2024sf1,t,Serbia,Croatia,12
2024,sf1,2024sf1,t,Serbia,Slovenia,10
2024,sf1,2024sf1,t,Serbia,Luxembourg,8
2024,sf1,2024sf1,t,Serbia,Ireland,7
2024,sf1,2024sf1,t,Serbia,Ukraine,6
2024,sf1,2024sf1,t,Serbia,Portugal,5
2024,sf1,2024sf1,t,Serbia,Cyprus,4
2024,sf1,2024sf1,t,Serbia,Moldova,3
2024,sf1,2024sf1,t,Serbia,Lithuania,2
2024,sf1,2024sf1,t,Serbia,Azerbaijan,1
2024,sf1,2024sf1,t,Slovenia,Croatia,12
2024,sf1,2024sf1,t,Slovenia,Serbia,10
2024,sf1,2024sf1,t,Slovenia,Ukraine,8
2024,sf1,2024sf1,t,Slovenia,Cyprus,7
2024,sf1,2024sf1,t,Slovenia,Lithuania,6
2024,sf1,2024sf1,t,Slovenia,Luxembourg,5
2024,sf1,2024sf1,t,Slovenia,Ireland,4
2024,sf1,2024sf1,t,Slovenia,Finland,3
2024,sf1,2024sf1,t,Slovenia,Portugal,2
2024,sf1,2024sf1,t,Slovenia,Poland,1
2024,sf1,2024sf1,t,Sweden,Croatia,12
2024,sf1,2024sf1,t,Sweden,Ukraine,10
2024,sf1,2024sf1,t,Sweden,Finland,8
2024,sf1,2024sf1,t,Sweden,Luxembourg,7
2024,sf1,2024sf1,t,Sweden,Ireland,6
2024,sf1,2024sf1,t,Sweden,Lithuania,5
2024,sf1,2024sf1,t,Sweden,Australia,4
2024,sf1,2024sf1,t,Sweden,Poland,3
2024,sf1,2024sf1,t,Sweden,Iceland,2
2024,sf1,2024sf1,t,Sweden,Cyprus,1
2024,sf1,2024sf1,t,Ukraine,Croatia,12
2024,sf1,2024sf1,t,Ukraine,Lithuania,10
2024,sf1,2024sf1,t,Ukraine,Ireland,8
2024,sf1,2024sf1,t,Ukraine,Luxembourg,7
2024,sf1,2024sf1,t,Ukraine,Finland,6
2024,sf1,2024sf1,t,Ukraine,Australia,5
2024,sf1,2024sf1,t,Ukraine,Moldova,4
2024,sf1,2024sf1,t,Ukraine,Poland,3
2024,sf1,2024sf1,t,Ukraine,Portugal,2
2024,sf1,2024sf1,t,Ukraine,Azerbaijan,1
2024,sf1,2024sf1,t,United Kingdom,Lithuania,12
2024,sf1,2024sf1,t,United Kingdom,Ireland,10
2024,sf1,2024sf1,t,United Kingdom,Croatia,8
2024,sf1,2024sf1,t,United Kingdom,Ukraine,7
2024,sf1,2024sf1,t,United Kingdom,Poland,6
2024,sf1,2024sf1,t,United Kingdom,Australia,5
2024,sf1,2024sf1,t,United Kingdom,Finland,4
2024,sf1,2024sf1,t,United Kingdom,Luxembourg,3
2024,sf1,2024sf1,t,United Kingdom,Portugal,2
2024,sf1,2024sf1,t,United Kingdom,Cyprus,1
2024,sf2,2024sf2,t,Albania,Israel,12
2024,sf2,2024sf2,t,Albania,Netherlands,10
2024,sf2,2024sf2,t,Albania,Greece,8
2024,sf2,2024sf2,t,Albania,Georgia,7
2024,sf2,2024sf2,t,Albania,Armenia,6
2024,sf2,2024sf2,t,Albania,Switzerland,5
2024,sf2,2024sf2,t,Albania,Austria,4
2024,sf2,2024sf2,t,Albania,Estonia,3
2024,sf2,2024sf2,t,Albania,Belgium,2
2024,sf2,2024sf2,t,Albania,Norway,1
2024,sf2,2024sf2,t,Armenia,Greece,12
2024,sf2,2024sf2,t,Armenia,Georgia,10
2024,sf2,2024sf2,t,Armenia,Netherlands,8
2024,sf2,2024sf2,t,Armenia,Switzerland,7
2024,sf2,2024sf2,t,Armenia,Israel,6
2024,sf2,2024sf2,t,Armenia,Malta,5
2024,sf2,2024sf2,t,Armenia,Austria,4
2024,sf2,2024sf2,t,Armenia,Denmark,3
2024,sf2,2024sf2,t,Armenia,Estonia,2
2024,sf2,2024sf2,t,Armenia,Czechia,1
2024,sf2,2024sf2,t,Austria,Netherlands,12
2024,sf2,2024sf2,t,Austria,Israel,10
2024,sf2,2024sf2,t,Austria,Switzerland,8
2024,sf2,2024sf2,t,Austria,Estonia,7
2024,sf2,2024sf2,t,Austria,Armenia,6
2024,sf2,2024sf2,t,Austria,Czechia,5
2024,sf2,2024sf2,t,Austria,Latvia,4
2024,sf2,2024sf2,t,Austria,Denmark,3
2024,sf2,2024sf2,t,Austria,Greece,2
2024,sf2,2024sf2,t,Austria,Georgia,1
2024,sf2,2024sf2,t,Belgium,Netherlands,12
2024,sf2,2024sf2,t,Belgium,Israel,10
2024,sf2,2024sf2,t,Belgium,Greece,8
2024,sf2,2024sf2,t,Belgium,Switzerland,7
2024,sf2,2024sf2,t,Belgium,Armenia,6
2024,sf2,2024sf2,t,Belgium,Latvia,5
2024,sf2,2024sf2,t,Belgium,Estonia,4
2024,sf2,2024sf2,t,Belgium,Norway,3
2024,sf2,2024sf2,t,Belgium,Georgia,2
2024,sf2,2024sf2,t,Belgium,Austria,1
2024,sf2,2024sf2,t,Czechia,Israel,12
2024,sf2,2024sf2,t,Czechia,Netherlands,10
2024,sf2,2024sf2,t,Czechia,Switzerland,8
2024,sf2,2024sf2,t,Czechia,Armenia,7
2024,sf2,2024sf2,t,Czechia,Estonia,6
2024,sf2,2024sf2,t,Czechia,Latvia,5
2024,sf2,2024sf2,t,Czechia,Greece,4
2024,sf2,2024sf2,t,Czechia,Norway,3
2024,sf2,2024sf2,t,Czechia,Austria,2
2024,sf2,2024sf2,t,Czechia,Georgia,1
2024,sf2,2024sf2,t,Denmark,Israel,12
2024,sf2,2024sf2,t,Denmark,Netherlands,10
2024,sf2,2024sf2,t,Denmark,Norway,8
2024,sf2,2024sf2,t,Denmark,Latvia,7
2024,sf2,2024sf2,t,Denmark,Switzerland,6
2024,sf2,2024sf2,t,Denmark,Armenia,5
2024,sf2,2024sf2,t,Denmark,Estonia,4
2024,sf2,2024sf2,t,Denmark,Austria,3
2024,sf2,2024sf2,t,Denmark,Greece,2
2024,sf2,2024sf2,t,Denmark,Czechia,1
2024,sf2,2024sf2,t,Estonia,Latvia,12
2024,sf2,2024sf2,t,Estonia,Netherlands,10
2024,sf2,2024sf2,t,Estonia,Israel,8
2024,sf2,2024sf2,t,Estonia,Switzerland,7
2024,sf2,2024sf2,t,Estonia,Norway,6
2024,sf2,2024sf2,t,Estonia,Denmark,5
2024,sf2,2024sf2,t,Estonia,Armenia,4
2024,sf2,2024sf2,t,Estonia,Austria,3
2024,sf2,2024sf2,t,Estonia,Czechia,2
2024,sf2,2024sf2,t,Estonia,Georgia,1
2024,sf2,2024sf2,t,France,Israel,12
2024,sf2,2024sf2,t,France,Armenia,10
2024,sf2,2024sf2,t,France,Switzerland,8
2024,sf2,2024sf2,t,France,Netherlands,7
2024,sf2,2024sf2,t,France,Georgia,6
2024,sf2,2024sf2,t,France,Belgium,5
2024,sf2,2024sf2,t,France,Greece,4
2024,sf2,2024sf2,t,France,Norway,3
2024,sf2,2024sf2,t,France,Estonia,2
2024,sf2,2024sf2,t,France,Malta,1
2024,sf2,2024sf2,t,Georgia,Armenia,12
2024,sf2,2024sf2,t,Georgia,Israel,10
2024,sf2,2024sf2,t,Georgia,Netherlands,8
2024,sf2,2024sf2,t,Georgia,Latvia,7
2024,sf2,2024sf2,t,Georgia,Greece,6
2024,sf2,2024sf2,t,Georgia,Switzerland,5
2024,sf2,2024sf2,t,Georgia,Czechia,4
2024,sf2,2024sf2,t,Georgia,San Marino,3
2024,sf2,2024sf2,t,Georgia,Belgium,2
2024,sf2,2024sf2,t,Georgia,Austria,1
2024,sf2,2024sf2,t,Greece,Netherlands,12
2024,sf2,2024sf2,t,Greece,Israel,10
2024,sf2,2024sf2,t,Greece,Armenia,8
2024,sf2,2024sf2,t,Greece,Switzerland,7
2024,sf2,2024sf2,t,Greece,Georgia,6
2024,sf2,2024sf2,t,Greece,Albania,5
2024,sf2,2024sf2,t,Greece,Austria,4
2024,sf2,2024sf2,t,Greece,Malta,3
2024,sf2,2024sf2,t,Greece,Estonia,2
2024,sf2,2024sf2,t,Greece,Belgium,1
2024,sf2,2024sf2,t,Israel,Armenia,12
2024,sf2,2024sf2,t,Israel,Estonia,10
2024,sf2,2024sf2,t,Israel,Austria,8
2024,sf2,2024sf2,t,Israel,Netherlands,7
2024,sf2,2024sf2,t,Israel,Georgia,6
2024,sf2,2024sf2,t,Israel,Czechia,5
2024,sf2,2024sf2,t,Israel,Switzerland,4
2024,sf2,2024sf2,t,Israel,Greece,3
2024,sf2,2024sf2,t,Israel,Belgium,2
2024,sf2,2024sf2,t,Israel,Denmark,1
2024,sf2,2024sf2,t,Italy,Israel,12
2024,sf2,2024sf2,t,Italy,Netherlands,10
2024,sf2,2024sf2,t,Italy,Switzerland,8
2024,sf2,2024sf2,t,Italy,Armenia,7
2024,sf2,2024sf2,t,Italy,Greece,6
2024,sf2,2024sf2,t,Italy,Georgia,5
2024,sf2,2024sf2,t,Italy,Albania,4
2024,sf2,2024sf2,t,Italy,Estonia,3
2024,sf2,2024sf2,t,Italy,Czechia,2
2024,sf2,2024sf2,t,Italy,San Marino,1
2024,sf2,2024sf2,t,Latvia,Estonia,12
2024,sf2,2024sf2,t,Latvia,Israel,10
2024,sf2,2024sf2,t,Latvia,Netherlands,8
2024,sf2,2024sf2,t,Latvia,Switzerland,7
2024,sf2,2024sf2,t,Latvia,Norway,6
2024,sf2,2024sf2,t,Latvia,Armenia,5
2024,sf2,2024sf2,t,Latvia,Denmark,4
2024,sf2,2024sf2,t,Latvia,Czechia,3
2024,sf2,2024sf2,t,Latvia,Austria,2
2024,sf2,2024sf2,t,Latvia,Belgium,1
2024,sf2,2024sf2,t,Malta,Netherlands,12
2024,sf2,2024sf2,t,Malta,Israel,10
2024,sf2,2024sf2,t,Malta,Switzerland,8
2024,sf2,2024sf2,t,Malta,Latvia,7
2024,sf2,2024sf2,t,Malta,Greece,6
2024,sf2,2024sf2,t,Malta,Armenia,5
2024,sf2,2024sf2,t,Malta,Georgia,4
2024,sf2,2024sf2,t,Malta,Austria,3
2024,sf2,2024sf2,t,Malta,Czechia,2
2024,sf2,2024sf2,t,Malta,Denmark,1
2024,sf2,2024sf2,t,Netherlands,Israel,12
2024,sf2,2024sf2,t,Netherlands,Armenia,10
2024,sf2,2024sf2,t,Netherlands,Switzerland,8
2024,sf2,2024sf2,t,Netherlands,Estonia,7
2024,sf2,2024sf2,t,Netherlands,Greece,6
2024,sf2,2024sf2,t,Netherlands,Belgium,5
2024,sf2,2024sf2,t,Netherlands,Norway,4
2024,sf2,2024sf2,t,Netherlands,Latvia,3
2024,sf2,2024sf2,t,Netherlands,Austria,2
2024,sf2,2024sf2,t,Netherlands,Czechia,1
2024,sf2,2024sf2,t,Norway,Israel,12
2024,sf2,2024sf2,t,Norway,Denmark,10
2024,sf2,2024sf2,t,Norway,Netherlands,8
2024,sf2,2024sf2,t,Norway,Switzerland,7
2024,sf2,2024sf2,t,Norway,Latvia,6
2024,sf2,2024sf2,t,Norway,Armenia,5
2024,sf2,2024sf2,t,Norway,Estonia,4
2024,sf2,2024sf2,t,Norway,Czechia,3
2024,sf2,2024sf2,t,Norway,Austria,2
2024,sf2,2024sf2,t,Norway,Greece,1
2024,sf2,2024sf2,t,San Marino,Switzerland,12
2024,sf2,2024sf2,t,San Marino,Netherlands,10
2024,sf2,2024sf2,t,San Marino,Armenia,8
2024,sf2,2024sf2,t,San Marino,Denmark,7
2024,sf2,2024sf2,t,San Marino,Czechia,6
2024,sf2,2024sf2,t,San Marino,Norway,5
2024,sf2,2024sf2,t,San Marino,Malta,4
2024,sf2,2024sf2,t,San Marino,Latvia,3
2024,sf2,2024sf2,t,San Marino,Albania,2
2024,sf2,2024sf2,t,San Marino,Estonia,1
2024,sf2,2024sf2,t,Spain,Israel,12
2024,sf2,2024sf2,t,Spain,San Marino,10
2024,sf2,2024sf2,t,Spain,Netherlands,8
2024,sf2,2024sf2,t,Spain,Armenia,7
2024,sf2,2024sf2,t,Spain,Latvia,6
2024,sf2,2024sf2,t,Spain,Greece,5
2024,sf2,2024sf2,t,Spain,Switzerland,4
2024,sf2,2024sf2,t,Spain,Austria,3
2024,sf2,2024sf2,t,Spain,Czechia,2
2024,sf2,2024sf2,t,Spain,Georgia,1
2024,sf2,2024sf2,t,Switzerland,Israel,12
2024,sf2,2024sf2,t,Switzerland,Netherlands,10
2024,sf2,2024sf2,t,Switzerland,Greece,8
2024,sf2,2024sf2,t,Switzerland,Latvia,7
2024,sf2,2024sf2,t,Switzerland,Armenia,6
2024,sf2,2024sf2,t,Switzerland,Estonia,5
2024,sf2,2024sf2,t,Switzerland,Austria,4
2024,sf2,2024sf2,t,Switzerland,Albania,3
2024,sf2,2024sf2,t,Switzerland,Denmark,2
2024,sf2,2024sf2,t,Switzerland,Norway,1
2024,f,2024f,t,Albania,Croatia,12
2024,f,2024f,t,Albania,Israel,10
2024,f,2024f,t,Albania,Italy,8
2024,f,2024f,t,Albania,Ukraine,7
2024,f,2024f,t,Albania,France,6
2024,f,2024f,t,Albania,Cyprus,5
2024,f,2024f,t,Albania,Greece,4
2024,f,2024f,t,Albania,Switzerland,3
2024,f,2024f,t,Albania,Serbia,2
2024,f,2024f,t,Albania,Armenia,1
2024,f,2024f,j,Albania,Switzerland,12
2024,f,2024f,j,Albania,Italy,10
2024,f,2024f,j,Albania,Armenia,8
2024,f,2024f,j,Albania,Greece,7
2024,f,2024f,j,Albania,Norway,6
2024,f,2024f,j,Albania,Portugal,5
2024,f,2024f,j,Albania,Luxembourg,4
2024,f,2024f,j,Albania,Croatia,3
2024,f,2024f,j,Albania,Slovenia,2
2024,f,2024f,j,Albania,Serbia,1
2024,f,2024f,t,Armenia,France,12
2024,f,2024f,t,Armenia,Greece,10
2024,f,2024f,t,Armenia,Switzerland,8
2024,f,2024f,t,Armenia,Croatia,7
2024,f,2024f,t,Armenia,Italy,6
2024,f,2024f,t,Armenia,Georgia,5
2024,f,2024f,t,Armenia,Cyprus,4
2024,f,2024f,t,Armenia,Ukraine,3
2024,f,2024f,t,Armenia,Ireland,2
2024,f,2024f,t,Armenia,Israel,1
2024,f,2024f,j,Armenia,France,12
2024,f,2024f,j,Armenia,Portugal,10
2024,f,2024f,j,Armenia,Italy,8
2024,f,2024f,j,Armenia,Switzerland,7
2024,f,2024f,j,Armenia,Croatia,6
2024,f,2024f,j,Armenia,Serbia,5
2024,f,2024f,j,Armenia,Greece,4
2024,f,2024f,j,Armenia,Georgia,3
2024,f,2024f,j,Armenia,Cyprus,2
2024,f,2024f,j,Armenia,Germany,1
2024,f,2024f,t,Australia,Israel,12
2024,f,2024f,t,Australia,Croatia,10
2024,f,2024f,t,Australia,Ireland,8
2024,f,2024f,t,Australia,Switzerland,7
2024,f,2024f,t,Australia,Ukraine,6
2024,f,2024f,t,Australia,Cyprus,5
2024,f,2024f,t,Australia,Finland,4
2024,f,2024f,t,Australia,Greece,3
2024,f,2024f,t,Australia,France,2
2024,f,2024f,t,Australia,Armenia,1
2024,f,2024f,j,Australia,Ireland,12
2024,f,2024f,j,Australia,Switzerland,10
2024,f,2024f,j,Australia,Croatia,8
2024,f,2024f,j,Australia,Italy,7
2024,f,2024f,j,Australia,Cyprus,6
2024,f,2024f,j,Australia,Sweden,5
2024,f,2024f,j,Australia,United Kingdom,4
2024,f,2024f,j,Australia,Finland,3
2024,f,2024f,j,Australia,Luxembourg,2
2024,f,2024f,j,Australia,Ukraine,1
2024,f,2024f,t,Austria,Croatia,12
2024,f,2024f,t,Austria,Israel,10
2024,f,2024f,t,Austria,Switzerland,8
2024,f,2024f,t,Austria,Ukraine,7
2024,f,2024f,t,Austria,France,6
2024,f,2024f,t,Austria,Serbia,5
2024,f,2024f,t,Austria,Germany,4
2024,f,2024f,t,Austria,Armenia,3
2024,f,2024f,t,Austria,Ireland,2
2024,f,2024f,t,Austria,Italy,1
2024,f,2024f,j,Austria,Switzerland,12
2024,f,2024f,j,Austria,Italy,10
2024,f,2024f,j,Austria,Croatia,8
2024,f,2024f,j,Austria,Armenia,7
2024,f,2024f,j,Austria,Ukraine,6
2024,f,2024f,j,Austria,France,5
2024,f,2024f,j,Austria,Spain,4
2024,f,2024f,j,Austria,Ireland,3
2024,f,2024f,j,Austria,Estonia,2
2024,f,2024f,j,Austria,Norway,1
2024,f,2024f,t,Azerbaijan,Croatia,12
2024,f,2024f,t,Azerbaijan,Switzerland,10
2024,f,2024f,t,Azerbaijan,Ukraine,8
2024,f,2024f,t,Azerbaijan,Israel,7
2024,f,2024f,t,Azerbaijan,Cyprus,6
2024,f,2024f,t,Azerbaijan,Georgia,5
2024,f,2024f,t,Azerbaijan,Ireland,4
2024,f,2024f,t,Azerbaijan,Italy,3
2024,f,2024f,t,Azerbaijan,France,2
2024,f,2024f,t,Azerbaijan,Greece,1
2024,f,2024f,j,Azerbaijan,Switzerland,12
2024,f,2024f,j,Azerbaijan,Ireland,10
2024,f,2024f,j,Azerbaijan,Luxembourg,8
2024,f,2024f,j,Azerbaijan,Georgia,7
2024,f,2024f,j,Azerbaijan,Italy,6
2024,f,2024f,j,Azerbaijan,Sweden,5
2024,f,2024f,j,Azerbaijan,Croatia,4
2024,f,2024f,j,Azerbaijan,Slovenia,3
2024,f,2024f,j,Azerbaijan,Cyprus,2
2024,f,2024f,j,Azerbaijan,Ukraine,1
2024,f,2024f,t,Belgium,Israel,12
2024,f,2024f,t,Belgium,France,10
2024,f,2024f,t,Belgium,Croatia,8
2024,f,2024f,t,Belgium,Ukraine,7
2024,f,2024f,t,Belgium,Switzerland,6
2024,f,2024f,t,Belgium,Armenia,5
2024,f,2024f,t,Belgium,Greece,4
2024,f,2024f,t,Belgium,Italy,3
2024,f,2024f,t,Belgium,Ireland,2
2024,f,2024f,t,Belgium,Luxembourg,1
2024,f,2024f,j,Belgium,France,12
2024,f,2024f,j,Belgium,Switzerland,10
2024,f,2024f,j,Belgium,Germany,8
2024,f,2024f,j,Belgium,Italy,7
2024,f,2024f,j,Belgium,United Kingdom,6
2024,f,2024f,j,Belgium,Israel,5
2024,f,2024f,j,Belgium,Ireland,4
2024,f,2024f,j,Belgium,Sweden,3
2024,f,2024f,j,Belgium,Portugal,2
2024,f,2024f,j,Belgium,Ukraine,1
2024,f,2024f,t,Croatia,Serbia,12
2024,f,2024f,t,Croatia,Slovenia,10
2024,f,2024f,t,Croatia,Ukraine,8
2024,f,2024f,t,Croatia,Italy,7
2024,f,2024f,t,Croatia,France,6
2024,f,2024f,t,Croatia,Ireland,5
2024,f,2024f,t,Croatia,Estonia,4
2024,f,2024f,t,Croatia,Armenia,3
2024,f,2024f,t,Croatia,Sweden,2
2024,f,2024f,t,Croatia,Switzerland,1
2024,f,2024f,j,Croatia,Portugal,12
2024,f,2024f,j,Croatia,Slovenia,10
2024,f,2024f,j,Croatia,Ireland,8
2024,f,2024f,j,Croatia,Ukraine,7
2024,f,2024f,j,Croatia,Italy,6
2024,f,2024f,j,Croatia,Luxembourg,5
2024,f,2024f,j,Croatia,France,4
2024,f,2024f,j,Croatia,Serbia,3
2024,f,2024f,j,Croatia,Sweden,2
2024,f,2024f,j,Croatia,Cyprus,1
2024,f,2024f,t,Cyprus,Greece,12
2024,f,2024f,t,Cyprus,Israel,10
2024,f,2024f,t,Cyprus,Ukraine,8
2024,f,2024f,t,Cyprus,France,7
2024,f,2024f,t,Cyprus,Switzerland,6
2024,f,2024f,t,Cyprus,Croatia,5
2024,f,2024f,t,Cyprus,Armenia,4
2024,f,2024f,t,Cyprus,Italy,3
2024,f,2024f,t,Cyprus,Ireland,2
2024,f,2024f,t,Cyprus,Sweden,1
2024,f,2024f,j,Cyprus,Croatia,12
2024,f,2024f,j,Cyprus,France,10
2024,f,2024f,j,Cyprus,Israel,8
2024,f,2024f,j,Cyprus,Greece,7
2024,f,2024f,j,Cyprus,Switzerland,6
2024,f,2024f,j,Cyprus,Serbia,5
2024,f,2024f,j,Cyprus,Luxembourg,4
2024,f,2024f,j,Cyprus,Italy,3
2024,f,2024f,j,Cyprus,Sweden,2
2024,f,2024f,j,Cyprus,Ukraine,1
2024,f,2024f,t,Czechia,Ukraine,12
2024,f,2024f,t,Czechia,Israel,10
2024,f,2024f,t,Czechia,Croatia,8
2024,f,2024f,t,Czechia,Switzerland,7
2024,f,2024f,t,Czechia,Ireland,6
2024,f,2024f,t,Czechia,Armenia,5
2024,f,2024f,t,Czechia,France,4
2024,f,2024f,t,Czechia,Sweden,3
2024,f,2024f,t,Czechia,Greece,2
2024,f,2024f,t,Czechia,Lithuania,1
2024,f,2024f,j,Czechia,Ukraine,12
2024,f,2024f,j,Czechia,Switzerland,10
2024,f,2024f,j,Czechia,Sweden,8
2024,f,2024f,j,Czechia,Ireland,7
2024,f,2024f,j,Czechia,Armenia,6
2024,f,2024f,j,Czechia,Germany,5
2024,f,2024f,j,Czechia,France,4
2024,f,2024f,j,Czechia,Portugal,3
2024,f,2024f,j,Czechia,Croatia,2
2024,f,2024f,j,Czechia,Norway,1
2024,f,2024f,t,Denmark,Croatia,12
2024,f,2024f,t,Denmark,Ukraine,10
2024,f,2024f,t,Denmark,Israel,8
2024,f,2024f,t,Denmark,France,7
2024,f,2024f,t,Denmark,Sweden,6
2024,f,2024f,t,Denmark,Switzerland,5
2024,f,2024f,t,Denmark,Latvia,4
2024,f,2024f,t,Denmark,Ireland,3
2024,f,2024f,t,Denmark,Finland,2
2024,f,2024f,t,Denmark,Lithuania,1
2024,f,2024f,j,Denmark,Switzerland,12
2024,f,2024f,j,Denmark,France,10
2024,f,2024f,j,Denmark,Croatia,8
2024,f,2024f,j,Denmark,Ireland,7
2024,f,2024f,j,Denmark,Ukraine,6
2024,f,2024f,j,Denmark,Sweden,5
2024,f,2024f,j,Denmark,Latvia,4
2024,f,2024f,j,Denmark,Armenia,3
2024,f,2024f,j,Denmark,Serbia,2
2024,f,2024f,j,Denmark,Luxembourg,1
2024,f,2024f,t,Estonia,Ukraine,12
2024,f,2024f,t,Estonia,Croatia,10
2024,f,2024f,t,Estonia,Finland,8
2024,f,2024f,t,Estonia,Switzerland,7
2024,f,2024f,t,Estonia,Israel,6
2024,f,2024f,t,Estonia,France,5
2024,f,2024f,t,Estonia,Lithuania,4
2024,f,2024f,t,Estonia,Latvia,3
2024,f,2024f,t,Estonia,Ireland,2
2024,f,2024f,t,Estonia,Sweden,1
2024,f,2024f,j,Estonia,Switzerland,12
2024,f,2024f,j,Estonia,Ukraine,10
2024,f,2024f,j,Estonia,Croatia,8
2024,f,2024f,j,Estonia,France,7
2024,f,2024f,j,Estonia,Sweden,6
2024,f,2024f,j,Estonia,Israel,5
2024,f,2024f,j,Estonia,Germany,4
2024,f,2024f,j,Estonia,Italy,3
2024,f,2024f,j,Estonia,Lithuania,2
2024,f,2024f,j,Estonia,Latvia,1
2024,f,2024f,t,Finland,Israel,12
2024,f,2024f,t,Finland,Croatia,10
2024,f,2024f,t,Finland,Switzerland,8
2024,f,2024f,t,Finland,Estonia,7
2024,f,2024f,t,Finland,Ukraine,6
2024,f,2024f,t,Finland,Ireland,5
2024,f,2024f,t,Finland,France,4
2024,f,2024f,t,Finland,Spain,3
2024,f,2024f,t,Finland,Austria,2
2024,f,2024f,t,Finland,Norway,1
2024,f,2024f,j,Finland,Switzerland,12
2024,f,2024f,j,Finland,Croatia,10
2024,f,2024f,j,Finland,Ukraine,8
2024,f,2024f,j,Finland,Sweden,7
2024,f,2024f,j,Finland,Ireland,6
2024,f,2024f,j,Finland,France,5
2024,f,2024f,j,Finland,Luxembourg,4
2024,f,2024f,j,Finland,Germany,3
2024,f,2024f,j,Finland,Norway,2
2024,f,2024f,j,Finland,Spain,1
2024,f,2024f,t,France,Israel,12
2024,f,2024f,t,France,Armenia,10
2024,f,2024f,t,France,Ukraine,8
2024,f,2024f,t,France,Croatia,7
2024,f,2024f,t,France,Switzerland,6
2024,f,2024f,t,France,Portugal,5
2024,f,2024f,t,France,Italy,4
2024,f,2024f,t,France,Luxembourg,3
2024,f,2024f,t,France,Spain,2
2024,f,2024f,t,France,Greece,1
2024,f,2024f,j,France,Portugal,12
2024,f,2024f,j,France,Ukraine,10
2024,f,2024f,j,France,Germany,8
2024,f,2024f,j,France,Luxembourg,7
2024,f,2024f,j,France,Armenia,6
2024,f,2024f,j,France,Switzerland,5
2024,f,2024f,j,France,Greece,4
2024,f,2024f,j,France,Israel,3
2024,f,2024f,j,France,Croatia,2
2024,f,2024f,j,France,Lithuania,1
2024,f,2024f,t,Georgia,Ukraine,12
2024,f,2024f,t,Georgia,Armenia,10
2024,f,2024f,t,Georgia,Israel,8
2024,f,2024f,t,Georgia,Switzerland,7
2024,f,2024f,t,Georgia,France,6
2024,f,2024f,t,Georgia,Croatia,5
2024,f,2024f,t,Georgia,Ireland,4
2024,f,2024f,t,Georgia,Italy,3
2024,f,2024f,t,Georgia,Greece,2
2024,f,2024f,t,Georgia,Latvia,1
2024,f,2024f,j,Georgia,Switzerland,12
2024,f,2024f,j,Georgia,France,10
2024,f,2024f,j,Georgia,Latvia,8
2024,f,2024f,j,Georgia,Italy,7
2024,f,2024f,j,Georgia,Armenia,6
2024,f,2024f,j,Georgia,Ukraine,5
2024,f,2024f,j,Georgia,Portugal,4
2024,f,2024f,j,Georgia,Israel,3
2024,f,2024f,j,Georgia,Germany,2
2024,f,2024f,j,Georgia,Croatia,1
2024,f,2024f,t,Germany,Israel,12
2024,f,2024f,t,Germany,Croatia,10
2024,f,2024f,t,Germany,Ukraine,8
2024,f,2024f,t,Germany,Switzerland,7
2024,f,2024f,t,Germany,France,6
2024,f,2024f,t,Germany,Greece,5
2024,f,2024f,t,Germany,Armenia,4
2024,f,2024f,t,Germany,Italy,3
2024,f,2024f,t,Germany,Lithuania,2
2024,f,2024f,t,Germany,Ireland,1
2024,f,2024f,j,Germany,Sweden,12
2024,f,2024f,j,Germany,France,10
2024,f,2024f,j,Germany,Israel,8
2024,f,2024f,j,Germany,Armenia,7
2024,f,2024f,j,Germany,Croatia,6
2024,f,2024f,j,Germany,Switzerland,5
2024,f,2024f,j,Germany,Ukraine,4
2024,f,2024f,j,Germany,Luxembourg,3
2024,f,2024f,j,Germany,Italy,2
2024,f,2024f,j,Germany,Lithuania,1
2024,f,2024f,t,Greece,Cyprus,12
2024,f,2024f,t,Greece,France,10
2024,f,2024f,t,Greece,Switzerland,8
2024,f,2024f,t,Greece,Israel,7
2024,f,2024f,t,Greece,Croatia,6
2024,f,2024f,t,Greece,Armenia,5
2024,f,2024f,t,Greece,Italy,4
2024,f,2024f,t,Greece,Ukraine,3
2024,f,2024f,t,Greece,Ireland,2
2024,f,2024f,t,Greece,Sweden,1
2024,f,2024f,j,Greece,Switzerland,12
2024,f,2024f,j,Greece,Cyprus,10
2024,f,2024f,j,Greece,Italy,8
2024,f,2024f,j,Greece,France,7
2024,f,2024f,j,Greece,Portugal,6
2024,f,2024f,j,Greece,Germany,5
2024,f,2024f,j,Greece,Armenia,4
2024,f,2024f,j,Greece,Luxembourg,3
2024,f,2024f,j,Greece,Ukraine,2
2024,f,2024f,j,Greece,Sweden,1
2024,f,2024f,t,Iceland,Croatia,12
2024,f,2024f,t,Iceland,France,10
2024,f,2024f,t,Iceland,Israel,8
2024,f,2024f,t,Iceland,Sweden,7
2024,f,2024f,t,Iceland,Switzerland,6
2024,f,2024f,t,Iceland,Ukraine,5
2024,f,2024f,t,Iceland,Lithuania,4
2024,f,2024f,t,Iceland,Ireland,3
2024,f,2024f,t,Iceland,Germany,2
2024,f,2024f,t,Iceland,Finland,1
2024,f,2024f,j,Iceland,France,12
2024,f,2024f,j,Iceland,Croatia,10
2024,f,2024f,j,Iceland,United Kingdom,8
2024,f,2024f,j,Iceland,Ireland,7
2024,f,2024f,j,Iceland,Switzerland,6
2024,f,2024f,j,Iceland,Armenia,5
2024,f,2024f,j,Iceland,Portugal,4
2024,f,2024f,j,Iceland,Ukraine,3
2024,f,2024f,j,Iceland,Germany,2
2024,f,2024f,j,Iceland,Sweden,1
2024,f,2024f,t,Ireland,Croatia,12
2024,f,2024f,t,Ireland,Israel,10
2024,f,2024f,t,Ireland,Ukraine,8
2024,f,2024f,t,Ireland,Lithuania,7
2024,f,2024f,t,Ireland,Switzerland,6
2024,f,2024f,t,Ireland,Latvia,5
2024,f,2024f,t,Ireland,France,4
2024,f,2024f,t,Ireland,Finland,3
2024,f,2024f,t,Ireland,Spain,2
2024,f,2024f,t,Ireland,Italy,1
2024,f,2024f,j,Ireland,Switzerland,12
2024,f,2024f,j,Ireland,Sweden,10
2024,f,2024f,j,Ireland,Luxembourg,8
2024,f,2024f,j,Ireland,Croatia,7
2024,f,2024f,j,Ireland,Germany,6
2024,f,2024f,j,Ireland,Portugal,5
2024,f,2024f,j,Ireland,United Kingdom,4
2024,f,2024f,j,Ireland,France,3
2024,f,2024f,j,Ireland,Ukraine,2
2024,f,2024f,j,Ireland,Serbia,1
2024,f,2024f,t,Israel,Luxembourg,12
2024,f,2024f,t,Israel,Ukraine,10
2024,f,2024f,t,Israel,Germany,8
2024,f,2024f,t,Israel,Italy,7
2024,f,2024f,t,Israel,Armenia,6
2024,f,2024f,t,Israel,Croatia,5
2024,f,2024f,t,Israel,Georgia,4
2024,f,2024f,t,Israel,Austria,3
2024,f,2024f,t,Israel,France,2
2024,f,2024f,t,Israel,Cyprus,1
2024,f,2024f,j,Israel,Luxembourg,12
2024,f,2024f,j,Israel,Germany,10
2024,f,2024f,j,Israel,Ukraine,8
2024,f,2024f,j,Israel,Austria,7
2024,f,2024f,j,Israel,Italy,6
2024,f,2024f,j,Israel,Switzerland,5
2024,f,2024f,j,Israel,Croatia,4
2024,f,2024f,j,Israel,Portugal,3
2024,f,2024f,j,Israel,Georgia,2
2024,f,2024f,j,Israel,France,1
2024,f,2024f,t,Italy,Israel,12
2024,f,2024f,t,Italy,Ukraine,10
2024,f,2024f,t,Italy,Croatia,8
2024,f,2024f,t,Italy,Switzerland,7
2024,f,2024f,t,Italy,France,6
2024,f,2024f,t,Italy,Georgia,5
2024,f,2024f,t,Italy,Armenia,4
2024,f,2024f,t,Italy,Ireland,3
2024,f,2024f,t,Italy,Greece,2
2024,f,2024f,t,Italy,Spain,1
2024,f,2024f,j,Italy,Switzerland,12
2024,f,2024f,j,Italy,Ireland,10
2024,f,2024f,j,Italy,Croatia,8
2024,f,2024f,j,Italy,Spain,7
2024,f,2024f,j,Italy,Sweden,6
2024,f,2024f,j,Italy,Austria,5
2024,f,2024f,j,Italy,Germany,4
2024,f,2024f,j,Italy,Armenia,3
2024,f,2024f,j,Italy,Estonia,2
2024,f,2024f,j,Italy,France,1
2024,f,2024f,t,Latvia,Estonia,12
2024,f,2024f,t,Latvia,Ukraine,10
2024,f,2024f,t,Latvia,Lithuania,8
2024,f,2024f,t,Latvia,Israel,7
2024,f,2024f,t,Latvia,France,6
2024,f,2024f,t,Latvia,Croatia,5
2024,f,2024f,t,Latvia,Switzerland,4
2024,f,2024f,t,Latvia,Ireland,3
2024,f,2024f,t,Latvia,Armenia,2
2024,f,2024f,t,Latvia,Finland,1
2024,f,2024f,j,Latvia,Switzerland,12
2024,f,2024f,j,Latvia,France,10
2024,f,2024f,j,Latvia,Ukraine,8
2024,f,2024f,j,Latvia,Armenia,7
2024,f,2024f,j,Latvia,Croatia,6
2024,f,2024f,j,Latvia,Sweden,5
2024,f,2024f,j,Latvia,Germany,4
2024,f,2024f,j,Latvia,United Kingdom,3
2024,f,2024f,j,Latvia,Israel,2
2024,f,2024f,j,Latvia,Portugal,1
2024,f,2024f,t,Lithuania,Ukraine,12
2024,f,2024f,t,Lithuania,Croatia,10
2024,f,2024f,t,Lithuania,Switzerland,8
2024,f,2024f,t,Lithuania,France,7
2024,f,2024f,t,Lithuania,Estonia,6
2024,f,2024f,t,Lithuania,Ireland,5
2024,f,2024f,t,Lithuania,Latvia,4
2024,f,2024f,t,Lithuania,Israel,3
2024,f,2024f,t,Lithuania,Italy,2
2024,f,2024f,t,Lithuania,Sweden,1
2024,f,2024f,j,Lithuania,Switzerland,12
2024,f,2024f,j,Lithuania,Croatia,10
2024,f,2024f,j,Lithuania,Portugal,8
2024,f,2024f,j,Lithuania,France,7
2024,f,2024f,j,Lithuania,Ukraine,6
2024,f,2024f,j,Lithuania,Sweden,5
2024,f,2024f,j,Lithuania,Israel,4
2024,f,2024f,j,Lithuania,Ireland,3
2024,f,2024f,j,Lithuania,Norway,2
2024,f,2024f,j,Lithuania,Germany,1
2024,f,2024f,t,Luxembourg,Israel,12
2024,f,2024f,t,Luxembourg,Croatia,10
2024,f,2024f,t,Luxembourg,France,8
2024,f,2024f,t,Luxembourg,Ukraine,7
2024,f,2024f,t,Luxembourg,Portugal,6
2024,f,2024f,t,Luxembourg,Greece,5
2024,f,2024f,t,Luxembourg,Lithuania,4
2024,f,2024f,t,Luxembourg,Italy,3
2024,f,2024f,t,Luxembourg,Switzerland,2
2024,f,2024f,t,Luxembourg,Germany,1
2024,f,2024f,j,Luxembourg,Switzerland,12
2024,f,2024f,j,Luxembourg,France,10
2024,f,2024f,j,Luxembourg,Latvia,8
2024,f,2024f,j,Luxembourg,Cyprus,7
2024,f,2024f,j,Luxembourg,Croatia,6
2024,f,2024f,j,Luxembourg,Ukraine,5
2024,f,2024f,j,Luxembourg,Germany,4
2024,f,2024f,j,Luxembourg,Portugal,3
2024,f,2024f,j,Luxembourg,Armenia,2
2024,f,2024f,j,Luxembourg,Sweden,1
2024,f,2024f,t,Malta,Ukraine,12
2024,f,2024f,t,Malta,Croatia,10
2024,f,2024f,t,Malta,Italy,8
2024,f,2024f,t,Malta,France,7
2024,f,2024f,t,Malta,Switzerland,6
2024,f,2024f,t,Malta,Israel,5
2024,f,2024f,t,Malta,Ireland,4
2024,f,2024f,t,Malta,Serbia,3
2024,f,2024f,t,Malta,Greece,2
2024,f,2024f,t,Malta,Sweden,1
2024,f,2024f,j,Malta,Switzerland,12
2024,f,2024f,j,Malta,Croatia,10
2024,f,2024f,j,Malta,Italy,8
2024,f,2024f,j,Malta,Ireland,7
2024,f,2024f,j,Malta,France,6
2024,f,2024f,j,Malta,Latvia,5
2024,f,2024f,j,Malta,Luxembourg,4
2024,f,2024f,j,Malta,Israel,3
2024,f,2024f,j,Malta,Georgia,2
2024,f,2024f,j,Malta,Portugal,1
2024,f,2024f,t,Moldova,Ukraine,12
2024,f,2024f,t,Moldova,Israel,10
2024,f,2024f,t,Moldova,Sweden,8
2024,f,2024f,t,Moldova,Croatia,7
2024,f,2024f,t,Moldova,France,6
2024,f,2024f,t,Moldova,Switzerland,5
2024,f,2024f,t,Moldova,Italy,4
2024,f,2024f,t,Moldova,Greece,3
2024,f,2024f,t,Moldova,Ireland,2
2024,f,2024f,t,Moldova,Armenia,1
2024,f,2024f,j,Moldova,Ukraine,12
2024,f,2024f,j,Moldova,Italy,10
2024,f,2024f,j,Moldova,Croatia,8
2024,f,2024f,j,Moldova,Switzerland,7
2024,f,2024f,j,Moldova,France,6
2024,f,2024f,j,Moldova,Lithuania,5
2024,f,2024f,j,Moldova,Portugal,4
2024,f,2024f,j,Moldova,Israel,3
2024,f,2024f,j,Moldova,Luxembourg,2
2024,f,2024f,j,Moldova,Sweden,1
2024,f,2024f,t,Netherlands,Israel,12
2024,f,2024f,t,Netherlands,Croatia,10
2024,f,2024f,t,Netherlands,Ukraine,8
2024,f,2024f,t,Netherlands,Switzerland,7
2024,f,2024f,t,Netherlands,Ireland,6
2024,f,2024f,t,Netherlands,France,5
2024,f,2024f,t,Netherlands,Greece,4
2024,f,2024f,t,Netherlands,Armenia,3
2024,f,2024f,t,Netherlands,Italy,2
2024,f,2024f,t,Netherlands,Lithuania,1
2024,f,2024f,j,Netherlands,Switzerland,12
2024,f,2024f,j,Netherlands,France,10
2024,f,2024f,j,Netherlands,Portugal,8
2024,f,2024f,j,Netherlands,Croatia,7
2024,f,2024f,j,Netherlands,Italy,6
2024,f,2024f,j,Netherlands,Germany,5
2024,f,2024f,j,Netherlands,Lithuania,4
2024,f,2024f,j,Netherlands,Armenia,3
2024,f,2024f,j,Netherlands,Ukraine,2
2024,f,2024f,j,Netherlands,Latvia,1
2024,f,2024f,t,Norway,Croatia,12
2024,f,2024f,t,Norway,Sweden,10
2024,f,2024f,t,Norway,Ukraine,8
2024,f,2024f,t,Norway,France,7
2024,f,2024f,t,Norway,Switzerland,6
2024,f,2024f,t,Norway,Israel,5
2024,f,2024f,t,Norway,Ireland,4
2024,f,2024f,t,Norway,Lithuania,3
2024,f,2024f,t,Norway,Latvia,2
2024,f,2024f,t,Norway,Finland,1
2024,f,2024f,j,Norway,Switzerland,12
2024,f,2024f,j,Norway,France,10
2024,f,2024f,j,Norway,Israel,8
2024,f,2024f,j,Norway,Armenia,7
2024,f,2024f,j,Norway,Germany,6
2024,f,2024f,j,Norway,Italy,5
2024,f,2024f,j,Norway,Ukraine,4
2024,f,2024f,j,Norway,Sweden,3
2024,f,2024f,j,Norway,Greece,2
2024,f,2024f,j,Norway,Georgia,1
2024,f,2024f,t,Poland,Ukraine,12
2024,f,2024f,t,Poland,Croatia,10
2024,f,2024f,t,Poland,Switzerland,8
2024,f,2024f,t,Poland,France,7
2024,f,2024f,t,Poland,Ireland,6
2024,f,2024f,t,Poland,Israel,5
2024,f,2024f,t,Poland,Italy,4
2024,f,2024f,t,Poland,Lithuania,3
2024,f,2024f,t,Poland,Sweden,2
2024,f,2024f,t,Poland,Finland,1
2024,f,2024f,j,Poland,Switzerland,12
2024,f,2024f,j,Poland,Ukraine,10
2024,f,2024f,j,Poland,Croatia,8
2024,f,2024f,j,Poland,Italy,7
2024,f,2024f,j,Poland,Portugal,6
2024,f,2024f,j,Poland,Sweden,5
2024,f,2024f,j,Poland,Germany,4
2024,f,2024f,j,Poland,France,3
2024,f,2024f,j,Poland,Latvia,2
2024,f,2024f,j,Poland,Ireland,1
2024,f,2024f,t,Portugal,Israel,12
2024,f,2024f,t,Portugal,Ukraine,10
2024,f,2024f,t,Portugal,France,8
2024,f,2024f,t,Portugal,Croatia,7
2024,f,2024f,t,Portugal,Switzerland,6
2024,f,2024f,t,Portugal,Ireland,5
2024,f,2024f,t,Portugal,Italy,4
2024,f,2024f,t,Portugal,Spain,3
2024,f,2024f,t,Portugal,Armenia,2
2024,f,2024f,t,Portugal,Cyprus,1
2024,f,2024f,j,Portugal,Switzerland,12
2024,f,2024f,j,Portugal,Ireland,10
2024,f,2024f,j,Portugal,Armenia,8
2024,f,2024f,j,Portugal,Lithuania,7
2024,f,2024f,j,Portugal,Ukraine,6
2024,f,2024f,j,Portugal,Italy,5
2024,f,2024f,j,Portugal,United Kingdom,4
2024,f,2024f,j,Portugal,Sweden,3
2024,f,2024f,j,Portugal,Germany,2
2024,f,2024f,j,Portugal,Serbia,1
2024,f,2024f,t,San Marino,Israel,12
2024,f,2024f,t,San Marino,Ukraine,10
2024,f,2024f,t,San Marino,Croatia,8
2024,f,2024f,t,San Marino,Greece,7
2024,f,2024f,t,San Marino,France,6
2024,f,2024f,t,San Marino,Switzerland,5
2024,f,2024f,t,San Marino,Cyprus,4
2024,f,2024f,t,San Marino,Italy,3
2024,f,2024f,t,San Marino,Ireland,2
2024,f,2024f,t,San Marino,Lithuania,1
2024,f,2024f,j,San Marino,Switzerland,12
2024,f,2024f,j,San Marino,Italy,10
2024,f,2024f,j,San Marino,Armenia,8
2024,f,2024f,j,San Marino,Ireland,7
2024,f,2024f,j,San Marino,Spain,6
2024,f,2024f,j,San Marino,Portugal,5
2024,f,2024f,j,San Marino,Finland,4
2024,f,2024f,j,San Marino,Cyprus,3
2024,f,2024f,j,San Marino,Sweden,2
2024,f,2024f,j,San Marino,Germany,1
2024,f,2024f,t,Serbia,Croatia,12
2024,f,2024f,t,Serbia,France,10
2024,f,2024f,t,Serbia,Greece,8
2024,f,2024f,t,Serbia,Ireland,7
2024,f,2024f,t,Serbia,Switzerland,6
2024,f,2024f,t,Serbia,Sweden,5
2024,f,2024f,t,Serbia,Italy,4
2024,f,2024f,t,Serbia,Israel,3
2024,f,2024f,t,Serbia,Slovenia,2
2024,f,2024f,t,Serbia,Armenia,1
2024,f,2024f,j,Serbia,Croatia,12
2024,f,2024f,j,Serbia,Switzerland,10
2024,f,2024f,j,Serbia,France,8
2024,f,2024f,j,Serbia,Lithuania,7
2024,f,2024f,j,Serbia,Italy,6
2024,f,2024f,j,Serbia,Sweden,5
2024,f,2024f,j,Serbia,United Kingdom,4
2024,f,2024f,j,Serbia,Greece,3
2024,f,2024f,j,Serbia,Ireland,2
2024,f,2024f,j,Serbia,Ukraine,1
2024,f,2024f,t,Slovenia,Croatia,12
2024,f,2024f,t,Slovenia,Israel,10
2024,f,2024f,t,Slovenia,Ukraine,8
2024,f,2024f,t,Slovenia,France,7
2024,f,2024f,t,Slovenia,Cyprus,6
2024,f,2024f,t,Slovenia,Serbia,5
2024,f,2024f,t,Slovenia,Switzerland,4
2024,f,2024f,t,Slovenia,Italy,3
2024,f,2024f,t,Slovenia,Ireland,2
2024,f,2024f,t,Slovenia,Sweden,1
2024,f,2024f,j,Slovenia,France,12
2024,f,2024f,j,Slovenia,Switzerland,10
2024,f,2024f,j,Slovenia,Portugal,8
2024,f,2024f,j,Slovenia,Armenia,7
2024,f,2024f,j,Slovenia,Croatia,6
2024,f,2024f,j,Slovenia,Luxembourg,5
2024,f,2024f,j,Slovenia,Serbia,4
2024,f,2024f,j,Slovenia,Italy,3
2024,f,2024f,j,Slovenia,Greece,2
2024,f,2024f,j,Slovenia,Ireland,1
2024,f,2024f,t,Spain,Israel,12
2024,f,2024f,t,Spain,Ukraine,10
2024,f,2024f,t,Spain,Croatia,8
2024,f,2024f,t,Spain,Ireland,7
2024,f,2024f,t,Spain,Switzerland,6
2024,f,2024f,t,Spain,France,5
2024,f,2024f,t,Spain,Italy,4
2024,f,2024f,t,Spain,Armenia,3
2024,f,2024f,t,Spain,Greece,2
2024,f,2024f,t,Spain,Lithuania,1
2024,f,2024f,j,Spain,Switzerland,12
2024,f,2024f,j,Spain,Ireland,10
2024,f,2024f,j,Spain,Sweden,8
2024,f,2024f,j,Spain,France,7
2024,f,2024f,j,Spain,Austria,6
2024,f,2024f,j,Spain,Germany,5
2024,f,2024f,j,Spain,Latvia,4
2024,f,2024f,j,Spain,Portugal,3
2024,f,2024f,j,Spain,United Kingdom,2
2024,f,2024f,j,Spain,Italy,1
2024,f,2024f,t,Sweden,Israel,12
2024,f,2024f,t,Sweden,Croatia,10
2024,f,2024f,t,Sweden,Ukraine,8
2024,f,2024f,t,Sweden,Switzerland,7
2024,f,2024f,t,Sweden,France,6
2024,f,2024f,t,Sweden,Finland,5
2024,f,2024f,t,Sweden,Ireland,4
2024,f,2024f,t,Sweden,Lithuania,3
2024,f,2024f,t,Sweden,Armenia,2
2024,f,2024f,t,Sweden,Italy,1
2024,f,2024f,j,Sweden,Switzerland,12
2024,f,2024f,j,Sweden,Croatia,10
2024,f,2024f,j,Sweden,United Kingdom,8
2024,f,2024f,j,Sweden,Italy,7
2024,f,2024f,j,Sweden,Luxembourg,6
2024,f,2024f,j,Sweden,France,5
2024,f,2024f,j,Sweden,Portugal,4
2024,f,2024f,j,Sweden,Ukraine,3
2024,f,2024f,j,Sweden,Cyprus,2
2024,f,2024f,j,Sweden,Austria,1
2024,f,2024f,t,Switzerland,Israel,12
2024,f,2024f,t,Switzerland,Croatia,10
2024,f,2024f,t,Switzerland,Italy,8
2024,f,2024f,t,Switzerland,France,7
2024,f,2024f,t,Switzerland,Ukraine,6
2024,f,2024f,t,Switzerland,Serbia,5
2024,f,2024f,t,Switzerland,Greece,4
2024,f,2024f,t,Switzerland,Germany,3
2024,f,2024f,t,Switzerland,Portugal,2
2024,f,2024f,t,Switzerland,Armenia,1
2024,f,2024f,j,Switzerland,Greece,12
2024,f,2024f,j,Switzerland,Ireland,10
2024,f,2024f,j,Switzerland,Croatia,8
2024,f,2024f,j,Switzerland,Portugal,7
2024,f,2024f,j,Switzerland,Italy,6
2024,f,2024f,j,Switzerland,France,5
2024,f,2024f,j,Switzerland,Armenia,4
2024,f,2024f,j,Switzerland,United Kingdom,3
2024,f,2024f,j,Switzerland,Ukraine,2
2024,f,2024f,j,Switzerland,Spain,1
2024,f,2024f,t,Ukraine,Switzerland,12
2024,f,2024f,t,Ukraine,Croatia,10
2024,f,2024f,t,Ukraine,Ireland,8
2024,f,2024f,t,Ukraine,Lithuania,7
2024,f,2024f,t,Ukraine,France,6
2024,f,2024f,t,Ukraine,Latvia,5
2024,f,2024f,t,Ukraine,Estonia,4
2024,f,2024f,t,Ukraine,Norway,3
2024,f,2024f,t,Ukraine,Finland,2
2024,f,2024f,t,Ukraine,Armenia,1
2024,f,2024f,j,Ukraine,Switzerland,12
2024,f,2024f,j,Ukraine,Ireland,10
2024,f,2024f,j,Ukraine,Sweden,8
2024,f,2024f,j,Ukraine,Germany,7
2024,f,2024f,j,Ukraine,France,6
2024,f,2024f,j,Ukraine,Lithuania,5
2024,f,2024f,j,Ukraine,Croatia,4
2024,f,2024f,j,Ukraine,Portugal,3
2024,f,2024f,j,Ukraine,Italy,2
2024,f,2024f,j,Ukraine,Luxembourg,1
2024,f,2024f,t,United Kingdom,Israel,12
2024,f,2024f,t,United Kingdom,Ireland,10
2024,f,2024f,t,United Kingdom,Lithuania,8
2024,f,2024f,t,United Kingdom,Croatia,7
2024,f,2024f,t,United Kingdom,Ukraine,6
2024,f,2024f,t,United Kingdom,Switzerland,5
2024,f,2024f,t,United Kingdom,Latvia,4
2024,f,2024f,t,United Kingdom,Finland,3
2024,f,2024f,t,United Kingdom,France,2
2024,f,2024f,t,United Kingdom,Greece,1
2024,f,2024f,j,United Kingdom,Portugal,12
2024,f,2024f,j,United Kingdom,Switzerland,10
2024,f,2024f,j,United Kingdom,Croatia,8
2024,f,2024f,j,United Kingdom,Ireland,7
2024,f,2024f,j,United Kingdom,Sweden,6
2024,f,2024f,j,United Kingdom,Italy,5
2024,f,2024f,j,United Kingdom,Luxembourg,4
2024,f,2024f,j,United Kingdom,Latvia,3
2024,f,2024f,j,United Kingdom,Germany,2
2024,f,2024f,j,United Kingdom,Cyprus,1"""

df75_24 = add_data_to_df(df75_22, data24)

df75_24.to_excel("Data Preparation/Datasets/eurovision_song_contest_1975_2024.xlsx")


unwanted_countries = ['Andorra', 'Morocco', 'Slovakia', '0']
df75_24 = df75_24[
    ~df75_24['From country'].isin(unwanted_countries) &  # From country için filtreleme
    ~df75_24['To country'].isin(unwanted_countries)  # To country için filtreleme
    ]

# 2. Boş değerleri içeren satırları silelim
df75_24 = df75_24.dropna()

# 3. "The Netherands", "Netherlands" -> "The Netherlands" ve "Macedonia" -> "North Macedonia" dönüşümleri
replace_map = {
    'The Netherands': 'The Netherlands',
    'Netherlands': 'The Netherlands',
    'Macedonia': 'North Macedonia'
}
df75_24['From country'] = df75_24['From country'].replace(replace_map)
df75_24['To country'] = df75_24['To country'].replace(replace_map)

# Sonuçları kontrol edelim (örneğin, ilk 5 satırı gösterelim)
print(df75_24.head())

# İsterseniz, düzenlenmiş DataFrame'i kaydedebilirsiniz:
# df75_24.to_csv('cleaned_df75_24.csv', index=False)

df75_24.to_excel("Data Preparation/Datasets/eurovision_song_contest_1975_2024.xlsx")

df75_24 = pd.read_excel("Data Preparation/Datasets/eurovision_song_contest_1975_2024.xlsx")
df75_24 = df75_24[df75_24['From country'] != 0]
df75_24 = df75_24[df75_24['To country'] != 0]

data23 = """Year,(semi-) final,Edition,Jury or Televoting,From country,To country,Points
2023,sf1,2023sf1,t,Azerbaijan,Israel,12
2023,sf1,2023sf1,t,Azerbaijan,Sweden,10
2023,sf1,2023sf1,t,Azerbaijan,Finland,8
2023,sf1,2023sf1,t,Azerbaijan,Switzerland,7
2023,sf1,2023sf1,t,Azerbaijan,Latvia,6
2023,sf1,2023sf1,t,Azerbaijan,Czechia,5
2023,sf1,2023sf1,t,Azerbaijan,Moldova,4
2023,sf1,2023sf1,t,Azerbaijan,Serbia,3
2023,sf1,2023sf1,t,Azerbaijan,Norway,2
2023,sf1,2023sf1,t,Azerbaijan,Netherlands,1
2023,sf1,2023sf1,t,Croatia,Finland,12
2023,sf1,2023sf1,t,Croatia,Serbia,10
2023,sf1,2023sf1,t,Croatia,Czechia,8
2023,sf1,2023sf1,t,Croatia,Israel,7
2023,sf1,2023sf1,t,Croatia,Norway,6
2023,sf1,2023sf1,t,Croatia,Portugal,5
2023,sf1,2023sf1,t,Croatia,Sweden,4
2023,sf1,2023sf1,t,Croatia,Moldova,3
2023,sf1,2023sf1,t,Croatia,Switzerland,2
2023,sf1,2023sf1,t,Croatia,Azerbaijan,1
2023,sf1,2023sf1,t,Czechia,Israel,12
2023,sf1,2023sf1,t,Czechia,Norway,10
2023,sf1,2023sf1,t,Czechia,Finland,8
2023,sf1,2023sf1,t,Czechia,Moldova,7
2023,sf1,2023sf1,t,Czechia,Sweden,6
2023,sf1,2023sf1,t,Czechia,Switzerland,5
2023,sf1,2023sf1,t,Czechia,Croatia,4
2023,sf1,2023sf1,t,Czechia,Serbia,3
2023,sf1,2023sf1,t,Czechia,Portugal,2
2023,sf1,2023sf1,t,Czechia,Latvia,1
2023,sf1,2023sf1,t,Finland,Czechia,12
2023,sf1,2023sf1,t,Finland,Norway,10
2023,sf1,2023sf1,t,Finland,Switzerland,8
2023,sf1,2023sf1,t,Finland,Moldova,7
2023,sf1,2023sf1,t,Finland,Croatia,6
2023,sf1,2023sf1,t,Finland,Sweden,5
2023,sf1,2023sf1,t,Finland,Serbia,4
2023,sf1,2023sf1,t,Finland,Latvia,3
2023,sf1,2023sf1,t,Finland,Portugal,2
2023,sf1,2023sf1,t,Finland,Israel,1
2023,sf1,2023sf1,t,France,Portugal,12
2023,sf1,2023sf1,t,France,Moldova,10
2023,sf1,2023sf1,t,France,Israel,8
2023,sf1,2023sf1,t,France,Finland,7
2023,sf1,2023sf1,t,France,Switzerland,6
2023,sf1,2023sf1,t,France,Sweden,5
2023,sf1,2023sf1,t,France,Czechia,4
2023,sf1,2023sf1,t,France,Latvia,3
2023,sf1,2023sf1,t,France,Serbia,2
2023,sf1,2023sf1,t,France,Norway,1
2023,sf1,2023sf1,t,Germany,Finland,12
2023,sf1,2023sf1,t,Germany,Croatia,10
2023,sf1,2023sf1,t,Germany,Switzerland,8
2023,sf1,2023sf1,t,Germany,Czechia,7
2023,sf1,2023sf1,t,Germany,Moldova,6
2023,sf1,2023sf1,t,Germany,Portugal,5
2023,sf1,2023sf1,t,Germany,Sweden,4
2023,sf1,2023sf1,t,Germany,Norway,3
2023,sf1,2023sf1,t,Germany,Israel,2
2023,sf1,2023sf1,t,Germany,Latvia,1
2023,sf1,2023sf1,t,Ireland,Finland,12
2023,sf1,2023sf1,t,Ireland,Moldova,10
2023,sf1,2023sf1,t,Ireland,Sweden,8
2023,sf1,2023sf1,t,Ireland,Switzerland,7
2023,sf1,2023sf1,t,Ireland,Israel,6
2023,sf1,2023sf1,t,Ireland,Croatia,5
2023,sf1,2023sf1,t,Ireland,Latvia,4
2023,sf1,2023sf1,t,Ireland,Czechia,3
2023,sf1,2023sf1,t,Ireland,Norway,2
2023,sf1,2023sf1,t,Ireland,Portugal,1
2023,sf1,2023sf1,t,Israel,Finland,12
2023,sf1,2023sf1,t,Israel,Norway,10
2023,sf1,2023sf1,t,Israel,Czechia,8
2023,sf1,2023sf1,t,Israel,Sweden,7
2023,sf1,2023sf1,t,Israel,Moldova,6
2023,sf1,2023sf1,t,Israel,Croatia,5
2023,sf1,2023sf1,t,Israel,Switzerland,4
2023,sf1,2023sf1,t,Israel,Portugal,3
2023,sf1,2023sf1,t,Israel,Malta,2
2023,sf1,2023sf1,t,Israel,Azerbaijan,1
2023,sf1,2023sf1,t,Italy,Moldova,12
2023,sf1,2023sf1,t,Italy,Norway,10
2023,sf1,2023sf1,t,Italy,Czechia,8
2023,sf1,2023sf1,t,Italy,Finland,7
2023,sf1,2023sf1,t,Italy,Israel,6
2023,sf1,2023sf1,t,Italy,Croatia,5
2023,sf1,2023sf1,t,Italy,Switzerland,4
2023,sf1,2023sf1,t,Italy,Sweden,3
2023,sf1,2023sf1,t,Italy,Portugal,2
2023,sf1,2023sf1,t,Italy,Serbia,1
2023,sf1,2023sf1,t,Latvia,Finland,12
2023,sf1,2023sf1,t,Latvia,Sweden,10
2023,sf1,2023sf1,t,Latvia,Israel,8
2023,sf1,2023sf1,t,Latvia,Croatia,7
2023,sf1,2023sf1,t,Latvia,Moldova,6
2023,sf1,2023sf1,t,Latvia,Czechia,5
2023,sf1,2023sf1,t,Latvia,Norway,4
2023,sf1,2023sf1,t,Latvia,Switzerland,3
2023,sf1,2023sf1,t,Latvia,Azerbaijan,2
2023,sf1,2023sf1,t,Latvia,Ireland,1
2023,sf1,2023sf1,t,Malta,Sweden,12
2023,sf1,2023sf1,t,Malta,Norway,10
2023,sf1,2023sf1,t,Malta,Israel,8
2023,sf1,2023sf1,t,Malta,Finland,7
2023,sf1,2023sf1,t,Malta,Switzerland,6
2023,sf1,2023sf1,t,Malta,Serbia,5
2023,sf1,2023sf1,t,Malta,Portugal,4
2023,sf1,2023sf1,t,Malta,Ireland,3
2023,sf1,2023sf1,t,Malta,Czechia,2
2023,sf1,2023sf1,t,Malta,Moldova,1
2023,sf1,2023sf1,t,Moldova,Israel,12
2023,sf1,2023sf1,t,Moldova,Sweden,10
2023,sf1,2023sf1,t,Moldova,Norway,8
2023,sf1,2023sf1,t,Moldova,Switzerland,7
2023,sf1,2023sf1,t,Moldova,Finland,6
2023,sf1,2023sf1,t,Moldova,Czechia,5
2023,sf1,2023sf1,t,Moldova,Portugal,4
2023,sf1,2023sf1,t,Moldova,Croatia,3
2023,sf1,2023sf1,t,Moldova,Netherlands,2
2023,sf1,2023sf1,t,Moldova,Latvia,1
2023,sf1,2023sf1,t,Netherlands,Sweden,12
2023,sf1,2023sf1,t,Netherlands,Finland,10
2023,sf1,2023sf1,t,Netherlands,Switzerland,8
2023,sf1,2023sf1,t,Netherlands,Portugal,7
2023,sf1,2023sf1,t,Netherlands,Czechia,6
2023,sf1,2023sf1,t,Netherlands,Norway,5
2023,sf1,2023sf1,t,Netherlands,Israel,4
2023,sf1,2023sf1,t,Netherlands,Moldova,3
2023,sf1,2023sf1,t,Netherlands,Croatia,2
2023,sf1,2023sf1,t,Netherlands,Latvia,1
2023,sf1,2023sf1,t,Norway,Finland,12
2023,sf1,2023sf1,t,Norway,Sweden,10
2023,sf1,2023sf1,t,Norway,Switzerland,8
2023,sf1,2023sf1,t,Norway,Czechia,7
2023,sf1,2023sf1,t,Norway,Moldova,6
2023,sf1,2023sf1,t,Norway,Israel,5
2023,sf1,2023sf1,t,Norway,Croatia,4
2023,sf1,2023sf1,t,Norway,Ireland,3
2023,sf1,2023sf1,t,Norway,Portugal,2
2023,sf1,2023sf1,t,Norway,Netherlands,1
2023,sf1,2023sf1,t,Portugal,Moldova,12
2023,sf1,2023sf1,t,Portugal,Finland,10
2023,sf1,2023sf1,t,Portugal,Sweden,8
2023,sf1,2023sf1,t,Portugal,Israel,7
2023,sf1,2023sf1,t,Portugal,Czechia,6
2023,sf1,2023sf1,t,Portugal,Switzerland,5
2023,sf1,2023sf1,t,Portugal,Latvia,4
2023,sf1,2023sf1,t,Portugal,Norway,3
2023,sf1,2023sf1,t,Portugal,Ireland,2
2023,sf1,2023sf1,t,Portugal,Netherlands,1
2023,sf1,2023sf1,t,Serbia,Croatia,12
2023,sf1,2023sf1,t,Serbia,Finland,10
2023,sf1,2023sf1,t,Serbia,Czechia,8
2023,sf1,2023sf1,t,Serbia,Israel,7
2023,sf1,2023sf1,t,Serbia,Sweden,6
2023,sf1,2023sf1,t,Serbia,Norway,5
2023,sf1,2023sf1,t,Serbia,Moldova,4
2023,sf1,2023sf1,t,Serbia,Portugal,3
2023,sf1,2023sf1,t,Serbia,Latvia,2
2023,sf1,2023sf1,t,Serbia,Switzerland,1
2023,sf1,2023sf1,t,Sweden,Finland,12
2023,sf1,2023sf1,t,Sweden,Norway,10
2023,sf1,2023sf1,t,Sweden,Switzerland,8
2023,sf1,2023sf1,t,Sweden,Czechia,7
2023,sf1,2023sf1,t,Sweden,Moldova,6
2023,sf1,2023sf1,t,Sweden,Croatia,5
2023,sf1,2023sf1,t,Sweden,Portugal,4
2023,sf1,2023sf1,t,Sweden,Israel,3
2023,sf1,2023sf1,t,Sweden,Netherlands,2
2023,sf1,2023sf1,t,Sweden,Serbia,1
2023,sf1,2023sf1,t,Switzerland,Portugal,12
2023,sf1,2023sf1,t,Switzerland,Finland,10
2023,sf1,2023sf1,t,Switzerland,Sweden,8
2023,sf1,2023sf1,t,Switzerland,Israel,7
2023,sf1,2023sf1,t,Switzerland,Serbia,6
2023,sf1,2023sf1,t,Switzerland,Croatia,5
2023,sf1,2023sf1,t,Switzerland,Czechia,4
2023,sf1,2023sf1,t,Switzerland,Norway,3
2023,sf1,2023sf1,t,Switzerland,Moldova,2
2023,sf1,2023sf1,t,Switzerland,Ireland,1
2023,sf2,2023sf2,t,Albania,Australia,12
2023,sf2,2023sf2,t,Albania,Austria,10
2023,sf2,2023sf2,t,Albania,Armenia,8
2023,sf2,2023sf2,t,Albania,Poland,7
2023,sf2,2023sf2,t,Albania,Cyprus,6
2023,sf2,2023sf2,t,Albania,Lithuania,5
2023,sf2,2023sf2,t,Albania,Slovenia,4
2023,sf2,2023sf2,t,Albania,Belgium,3
2023,sf2,2023sf2,t,Albania,Estonia,2
2023,sf2,2023sf2,t,Albania,Iceland,1
2023,sf2,2023sf2,t,Armenia,Georgia,12
2023,sf2,2023sf2,t,Armenia,Cyprus,10
2023,sf2,2023sf2,t,Armenia,Poland,8
2023,sf2,2023sf2,t,Armenia,Albania,7
2023,sf2,2023sf2,t,Armenia,Estonia,6
2023,sf2,2023sf2,t,Armenia,Slovenia,5
2023,sf2,2023sf2,t,Armenia,Australia,4
2023,sf2,2023sf2,t,Armenia,Austria,3
2023,sf2,2023sf2,t,Armenia,Greece,2
2023,sf2,2023sf2,t,Armenia,Belgium,1
2023,sf2,2023sf2,t,Australia,Austria,12
2023,sf2,2023sf2,t,Australia,Cyprus,10
2023,sf2,2023sf2,t,Australia,Slovenia,8
2023,sf2,2023sf2,t,Australia,Belgium,7
2023,sf2,2023sf2,t,Australia,Lithuania,6
2023,sf2,2023sf2,t,Australia,Iceland,5
2023,sf2,2023sf2,t,Australia,Estonia,4
2023,sf2,2023sf2,t,Australia,Albania,3
2023,sf2,2023sf2,t,Australia,Armenia,2
2023,sf2,2023sf2,t,Australia,Georgia,1
2023,sf2,2023sf2,t,Austria,Belgium,12
2023,sf2,2023sf2,t,Austria,Slovenia,10
2023,sf2,2023sf2,t,Austria,Australia,8
2023,sf2,2023sf2,t,Austria,Poland,7
2023,sf2,2023sf2,t,Austria,Albania,6
2023,sf2,2023sf2,t,Austria,Lithuania,5
2023,sf2,2023sf2,t,Austria,Armenia,4
2023,sf2,2023sf2,t,Austria,Estonia,3
2023,sf2,2023sf2,t,Austria,Cyprus,2
2023,sf2,2023sf2,t,Austria,Iceland,1
2023,sf2,2023sf2,t,Belgium,Armenia,12
2023,sf2,2023sf2,t,Belgium,Austria,10
2023,sf2,2023sf2,t,Belgium,Albania,8
2023,sf2,2023sf2,t,Belgium,Poland,7
2023,sf2,2023sf2,t,Belgium,Australia,6
2023,sf2,2023sf2,t,Belgium,Lithuania,5
2023,sf2,2023sf2,t,Belgium,Cyprus,4
2023,sf2,2023sf2,t,Belgium,Slovenia,3
2023,sf2,2023sf2,t,Belgium,Estonia,2
2023,sf2,2023sf2,t,Belgium,Iceland,1
2023,sf2,2023sf2,t,Cyprus,Greece,12
2023,sf2,2023sf2,t,Cyprus,Armenia,10
2023,sf2,2023sf2,t,Cyprus,Lithuania,8
2023,sf2,2023sf2,t,Cyprus,Australia,7
2023,sf2,2023sf2,t,Cyprus,Poland,6
2023,sf2,2023sf2,t,Cyprus,Austria,5
2023,sf2,2023sf2,t,Cyprus,Belgium,4
2023,sf2,2023sf2,t,Cyprus,Estonia,3
2023,sf2,2023sf2,t,Cyprus,Slovenia,2
2023,sf2,2023sf2,t,Cyprus,Albania,1
2023,sf2,2023sf2,t,Denmark,Iceland,12
2023,sf2,2023sf2,t,Denmark,Australia,10
2023,sf2,2023sf2,t,Denmark,Belgium,8
2023,sf2,2023sf2,t,Denmark,Poland,7
2023,sf2,2023sf2,t,Denmark,Austria,6
2023,sf2,2023sf2,t,Denmark,Lithuania,5
2023,sf2,2023sf2,t,Denmark,Cyprus,4
2023,sf2,2023sf2,t,Denmark,Albania,3
2023,sf2,2023sf2,t,Denmark,Slovenia,2
2023,sf2,2023sf2,t,Denmark,Estonia,1
2023,sf2,2023sf2,t,Estonia,Australia,12
2023,sf2,2023sf2,t,Estonia,Lithuania,10
2023,sf2,2023sf2,t,Estonia,Poland,8
2023,sf2,2023sf2,t,Estonia,Slovenia,7
2023,sf2,2023sf2,t,Estonia,Austria,6
2023,sf2,2023sf2,t,Estonia,Cyprus,5
2023,sf2,2023sf2,t,Estonia,Belgium,4
2023,sf2,2023sf2,t,Estonia,Armenia,3
2023,sf2,2023sf2,t,Estonia,Iceland,2
2023,sf2,2023sf2,t,Estonia,Georgia,1
2023,sf2,2023sf2,t,Georgia,Armenia,12
2023,sf2,2023sf2,t,Georgia,Lithuania,10
2023,sf2,2023sf2,t,Georgia,Poland,8
2023,sf2,2023sf2,t,Georgia,Australia,7
2023,sf2,2023sf2,t,Georgia,Iceland,6
2023,sf2,2023sf2,t,Georgia,Cyprus,5
2023,sf2,2023sf2,t,Georgia,Austria,4
2023,sf2,2023sf2,t,Georgia,Belgium,3
2023,sf2,2023sf2,t,Georgia,Estonia,2
2023,sf2,2023sf2,t,Georgia,Slovenia,1
2023,sf2,2023sf2,t,Greece,Cyprus,12
2023,sf2,2023sf2,t,Greece,Albania,10
2023,sf2,2023sf2,t,Greece,Armenia,8
2023,sf2,2023sf2,t,Greece,Georgia,7
2023,sf2,2023sf2,t,Greece,Austria,6
2023,sf2,2023sf2,t,Greece,Poland,5
2023,sf2,2023sf2,t,Greece,Australia,4
2023,sf2,2023sf2,t,Greece,Estonia,3
2023,sf2,2023sf2,t,Greece,Slovenia,2
2023,sf2,2023sf2,t,Greece,Belgium,1
2023,sf2,2023sf2,t,Iceland,Australia,12
2023,sf2,2023sf2,t,Iceland,Poland,10
2023,sf2,2023sf2,t,Iceland,Austria,8
2023,sf2,2023sf2,t,Iceland,Belgium,7
2023,sf2,2023sf2,t,Iceland,Denmark,6
2023,sf2,2023sf2,t,Iceland,Cyprus,5
2023,sf2,2023sf2,t,Iceland,Lithuania,4
2023,sf2,2023sf2,t,Iceland,Estonia,3
2023,sf2,2023sf2,t,Iceland,Albania,2
2023,sf2,2023sf2,t,Iceland,Slovenia,1
2023,sf2,2023sf2,t,Lithuania,Poland,12
2023,sf2,2023sf2,t,Lithuania,Estonia,10
2023,sf2,2023sf2,t,Lithuania,Australia,8
2023,sf2,2023sf2,t,Lithuania,Slovenia,7
2023,sf2,2023sf2,t,Lithuania,Austria,6
2023,sf2,2023sf2,t,Lithuania,Belgium,5
2023,sf2,2023sf2,t,Lithuania,Cyprus,4
2023,sf2,2023sf2,t,Lithuania,Georgia,3
2023,sf2,2023sf2,t,Lithuania,Iceland,2
2023,sf2,2023sf2,t,Lithuania,Armenia,1
2023,sf2,2023sf2,t,Poland,Slovenia,12
2023,sf2,2023sf2,t,Poland,Austria,10
2023,sf2,2023sf2,t,Poland,Australia,8
2023,sf2,2023sf2,t,Poland,Cyprus,7
2023,sf2,2023sf2,t,Poland,Lithuania,6
2023,sf2,2023sf2,t,Poland,Armenia,5
2023,sf2,2023sf2,t,Poland,Albania,4
2023,sf2,2023sf2,t,Poland,Belgium,3
2023,sf2,2023sf2,t,Poland,Estonia,2
2023,sf2,2023sf2,t,Poland,Georgia,1
2023,sf2,2023sf2,t,Romania,Slovenia,12
2023,sf2,2023sf2,t,Romania,Australia,10
2023,sf2,2023sf2,t,Romania,Albania,8
2023,sf2,2023sf2,t,Romania,Austria,7
2023,sf2,2023sf2,t,Romania,Armenia,6
2023,sf2,2023sf2,t,Romania,Estonia,5
2023,sf2,2023sf2,t,Romania,Cyprus,4
2023,sf2,2023sf2,t,Romania,Poland,3
2023,sf2,2023sf2,t,Romania,Georgia,2
2023,sf2,2023sf2,t,Romania,Lithuania,1
2023,sf2,2023sf2,t,San Marino,Lithuania,12
2023,sf2,2023sf2,t,San Marino,Estonia,10
2023,sf2,2023sf2,t,San Marino,Austria,8
2023,sf2,2023sf2,t,San Marino,Iceland,7
2023,sf2,2023sf2,t,San Marino,Australia,6
2023,sf2,2023sf2,t,San Marino,Belgium,5
2023,sf2,2023sf2,t,San Marino,Armenia,4
2023,sf2,2023sf2,t,San Marino,Georgia,3
2023,sf2,2023sf2,t,San Marino,Poland,2
2023,sf2,2023sf2,t,San Marino,Cyprus,1
2023,sf2,2023sf2,t,Slovenia,Albania,12
2023,sf2,2023sf2,t,Slovenia,Austria,10
2023,sf2,2023sf2,t,Slovenia,Poland,8
2023,sf2,2023sf2,t,Slovenia,Belgium,7
2023,sf2,2023sf2,t,Slovenia,Australia,6
2023,sf2,2023sf2,t,Slovenia,Estonia,5
2023,sf2,2023sf2,t,Slovenia,Cyprus,4
2023,sf2,2023sf2,t,Slovenia,Iceland,3
2023,sf2,2023sf2,t,Slovenia,Lithuania,2
2023,sf2,2023sf2,t,Slovenia,Armenia,1
2023,sf2,2023sf2,t,Spain,Slovenia,12
2023,sf2,2023sf2,t,Spain,Armenia,10
2023,sf2,2023sf2,t,Spain,Belgium,8
2023,sf2,2023sf2,t,Spain,Australia,7
2023,sf2,2023sf2,t,Spain,Austria,6
2023,sf2,2023sf2,t,Spain,Lithuania,5
2023,sf2,2023sf2,t,Spain,Poland,4
2023,sf2,2023sf2,t,Spain,Cyprus,3
2023,sf2,2023sf2,t,Spain,Albania,2
2023,sf2,2023sf2,t,Spain,Estonia,1
2023,sf2,2023sf2,t,Ukraine,Poland,12
2023,sf2,2023sf2,t,Ukraine,Lithuania,10
2023,sf2,2023sf2,t,Ukraine,Estonia,8
2023,sf2,2023sf2,t,Ukraine,Australia,7
2023,sf2,2023sf2,t,Ukraine,Slovenia,6
2023,sf2,2023sf2,t,Ukraine,Austria,5
2023,sf2,2023sf2,t,Ukraine,Cyprus,4
2023,sf2,2023sf2,t,Ukraine,Armenia,3
2023,sf2,2023sf2,t,Ukraine,Georgia,2
2023,sf2,2023sf2,t,Ukraine,Belgium,1
2023,sf2,2023sf2,t,United Kingdom,Lithuania,12
2023,sf2,2023sf2,t,United Kingdom,Poland,10
2023,sf2,2023sf2,t,United Kingdom,Australia,8
2023,sf2,2023sf2,t,United Kingdom,Austria,7
2023,sf2,2023sf2,t,United Kingdom,Belgium,6
2023,sf2,2023sf2,t,United Kingdom,Albania,5
2023,sf2,2023sf2,t,United Kingdom,Cyprus,4
2023,sf2,2023sf2,t,United Kingdom,Slovenia,3
2023,sf2,2023sf2,t,United Kingdom,Estonia,2
2023,sf2,2023sf2,t,United Kingdom,Iceland,1
2023,f,2023f,t,Albania,Italy,12
2023,f,2023f,t,Albania,Sweden,10
2023,f,2023f,t,Albania,Croatia,8
2023,f,2023f,t,Albania,Cyprus,7
2023,f,2023f,t,Albania,Finland,6
2023,f,2023f,t,Albania,Israel,5
2023,f,2023f,t,Albania,Norway,4
2023,f,2023f,t,Albania,France,3
2023,f,2023f,t,Albania,Slovenia,2
2023,f,2023f,t,Albania,Poland,1
2023,f,2023f,j,Albania,Sweden,12
2023,f,2023f,j,Albania,Armenia,10
2023,f,2023f,j,Albania,Estonia,8
2023,f,2023f,j,Albania,Switzerland,7
2023,f,2023f,j,Albania,Israel,6
2023,f,2023f,j,Albania,Belgium,5
2023,f,2023f,j,Albania,Cyprus,4
2023,f,2023f,j,Albania,Australia,3
2023,f,2023f,j,Albania,Italy,2
2023,f,2023f,j,Albania,Spain,1
2023,f,2023f,t,Armenia,Israel,12
2023,f,2023f,t,Armenia,France,10
2023,f,2023f,t,Armenia,Cyprus,8
2023,f,2023f,t,Armenia,Sweden,7
2023,f,2023f,t,Armenia,Finland,6
2023,f,2023f,t,Armenia,Poland,5
2023,f,2023f,t,Armenia,Norway,4
2023,f,2023f,t,Armenia,Italy,3
2023,f,2023f,t,Armenia,Switzerland,2
2023,f,2023f,t,Armenia,Ukraine,1
2023,f,2023f,j,Armenia,Israel,12
2023,f,2023f,j,Armenia,Sweden,10
2023,f,2023f,j,Armenia,Finland,8
2023,f,2023f,j,Armenia,France,7
2023,f,2023f,j,Armenia,Spain,6
2023,f,2023f,j,Armenia,Cyprus,5
2023,f,2023f,j,Armenia,Norway,4
2023,f,2023f,j,Armenia,Ukraine,3
2023,f,2023f,j,Armenia,Austria,2
2023,f,2023f,j,Armenia,Poland,1
2023,f,2023f,t,Australia,Finland,12
2023,f,2023f,t,Australia,Sweden,10
2023,f,2023f,t,Australia,Cyprus,8
2023,f,2023f,t,Australia,Austria,7
2023,f,2023f,t,Australia,Norway,6
2023,f,2023f,t,Australia,Israel,5
2023,f,2023f,t,Australia,Croatia,4
2023,f,2023f,t,Australia,Belgium,3
2023,f,2023f,t,Australia,France,2
2023,f,2023f,t,Australia,Slovenia,1
2023,f,2023f,j,Australia,Belgium,12
2023,f,2023f,j,Australia,Lithuania,10
2023,f,2023f,j,Australia,Estonia,8
2023,f,2023f,j,Australia,Sweden,7
2023,f,2023f,j,Australia,Austria,6
2023,f,2023f,j,Australia,Finland,5
2023,f,2023f,j,Australia,Spain,4
2023,f,2023f,j,Australia,Cyprus,3
2023,f,2023f,j,Australia,Portugal,2
2023,f,2023f,j,Australia,Italy,1
2023,f,2023f,t,Austria,Finland,12
2023,f,2023f,t,Austria,Croatia,10
2023,f,2023f,t,Austria,Italy,8
2023,f,2023f,t,Austria,Norway,7
2023,f,2023f,t,Austria,Germany,6
2023,f,2023f,t,Austria,Ukraine,5
2023,f,2023f,t,Austria,Sweden,4
2023,f,2023f,t,Austria,Albania,3
2023,f,2023f,t,Austria,Switzerland,2
2023,f,2023f,t,Austria,Israel,1
2023,f,2023f,j,Austria,Italy,12
2023,f,2023f,j,Austria,Sweden,10
2023,f,2023f,j,Austria,Finland,8
2023,f,2023f,j,Austria,Lithuania,7
2023,f,2023f,j,Austria,Slovenia,6
2023,f,2023f,j,Austria,Czechia,5
2023,f,2023f,j,Austria,Switzerland,4
2023,f,2023f,j,Austria,Belgium,3
2023,f,2023f,j,Austria,Cyprus,2
2023,f,2023f,j,Austria,Armenia,1
2023,f,2023f,t,Azerbaijan,Israel,12
2023,f,2023f,t,Azerbaijan,Sweden,10
2023,f,2023f,t,Azerbaijan,Finland,8
2023,f,2023f,t,Azerbaijan,Ukraine,7
2023,f,2023f,t,Azerbaijan,Cyprus,6
2023,f,2023f,t,Azerbaijan,Slovenia,5
2023,f,2023f,t,Azerbaijan,Italy,4
2023,f,2023f,t,Azerbaijan,Czechia,3
2023,f,2023f,t,Azerbaijan,Norway,2
2023,f,2023f,t,Azerbaijan,Switzerland,1
2023,f,2023f,j,Azerbaijan,Israel,12
2023,f,2023f,j,Azerbaijan,Sweden,10
2023,f,2023f,j,Azerbaijan,Albania,8
2023,f,2023f,j,Azerbaijan,Spain,7
2023,f,2023f,j,Azerbaijan,Italy,6
2023,f,2023f,j,Azerbaijan,Australia,5
2023,f,2023f,j,Azerbaijan,Switzerland,4
2023,f,2023f,j,Azerbaijan,Finland,3
2023,f,2023f,j,Azerbaijan,Ukraine,2
2023,f,2023f,j,Azerbaijan,Estonia,1
2023,f,2023f,t,Belgium,Finland,12
2023,f,2023f,t,Belgium,Sweden,10
2023,f,2023f,t,Belgium,Norway,8
2023,f,2023f,t,Belgium,Italy,7
2023,f,2023f,t,Belgium,Armenia,6
2023,f,2023f,t,Belgium,Israel,5
2023,f,2023f,t,Belgium,Poland,4
2023,f,2023f,t,Belgium,Albania,3
2023,f,2023f,t,Belgium,France,2
2023,f,2023f,t,Belgium,Ukraine,1
2023,f,2023f,j,Belgium,Austria,12
2023,f,2023f,j,Belgium,Israel,10
2023,f,2023f,j,Belgium,Sweden,8
2023,f,2023f,j,Belgium,Italy,7
2023,f,2023f,j,Belgium,Spain,6
2023,f,2023f,j,Belgium,Finland,5
2023,f,2023f,j,Belgium,Australia,4
2023,f,2023f,j,Belgium,Czechia,3
2023,f,2023f,j,Belgium,Poland,2
2023,f,2023f,j,Belgium,France,1
2023,f,2023f,t,Croatia,Slovenia,12
2023,f,2023f,t,Croatia,Finland,10
2023,f,2023f,t,Croatia,Italy,8
2023,f,2023f,t,Croatia,Serbia,7
2023,f,2023f,t,Croatia,Albania,6
2023,f,2023f,t,Croatia,Norway,5
2023,f,2023f,t,Croatia,Israel,4
2023,f,2023f,t,Croatia,Czechia,3
2023,f,2023f,t,Croatia,Sweden,2
2023,f,2023f,t,Croatia,Moldova,1
2023,f,2023f,j,Croatia,Italy,12
2023,f,2023f,j,Croatia,Sweden,10
2023,f,2023f,j,Croatia,Israel,8
2023,f,2023f,j,Croatia,Finland,7
2023,f,2023f,j,Croatia,Spain,6
2023,f,2023f,j,Croatia,Slovenia,5
2023,f,2023f,j,Croatia,Serbia,4
2023,f,2023f,j,Croatia,Estonia,3
2023,f,2023f,j,Croatia,Moldova,2
2023,f,2023f,j,Croatia,Portugal,1
2023,f,2023f,t,Cyprus,Israel,12
2023,f,2023f,t,Cyprus,Ukraine,10
2023,f,2023f,t,Cyprus,Sweden,8
2023,f,2023f,t,Cyprus,Finland,7
2023,f,2023f,t,Cyprus,Italy,6
2023,f,2023f,t,Cyprus,Norway,5
2023,f,2023f,t,Cyprus,Armenia,4
2023,f,2023f,t,Cyprus,France,3
2023,f,2023f,t,Cyprus,Poland,2
2023,f,2023f,t,Cyprus,Moldova,1
2023,f,2023f,j,Cyprus,Sweden,12
2023,f,2023f,j,Cyprus,Austria,10
2023,f,2023f,j,Cyprus,Australia,8
2023,f,2023f,j,Cyprus,Israel,7
2023,f,2023f,j,Cyprus,Spain,6
2023,f,2023f,j,Cyprus,Italy,5
2023,f,2023f,j,Cyprus,Armenia,4
2023,f,2023f,j,Cyprus,Finland,3
2023,f,2023f,j,Cyprus,Switzerland,2
2023,f,2023f,j,Cyprus,Czechia,1
2023,f,2023f,t,Czechia,Ukraine,12
2023,f,2023f,t,Czechia,Finland,10
2023,f,2023f,t,Czechia,Israel,8
2023,f,2023f,t,Czechia,Norway,7
2023,f,2023f,t,Czechia,Sweden,6
2023,f,2023f,t,Czechia,Moldova,5
2023,f,2023f,t,Czechia,Croatia,4
2023,f,2023f,t,Czechia,Slovenia,3
2023,f,2023f,t,Czechia,Armenia,2
2023,f,2023f,t,Czechia,Italy,1
2023,f,2023f,j,Czechia,Ukraine,12
2023,f,2023f,j,Czechia,Sweden,10
2023,f,2023f,j,Czechia,Armenia,8
2023,f,2023f,j,Czechia,Australia,7
2023,f,2023f,j,Czechia,Slovenia,6
2023,f,2023f,j,Czechia,Finland,5
2023,f,2023f,j,Czechia,Italy,4
2023,f,2023f,j,Czechia,Spain,3
2023,f,2023f,j,Czechia,Estonia,2
2023,f,2023f,j,Czechia,Germany,1
2023,f,2023f,t,Denmark,Finland,12
2023,f,2023f,t,Denmark,Norway,10
2023,f,2023f,t,Denmark,Sweden,8
2023,f,2023f,t,Denmark,Ukraine,7
2023,f,2023f,t,Denmark,Belgium,6
2023,f,2023f,t,Denmark,Poland,5
2023,f,2023f,t,Denmark,Switzerland,4
2023,f,2023f,t,Denmark,Italy,3
2023,f,2023f,t,Denmark,Cyprus,2
2023,f,2023f,t,Denmark,Moldova,1
2023,f,2023f,j,Denmark,Sweden,12
2023,f,2023f,j,Denmark,Norway,10
2023,f,2023f,j,Denmark,Finland,8
2023,f,2023f,j,Denmark,Austria,7
2023,f,2023f,j,Denmark,France,6
2023,f,2023f,j,Denmark,Cyprus,5
2023,f,2023f,j,Denmark,Lithuania,4
2023,f,2023f,j,Denmark,Belgium,3
2023,f,2023f,j,Denmark,Australia,2
2023,f,2023f,j,Denmark,United Kingdom,1
2023,f,2023f,t,Estonia,Finland,12
2023,f,2023f,t,Estonia,Sweden,10
2023,f,2023f,t,Estonia,Ukraine,8
2023,f,2023f,t,Estonia,Norway,7
2023,f,2023f,t,Estonia,Australia,6
2023,f,2023f,t,Estonia,Lithuania,5
2023,f,2023f,t,Estonia,Switzerland,4
2023,f,2023f,t,Estonia,Poland,3
2023,f,2023f,t,Estonia,Italy,2
2023,f,2023f,t,Estonia,Slovenia,1
2023,f,2023f,j,Estonia,Sweden,12
2023,f,2023f,j,Estonia,Finland,10
2023,f,2023f,j,Estonia,Australia,8
2023,f,2023f,j,Estonia,Ukraine,7
2023,f,2023f,j,Estonia,Belgium,6
2023,f,2023f,j,Estonia,Italy,5
2023,f,2023f,j,Estonia,Israel,4
2023,f,2023f,j,Estonia,Armenia,3
2023,f,2023f,j,Estonia,Spain,2
2023,f,2023f,j,Estonia,Lithuania,1
2023,f,2023f,t,Finland,Norway,12
2023,f,2023f,t,Finland,Czechia,10
2023,f,2023f,t,Finland,Australia,8
2023,f,2023f,t,Finland,Slovenia,7
2023,f,2023f,t,Finland,Estonia,6
2023,f,2023f,t,Finland,Germany,5
2023,f,2023f,t,Finland,Croatia,4
2023,f,2023f,t,Finland,Moldova,3
2023,f,2023f,t,Finland,Austria,2
2023,f,2023f,t,Finland,Switzerland,1
2023,f,2023f,j,Finland,Sweden,12
2023,f,2023f,j,Finland,Switzerland,10
2023,f,2023f,j,Finland,Czechia,8
2023,f,2023f,j,Finland,France,7
2023,f,2023f,j,Finland,Italy,6
2023,f,2023f,j,Finland,Belgium,5
2023,f,2023f,j,Finland,United Kingdom,4
2023,f,2023f,j,Finland,Portugal,3
2023,f,2023f,j,Finland,Austria,2
2023,f,2023f,j,Finland,Cyprus,1
2023,f,2023f,t,France,Armenia,12
2023,f,2023f,t,France,Israel,10
2023,f,2023f,t,France,Moldova,8
2023,f,2023f,t,France,Italy,7
2023,f,2023f,t,France,Finland,6
2023,f,2023f,t,France,Portugal,5
2023,f,2023f,t,France,Ukraine,4
2023,f,2023f,t,France,Sweden,3
2023,f,2023f,t,France,Belgium,2
2023,f,2023f,t,France,Norway,1
2023,f,2023f,j,France,Israel,12
2023,f,2023f,j,France,Austria,10
2023,f,2023f,j,France,Finland,8
2023,f,2023f,j,France,Armenia,7
2023,f,2023f,j,France,Sweden,6
2023,f,2023f,j,France,Portugal,5
2023,f,2023f,j,France,Czechia,4
2023,f,2023f,j,France,Switzerland,3
2023,f,2023f,j,France,Italy,2
2023,f,2023f,j,France,Ukraine,1
2023,f,2023f,t,Georgia,Armenia,12
2023,f,2023f,t,Georgia,Ukraine,10
2023,f,2023f,t,Georgia,Finland,8
2023,f,2023f,t,Georgia,Sweden,7
2023,f,2023f,t,Georgia,Israel,6
2023,f,2023f,t,Georgia,Italy,5
2023,f,2023f,t,Georgia,Lithuania,4
2023,f,2023f,t,Georgia,Moldova,3
2023,f,2023f,t,Georgia,Norway,2
2023,f,2023f,t,Georgia,Croatia,1
2023,f,2023f,j,Georgia,Belgium,12
2023,f,2023f,j,Georgia,Armenia,10
2023,f,2023f,j,Georgia,Italy,8
2023,f,2023f,j,Georgia,Israel,7
2023,f,2023f,j,Georgia,Lithuania,6
2023,f,2023f,j,Georgia,Estonia,5
2023,f,2023f,j,Georgia,Sweden,4
2023,f,2023f,j,Georgia,Cyprus,3
2023,f,2023f,j,Georgia,Australia,2
2023,f,2023f,j,Georgia,Finland,1
2023,f,2023f,t,Germany,Finland,12
2023,f,2023f,t,Germany,Italy,10
2023,f,2023f,t,Germany,Albania,8
2023,f,2023f,t,Germany,Ukraine,7
2023,f,2023f,t,Germany,Croatia,6
2023,f,2023f,t,Germany,Norway,5
2023,f,2023f,t,Germany,Poland,4
2023,f,2023f,t,Germany,Switzerland,3
2023,f,2023f,t,Germany,Belgium,2
2023,f,2023f,t,Germany,Sweden,1
2023,f,2023f,j,Germany,Sweden,12
2023,f,2023f,j,Germany,Estonia,10
2023,f,2023f,j,Germany,Australia,8
2023,f,2023f,j,Germany,Spain,7
2023,f,2023f,j,Germany,Norway,6
2023,f,2023f,j,Germany,Czechia,5
2023,f,2023f,j,Germany,Italy,4
2023,f,2023f,j,Germany,Serbia,3
2023,f,2023f,j,Germany,Austria,2
2023,f,2023f,j,Germany,Lithuania,1
2023,f,2023f,t,Greece,Cyprus,12
2023,f,2023f,t,Greece,Finland,10
2023,f,2023f,t,Greece,Sweden,8
2023,f,2023f,t,Greece,Israel,7
2023,f,2023f,t,Greece,Norway,6
2023,f,2023f,t,Greece,Italy,5
2023,f,2023f,t,Greece,Albania,4
2023,f,2023f,t,Greece,France,3
2023,f,2023f,t,Greece,Armenia,2
2023,f,2023f,t,Greece,Czechia,1
2023,f,2023f,j,Greece,Belgium,12
2023,f,2023f,j,Greece,Portugal,10
2023,f,2023f,j,Greece,Israel,8
2023,f,2023f,j,Greece,Austria,7
2023,f,2023f,j,Greece,Sweden,6
2023,f,2023f,j,Greece,Australia,5
2023,f,2023f,j,Greece,Cyprus,4
2023,f,2023f,j,Greece,Albania,3
2023,f,2023f,j,Greece,Switzerland,2
2023,f,2023f,j,Greece,Serbia,1
2023,f,2023f,t,Iceland,Finland,12
2023,f,2023f,t,Iceland,Sweden,10
2023,f,2023f,t,Iceland,Norway,8
2023,f,2023f,t,Iceland,Poland,7
2023,f,2023f,t,Iceland,Belgium,6
2023,f,2023f,t,Iceland,Croatia,5
2023,f,2023f,t,Iceland,France,4
2023,f,2023f,t,Iceland,Australia,3
2023,f,2023f,t,Iceland,Ukraine,2
2023,f,2023f,t,Iceland,Italy,1
2023,f,2023f,j,Iceland,Australia,12
2023,f,2023f,j,Iceland,Finland,10
2023,f,2023f,j,Iceland,Austria,8
2023,f,2023f,j,Iceland,Sweden,7
2023,f,2023f,j,Iceland,Czechia,6
2023,f,2023f,j,Iceland,Belgium,5
2023,f,2023f,j,Iceland,Norway,4
2023,f,2023f,j,Iceland,Spain,3
2023,f,2023f,j,Iceland,Germany,2
2023,f,2023f,j,Iceland,Serbia,1
2023,f,2023f,t,Ireland,Finland,12
2023,f,2023f,t,Ireland,Lithuania,10
2023,f,2023f,t,Ireland,Poland,8
2023,f,2023f,t,Ireland,Ukraine,7
2023,f,2023f,t,Ireland,Sweden,6
2023,f,2023f,t,Ireland,Norway,5
2023,f,2023f,t,Ireland,Moldova,4
2023,f,2023f,t,Ireland,Belgium,3
2023,f,2023f,t,Ireland,Croatia,2
2023,f,2023f,t,Ireland,Israel,1
2023,f,2023f,j,Ireland,Sweden,12
2023,f,2023f,j,Ireland,Belgium,10
2023,f,2023f,j,Ireland,Finland,8
2023,f,2023f,j,Ireland,Israel,7
2023,f,2023f,j,Ireland,Armenia,6
2023,f,2023f,j,Ireland,France,5
2023,f,2023f,j,Ireland,Australia,4
2023,f,2023f,j,Ireland,Czechia,3
2023,f,2023f,j,Ireland,United Kingdom,2
2023,f,2023f,j,Ireland,Lithuania,1
2023,f,2023f,t,Israel,Finland,12
2023,f,2023f,t,Israel,Norway,10
2023,f,2023f,t,Israel,Ukraine,8
2023,f,2023f,t,Israel,Italy,7
2023,f,2023f,t,Israel,Croatia,6
2023,f,2023f,t,Israel,Moldova,5
2023,f,2023f,t,Israel,Sweden,4
2023,f,2023f,t,Israel,Armenia,3
2023,f,2023f,t,Israel,Czechia,2
2023,f,2023f,t,Israel,France,1
2023,f,2023f,j,Israel,Sweden’agit,12
2023,f,2023f,j,Israel,Norway,10
2023,f,2023f,j,Israel,Finland,8
2023,f,2023f,j,Israel,Ukraine,7
2023,f,2023f,j,Israel,Austria,6
2023,f,2023f,j,Israel,Estonia,5
2023,f,2023f,j,Israel,Czechia,4
2023,f,2023f,j,Israel,Belgium,3
2023,f,2023f,j,Israel,Poland,2
2023,f,2023f,j,Israel,Cyprus,1
2023,f,2023f,t,Italy,Moldova,12
2023,f,2023f,t,Italy,Norway,10
2023,f,2023f,t,Italy,Ukraine,8
2023,f,2023f,t,Italy,Albania,7
2023,f,2023f,t,Italy,Finland,6
2023,f,2023f,t,Italy,Israel,5
2023,f,2023f,t,Italy,Croatia,4
2023,f,2023f,t,Italy,Sweden,3
2023,f,2023f,t,Italy,Czechia,2
2023,f,2023f,t,Italy,Switzerland,1
2023,f,2023f,j,Italy,Israel,12
2023,f,2023f,j,Italy,Ukraine,10
2023,f,2023f,j,Italy,Sweden,8
2023,f,2023f,j,Italy,Czechia,7
2023,f,2023f,j,Italy,Estonia,6
2023,f,2023f,j,Italy,Armenia,5
2023,f,2023f,j,Italy,Switzerland,4
2023,f,2023f,j,Italy,Lithuania,3
2023,f,2023f,j,Italy,Belgium,2
2023,f,2023f,j,Italy,Serbia,1
2023,f,2023f,t,Latvia,Finland,12
2023,f,2023f,t,Latvia,Lithuania,10
2023,f,2023f,t,Latvia,Sweden,8
2023,f,2023f,t,Latvia,Ukraine,7
2023,f,2023f,t,Latvia,Estonia,6
2023,f,2023f,t,Latvia,Israel,5
2023,f,2023f,t,Latvia,Croatia,4
2023,f,2023f,t,Latvia,Norway,3
2023,f,2023f,t,Latvia,Slovenia,2
2023,f,2023f,t,Latvia,Czechia,1
2023,f,2023f,j,Latvia,Estonia,12
2023,f,2023f,j,Latvia,Sweden,10
2023,f,2023f,j,Latvia,Spain,8
2023,f,2023f,j,Latvia,Lithuania,7
2023,f,2023f,j,Latvia,Cyprus,6
2023,f,2023f,j,Latvia,Israel,5
2023,f,2023f,j,Latvia,Ukraine,4
2023,f,2023f,j,Latvia,Italy,3
2023,f,2023f,j,Latvia,Belgium,2
2023,f,2023f,j,Latvia,Armenia,1
2023,f,2023f,t,Lithuania,Finland,12
2023,f,2023f,t,Lithuania,Ukraine,10
2023,f,2023f,t,Lithuania,Poland,8
2023,f,2023f,t,Lithuania,Sweden,7
2023,f,2023f,t,Lithuania,Italy,6
2023,f,2023f,t,Lithuania,Estonia,5
2023,f,2023f,t,Lithuania,Croatia,4
2023,f,2023f,t,Lithuania,Israel,3
2023,f,2023f,t,Lithuania,Moldova,2
2023,f,2023f,t,Lithuania,France,1
2023,f,2023f,j,Lithuania,Sweden,12
2023,f,2023f,j,Lithuania,Israel,10
2023,f,2023f,j,Lithuania,Austria,8
2023,f,2023f,j,Lithuania,Belgium,7
2023,f,2023f,j,Lithuania,France,6
2023,f,2023f,j,Lithuania,Estonia,5
2023,f,2023f,j,Lithuania,Australia,4
2023,f,2023f,j,Lithuania,Finland,3
2023,f,2023f,j,Lithuania,Ukraine,2
2023,f,2023f,j,Lithuania,Cyprus,1
2023,f,2023f,t,Malta,Italy,12
2023,f,2023f,t,Malta,Sweden,10
2023,f,2023f,t,Malta,Finland,8
2023,f,2023f,t,Malta,Norway,7
2023,f,2023f,t,Malta,Israel,6
2023,f,2023f,t,Malta,Ukraine,5
2023,f,2023f,t,Malta,United Kingdom,4
2023,f,2023f,t,Malta,Albania,3
2023,f,2023f,t,Malta,Serbia,2
2023,f,2023f,t,Malta,France,1
2023,f,2023f,j,Malta,Sweden,12
2023,f,2023f,j,Malta,Italy,10
2023,f,2023f,j,Malta,Finland,8
2023,f,2023f,j,Malta,Israel,7
2023,f,2023f,j,Malta,Switzerland,6
2023,f,2023f,j,Malta,Cyprus,5
2023,f,2023f,j,Malta,Lithuania,4
2023,f,2023f,j,Malta,Portugal,3
2023,f,2023f,j,Malta,Norway,2
2023,f,2023f,j,Malta,Austria,1
2023,f,2023f,t,Moldova,Ukraine,12
2023,f,2023f,t,Moldova,Israel,10
2023,f,2023f,t,Moldova,Sweden,8
2023,f,2023f,t,Moldova,Finland,7
2023,f,2023f,t,Moldova,Norway,6
2023,f,2023f,t,Moldova,Italy,5
2023,f,2023f,t,Moldova,Poland,4
2023,f,2023f,t,Moldova,Cyprus,3
2023,f,2023f,t,Moldova,Armenia,2
2023,f,2023f,t,Moldova,Czechia,1
2023,f,2023f,j,Moldova,Sweden,12
2023,f,2023f,j,Moldova,Italy,10
2023,f,2023f,j,Moldova,Portugal,8
2023,f,2023f,j,Moldova,Estonia,7
2023,f,2023f,j,Moldova,Ukraine,6
2023,f,2023f,j,Moldova,Australia,5
2023,f,2023f,j,Moldova,Cyprus,4
2023,f,2023f,j,Moldova,Spain,3
2023,f,2023f,j,Moldova,Armenia,2
2023,f,2023f,j,Moldova,Albania,1
2023,f,2023f,t,Netherlands,Finland,12
2023,f,2023f,t,Netherlands,Belgium,10
2023,f,2023f,t,Netherlands,Sweden,8
2023,f,2023f,t,Netherlands,Norway,7
2023,f,2023f,t,Netherlands,Israel,6
2023,f,2023f,t,Netherlands,Estonia,5
2023,f,2023f,t,Netherlands,Austria,4
2023,f,2023f,t,Netherlands,Italy,3
2023,f,2023f,t,Netherlands,Poland,2
2023,f,2023f,t,Netherlands,Australia,1
2023,f,2023f,j,Netherlands,Sweden,12
2023,f,2023f,j,Netherlands,Finland,10
2023,f,2023f,j,Netherlands,Czechia,8
2023,f,2023f,j,Netherlands,Spain,7
2023,f,2023f,j,Netherlands,Switzerland,6
2023,f,2023f,j,Netherlands,Portugal,5
2023,f,2023f,j,Netherlands,Belgium,4
2023,f,2023f,j,Netherlands,France,3
2023,f,2023f,j,Netherlands,Israel,2
2023,f,2023f,j,Netherlands,Austria,1
2023,f,2023f,t,Norway,Finland,12
2023,f,2023f,t,Norway,Sweden,10
2023,f,2023f,t,Norway,France,8
2023,f,2023f,t,Norway,Italy,7
2023,f,2023f,t,Norway,Poland,6
2023,f,2023f,t,Norway,Switzerland,5
2023,f,2023f,t,Norway,Belgium,4
2023,f,2023f,t,Norway,Israel,3
2023,f,2023f,t,Norway,Cyprus,2
2023,f,2023f,t,Norway,Ukraine,1
2023,f,2023f,j,Norway,Finland,12
2023,f,2023f,j,Norway,Sweden,10
2023,f,2023f,j,Norway,Moldova,8
2023,f,2023f,j,Norway,Cyprus,7
2023,f,2023f,j,Norway,Italy,6
2023,f,2023f,j,Norway,Australia,5
2023,f,2023f,j,Norway,Czechia,4
2023,f,2023f,j,Norway,Israel,3
2023,f,2023f,j,Norway,Switzerland,2
2023,f,2023f,j,Norway,Spain,1
2023,f,2023f,t,Poland,Ukraine,12
2023,f,2023f,t,Poland,Finland,10
2023,f,2023f,t,Poland,Norway,8
2023,f,2023f,t,Poland,Sweden,7
2023,f,2023f,t,Poland,Croatia,6
2023,f,2023f,t,Poland,Israel,5
2023,f,2023f,t,Poland,Cyprus,4
2023,f,2023f,t,Poland,Czechia,3
2023,f,2023f,t,Poland,Slovenia,2
2023,f,2023f,t,Poland,Lithuania,1
2023,f,2023f,j,Poland,Israel,12
2023,f,2023f,j,Poland,Cyprus,10
2023,f,2023f,j,Poland,Estonia,8
2023,f,2023f,j,Poland,Sweden,7
2023,f,2023f,j,Poland,Italy,6
2023,f,2023f,j,Poland,Belgium,5
2023,f,2023f,j,Poland,Australia,4
2023,f,2023f,j,Poland,Lithuania,3
2023,f,2023f,j,Poland,Switzerland,2
2023,f,2023f,j,Poland,Armenia,1
2023,f,2023f,t,Portugal,Ukraine,12
2023,f,2023f,t,Portugal,Finland,10
2023,f,2023f,t,Portugal,Moldova,8
2023,f,2023f,t,Portugal,Sweden,7
2023,f,2023f,t,Portugal,Italy,6
2023,f,2023f,t,Portugal,Israel,5
2023,f,2023f,t,Portugal,Norway,4
2023,f,2023f,t,Portugal,Spain,3
2023,f,2023f,t,Portugal,France,2
2023,f,2023f,t,Portugal,Belgium,1
2023,f,2023f,j,Portugal,Australia,12
2023,f,2023f,j,Portugal,Spain,10
2023,f,2023f,j,Portugal,Estonia,8
2023,f,2023f,j,Portugal,Czechia,7
2023,f,2023f,j,Portugal,Belgium,6
2023,f,2023f,j,Portugal,Sweden,5
2023,f,2023f,j,Portugal,Serbia,4
2023,f,2023f,j,Portugal,Croatia,3
2023,f,2023f,j,Portugal,Switzerland,2
2023,f,2023f,j,Portugal,Norway,1
2023,f,2023f,t,Romania,Moldova,12
2023,f,2023f,t,Romania,Finland,10
2023,f,2023f,t,Romania,Sweden,8
2023,f,2023f,t,Romania,Italy,7
2023,f,2023f,t,Romania,Israel,6
2023,f,2023f,t,Romania,Norway,5
2023,f,2023f,t,Romania,Ukraine,4
2023,f,2023f,t,Romania,France,3
2023,f,2023f,t,Romania,Slovenia,2
2023,f,2023f,t,Romania,Cyprus,1
2023,f,2023f,j,Romania,Italy,12
2023,f,2023f,j,Romania,Sweden,10
2023,f,2023f,j,Romania,Estonia,8
2023,f,2023f,j,Romania,Moldova,7
2023,f,2023f,j,Romania,Cyprus,6
2023,f,2023f,j,Romania,Albania,5
2023,f,2023f,j,Romania,Israel,4
2023,f,2023f,j,Romania,Australia,3
2023,f,2023f,j,Romania,Belgium,2
2023,f,2023f,j,Romania,Poland,1
2023,f,2023f,t,San Marino,Finland,12
2023,f,2023f,t,San Marino,Israel,10
2023,f,2023f,t,San Marino,Sweden,8
2023,f,2023f,t,San Marino,Italy,7
2023,f,2023f,t,San Marino,Ukraine,6
2023,f,2023f,t,San Marino,Cyprus,5
2023,f,2023f,t,San Marino,Norway,4
2023,f,2023f,t,San Marino,Moldova,3
2023,f,2023f,t,San Marino,Lithuania,2
2023,f,2023f,t,San Marino,Poland,1
2023,f,2023f,j,San Marino,Italy,12
2023,f,2023f,j,San Marino,Estonia,10
2023,f,2023f,j,San Marino,Lithuania,8
2023,f,2023f,j,San Marino,Belgium,7
2023,f,2023f,j,San Marino,Austria,6
2023,f,2023f,j,San Marino,Australia,5
2023,f,2023f,j,San Marino,Sweden,4
2023,f,2023f,j,San Marino,Moldova,3
2023,f,2023f,j,San Marino,Spain,2
2023,f,2023f,j,San Marino,Norway,1
2023,f,2023f,t,Serbia,Finland,12
2023,f,2023f,t,Serbia,Croatia,10
2023,f,2023f,t,Serbia,Slovenia,8
2023,f,2023f,t,Serbia,Israel,7
2023,f,2023f,t,Serbia,Sweden,6
2023,f,2023f,t,Serbia,Norway,5
2023,f,2023f,t,Serbia,Czechia,4
2023,f,2023f,t,Serbia,Austria,3
2023,f,2023f,t,Serbia,Italy,2
2023,f,2023f,t,Serbia,France,1
2023,f,2023f,j,Serbia,Slovenia,12
2023,f,2023f,j,Serbia,Israel,10
2023,f,2023f,j,Serbia,Croatia,8
2023,f,2023f,j,Serbia,Finland,7
2023,f,2023f,j,Serbia,Austria,6
2023,f,2023f,j,Serbia,Sweden,5
2023,f,2023f,j,Serbia,France,4
2023,f,2023f,j,Serbia,Spain,3
2023,f,2023f,j,Serbia,Italy,2
2023,f,2023f,j,Serbia,Czechia,1
2023,f,2023f,t,Slovenia,Croatia,12
2023,f,2023f,t,Slovenia,Finland,10
2023,f,2023f,t,Slovenia,Italy,8
2023,f,2023f,t,Slovenia,Albania,7
2023,f,2023f,t,Slovenia,Serbia,6
2023,f,2023f,t,Slovenia,Norway,5
2023,f,2023f,t,Slovenia,Sweden,4
2023,f,2023f,t,Slovenia,France,3
2023,f,2023f,t,Slovenia,Belgium,2
2023,f,2023f,t,Slovenia,Poland,1
2023,f,2023f,j,Slovenia,Italy,12
2023,f,2023f,j,Slovenia,Estonia,10
2023,f,2023f,j,Slovenia,Lithuania,8
2023,f,2023f,j,Slovenia,Sweden,7
2023,f,2023f,j,Slovenia,Czechia,6
2023,f,2023f,j,Slovenia,Belgium,5
2023,f,2023f,j,Slovenia,Australia,4
2023,f,2023f,j,Slovenia,Austria,3
2023,f,2023f,j,Slovenia,Spain,2
2023,f,2023f,j,Slovenia,Switzerland,1
2023,f,2023f,t,Spain,Finland,12
2023,f,2023f,t,Spain,Ukraine,10
2023,f,2023f,t,Spain,Norway,8
2023,f,2023f,t,Spain,Israel,7
2023,f,2023f,t,Spain,Italy,6
2023,f,2023f,t,Spain,Sweden,5
2023,f,2023f,t,Spain,Portugal,4
2023,f,2023f,t,Spain,Belgium,3
2023,f,2023f,t,Spain,Armenia,2
2023,f,2023f,t,Spain,Moldova,1
2023,f,2023f,j,Spain,Sweden,12
2023,f,2023f,j,Spain,Italy,10
2023,f,2023f,j,Spain,Israel,8
2023,f,2023f,j,Spain,Estonia,7
2023,f,2023f,j,Spain,Portugal,6
2023,f,2023f,j,Spain,France,5
2023,f,2023f,j,Spain,Belgium,4
2023,f,2023f,j,Spain,Armenia,3
2023,f,2023f,j,Spain,Norway,2
2023,f,2023f,j,Spain,Finland,1
2023,f,2023f,t,Sweden,Finland,12
2023,f,2023f,t,Sweden,Norway,10
2023,f,2023f,t,Sweden,Switzerland,8
2023,f,2023f,t,Sweden,Belgium,7
2023,f,2023f,t,Sweden,Italy,6
2023,f,2023f,t,Sweden,Croatia,5
2023,f,2023f,t,Sweden,Ukraine,4
2023,f,2023f,t,Sweden,Czechia,3
2023,f,2023f,t,Sweden,France,2
2023,f,2023f,t,Sweden,Australia,1
2023,f,2023f,j,Sweden,Finland,12
2023,f,2023f,j,Sweden,France,10
2023,f,2023f,j,Sweden,Norway,8
2023,f,2023f,j,Sweden,Italy,7
2023,f,2023f,j,Sweden,Switzerland,6
2023,f,2023f,j,Sweden,Israel,5
2023,f,2023f,j,Sweden,United Kingdom,4
2023,f,2023f,j,Sweden,Czechia,3
2023,f,2023f,j,Sweden,Estonia,2
2023,f,2023f,j,Sweden,Cyprus,1
2023,f,2023f,t,Switzerland,Albania,12
2023,f,2023f,t,Switzerland,Italy,10
2023,f,2023f,t,Switzerland,Finland,8
2023,f,2023f,t,Switzerland,Portugal,7
2023,f,2023f,t,Switzerland,Croatia,6
2023,f,2023f,t,Switzerland,Sweden,5
2023,f,2023f,t,Switzerland,Germany,4
2023,f,2023f,t,Switzerland,Israel,3
2023,f,2023f,t,Switzerland,Norway,2
2023,f,2023f,t,Switzerland,Serbia,1
2023,f,2023f,j,Switzerland,Czechia,12
2023,f,2023f,j,Switzerland,Estonia,10
2023,f,2023f,j,Switzerland,Italy,8
2023,f,2023f,j,Switzerland,Austria,7
2023,f,2023f,j,Switzerland,Sweden,6
2023,f,2023f,j,Switzerland,Armenia,5
2023,f,2023f,j,Switzerland,Norway,4
2023,f,2023f,j,Switzerland,Spain,3
2023,f,2023f,j,Switzerland,Australia,2
2023,f,2023f,j,Switzerland,Israel,1
2023,f,2023f,t,Ukraine,Poland,12
2023,f,2023f,t,Ukraine,Finland,10
2023,f,2023f,t,Ukraine,Croatia,8
2023,f,2023f,t,Ukraine,Norway,7
2023,f,2023f,t,Ukraine,Moldova,6
2023,f,2023f,t,Ukraine,United Kingdom,5
2023,f,2023f,t,Ukraine,Lithuania,4
2023,f,2023f,t,Ukraine,Sweden,3
2023,f,2023f,t,Ukraine,Czechia,2
2023,f,2023f,t,Ukraine,Israel,1
2023,f,2023f,j,Ukraine,Sweden,12
2023,f,2023f,j,Ukraine,Lithuania,10
2023,f,2023f,j,Ukraine,Australia,8
2023,f,2023f,j,Ukraine,Czechia,7
2023,f,2023f,j,Ukraine,Poland,6
2023,f,2023f,j,Ukraine,Estonia,5
2023,f,2023f,j,Ukraine,United Kingdom,4
2023,f,2023f,j,Ukraine,Slovenia,3
2023,f,2023f,j,Ukraine,Italy,2
2023,f,2023f,j,Ukraine,Israel,1
2023,f,2023f,t,United Kingdom,Finland,12
2023,f,2023f,t,United Kingdom,Lithuania,10
2023,f,2023f,t,United Kingdom,Poland,8
2023,f,2023f,t,United Kingdom,Norway,7
2023,f,2023f,t,United Kingdom,Belgium,6
2023,f,2023f,t,United Kingdom,Sweden,5
2023,f,2023f,t,United Kingdom,Ukraine,4
2023,f,2023f,t,United Kingdom,Israel,3
2023,f,2023f,t,United Kingdom,Australia,2
2023,f,2023f,t,United Kingdom,Moldova,1
2023,f,2023f,j,United Kingdom,Sweden,12
2023,f,2023f,j,United Kingdom,Australia,10
2023,f,2023f,j,United Kingdom,Lithuania,8
2023,f,2023f,j,United Kingdom,Belgium,7
2023,f,2023f,j,United Kingdom,Estonia,6
2023,f,2023f,j,United Kingdom,Spain,5
2023,f,2023f,j,United Kingdom,Israel,4
2023,f,2023f,j,United Kingdom,Armenia,3
2023,f,2023f,j,United Kingdom,Italy,2
2023,f,2023f,j,United Kingdom,Slovenia,1"""

df75_24 = add_data_to_df(df75_24, data23)

df75_24.loc[df75_24["Year"] == 2023]

df75_24.drop(columns=["Unnamed: 0"], inplace=True)
df75_24 = pd.read_excel("Data Preparation/Datasets/eurovision_song_contest_1975_2024.xlsx")
df75_24.to_csv("Data Preparation/Datasets/eurovision_song_contest_1975_2024.csv", index=False)

