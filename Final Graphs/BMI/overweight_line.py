import pandas as pd
import pygal

df = pd.read_csv("spo2.csv")

data = df.iloc[32]
data.to_csv("p33_bmi.csv", header = False, index = False)
df1 = pd.read_csv("p33_bmi.csv")
os1 = df1["33"]

data2 = df.iloc[33]
data2.to_csv("p34_bmi.csv", header = False, index = False)
df2 = pd.read_csv("p34_bmi.csv")
os2 = df2["34"]

data3 = df.iloc[1]
data3.to_csv("p2_bmi.csv", header = False, index = False)
df3 = pd.read_csv("p2_bmi.csv")
os3 = df3["2"]

data4 = df.iloc[29]
data4.to_csv("p30_bmi.csv", header = False, index = False)
df4 = pd.read_csv("p30_bmi.csv")
os4 = df4["30"]

data5 = df.iloc[5]
data5.to_csv("p6_bmi.csv", header = False, index = False)
df5 = pd.read_csv("p6_bmi.csv")
os5 = df5["6"]

data6 = df.iloc[9]
data6.to_csv("p10_bmi.csv", header = False, index = False)
df6 = pd.read_csv("p10_bmi.csv")
os6 = df6["10"]

data7 = df.iloc[21]
data7.to_csv("p22_bmi.csv", header = False, index = False)
df7 = pd.read_csv("p22_bmi.csv")
os7 = df7["22"]

data8 = df.iloc[13]
data8.to_csv("p14_bmi.csv", header = False, index = False)
df8 = pd.read_csv("p14_bmi.csv")
os8 = df8["14"]

line_chart = pygal.Line()
line_chart.title = 'Overweight Oxygen Saturation over 60mins'
line_chart.add('P33', os1)
line_chart.add('P34', os2)
line_chart.add('P2', os3)
line_chart.add('P30', os4)
line_chart.add('P6', os5)
line_chart.add('P10', os6)
line_chart.add('P22', os7)
line_chart.add('P14', os8)
line_chart.render_to_file('ow_oxsat_line.svg')
