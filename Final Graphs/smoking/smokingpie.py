import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("participants.csv")
smoking = df.iloc[2]
smoking.to_csv("smoking.csv", header = False)

df2 = pd.read_csv("Smoking.csv")
data = df2['Smoking Status'].value_counts()
print(data)

colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
#titles = ["Non-Smokers: 28", "Ex-Smokers: 5", "Smokers: 3"]
titles = ["{0} ({1})".format(k, v) for k, v in data.items()]
plt.pie(data, labels =titles, colors=colors,
autopct='%1.1f%%', startangle=90) 
plt.title("Smoking Status")
plt.show()



