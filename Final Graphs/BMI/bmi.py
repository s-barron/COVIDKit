import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("participants.csv")
bmi = df.iloc[3]
bmi.to_csv("BMI.csv", header = False)
df2 = pd.read_csv("BMI.csv")
bmidata = df2["BMI"]
df3 = pd.read_csv("tp_participants.csv")

overweight = len([1 for i in bmidata if i > 25])
healthy = len([1 for i in bmidata if i < 25 and i > 18])
underweight = len([1 for i in bmidata if i < 18])

option = [(x / 10.0) for x in range(180, 251, 1)]

hw = df3.loc[df3['BMI'].isin(option)]
hw.to_csv("healthy.csv", header = True, index = False)
print(hw)

uw = df3.loc[df3['BMI'] < 18]
uw.to_csv("underweight.csv", header = True, index = False)

ow = df3.loc[df3['BMI'] > 25]
ow.to_csv("overweight.csv", header = True, index = False)

data = [overweight, healthy, underweight]
titles = ["Overweight: 8", "Healthy: 27 ", "Underweight: 1"]

colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
plt.pie(data, labels =titles, colors=colors,
autopct='%1.1f%%', startangle=90) 
plt.title("BMI")
plt.show()




