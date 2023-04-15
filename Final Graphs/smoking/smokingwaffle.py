import matplotlib.pyplot as plt
from pywaffle import Waffle
import pandas as pd

df = pd.read_csv("participants.csv")
smoking = df.iloc[2]
smoking.to_csv("smoking.csv", header = False)

df2 = pd.read_csv("Smoking.csv")
data = df2['Smoking Status'].value_counts()

fig = plt.figure(
    FigureClass=Waffle, 
    rows=4, 
    values=data, 
    colors=("#983D3D", "#232066", "#DCB732"),
    title={'label': 'Participant Smoking Status', 'loc': 'left'},
    labels=["{0} ({1})".format(k, v) for k, v in data.items()],
    #labels = ["Non-Smokers: 28", "Ex-Smokers: 5", "Smokers: 3"],
    legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
    icons='child', icon_size=30, #remove these 2 lines if you don't want icons
    icon_legend=True
)
fig.gca().set_facecolor('#EEEEEE')
fig.set_facecolor('#EEEEEE')
plt.show()


