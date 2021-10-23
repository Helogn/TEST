# this module was aimed to describe the contribute of points in the future
#2021/10/23
#He Jiang

import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
q = np.arange(0,200)
a = np.ones([1,200])
b1 = np.random.standard_normal(200)
b2 = np.random.standard_normal(200)

d = a + b1
f = a + b2

ax.scatter(q, f, d, zdir='z', s=20, c=None, depthshade=True)
plt.show( )