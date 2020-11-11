# 1D array, if shape is (N,1) = vector
# #[1,
# 2,
# 3,
# 4]
# 2x2 matrix
# [[1, 2],
#  3, 4]
# 2x2 structure  = 2x2 matrix = 2D array
# 1 2
# 3 4

import numpy as np
import matplotlib.pyplot as plt
x_uniform_rand = np.random.random((100, 1))
plt.hist(x_uniform_rand, 5)
print(x_uniform_rand)
plt.show()
x_normal_rand = np.random.normal(0,1,1000) # bell curve
plt.hist(x_normal_rand, 100)
print(x_normal_rand)
plt.show()


