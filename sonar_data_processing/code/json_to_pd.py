""" Converts jspn to pandas data frame 
    Author: Andres Pulido
    Oct 2021
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


df = pd.read_json(
    '/home/andrespulido8/Documents/PhD_Stuff/sonar_data_processing/data_log/json/Sonar_2021-10-16_11.45.04.json', lines=True)

print(df.head(3))
print(df.columns.values)

# find a way to collapse nans
#  df_channels = pd.DataFrame(np.zeros(df.shape[0], 11), index=range(df.shape[0]))
#  for ii in range(11):
#      for jj in range(df.shape[0]):
#          if df["channel"].iloc[jj] == ii:
#              df_channels.iloc[jj, ii+1] = df['latitude'].iloc[jj]


df["latitude"].plot()
df.plot.scatter(x="latitude", y="longitude")
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(df["latitude"], df["longitude"], df["altitude"])
plt.show()

print("end")
