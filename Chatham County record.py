import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

chatham = pd.read_csv("Chatham County.csv")
print(chatham.head())
#show the name and data type of the columns
print(chatham.info())

chatham = chatham.drop('Unnamed: 40', axis=1)
years = [int(col.split('-')[0]) for col in chatham.columns[1:]]
print(years)

deciduous_row = chatham[chatham['Period'] == 'Deciduous Forest'].iloc[0, 1:].values
evergreen_row = chatham[chatham['Period'] == 'Evergreen Forest'].iloc[0, 1:].values
mixed_row = chatham[chatham['Period'] == 'Mixed Forest'].iloc[0, 1:].values

plt.plot(years, deciduous_row, label='Deciduous Forest', color='green', marker='o', markersize=4)
plt.plot(years, evergreen_row, label='Evergreen Forest', color='darkgreen', marker='o', markersize=4)
plt.plot(years, mixed_row, label='Mixed Forest', color='lightgreen', marker='o', markersize=4)

# Customize the plot
plt.title('Forest Cover Change in Chatham County (1985-2023)')
plt.xlabel('Years')
plt.ylabel('Area Percentage')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Set x-axis ticks to show every 5 years
plt.xticks(years[::5], rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()