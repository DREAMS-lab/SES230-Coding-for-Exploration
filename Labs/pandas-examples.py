import pandas as pd
import matplotlib.pyplot as plt


list_of_data = [10, 20, 12, 34, 1, 2, 4, 29, 10, 12, 55, 0.01, 0.5, 0.1, 10, 23, 5, 23, 5]
pandas_series = pd.Series(list_of_data)
print(pandas_series.mean())
print(pandas_series.median())
print(pandas_series)
# plt.hist(list_of_data,5)
# plt.show()
#print(pandas_series.describe())




