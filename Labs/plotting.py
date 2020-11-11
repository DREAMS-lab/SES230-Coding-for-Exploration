import matplotlib.pyplot as plt
#plt.plot([1,2,3,4,5],[10,20,12,34,1],'-o')
#fig = plt.figure()
#ax = plt.axes(projection='3d')
free_space_inGB_for_some_folks = [10, 20, 12, 34, 1, 2, 4, 29, 10, 12, 55, 100, 0.5, 0.1, 10, 23, 56, 23, 56]
plt.hist(free_space_inGB_for_some_folks, 4)
plt.show()