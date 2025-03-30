import pandas as pd
from io import StringIO
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
pd.set_option('display.max_columns', None)


#region Data Preparation
data2015 = """Country,Year,Stage,Edition,Odd
Sweden,2015,f,2015 Final,2.1
Russia,2015,f,2015 Final,4
Italy,2015,f,2015 Final,5.3
Belgium,2015,f,2015 Final,10.1
Australia,2015,f,2015 Final,10.9
Estonia,2015,f,2015 Final,22.8
Serbia,2015,f,2015 Final,33.3
Norway,2015,f,2015 Final,39.8
Latvia,2015,f,2015 Final,47.4
Israel,2015,f,2015 Final,55.7
Azerbaijan,2015,f,2015 Final,55.4
Spain,2015,f,2015 Final,61.1
Slovenia,2015,f,2015 Final,69.4
Georgia,2015,f,2015 Final,104.5
United Kingdom,2015,f,2015 Final,115.4
Greece,2015,f,2015 Final,118.1
Romania,2015,f,2015 Final,120.3
Armenia,2015,f,2015 Final,124.1
Albania,2015,f,2015 Final,144.4
Cyprus,2015,f,2015 Final,132.3
Hungary,2015,f,2015 Final,127.6
France,2015,f,2015 Final,129.4
Lithuania,2015,f,2015 Final,135.4
Poland,2015,f,2015 Final,160.5
Austria,2015,f,2015 Final,148.9
Montenegro,2015,f,2015 Final,148.9
Germany,2015,f,2015 Final,163.3
Russia,2015,Sf1,2015 Semi1,1.01
Estonia,2015,Sf1,2015 Semi1,1.03
Romania,2015,Sf1,2015 Semi1,1.13
Georgia,2015,Sf1,2015 Semi1,1.14
Greece,2015,Sf1,2015 Semi1,1.14
Armenia,2015,Sf1,2015 Semi1,1.28
Belgium,2015,Sf1,2015 Semi1,1.29
Albania,2015,Sf1,2015 Semi1,1.42
Belarus,2015,Sf1,2015 Semi1,1.6
Hungary,2015,Sf1,2015 Semi1,1.71
Finland,2015,Sf1,2015 Semi1,1.78
Denmark,2015,Sf1,2015 Semi1,1.87
Serbia,2015,Sf1,2015 Semi1,2.17
FYR Macedonia,2015,Sf1,2015 Semi1,2.45
Moldova,2015,Sf1,2015 Semi1,2.77
Netherlands,2015,Sf1,2015 Semi1,3.17
Sweden,2015,Sf2,2015 Semi2,1.01
Norway,2015,Sf2,2015 Semi2,1.06
Azerbaijan,2015,Sf2,2015 Semi2,1.09
Slovenia,2015,Sf2,2015 Semi2,1.09
Latvia,2015,Sf2,2015 Semi2,1.24
Israel,2015,Sf2,2015 Semi2,1.23
Cyprus,2015,Sf2,2015 Semi2,1.29
Lithuania,2015,Sf2,2015 Semi2,1.35
Iceland,2015,Sf2,2015 Semi2,1.45
Poland,2015,Sf2,2015 Semi2,1.52
Malta,2015,Sf2,2015 Semi2,1.93
Montenegro,2015,Sf2,2015 Semi2,1.93
Switzerland,2015,Sf2,2015 Semi2,2.36
Czechia,2015,Sf2,2015 Semi2,2.35
Ireland,2015,Sf2,2015 Semi2,2.57
Portugal,2015,Sf2,2015 Semi2,6.55
San Marino,2015,Sf2,2015 Semi2,7.36
"""
df2015 = pd.read_csv(StringIO(data2015))
data2016 = """Country,Year,Stage,Edition,Odd
Russia,2016,f,2016 Final,1.75
Australia,2016,f,2016 Final,3.97
Ukraine,2016,f,2016 Final,14.35
Sweden,2016,f,2016 Final,22.25
France,2016,f,2016 Final,26.70
Armenia,2016,f,2016 Final,43.05
Malta,2016,f,2016 Final,41.95
Bulgaria,2016,f,2016 Final,66.10
United Kingdom,2016,f,2016 Final,71.20
Spain,2016,f,2016 Final,62.15
The Netherlands,2016,f,2016 Final,83.30
Austria,2016,f,2016 Final,90.35
Latvia,2016,f,2016 Final,99.45
Belgium,2016,f,2016 Final,100.90
Italy,2016,f,2016 Final,108.30
Cyprus,2016,f,2016 Final,125.80
Israel,2016,f,2016 Final,133.15
Poland,2016,f,2016 Final,162.85
Lithuania,2016,f,2016 Final,180.55
Serbia,2016,f,2016 Final,210.65
Azerbaijan,2016,f,2016 Final,248.70
Hungary,2016,f,2016 Final,292.90
Croatia,2016,f,2016 Final,310.70
Georgia,2016,f,2016 Final,313.10
Czechia,2016,f,2016 Final,323.90
Germany,2016,f,2016 Final,311.35
Russia,2016,Sf1,2016 Semi1,1.00
Armenia,2016,Sf1,2016 Semi1,1.02
Malta,2016,Sf1,2016 Semi1,1.08
The Netherlands,2016,Sf1,2016 Semi1,1.12
Iceland,2016,Sf1,2016 Semi1,1.13
Cyprus,2016,Sf1,2016 Semi1,1.15
Hungary,2016,Sf1,2016 Semi1,1.20
Czechia,2016,Sf1,2016 Semi1,1.30
Azerbaijan,2016,Sf1,2016 Semi1,1.37
Croatia,2016,Sf1,2016 Semi1,1.49
Bosnia & Herzegovina,2016,Sf1,2016 Semi1,1.62
Austria,2016,Sf1,2016 Semi1,2.20
Estonia,2016,Sf1,2016 Semi1,2.62
Greece,2016,Sf1,2016 Semi1,3.68
Finland,2016,Sf1,2016 Semi1,9.30
Moldova,2016,Sf1,2016 Semi1,12.40
San Marino,2016,Sf1,2016 Semi1,13.80
Montenegro,2016,Sf1,2016 Semi1,16.60
Ukraine,2016,Sf2,2016 Semi2,1.01
Australia,2016,Sf2,2016 Semi2,1.02
Serbia,2016,Sf2,2016 Semi2,1.06
Latvia,2016,Sf2,2016 Semi2,1.12
Belgium,2016,Sf2,2016 Semi2,1.12
Bulgaria,2016,Sf2,2016 Semi2,1.13
Israel,2016,Sf2,2016 Semi2,1.17
Lithuania,2016,Sf2,2016 Semi2,1.29
Poland,2016,Sf2,2016 Semi2,1.49
Norway,2016,Sf2,2016 Semi2,1.84
Georgia,2016,Sf2,2016 Semi2,2.01
North Macedonia,2016,Sf2,2016 Semi2,2.80
Denmark,2016,Sf2,2016 Semi2,2.96
Belarus,2016,Sf2,2016 Semi2,2.99
Ireland,2016,Sf2,2016 Semi2,3.68
Slovenia,2016,Sf2,2016 Semi2,4.75
Albania,2016,Sf2,2016 Semi2,9.26
Switzerland,2016,Sf2,2016 Semi2,13.00
"""
df2016 = pd.read_csv(StringIO(data2016))
data2017 = """Country,Year,Stage,Edition,Odd
Bulgaria,2017,f,2017 Final,2.75
Portugal,2017,f,2017 Final,2.75
Italy,2017,f,2017 Final,7.5
Belgium,2017,f,2017 Final,7
Romania,2017,f,2017 Final,20
Sweden,2017,f,2017 Final,26
Croatia,2017,f,2017 Final,40
United Kingdom,2017,f,2017 Final,50
Moldova,2017,f,2017 Final,50
France,2017,f,2017 Final,50
Armenia,2017,f,2017 Final,50
Norway,2017,f,2017 Final,70
The Netherlands,2017,f,2017 Final,150
Australia,2017,f,2017 Final,100
Denmark,2017,f,2017 Final,100
Azerbaijan,2017,f,2017 Final,100
Hungary,2017,f,2017 Final,150
Germany,2017,f,2017 Final,400
Poland,2017,f,2017 Final,250
Greece,2017,f,2017 Final,300
Austria,2017,f,2017 Final,300
Belarus,2017,f,2017 Final,300
Cyprus,2017,f,2017 Final,300
Ukraine,2017,f,2017 Final,400
Israel,2017,f,2017 Final,500
Spain,2017,f,2017 Final,500
Sweden,2017,sf1,2017 Semi1,1.02
Armenia,2017,sf1,2017 Semi1,1.02
Portugal,2017,sf1,2017 Semi1,1.02
Azerbaijan,2017,sf1,2017 Semi1,1.15
Moldova,2017,sf1,2017 Semi1,1.2
Greece,2017,sf1,2017 Semi1,1.2
Belgium,2017,sf1,2017 Semi1,1.2
Finland,2017,sf1,2017 Semi1,1.28
Australia,2017,sf1,2017 Semi1,1.4
Cyprus,2017,sf1,2017 Semi1,1.45
Poland,2017,sf1,2017 Semi1,1.5
Latvia,2017,sf1,2017 Semi1,2.55
Georgia,2017,sf1,2017 Semi1,3.75
Slovenia,2017,sf1,2017 Semi1,4.1
Iceland,2017,sf1,2017 Semi1,4.5
Montenegro,2017,sf1,2017 Semi1,7
Albania,2017,sf1,2017 Semi1,8
Czechia,2017,sf1,2017 Semi1,11
Bulgaria,2017,sf2,2017 Semi2,1
Romania,2017,sf2,2017 Semi2,1.02
The Netherlands,2017,sf2,2017 Semi2,1.03
Israel,2017,sf2,2017 Semi2,1.1
Denmark,2017,sf2,2017 Semi2,1.14
Hungary,2017,sf2,2017 Semi2,1.12
Estonia,2017,sf2,2017 Semi2,1.3
Belarus,2017,sf2,2017 Semi2,1.3
Croatia,2017,sf2,2017 Semi2,1.4
Austria,2017,sf2,2017 Semi2,1.5
Norway,2017,sf2,2017 Semi2,2.25
Serbia,2017,sf2,2017 Semi2,2.75
Switzerland,2017,sf2,2017 Semi2,2.8
North Macedonia,2017,sf2,2017 Semi2,3.25
Malta,2017,sf2,2017 Semi2,4.5
Ireland,2017,sf2,2017 Semi2,6
Lithuania,2017,sf2,2017 Semi2,7
San Marino,2017,sf2,2017 Semi2,13
"""
df2017=pd.read_csv(StringIO(data2017))
data2018= """Country,Year,Stage,Edition,Odd
Cyprus,2018,f,2018 Final,2.2
Israel,2018,f,2018 Final,3.25
Germany,2018,f,2018 Final,7.5
Ireland,2018,f,2018 Final,15
Estonia,2018,f,2018 Final,26
Sweden,2018,f,2018 Final,35
Lithuania,2018,f,2018 Final,41
United Kingdom,2018,f,2018 Final,31
Norway,2018,f,2018 Final,41
France,2018,f,2018 Final,51
Italy,2018,f,2018 Final,51
Australia,2018,f,2018 Final,67
Finland,2018,f,2018 Final,67
Czechia,2018,f,2018 Final,67
Moldova,2018,f,2018 Final,67
Bulgaria,2018,f,2018 Final,86
Denmark,2018,f,2018 Final,101
Hungary,2018,f,2018 Final,101
The Netherlands,2018,f,2018 Final,126
Austria,2018,f,2018 Final,126
Ukraine,2018,f,2018 Final,201
Spain,2018,f,2018 Final,201
Portugal,2018,f,2018 Final,201
Albania,2018,f,2018 Final,201
Slovenia,2018,f,2018 Final,201
Serbia,2018,f,2018 Final,301
Cyprus,2018,sf1,2018 Semi1,1.01
Israel,2018,sf1,2018 Semi1,1.02
Estonia,2018,sf1,2018 Semi1,1.05
Czechia,2018,sf1,2018 Semi1,1.05
Bulgaria,2018,sf1,2018 Semi1,1.09
Lithuania,2018,sf1,2018 Semi1,1.15
Austria,2018,sf1,2018 Semi1,1.35
Greece,2018,sf1,2018 Semi1,1.6
Switzerland,2018,sf1,2018 Semi1,1.55
Armenia,2018,sf1,2018 Semi1,1.85
Finland,2018,sf1,2018 Semi1,1.85
Belgium,2018,sf1,2018 Semi1,2.5
Azerbaijan,2018,sf1,2018 Semi1,2.55
Belarus,2018,sf1,2018 Semi1,3
Albania,2018,sf1,2018 Semi1,3.75
Ireland,2018,sf1,2018 Semi1,3.5
Croatia,2018,sf1,2018 Semi1,5.5
North Macedonia,2018,sf1,2018 Semi1,11
Iceland,2018,sf1,2018 Semi1,13
Sweden,2018,sf2,2018 Semi2,1.01
Norway,2018,sf2,2018 Semi2,1.02
Ukraine,2018,sf2,2018 Semi2,1.05
Moldova,2018,sf2,2018 Semi2,1.08
Denmark,2018,sf2,2018 Semi2,1.09
Australia,2018,sf2,2018 Semi2,1.12
Hungary,2018,sf2,2018 Semi2,1.2
The Netherlands,2018,sf2,2018 Semi2,1.4
Poland,2018,sf2,2018 Semi2,1.57
Malta,2018,sf2,2018 Semi2,1.67
Romania,2018,sf2,2018 Semi2,2.25
Slovenia,2018,sf2,2018 Semi2,2.2
Russia,2018,sf2,2018 Semi2,2.75
Latvia,2018,sf2,2018 Semi2,3
Serbia,2018,sf2,2018 Semi2,4.5
Montenegro,2018,sf2,2018 Semi2,6
Georgia,2018,sf2,2018 Semi2,9
San Marino,2018,sf2,2018 Semi2,13
"""
df2018=pd.read_csv(StringIO(data2018))
data2019 = """Country,Year,Stage,Edition,Odd
The Netherlands,2019,f,2019 Final,1.55
Italy,2019,f,2019 Final,8.00
Switzerland,2019,f,2019 Final,10.39
Australia,2019,f,2019 Final,10.50
Sweden,2019,f,2019 Final,15.67
Norway,2019,f,2019 Final,25.33
Azerbaijan,2019,f,2019 Final,34.50
Russia,2019,f,2019 Final,38.78
Iceland,2019,f,2019 Final,47.33
France,2019,f,2019 Final,61.56
Denmark,2019,f,2019 Final,92.78
Cyprus,2019,f,2019 Final,101.11
Estonia,2019,f,2019 Final,152.00
Spain,2019,f,2019 Final,144.00
North Macedonia,2019,f,2019 Final,193.00
Czechia,2019,f,2019 Final,197.00
Malta,2019,f,2019 Final,222.72
Greece,2019,f,2019 Final,221.67
Serbia,2019,f,2019 Final,259.67
United Kingdom,2019,f,2019 Final,401.11
Slovenia,2019,f,2019 Final,303.33
Belarus,2019,f,2019 Final,314.78
Israel,2019,f,2019 Final,395.89
Albania,2019,f,2019 Final,449.56
Germany,2019,f,2019 Final,436.44
San Marino,2019,f,2019 Final,422.11
Australia,2019,Sf1,2019 Semi1,1.01
Greece,2019,Sf1,2019 Semi1,1.01
Cyprus,2019,Sf1,2019 Semi1,1.04
Iceland,2019,Sf1,2019 Semi1,1.06
Serbia,2019,Sf1,2019 Semi1,1.07
Czechia,2019,Sf1,2019 Semi1,1.07
Hungary,2019,Sf1,2019 Semi1,1.17
Slovenia,2019,Sf1,2019 Semi1,1.36
Estonia,2019,Sf1,2019 Semi1,1.54
Portugal,2019,Sf1,2019 Semi1,1.73
Belgium,2019,Sf1,2019 Semi1,2.10
Poland,2019,Sf1,2019 Semi1,2.26
Belarus,2019,Sf1,2019 Semi1,2.27
Georgia,2019,Sf1,2019 Semi1,3.75
San Marino,2019,Sf1,2019 Semi1,5.73
Finland,2019,Sf1,2019 Semi1,6.31
Montenegro,2019,Sf1,2019 Semi1,15.35
Sweden,2019,Sf2,2019 Semi2,1.01
The Netherlands,2019,Sf2,2019 Semi2,1.01
Russia,2019,Sf2,2019 Semi2,1.01
Azerbaijan,2019,Sf2,2019 Semi2,1.02
Switzerland,2019,Sf2,2019 Semi2,1.03
Malta,2019,Sf2,2019 Semi2,1.13
Norway,2019,Sf2,2019 Semi2,1.19
North Macedonia,2019,Sf2,2019 Semi2,1.33
Denmark,2019,Sf2,2019 Semi2,1.75
Armenia,2019,Sf2,2019 Semi2,1.89
Romania,2019,Sf2,2019 Semi2,1.93
Lithuania,2019,Sf2,2019 Semi2,2.76
Albania,2019,Sf2,2019 Semi2,2.61
Moldova,2019,Sf2,2019 Semi2,3.75
Austria,2019,Sf2,2019 Semi2,5.02
Croatia,2019,Sf2,2019 Semi2,5.88
Latvia,2019,Sf2,2019 Semi2,12.28
Ireland,2019,Sf2,2019 Semi2,14.00
"""
df2019=pd.read_csv(StringIO(data2019))
data2021 = """Country,Year,Stage,Edition,Odd
Italy,2021,f,2021 Final,3.24
France,2021,f,2021 Final,4.5
Malta,2021,f,2021 Final,5.0
Ukraine,2021,f,2021 Final,12.0
Finland,2021,f,2021 Final,10.0
Switzerland,2021,f,2021 Final,16.0
Iceland,2021,f,2021 Final,16.0
Lithuania,2021,f,2021 Final,50.0
Sweden,2021,f,2021 Final,25.0
San Marino,2021,f,2021 Final,50.0
Norway,2021,f,2021 Final,50.0
Portugal,2021,f,2021 Final,75.0
Bulgaria,2021,f,2021 Final,75.0
Cyprus,2021,f,2021 Final,75.0
Azerbaijan,2021,f,2021 Final,130.0
Greece,2021,f,2021 Final,75.0
Russia,2021,f,2021 Final,100.0
Serbia,2021,f,2021 Final,100.0
Israel,2021,f,2021 Final,100.0
The Netherlands,2021,f,2021 Final,250.0
Belgium,2021,f,2021 Final,100.0
United Kingdom,2021,f,2021 Final,100.0
Moldova,2021,f,2021 Final,100.0
Germany,2021,f,2021 Final,250.0
Spain,2021,f,2021 Final,250.0
Albania,2021,f,2021 Final,250.0
Malta,2021,SF1,2021 Semi1,1.01
Cyprus,2021,SF1,2021 Semi1,1.01
Ukraine,2021,SF1,2021 Semi1,1.02
Lithuania,2021,SF1,2021 Semi1,1.02
Russia,2021,SF1,2021 Semi1,1.07
Sweden,2021,SF1,2021 Semi1,1.11
Norway,2021,SF1,2021 Semi1,1.25
Croatia,2021,SF1,2021 Semi1,1.33
Azerbaijan,2021,SF1,2021 Semi1,1.3
Belgium,2021,SF1,2021 Semi1,1.91
Israel,2021,SF1,2021 Semi1,1.84
Romania,2021,SF1,2021 Semi1,2.54
Australia,2021,SF1,2021 Semi1,3.4
North Macedonia,2021,SF1,2021 Semi1,5.0
Ireland,2021,SF1,2021 Semi1,8.2
Slovenia,2021,SF1,2021 Semi1,3.5
Switzerland,2021,SF2,2021 Semi2,1.01
Iceland,2021,SF2,2021 Semi2,1.01
Bulgaria,2021,SF2,2021 Semi2,1.03
Finland,2021,SF2,2021 Semi2,1.03
Greece,2021,SF2,2021 Semi2,1.07
San Marino,2021,SF2,2021 Semi2,1.11
Portugal,2021,SF2,2021 Semi2,1.1
Serbia,2021,SF2,2021 Semi2,1.14
Albania,2021,SF2,2021 Semi2,1.02
Austria,2021,SF2,2021 Semi2,1.71
Denmark,2021,SF2,2021 Semi2,2.06
Moldova,2021,SF2,2021 Semi2,2.48
Estonia,2021,SF2,2021 Semi2,3.85
Latvia,2021,SF2,2021 Semi2,3.0
Czechia,2021,SF2,2021 Semi2,16.0
Poland,2021,SF2,2021 Semi2,14.0
Georgia,2021,SF2,2021 Semi2,14.0
"""
df2021=pd.read_csv(StringIO(data2021))
data2022 = """Country,Year,Stage,Edition,Odd
Ukraine,2022,f,2022 Final,1.34
Sweden,2022,f,2022 Final,5.5
Spain,2022,f,2022 Final,14.0
United Kingdom,2022,f,2022 Final,10.0
Italy,2022,f,2022 Final,23.0
Norway,2022,f,2022 Final,23.0
Poland,2022,f,2022 Final,81.0
Serbia,2022,f,2022 Final,51.0
Greece,2022,f,2022 Final,56.0
Moldova,2022,f,2022 Final,71.0
The Netherlands,2022,f,2022 Final,101.0
Finland,2022,f,2022 Final,176.0
Estonia,2022,f,2022 Final,201.0
Australia,2022,f,2022 Final,201.0
Czechia,2022,f,2022 Final,226.0
Portugal,2022,f,2022 Final,301.0
Armenia,2022,f,2022 Final,251.0
Germany,2022,f,2022 Final,201.0
France,2022,f,2022 Final,251.0
Azerbaijan,2022,f,2022 Final,251.0
Iceland,2022,f,2022 Final,251.0
Romania,2022,f,2022 Final,301.0
Switzerland,2022,f,2022 Final,226.0
Belgium,2022,f,2022 Final,201.0
Lithuania,2022,f,2022 Final,301.0
Ukraine,2022,SF1,2022 Semi1,1.01
Greece,2022,SF1,2022 Semi1,1.01
Norway,2022,SF1,2022 Semi1,1.01
The Netherlands,2022,SF1,2022 Semi1,1.01
Portugal,2022,SF1,2022 Semi1,1.02
Armenia,2022,SF1,2022 Semi1,1.06
Moldova,2022,SF1,2022 Semi1,1.07
Albania,2022,SF1,2022 Semi1,1.36
Austria,2022,SF1,2022 Semi1,1.68
Latvia,2022,SF1,2022 Semi1,1.87
Lithuania,2022,SF1,2022 Semi1,2.75
Iceland,2022,SF1,2022 Semi1,2.63
Switzerland,2022,SF1,2022 Semi1,2.88
Croatia,2022,SF1,2022 Semi1,3.45
Denmark,2022,SF1,2022 Semi1,3.25
Bulgaria,2022,SF1,2022 Semi1,7.0
Slovenia,2022,SF1,2022 Semi1,17.0
Sweden,2022,SF2,2022 Semi2,1.01
Poland,2022,SF2,2022 Semi2,1.01
Australia,2022,SF2,2022 Semi2,1.02
Czechia,2022,SF2,2022 Semi2,1.04
Estonia,2022,SF2,2022 Semi2,1.06
Serbia,2022,SF2,2022 Semi2,1.25
Finland,2022,SF2,2022 Semi2,1.28
Azerbaijan,2022,SF2,2022 Semi2,1.36
Belgium,2022,SF2,2022 Semi2,1.67
Malta,2022,SF2,2022 Semi2,1.61
San Marino,2022,SF2,2022 Semi2,1.62
Romania,2022,SF2,2022 Semi2,2.95
Ireland,2022,SF2,2022 Semi2,2.95
Israel,2022,SF2,2022 Semi2,3.1
Cyprus,2022,SF2,2022 Semi2,3.5
Montenegro,2022,SF2,2022 Semi2,6.5
North Macedonia,2022,SF2,2022 Semi2,7.0
Georgia,2022,SF2,2022 Semi2,11.0
"""
df2022 = pd.read_csv(StringIO(data2022))
data2023 = """Country,Year,Stage,Edition,Odd
Sweden,2023,f,2023 Final,1.64
Finland,2023,f,2023 Final,4.0
Israel,2023,f,2023 Final,8.0
Ukraine,2023,f,2023 Final,15.0
Italy,2023,f,2023 Final,27.0
Norway,2023,f,2023 Final,50.0
France,2023,f,2023 Final,95.0
Belgium,2023,f,2023 Final,160.0
United Kingdom,2023,f,2023 Final,160.0
Spain,2023,f,2023 Final,180.0
Poland,2023,f,2023 Final,150.0
Croatia,2023,f,2023 Final,180.0
Australia,2023,f,2023 Final,300.0
Austria,2023,f,2023 Final,300.0
Switzerland,2023,f,2023 Final,300.0
Armenia,2023,f,2023 Final,500.0
Cyprus,2023,f,2023 Final,230.0
Germany,2023,f,2023 Final,300.0
Czechia,2023,f,2023 Final,500.0
Estonia,2023,f,2023 Final,300.0
Moldova,2023,f,2023 Final,290.0
Lithuania,2023,f,2023 Final,500.0
Slovenia,2023,f,2023 Final,500.0
Portugal,2023,f,2023 Final,500.0
Serbia,2023,f,2023 Final,300.0
Albania,2023,f,2023 Final,500.0
Finland,2023,SF1,2023 Semi1,1.0
Sweden,2023,SF1,2023 Semi1,1.0
Israel,2023,SF1,2023 Semi1,1.0
Norway,2023,SF1,2023 Semi1,1.0
Czechia,2023,SF1,2023 Semi1,1.01
Moldova,2023,SF1,2023 Semi1,1.06
Portugal,2023,SF1,2023 Semi1,1.13
Switzerland,2023,SF1,2023 Semi1,1.3
Serbia,2023,SF1,2023 Semi1,1.4
Croatia,2023,SF1,2023 Semi1,1.4
Netherlands,2023,SF1,2023 Semi1,2.5
Malta,2023,SF1,2023 Semi1,2.4
Latvia,2023,SF1,2023 Semi1,4.0
Azerbaijan,2023,SF1,2023 Semi1,5.0
Ireland,2023,SF1,2023 Semi1,5.5
Austria,2023,SF2,2023 Semi2,1.01
Australia,2023,SF2,2023 Semi2,1.01
Armenia,2023,SF2,2023 Semi2,1.01
Cyprus,2023,SF2,2023 Semi2,1.02
Slovenia,2023,SF2,2023 Semi2,1.02
Belgium,2023,SF2,2023 Semi2,1.02
Poland,2023,SF2,2023 Semi2,1.03
Lithuania,2023,SF2,2023 Semi2,1.08
Georgia,2023,SF2,2023 Semi2,1.25
Estonia,2023,SF2,2023 Semi2,1.8
Albania,2023,SF2,2023 Semi2,1.8
Iceland,2023,SF2,2023 Semi2,2.95
Greece,2023,SF2,2023 Semi2,5.0
Denmark,2023,SF2,2023 Semi2,5.5
San Marino,2023,SF2,2023 Semi2,11.0
Romania,2023,SF2,2023 Semi2,11.0
"""
df2023 = pd.read_csv(StringIO(data2023))
data2024 = """Country,Year,Stage,Edition,Odd
Croatia,2024,f,2024 Final,1.57
Israel,2024,f,2024 Final,4.5
Switzerland,2024,f,2024 Final,4.5
France,2024,f,2024 Final,17.0
Ireland,2024,f,2024 Final,15.0
Ukraine,2024,f,2024 Final,34.0
Finland,2024,f,2024 Final,51.0
Italy,2024,f,2024 Final,41.0
Greece,2024,f,2024 Final,151.0
Austria,2024,f,2024 Final,151.0
Spain,2024,f,2024 Final,101.0
United Kingdom,2024,f,2024 Final,101.0
Sweden,2024,f,2024 Final,151.0
Lithuania,2024,f,2024 Final,201.0
Norway,2024,f,2024 Final,151.0
Armenia,2024,f,2024 Final,201.0
Georgia,2024,f,2024 Final,201.0
Cyprus,2024,f,2024 Final,251.0
Estonia,2024,f,2024 Final,201.0
Germany,2024,f,2024 Final,251.0
Portugal,2024,f,2024 Final,251.0
Latvia,2024,f,2024 Final,251.0
Slovenia,2024,f,2024 Final,251.0
Luxembourg,2024,f,2024 Final,251.0
Serbia,2024,f,2024 Final,251.0
Croatia,2024,SF1,2024 Semi1,1.0
Ukraine,2024,SF1,2024 Semi1,1.0
Lithuania,2024,SF1,2024 Semi1,1.02
Ireland,2024,SF1,2024 Semi1,1.02
Finland,2024,SF1,2024 Semi1,1.02
Luxembourg,2024,SF1,2024 Semi1,1.07
Cyprus,2024,SF1,2024 Semi1,1.07
Poland,2024,SF1,2024 Semi1,1.14
Portugal,2024,SF1,2024 Semi1,1.21
Australia,2024,SF1,2024 Semi1,2.2
Serbia,2024,SF1,2024 Semi1,2.18
Slovenia,2024,SF1,2024 Semi1,3.05
Moldova,2024,SF1,2024 Semi1,3.0
Azerbaijan,2024,SF1,2024 Semi1,6.4
Iceland,2024,SF1,2024 Semi1,2.5
Netherlands,2024,SF2,2024 Semi2,1.01
Switzerland,2024,SF2,2024 Semi2,1.01
Armenia,2024,SF2,2024 Semi2,1.03
Israel,2024,SF2,2024 Semi2,1.06
Greece,2024,SF2,2024 Semi2,1.06
Georgia,2024,SF2,2024 Semi2,1.08
Norway,2024,SF2,2024 Semi2,1.17
Estonia,2024,SF2,2024 Semi2,1.31
Austria,2024,SF2,2024 Semi2,1.38
Belgium,2024,SF2,2024 Semi2,1.43
Malta,2024,SF2,2024 Semi2,2.52
Denmark,2024,SF2,2024 Semi2,2.56
San Marino,2024,SF2,2024 Semi2,3.95
Czechia,2024,SF2,2024 Semi2,3.6
Albania,2024,SF2,2024 Semi2,4.3
Latvia,2024,SF2,2024 Semi2,5.1
"""
df2024 = pd.read_csv(StringIO(data2024))
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
df2025 = pd.read_csv(StringIO(data2025))

dataframes = [df2015, df2016, df2017, df2018, df2019, df2021, df2022, df2023, df2024, df2025]


final_df = pd.concat(dataframes, ignore_index=True)

final_df["Odd"] = final_df.groupby("Edition")["Odd"].transform(
    lambda x: scaler.fit_transform(x.values.reshape(-1, 1)).flatten()
)
final_df["Odd"]

final_df["Odd"] = 1 - final_df["Odd"]

final_df.to_csv("Data Preparation/LastSets/OddDatas.csv", index=False)
#endregion

