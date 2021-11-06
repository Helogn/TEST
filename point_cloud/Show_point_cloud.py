# this module was aimed to describe the contribute of points in the future
#2021/10/23
#He Jiang

import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
q = np.arange(0,200)
a = np.ones([1,200])
b1 = np.random.standard_normal(200)
b2 = np.random.standard_normal(200)

d = a + b1
f = a + b2

# ax.scatter(q, f, d, zdir='z', s=20, c=None, depthshade=True)
# plt.show( )


#-------------------open 3d--------------------------
# pcd = o3d.geometry.PointCloud()
# pcd.points = o3d.utility.Vector3dVector(point_cloud[:,:3])
# pcd.colors = o3d.utility.Vector3dVector(point_cloud[:,3:6]/255)
# pcd.normals = o3d.utility.Vector3dVector(point_cloud[:,6:9])

# o3d.visualization.draw_geometries([pcd])