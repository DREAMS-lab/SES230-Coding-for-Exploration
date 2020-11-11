import pandas as pd
import numpy as np

series_with_index = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(series_with_index)

dictionary = {'b': 1, 'a': 0, 'c': 2}
series_from_dict = pd.Series(dictionary)
print(series_from_dict)

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4],
                                                                             index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

d = {'one': pd.Series([1., 2., 3.], ), 'two': pd.Series([1, 2, 3, 4], index=[5, 6, 7, 1])}
df = pd.DataFrame(d)
print(df)
