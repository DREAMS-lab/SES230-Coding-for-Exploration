# processing star cluster CSV file
import pandas as pd
hyg_data = pd.read_csv('hygdata_v3.csv')
absmag_column_data = hyg_data["dist"]
print("Maximum value", absmag_column_data.max())
print("Mean value", absmag_column_data.mean())
print("Median value", absmag_column_data.median())



