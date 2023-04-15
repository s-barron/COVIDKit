import pandas as pd
import pygal

df = pd.read_csv("spo2.csv")

data = df.iloc[10]
data.to_csv("p11_bmi.csv", header = False, index = False)
df1 = pd.read_csv("p11_bmi.csv")
os = df1["11"]


line_chart = pygal.Line()
line_chart.title = 'Underweight Oxygen Saturation over 60mins'
line_chart.add('P11', os)
line_chart.render_to_file('uw_oxsat_line.svg')