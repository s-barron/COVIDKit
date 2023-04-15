import pandas as pd
import pygal 

df = pd.read_csv("tp_participants.csv")

option1 = ['Smoker ']
option2 = ['Ex-Smoker ']
option3 = ['Non-Smoker']
  
# selecting rows based on condition 
smoker = df.loc[df['Smoking Status'].isin(option1)]
smoker.to_csv("smoker.csv", index = False, header = True)

ex_smoker = df.loc[df['Smoking Status'].isin(option2)]
ex_smoker.to_csv("ex_smoker.csv", index = False, header = True)

non_smoker = df.loc[df['Smoking Status'].isin(option3)]
non_smoker.to_csv("non_smoker.csv", index = False, header = True)

df2 = pd.read_csv("spo2.csv")

data = df2.iloc[9]
data.to_csv("p10_oxsat.csv", index = False, header = False)
df3 = pd.read_csv("p10_oxsat.csv")
os = df3["10"]

data2 = df2.iloc[17]
data2.to_csv("p18_oxsat.csv", index = False, header = False)
df4 = pd.read_csv("p18_oxsat.csv")
os2 = df4["18"]

data3 = df2.iloc[28]
data3.to_csv("p29_oxsat.csv", index = False, header = False)
df5 = pd.read_csv("p29_oxsat.csv")
os3 = df5["29"]


line_chart = pygal.Line()
line_chart.title = 'Smoker Oxygen Saturation over 60mins'
line_chart.add('P10', os)
line_chart.add('P18', os2)
line_chart.add('P29', os3)

line_chart.render_to_file('smoker_line.svg')

es1 = df2.iloc[10]
es1.to_csv("p11_oxsat.csv", index = False, header = False)
df6 = pd.read_csv("p11_oxsat.csv")
os4 = df6["11"]

es2 = df2.iloc[13]
es2.to_csv("p14_oxsat.csv", index = False, header = False)
df7 = pd.read_csv("p14_oxsat.csv")
os5 = df7["14"]

es3 = df2.iloc[23]
es3.to_csv("p24_oxsat.csv", index = False, header = False)
df8 = pd.read_csv("p24_oxsat.csv")
os6 = df8["24"]

es4 = df2.iloc[24]
es4.to_csv("p25_oxsat.csv", index = False, header = False)
df9 = pd.read_csv("p25_oxsat.csv")
os7 = df9["25"]

es5 = df2.iloc[31]
es5.to_csv("p32_oxsat.csv", index = False, header = False)
df10 = pd.read_csv("p32_oxsat.csv")
os8 = df10["32"]

line_chart = pygal.Line()
line_chart.title = 'Ex-Smoker Oxygen Saturation over 60mins'
line_chart.add('P11', os4)
line_chart.add('P14', os5)
line_chart.add('P24', os6)
line_chart.add('P25', os7)
line_chart.add('P32', os8)

line_chart.render_to_file('exsmoker_line.svg')




