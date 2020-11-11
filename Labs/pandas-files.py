import pandas as pd

hyg_data = pd.read_csv('hygdata_v3.csv')
# print(hyg_data.head())
absmag_ = hyg_data["absmag"]
print(absmag_.mean())
absmag_list = absmag_.to_list()
