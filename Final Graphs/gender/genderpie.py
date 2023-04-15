import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("participants.csv")
gender = df.iloc[1]
gender.to_csv("Gender.csv", header = False)

df2 = pd.read_csv("Gender.csv")
data = df2['Gender'].value_counts()
print(data)

titles = ["{0} ({1})".format(k, v) for k, v in data.items()]
colors = ["#1f77b4", "#ff7f0e"]
plt.pie(data, labels =titles, colors=colors,
autopct='%1.1f%%', startangle=90) 
plt.title("Gender of Participants")
plt.show()











