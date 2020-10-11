import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, read_csv


df = read_csv("data.csv")

print(df.to_numpy()[:,2])

data = df.to_numpy()[:,2]

averages = [0 for i in range(24)]
amount = [0 for i in range(24)]

for i in range(24):
    for j in range(i, len(data), 24):
        averages[i] += data[j]
        amount[i] += 1


averages = np.array(averages) / np.array(amount)
averages = averages * 10**-6
averages = np.round(averages, 1)

labels = [str(i) for i in range(24)]

width = 0.35
x = np.arange(24)
fig, ax = plt.subplots()

rect = ax.bar(x, averages, width)

ax.set_ylabel('Mbps')
ax.set_xlabel('Time')
ax.set_title('Internet Speed by Time of day')
ax.set_xticks(x)
ax.set_xticklabels(labels)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rect)

plt.show()
