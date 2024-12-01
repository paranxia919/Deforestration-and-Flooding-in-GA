import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import requests
import zipfile
import io
import geopandas as gpd
import matplotlib.colors as colors

#Process EPA data
epa_data = pd.read_csv("./EPA/EPA.csv")
ga_counties = gpd.read_file('Georgia_Counties.shp')
epa_data = epa_data.rename(columns={'CountyFIPS': 'GEOID10'})
epa_data['GEOID10'] = epa_data['GEOID10'].astype(str)
merged_data = pd.merge(epa_data, ga_counties, on='GEOID10')
merged_data1 = gpd.GeoDataFrame(merged_data)
merged_data1['Value'] = merged_data1['Value'].str.rstrip('%').astype(float)

#Process FEMA data
fema_data = pd.read_csv("./FEMA/FEMA.csv")
fema_data = fema_data.rename(columns={'CountyFIPS': 'GEOID10'})
fema_data['GEOID10'] = fema_data['GEOID10'].astype(str)
merged_data2 = pd.merge(fema_data, ga_counties, on='GEOID10')
merged_data2 = gpd.GeoDataFrame(merged_data2)
merged_data2['Value'] = merged_data2['Value'].str.rstrip('%').astype(float)

# # Define custom colors for each range (from light to dark)
# custom_colors = [
#     '#FFFFD4',  # Very light yellow
#     '#FED98E',  # Light yellow
#     '#FE9929',  # Orange
#     '#D95F0E',  # Dark orange
#     '#B22222',  # Firebrick red
#     '#993404',  # Burnt orange
#     '#8B0000'   # Dark red
# ]

# # Create custom colormap
# custom_cmap = colors.ListedColormap(custom_colors)

# # Define bins
# bins = [0, 10, 20, 30, 40, 50, 100]

# # Create the side by side map
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
# fig.suptitle('Comparison of EPA and FEMA Flood Hazard Areas in Georgia (2020)', 
#              fontsize=16, y=0.95)
# #plot EPA data
# merged_data1.plot(column='Value',
#                 ax=ax1,
#                 legend=True,
#                 legend_kwds={
#                     'title': 'Flood Hazard Area percentage'
#                 },
#                 cmap=custom_cmap,
#                 scheme='user_defined',
#                 classification_kwds={'bins': bins},
#                 edgecolor='black',
#                 linewidth=0.5)

# #plot FEMA data
# merged_data2.plot(column='Value',
#                 ax=ax2,
#                 legend=True,
#                 legend_kwds={
#                     'title': 'Flood Hazard Area percentage'
#                 },
#                 cmap=custom_cmap,
#                 scheme='user_defined',
#                 classification_kwds={'bins': bins},
#                 edgecolor='black',
#                 linewidth=0.5)

# # Add subtitles for each map
# ax1.set_title('EPA Flood Hazard Areas', pad=20, fontsize=14)
# ax2.set_title('FEMA Flood Hazard Areas', pad=20, fontsize=14)

# # Remove axes
# ax1.axis('off')
# ax2.axis('off')

# # Adjust font size of the legends
# plt.setp(ax1.get_legend().get_texts(), fontsize='10')
# plt.setp(ax2.get_legend().get_texts(), fontsize='10')

# # Adjust the spacing between subplots and margins
# plt.subplots_adjust(wspace=0.5, left=0.05, right=0.95)

# plt.show()

#Further analysis
#top 5 counties with the highest percentage of flood hazard area for EPA (Print only the county names and the percentage)
epa_data_sorted = merged_data1.sort_values(by='Value', ascending=False)
top_5_counties = epa_data_sorted.head(5)
print(top_5_counties[['County', 'Value']])

#top 5 counties with the highest percentage of flood hazard area for FEMA
fema_data_sorted = merged_data2.sort_values(by='Value', ascending=False)
top_5_counties_fema = fema_data_sorted.head(5)
print(top_5_counties_fema[['County', 'Value']])

