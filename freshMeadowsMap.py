# Ahalya Sanjiv
# MHC 4
# Professor Katherine St. John
# HW#4.6

# Plotting a Map of Fresh Meadows with 311 Complaints
import folium
import pandas as pd
import numpy as np

freshMeadows = pd.read_csv('service_requests.csv', nrows=500, low_memory = False)
freshMeadows.dropna(how="all", inplace=True)

mapFM= folium.Map(location=[40.74, -73.787], tiles='Stamen Terrain',zoom_start=14)

for index,row in freshMeadows.iterrows():
	lat = row["Latitude"]
	lon = row["Longitude"]
	complaint = str(row["Complaint Type"])
	if (np.isnan(lat) == False):
		mapFM.simple_marker([lat, lon], popup = complaint)
	
mapFM.save(outfile='service_requests.html')