import pandas as pd
from io import StringIO

data2015 = """Year,Stage,Rank,Country,Score,Edition
2015,Semi 1,1,Russia,182,2015sf1
2015,Semi 1,2,Belgium,149,2015sf1
2015,Semi 1,3,Estonia,105,2015sf1
2015,Semi 1,4,Georgia,98,2015sf1
2015,Semi 1,5,Romania,89,2015sf1
2015,Semi 1,6,Greece,81,2015sf1
2015,Semi 1,7,Armenia,77,2015sf1
2015,Semi 1,8,Hungary,67,2015sf1
2015,Semi 1,9,Serbia,63,2015sf1
2015,Semi 1,10,Albania,62,2015sf1
2015,Semi 1,11,Moldova,41,2015sf1
2015,Semi 1,12,Belarus,39,2015sf1
2015,Semi 1,13,Denmark,33,2015sf1
2015,Semi 1,14,The Netherlands,33,2015sf1
2015,Semi 1,15,North Macedonia,28,2015sf1
2015,Semi 1,16,Finland,13,2015sf1
2015,Semi 2,1,Sweden,217,2015sf2
2015,Semi 2,2,Latvia,155,2015sf2
2015,Semi 2,3,Israel,151,2015sf2
2015,Semi 2,4,Norway,123,2015sf2
2015,Semi 2,5,Slovenia,92,2015sf2
2015,Semi 2,6,Cyprus,87,2015sf2
2015,Semi 2,7,Lithuania,67,2015sf2
2015,Semi 2,8,Poland,57,2015sf2
2015,Semi 2,9,Montenegro,57,2015sf2
2015,Semi 2,10,Azerbaijan,53,2015sf2
2015,Semi 2,11,Malta,43,2015sf2
2015,Semi 2,12,Ireland,35,2015sf2
2015,Semi 2,13,Czechia,33,2015sf2
2015,Semi 2,14,Portugal,19,2015sf2
2015,Semi 2,15,Iceland,14,2015sf2
2015,Semi 2,16,San Marino,11,2015sf2
2015,Semi 2,17,Switzerland,4,2015sf2
2015,Final,1,Sweden,365,2015final
2015,Final,2,Russia,303,2015final
2015,Final,3,Italy,292,2015final
2015,Final,4,Belgium,217,2015final
2015,Final,5,Australia,196,2015final
2015,Final,6,Latvia,186,2015final
2015,Final,7,Estonia,106,2015final
2015,Final,8,Norway,102,2015final
2015,Final,9,Israel,97,2015final
2015,Final,10,Serbia,53,2015final
2015,Final,11,Georgia,51,2015final
2015,Final,12,Azerbaijan,49,2015final
2015,Final,13,Montenegro,44,2015final
2015,Final,14,Slovenia,39,2015final
2015,Final,15,Romania,35,2015final
2015,Final,16,Armenia,34,2015final
2015,Final,17,Albania,34,2015final
2015,Final,18,Lithuania,30,2015final
2015,Final,19,Greece,23,2015final
2015,Final,20,Hungary,19,2015final
2015,Final,21,Spain,15,2015final
2015,Final,22,Cyprus,11,2015final
2015,Final,23,Poland,10,2015final
2015,Final,24,United Kingdom,5,2015final
2015,Final,25,France,4,2015final
2015,Final,26,Austria,0,2015final
2015,Final,26,Germany,0,2015final
"""
df2015 = pd.read_csv(StringIO(data2015))

data2016 = """Year,Stage,Rank,Country,Score,Edition
2016,Semi 1,1,Russia,342,2016sf1
2016,Semi 1,2,Armenia,243,2016sf1
2016,Semi 1,3,Malta,209,2016sf1
2016,Semi 1,4,Hungary,197,2016sf1
2016,Semi 1,5,The Netherlands,197,2016sf1
2016,Semi 1,6,Azerbaijan,185,2016sf1
2016,Semi 1,7,Austria,170,2016sf1
2016,Semi 1,8,Cyprus,164,2016sf1
2016,Semi 1,9,Czechia,161,2016sf1
2016,Semi 1,10,Croatia,133,2016sf1
2016,Semi 1,11,Bosnia and Herzegovina,104,2016sf1
2016,Semi 1,12,San Marino,68,2016sf1
2016,Semi 1,13,Montenegro,60,2016sf1
2016,Semi 1,14,Iceland,51,2016sf1
2016,Semi 1,15,Finland,51,2016sf1
2016,Semi 1,16,Greece,44,2016sf1
2016,Semi 1,17,Moldova,33,2016sf1
2016,Semi 1,18,Estonia,24,2016sf1
2016,Semi 2,1,Australia,330,2016sf2
2016,Semi 2,2,Ukraine,287,2016sf2
2016,Semi 2,3,Belgium,274,2016sf2
2016,Semi 2,4,Lithuania,222,2016sf2
2016,Semi 2,5,Bulgaria,220,2016sf2
2016,Semi 2,6,Poland,151,2016sf2
2016,Semi 2,7,Israel,147,2016sf2
2016,Semi 2,8,Latvia,132,2016sf2
2016,Semi 2,9,Georgia,123,2016sf2
2016,Semi 2,10,Serbia,105,2016sf2
2016,Semi 2,11,North Macedonia,88,2016sf2
2016,Semi 2,12,Belarus,84,2016sf2
2016,Semi 2,13,Norway,63,2016sf2
2016,Semi 2,14,Slovenia,57,2016sf2
2016,Semi 2,15,Ireland,46,2016sf2
2016,Semi 2,16,Albania,45,2016sf2
2016,Semi 2,17,Denmark,34,2016sf2
2016,Semi 2,18,Switzerland,28,2016sf2
2016,Final,1,Ukraine,534,2016final
2016,Final,2,Australia,511,2016final
2016,Final,3,Russia,491,2016final
2016,Final,4,Bulgaria,307,2016final
2016,Final,5,Sweden,261,2016final
2016,Final,6,France,257,2016final
2016,Final,7,Armenia,249,2016final
2016,Final,8,Poland,229,2016final
2016,Final,9,Lithuania,200,2016final
2016,Final,10,Belgium,181,2016final
2016,Final,11,The Netherlands,153,2016final
2016,Final,12,Malta,153,2016final
2016,Final,13,Austria,151,2016final
2016,Final,14,Israel,135,2016final
2016,Final,15,Latvia,132,2016final
2016,Final,16,Italy,124,2016final
2016,Final,17,Azerbaijan,117,2016final
2016,Final,18,Serbia,115,2016final
2016,Final,19,Hungary,108,2016final
2016,Final,20,Georgia,104,2016final
2016,Final,21,Cyprus,96,2016final
2016,Final,22,Spain,77,2016final
2016,Final,23,Croatia,73,2016final
2016,Final,24,United Kingdom,62,2016final
2016,Final,25,Czechia,41,2016final
2016,Final,26,Germany,11,2016final
"""
df2016 = pd.read_csv(StringIO(data2016))

data2017 = """Year,Stage,Rank,Country,Score,Edition
2017,Semi 1,1,Portugal,370,2017sf1
2017,Semi 1,2,Moldova,291,2017sf1
2017,Semi 1,3,Sweden,227,2017sf1
2017,Semi 1,4,Belgium,165,2017sf1
2017,Semi 1,5,Cyprus,164,2017sf1
2017,Semi 1,6,Australia,160,2017sf1
2017,Semi 1,7,Armenia,152,2017sf1
2017,Semi 1,8,Azerbaijan,150,2017sf1
2017,Semi 1,9,Poland,119,2017sf1
2017,Semi 1,10,Greece,115,2017sf1
2017,Semi 1,11,Georgia,99,2017sf1
2017,Semi 1,12,Finland,92,2017sf1
2017,Semi 1,13,Czechia,83,2017sf1
2017,Semi 1,14,Albania,76,2017sf1
2017,Semi 1,15,Iceland,60,2017sf1
2017,Semi 1,16,Montenegro,56,2017sf1
2017,Semi 1,17,Slovenia,36,2017sf1
2017,Semi 1,18,Latvia,21,2017sf1
2017,Semi 2,1,Bulgaria,403,2017sf2
2017,Semi 2,2,Hungary,231,2017sf2
2017,Semi 2,3,Israel,207,2017sf2
2017,Semi 2,4,The Netherlands,200,2017sf2
2017,Semi 2,5,Norway,189,2017sf2
2017,Semi 2,6,Romania,174,2017sf2
2017,Semi 2,7,Austria,147,2017sf2
2017,Semi 2,8,Latvia,132,2017sf2
2017,Semi 2,9,Belarus,110,2017sf2
2017,Semi 2,10,Denmark,101,2017sf2
2017,Semi 2,11,Serbia,98,2017sf2
2017,Semi 2,12,Switzerland,97,2017sf2
2017,Semi 2,13,North Macedonia,86,2017sf2
2017,Semi 2,14,Estonia,85,2017sf2
2017,Semi 2,15,Lithuania,69,2017sf2
2017,Semi 2,16,Malta,55,2017sf2
2017,Semi 2,17,Ireland,42,2017sf2
2017,Semi 2,18,San Marino,1,2017sf2
2017,Final,1,Portugal,758,2017final
2017,Final,2,Bulgaria,615,2017final
2017,Final,3,Moldova,374,2017final
2017,Final,4,Belgium,363,2017final
2017,Final,5,Sweden,344,2017final
2017,Final,6,Italy,334,2017final
2017,Final,7,Romania,282,2017final
2017,Final,8,Hungary,200,2017final
2017,Final,9,Australia,173,2017final
2017,Final,10,Norway,158,2017final
2017,Final,11,The Netherlands,150,2017final
2017,Final,12,France,135,2017final
2017,Final,13,Croatia,128,2017final
2017,Final,14,Azerbaijan,120,2017final
2017,Final,15,United Kingdom,111,2017final
2017,Final,16,Austria,93,2017final
2017,Final,17,Armenia,79,2017final
2017,Final,18,Denmark,77,2017final
2017,Final,19,Greece,77,2017final
2017,Final,20,Georgia,68,2017final
2017,Final,21,Cyprus,68,2017final
2017,Final,22,Poland,64,2017final
2017,Final,23,Israel,39,2017final
2017,Final,24,Ukraine,36,2017final
2017,Final,25,Germany,6,2017final
2017,Final,26,Spain,5,2017final
"""
df2017 = pd.read_csv(StringIO(data2017))

data2018 = """Year,Stage,Rank,Country,Score,Edition
2018,Semi 1,1,Israel,283,2018sf1
2018,Semi 1,2,Cyprus,262,2018sf1
2018,Semi 1,3,Czechia,232,2018sf1
2018,Semi 1,4,Austria,231,2018sf1
2018,Semi 1,5,Estonia,201,2018sf1
2018,Semi 1,6,Ireland,179,2018sf1
2018,Semi 1,7,Bulgaria,177,2018sf1
2018,Semi 1,8,Albania,162,2018sf1
2018,Semi 1,9,Lithuania,119,2018sf1
2018,Semi 1,10,Finland,108,2018sf1
2018,Semi 1,11,Azerbaijan,94,2018sf1
2018,Semi 1,12,Belgium,91,2018sf1
2018,Semi 1,13,Switzerland,86,2018sf1
2018,Semi 1,14,Greece,81,2018sf1
2018,Semi 1,15,Armenia,79,2018sf1
2018,Semi 1,16,Belarus,65,2018sf1
2018,Semi 1,17,Croatia,63,2018sf1
2018,Semi 1,18,North Macedonia,24,2018sf1
2018,Semi 1,19,Iceland,15,2018sf1
2018,Semi 2,1,Norway,266,2018sf2
2018,Semi 2,2,Sweden,254,2018sf2
2018,Semi 2,3,Moldova,235,2018sf2
2018,Semi 2,4,Australia,212,2018sf2
2018,Semi 2,5,Denmark,204,2018sf2
2018,Semi 2,6,Ukraine,179,2018sf2
2018,Semi 2,7,The Netherlands,174,2018sf2
2018,Semi 2,8,Slovenia,132,2018sf2
2018,Semi 2,9,Serbia,117,2018sf2
2018,Semi 2,10,Hungary,111,2018sf2
2018,Semi 2,11,Romania,107,2018sf2
2018,Semi 2,12,Latvia,106,2018sf2
2018,Semi 2,13,Malta,101,2018sf2
2018,Semi 2,14,Poland,81,2018sf2
2018,Semi 2,15,Russia,65,2018sf2
2018,Semi 2,16,Montenegro,40,2018sf2
2018,Semi 2,17,San Marino,28,2018sf2
2018,Semi 2,18,Georgia,24,2018sf2
2018,Final,1,Israel,529,2018final
2018,Final,2,Cyprus,436,2018final
2018,Final,3,Austria,342,2018final
2018,Final,4,Germany,340,2018final
2018,Final,5,Italy,308,2018final
2018,Final,6,Czechia,281,2018final
2018,Final,7,Sweden,274,2018final
2018,Final,8,Estonia,245,2018final
2018,Final,9,Denmark,226,2018final
2018,Final,10,Moldova,209,2018final
2018,Final,11,Albania,184,2018final
2018,Final,12,Lithuania,181,2018final
2018,Final,13,France,173,2018final
2018,Final,14,Bulgaria,166,2018final
2018,Final,15,Norway,144,2018final
2018,Final,16,Ireland,136,2018final
2018,Final,17,Ukraine,130,2018final
2018,Final,18,The Netherlands,121,2018final
2018,Final,19,Serbia,113,2018final
2018,Final,20,Australia,99,2018final
2018,Final,21,Hungary,93,2018final
2018,Final,22,Slovenia,64,2018final
2018,Final,23,Spain,61,2018final
2018,Final,24,United Kingdom,48,2018final
2018,Final,25,Finland,46,2018final
2018,Final,26,Portugal,39,2018final
"""
df2018 = pd.read_csv(StringIO(data2018))

data2019 = """Year,Stage,Rank,Country,Score,Edition
2019,Semi 1,1,Australia,261,2019sf1
2019,Semi 1,2,Czechia,242,2019sf1
2019,Semi 1,3,Iceland,221,2019sf1
2019,Semi 1,4,Estonia,198,2019sf1
2019,Semi 1,5,Greece,185,2019sf1
2019,Semi 1,6,Slovenia,167,2019sf1
2019,Semi 1,7,Serbia,156,2019sf1
2019,Semi 1,8,San Marino,150,2019sf1
2019,Semi 1,9,Cyprus,149,2019sf1
2019,Semi 1,10,Belarus,122,2019sf1
2019,Semi 1,11,Poland,120,2019sf1
2019,Semi 1,12,Hungary,97,2019sf1
2019,Semi 1,13,Belgium,70,2019sf1
2019,Semi 1,14,Georgia,62,2019sf1
2019,Semi 1,15,Portugal,51,2019sf1
2019,Semi 1,16,Montenegro,46,2019sf1
2019,Semi 1,17,Finland,23,2019sf1
2019,Semi 2,1,The Netherlands,280,2019sf2
2019,Semi 2,2,North Macedonia,239,2019sf2
2019,Semi 2,3,Sweden,238,2019sf2
2019,Semi 2,4,Switzerland,232,2019sf2
2019,Semi 2,5,Azerbaijan,224,2019sf2
2019,Semi 2,6,Russia,217,2019sf2
2019,Semi 2,7,Norway,210,2019sf2
2019,Semi 2,8,Malta,157,2019sf2
2019,Semi 2,9,Albania,96,2019sf2
2019,Semi 2,10,Denmark,94,2019sf2
2019,Semi 2,11,Lithuania,93,2019sf2
2019,Semi 2,12,Moldova,85,2019sf2
2019,Semi 2,13,Romania,71,2019sf2
2019,Semi 2,14,Croatia,64,2019sf2
2019,Semi 2,15,Latvia,50,2019sf2
2019,Semi 2,16,Armenia,49,2019sf2
2019,Semi 2,17,Austria,21,2019sf2
2019,Semi 2,18,Ireland,16,2019sf2
2019,Final,1,The Netherlands,498,2019final
2019,Final,2,Italy,472,2019final
2019,Final,3,Russia,370,2019final
2019,Final,4,Switzerland,364,2019final
2019,Final,5,Sweden,334,2019final
2019,Final,6,Norway,331,2019final
2019,Final,7,North Macedonia,305,2019final
2019,Final,8,Azerbaijan,302,2019final
2019,Final,9,Australia,284,2019final
2019,Final,10,Iceland,232,2019final
2019,Final,11,Czechia,157,2019final
2019,Final,12,Denmark,120,2019final
2019,Final,13,Cyprus,109,2019final
2019,Final,14,Malta,107,2019final
2019,Final,15,Slovenia,105,2019final
2019,Final,16,France,105,2019final
2019,Final,17,Albania,90,2019final
2019,Final,18,Serbia,89,2019final
2019,Final,19,San Marino,77,2019final
2019,Final,20,Estonia,76,2019final
2019,Final,21,Greece,74,2019final
2019,Final,22,Spain,54,2019final
2019,Final,23,Israel,35,2019final
2019,Final,24,Belarus,31,2019final
2019,Final,25,Germany,24,2019final
2019,Final,26,United Kingdom,11,2019final
"""
df2019 = pd.read_csv(StringIO(data2019))

data2021 = """Year,Stage,Rank,Country,Score,Edition
2021,Semi 1,1,Malta,325,2021sf1
2021,Semi 1,2,Ukraine,267,2021sf1
2021,Semi 1,3,Russia,225,2021sf1
2021,Semi 1,4,Lithuania,203,2021sf1
2021,Semi 1,5,Israel,192,2021sf1
2021,Semi 1,6,Cyprus,170,2021sf1
2021,Semi 1,7,Sweden,142,2021sf1
2021,Semi 1,8,Azerbaijan,138,2021sf1
2021,Semi 1,9,Belgium,117,2021sf1
2021,Semi 1,10,Norway,115,2021sf1
2021,Semi 1,11,Croatia,110,2021sf1
2021,Semi 1,12,Romania,85,2021sf1
2021,Semi 1,13,Slovenia,44,2021sf1
2021,Semi 1,14,Australia,28,2021sf1
2021,Semi 1,15,North Macedonia,23,2021sf1
2021,Semi 1,16,Ireland,20,2021sf1
2021,Semi 2,1,Switzerland,291,2021sf2
2021,Semi 2,2,Iceland,288,2021sf2
2021,Semi 2,3,Bulgaria,250,2021sf2
2021,Semi 2,4,Portugal,239,2021sf2
2021,Semi 2,5,Finland,234,2021sf2
2021,Semi 2,6,Greece,184,2021sf2
2021,Semi 2,7,Moldova,179,2021sf2
2021,Semi 2,8,San Marino,118,2021sf2
2021,Semi 2,9,Serbia,124,2021sf2
2021,Semi 2,10,Albania,112,2021sf2
2021,Semi 2,11,Denmark,89,2021sf2
2021,Semi 2,12,Austria,66,2021sf2
2021,Semi 2,13,Estonia,58,2021sf2
2021,Semi 2,14,Poland,35,2021sf2
2021,Semi 2,15,Czechia,23,2021sf2
2021,Semi 2,16,Georgia,16,2021sf2
2021,Semi 2,17,Latvia,14,2021sf2
2021,Final,1,Italy,524,2021final
2021,Final,2,France,499,2021final
2021,Final,3,Switzerland,432,2021final
2021,Final,4,Iceland,378,2021final
2021,Final,5,Ukraine,364,2021final
2021,Final,6,Finland,301,2021final
2021,Final,7,Malta,255,2021final
2021,Final,8,Lithuania,220,2021final
2021,Final,9,Russia,204,2021final
2021,Final,10,Greece,170,2021final
2021,Final,11,Bulgaria,170,2021final
2021,Final,12,Portugal,153,2021final
2021,Final,13,Moldova,115,2021final
2021,Final,14,Sweden,109,2021final
2021,Final,15,Serbia,102,2021final
2021,Final,16,Cyprus,94,2021final
2021,Final,17,Israel,93,2021final
2021,Final,18,Norway,75,2021final
2021,Final,19,Belgium,74,2021final
2021,Final,20,Azerbaijan,65,2021final
2021,Final,21,Albania,57,2021final
2021,Final,22,San Marino,50,2021final
2021,Final,23,The Netherlands,11,2021final
2021,Final,24,Spain,6,2021final
2021,Final,25,Germany,3,2021final
2021,Final,26,United Kingdom,0,2021final
"""
df2021 = pd.read_csv(StringIO(data2021))

data2022 = """Year,Stage,Rank,Country,Score,Edition
2022,Semi 1,1,Ukraine,337,2022sf1
2022,Semi 1,2,The Netherlands,221,2022sf1
2022,Semi 1,3,Greece,211,2022sf1
2022,Semi 1,4,Portugal,208,2022sf1
2022,Semi 1,5,Armenia,187,2022sf1
2022,Semi 1,6,Norway,177,2022sf1
2022,Semi 1,7,Lithuania,159,2022sf1
2022,Semi 1,8,Moldova,154,2022sf1
2022,Semi 1,9,Switzerland,118,2022sf1
2022,Semi 1,10,Iceland,103,2022sf1
2022,Semi 1,11,Croatia,75,2022sf1
2022,Semi 1,12,Albania,58,2022sf1
2022,Semi 1,13,Denmark,55,2022sf1
2022,Semi 1,14,Latvia,55,2022sf1
2022,Semi 1,15,Austria,42,2022sf1
2022,Semi 1,16,Bulgaria,29,2022sf1
2022,Semi 1,17,Slovenia,15,2022sf1
2022,Semi 2,1,Sweden,396,2022sf2
2022,Semi 2,2,Australia,243,2022sf2
2022,Semi 2,3,Serbia,237,2022sf2
2022,Semi 2,4,Czechia,227,2022sf2
2022,Semi 2,5,Estonia,209,2022sf2
2022,Semi 2,6,Poland,198,2022sf2
2022,Semi 2,7,Finland,162,2022sf2
2022,Semi 2,8,Belgium,151,2022sf2
2022,Semi 2,9,San Marino,118,2022sf2
2022,Semi 2,10,Azerbaijan,96,2022sf2
2022,Semi 2,11,North Macedonia,76,2022sf2
2022,Semi 2,12,Cyprus,63,2022sf2
2022,Semi 2,13,Israel,61,2022sf2
2022,Semi 2,14,San Marino,50,2022sf2
2022,Semi 2,15,Ireland,47,2022sf2
2022,Semi 2,16,Malta,47,2022sf2
2022,Semi 2,17,Montenegro,33,2022sf2
2022,Semi 2,18,Georgia,22,2022sf2
2022,Final,1,Ukraine,631,2022final
2022,Final,2,United Kingdom,466,2022final
2022,Final,3,Spain,459,2022final
2022,Final,4,Sweden,438,2022final
2022,Final,5,Serbia,312,2022final
2022,Final,6,Italy,268,2022final
2022,Final,7,Moldova,253,2022final
2022,Final,8,Greece,215,2022final
2022,Final,9,Portugal,207,2022final
2022,Final,10,Norway,182,2022final
2022,Final,11,The Netherlands,171,2022final
2022,Final,12,Poland,151,2022final
2022,Final,13,Estonia,141,2022final
2022,Final,14,Lithuania,128,2022final
2022,Final,15,Australia,125,2022final
2022,Final,16,Azerbaijan,106,2022final
2022,Final,17,Switzerland,78,2022final
2022,Final,18,Romania,65,2022final
2022,Final,19,Belgium,64,2022final
2022,Final,20,Armenia,61,2022final
2022,Final,21,Albania,57,2022final
2022,Final,22,Czechia,38,2022final
2022,Final,23,Iceland,20,2022final
2022,Final,24,France,17,2022final
2022,Final,25,Germany,6,2022final
2022,Final,26,Finland,38,2022final
"""
df2022 = pd.read_csv(StringIO(data2022))

data2023 = """Year,Stage,Rank,Country,Score,Edition
2023,Semi 1,1,Finland,177,2023sf1
2023,Semi 1,2,Sweden,135,2023sf1
2023,Semi 1,3,Israel,127,2023sf1
2023,Semi 1,4,Czechia,110,2023sf1
2023,Semi 1,5,Moldova,109,2023sf1
2023,Semi 1,6,Norway,102,2023sf1
2023,Semi 1,7,Switzerland,97,2023sf1
2023,Semi 1,8,Croatia,76,2023sf1
2023,Semi 1,9,Portugal,74,2023sf1
2023,Semi 1,10,Serbia,37,2023sf1
2023,Semi 1,11,Latvia,34,2023sf1
2023,Semi 1,12,Albania,10,2023sf1
2023,Semi 1,13,The Netherlands,7,2023sf1
2023,Semi 1,14,Azerbaijan,4,2023sf1
2023,Semi 1,15,Malta,3,2023sf1
2023,Semi 2,1,Australia,149,2023sf2
2023,Semi 2,2,Austria,137,2023sf2
2023,Semi 2,3,Poland,124,2023sf2
2023,Semi 2,4,Lithuania,110,2023sf2
2023,Semi 2,5,Slovenia,103,2023sf2
2023,Semi 2,6,Armenia,99,2023sf2
2023,Semi 2,7,Cyprus,94,2023sf2
2023,Semi 2,8,Belgium,90,2023sf2
2023,Semi 2,9,Estonia,74,2023sf2
2023,Semi 2,10,Albania,83,2023sf2
2023,Semi 2,11,Iceland,44,2023sf2
2023,Semi 2,12,Georgia,33,2023sf2
2023,Semi 2,13,Greece,14,2023sf2
2023,Semi 2,14,Denmark,6,2023sf2
2023,Semi 2,15,San Marino,0,2023sf2
2023,Semi 2,16,Romania,0,2023sf2
2023,Final,1,Sweden,583,2023final
2023,Final,2,Finland,526,2023final
2023,Final,3,Israel,362,2023final
2023,Final,4,Italy,350,2023final
2023,Final,5,Norway,268,2023final
2023,Final,6,Ukraine,243,2023final
2023,Final,7,Belgium,182,2023final
2023,Final,8,Estonia,168,2023final
2023,Final,9,Australia,151,2023final
2023,Final,10,Czechia,129,2023final
2023,Final,11,Lithuania,127,2023final
2023,Final,12,Cyprus,126,2023final
2023,Final,13,Croatia,123,2023final
2023,Final,14,Armenia,122,2023final
2023,Final,15,Austria,120,2023final
2023,Final,16,France,104,2023final
2023,Final,17,Spain,100,2023final
2023,Final,18,Moldova,96,2023final
2023,Final,19,Poland,93,2023final
2023,Final,20,Switzerland,92,2023final
2023,Final,21,Slovenia,78,2023final
2023,Final,22,Portugal,59,2023final
2023,Final,23,Albania,76,2023final
2023,Final,24,Serbia,30,2023final
2023,Final,25,United Kingdom,24,2023final
2023,Final,26,Germany,18,2023final
"""
df2023 = pd.read_csv(StringIO(data2023))

data2024 = """Year,Stage,Rank,Country,Score,Edition
2024,Semi 1,1,Croatia,177,2024sf1
2024,Semi 1,2,Ukraine,173,2024sf1
2024,Semi 1,3,Ireland,124,2024sf1
2024,Semi 1,4,Lithuania,119,2024sf1
2024,Semi 1,5,Luxembourg,117,2024sf1
2024,Semi 1,6,Cyprus,67,2024sf1
2024,Semi 1,7,Finland,59,2024sf1
2024,Semi 1,8,Portugal,58,2024sf1
2024,Semi 1,9,Slovenia,51,2024sf1
2024,Semi 1,10,Serbia,47,2024sf1
2024,Semi 1,11,Australia,41,2024sf1
2024,Semi 1,12,Poland,35,2024sf1
2024,Semi 1,13,Moldova,20,2024sf1
2024,Semi 1,14,Azerbaijan,11,2024sf1
2024,Semi 1,15,Iceland,3,2024sf1
2024,Semi 2,1,Israel,194,2024sf2
2024,Semi 2,2,The Netherlands,182,2024sf2
2024,Semi 2,3,Armenia,137,2024sf2
2024,Semi 2,4,Switzerland,132,2024sf2
2024,Semi 2,5,Greece,86,2024sf2
2024,Semi 2,6,Estonia,79,2024sf2
2024,Semi 2,7,Latvia,72,2024sf2
2024,Semi 2,8,Georgia,54,2024sf2
2024,Semi 2,9,Austria,46,2024sf2
2024,Semi 2,10,Norway,43,2024sf2
2024,Semi 2,11,Czechia,38,2024sf2
2024,Semi 2,12,Denmark,36,2024sf2
2024,Semi 2,13,Belgium,18,2024sf2
2024,Semi 2,14,San Marino,16,2024sf2
2024,Semi 2,15,Albania,14,2024sf2
2024,Semi 2,16,Malta,13,2024sf2
2024,Final,1,Switzerland,591,2024final
2024,Final,2,Croatia,547,2024final
2024,Final,3,Ukraine,453,2024final
2024,Final,4,France,445,2024final
2024,Final,5,Israel,375,2024final
2024,Final,6,Ireland,278,2024final
2024,Final,7,Italy,268,2024final
2024,Final,8,Armenia,183,2024final
2024,Final,9,Sweden,174,2024final
2024,Final,10,Portugal,152,2024final
2024,Final,11,Greece,126,2024final
2024,Final,12,Germany,117,2024final
2024,Final,13,Luxembourg,103,2024final
2024,Final,14,Lithuania,90,2024final
2024,Final,15,Cyprus,78,2024final
2024,Final,16,Latvia,64,2024final
2024,Final,17,Serbia,54,2024final
2024,Final,18,United Kingdom,46,2024final
2024,Final,19,Finland,38,2024final
2024,Final,20,Estonia,37,2024final
2024,Final,21,Georgia,34,2024final
2024,Final,22,Spain,30,2024final
2024,Final,23,Slovenia,27,2024final
2024,Final,24,Austria,24,2024final
2024,Final,25,Norway,16,2024final
"""
df2024 = pd.read_csv(StringIO(data2024))

data2025="""Year,Stage,Rank,Country,Score,Edition
2025,Semi 1,,Iceland,,2025sf1
2025,Semi 1,,Poland,,2025sf1
2025,Semi 1,,Slovenia,,2025sf1
2025,Semi 1,,Estonia,,2025sf1
2025,Semi 1,,Ukraine,,2025sf1
2025,Semi 1,,Sweden,,2025sf1
2025,Semi 1,,Portugal,,2025sf1
2025,Semi 1,,Norway,,2025sf1
2025,Semi 1,,Belgium,,2025sf1
2025,Semi 1,,Azerbaijan,,2025sf1
2025,Semi 1,,San Marino,,2025sf1
2025,Semi 1,,Albania,,2025sf1
2025,Semi 1,,The Netherlands,,2025sf1
2025,Semi 1,,Croatia,,2025sf1
2025,Semi 1,,Cyprus,,2025sf1

2025,Semi 2,,Australia,,2025sf2
2025,Semi 2,,Montenegro,,2025sf2
2025,Semi 2,,Ireland,,2025sf2
2025,Semi 2,,Latvia,,2025sf2
2025,Semi 2,,Armenia,,2025sf2
2025,Semi 2,,Austria,,2025sf2
2025,Semi 2,,Greece,,2025sf2
2025,Semi 2,,Lithuania,,2025sf2
2025,Semi 2,,Malta,,2025sf2
2025,Semi 2,,Georgia,,2025sf2
2025,Semi 2,,Denmark,,2025sf2
2025,Semi 2,,Czechia,,2025sf2
2025,Semi 2,,Luxembourg,,2025sf2
2025,Semi 2,,Israel,,2025sf2
2025,Semi 2,,Serbia,,2025sf2
2025,Semi 2,,Finland,,2025sf2

2025,Final,,Switzerland,,2025final
2025,Final,,Germany,,2025final
2025,Final,,United Kingdom,,2025final
2025,Final,,France,,2025final
2025,Final,,Spain,,2025final
2025,Final,,Italy,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
2025,Final,,,,2025final
"""
df2025 = pd.read_csv(StringIO(data2025))

dataframes = [df2015, df2016, df2017, df2018, df2019, df2021, df2022, df2023, df2024, df2025]


final_df = pd.concat(dataframes, ignore_index=True)

final_df.to_csv("Data Preparation/LastSets/Results.csv", index=False)