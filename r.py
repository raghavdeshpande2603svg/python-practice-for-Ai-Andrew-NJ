import matplotlib.pyplot as plt
import numpy as np

X = np.array([1, 2, 6, 8])
Y = np.array([3, 8, 1, 10])
##for plotting the graph 
plt.pie(X, labels=['A', 'B', 'C', 'D'])
plt.show()
