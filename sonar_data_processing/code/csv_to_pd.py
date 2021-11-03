""" Converts csv file to pandas data frame
    Author: Andres Pulido
    Oct 2021
"""
import pandas
import matplotlib.pyplot as plt
import numpy as np

df = pandas.read_csv(
    '/home/andrespulido8/Documents/PhD_Stuff/APRILab/sonar_data_processing/data_log/sonar_csv/Sonar_2021-10-16_14.38.24.csv.tab',
    # usecols=['time(millisecond)', 'datetime(utc)', 'latitude', 'longitude', 'height_above_takeoff(feet)',
    #         'height_above_ground_at_drone_location(feet)', 'ground_elevation_at_drone_location(feet)',
    #         'altitude_above_seaLevel(feet)', 'height_sonar(feet)', 'speed(mph)', 'distance(feet)', ' xSpeed(mph)', ' ySpeed(mph)', ' zSpeed(mph)',
    #         ' compass_heading(degrees)', ' pitch(degrees)', ' roll(degrees)', 'altitude(feet)'], parse_dates=['datetime(utc)'])
)
# df.drop(columns=["isPhoto", "isVideo", "voltageCell1", "voltageCell2", "voltageCell3",
#        "voltageCell4", "voltageCell5", "voltageCell6", "current(A)", "battery_temperature(f)"])

print(df.head(3))

print(df.columns.values)

df.plot.scatter(x="time(millisecond)", y="altitude(feet)")
plt.show()

df['size'] = np.repeat(5, df.shape[0])
df['size'].iloc[0] = 10

df.plot.scatter(x=df["latitude"], y=df["longitude"])
#ax.add_patch(plt.Circle((df["latitude"][0], df["longitude"][0]), 5, color='r'))
plt.show()

print("end")
