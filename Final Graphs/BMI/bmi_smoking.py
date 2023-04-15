import pandas as pd
import pygal

df = pd.read_csv("tp_participants.csv")

option = ['Smoker ']

ow = df.loc[(df['BMI'] > 25) & 
             df['Smoking Status'].isin(option)]
print(ow)
ow.to_csv("ow_smoker.csv", header = True, index = False)

df2 = pd.read_csv("spo2.csv")
data = df2.iloc[9]
data.to_csv("owsmoker_spo2.csv", header = False, index = False)
df3 = pd.read_csv("owsmoker_spo2.csv")
os = df3['10']
print(min(os))

line_chart = pygal.Line()
line_chart.title = 'Overweight Smoker Oxygen Saturation over 60mins'
line_chart.add('P10', os)
line_chart.render_to_file('owsmoker_line.svg')











