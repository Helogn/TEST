# this module use point cloud to show a lung!
# He Jiang
# 2021/10/23

import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np
dataset = sitk.ReadImage('D:/Test/biyesheji/biyesheji/mhd/landmark/VESSEL12_01.mhd')
data = sitk.GetArrayFromImage(dataset)
frame_num, width, height = data.shape
# TEST =data[data>0].index(data)
# TEST = data>0
# b = TEST.ravel()
A = np.array(np.where(data>0))

# X = A % (height * width)
# Y = A %(height * frame_num)
# Z = A % (width * frame_num)
# X1 = X[::10000]    # resample for array
# Y1 = Y[::10000]
# Z1 = Z[::10000]
M = 10000
X1 = A[0][::M]
Y1 = A[1][::M]
Z1 = A[2][::M]
# V = A[1]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# ss = 1:300
# print(Z[20000:20300])
# ax.scatter(Z[20000:21300], Y[20000:21300],X[20000:21300], zdir='z', s=20, c=None, depthshade=True)
ax.scatter(Z1, X1, Y1, zdir='z', s=20, c=None, depthshade=True)
plt.show( )


# TEST.index(0)
# TEST_list = TEST.tolist()
# TEST_list.index(0)
# print(data)




# ax.scatter(q, f, d, zdir='z', s=20, c=None, depthshade=True)
# plt.show( )