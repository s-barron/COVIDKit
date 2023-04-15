import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("participants.csv")
age = df.iloc[5]
age.to_csv("age.csv", header = False, index = False)
df2 = pd.read_csv("age.csv")
agedata = df2["Age"]

u_20 = len([1 for i in agedata if i < 20])
u_30 = len([1 for i in agedata if i < 30 and i >= 20])
u_40 = len([1 for i in agedata if i < 40 and i >= 30])
u_50 = len([1 for i in agedata if i < 50 and i >= 40])
u_60 = len([1 for i in agedata if i < 60 and i >= 50])
u_70 = len([1 for i in agedata if i < 70 and i >= 60])
u_80 = len([1 for i in agedata if i < 80 and i >= 70])

height = [u_20,u_30,u_40,u_50,u_60,u_70,u_80]
bars = ('<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79')

y_pos = np.arange(len(bars))
plt.ylim(0, 20)
plt.bar(y_pos, height,  color=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
plt.xticks(y_pos, bars)
plt.show()
                   