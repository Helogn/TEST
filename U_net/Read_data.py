import numpy as np  
import os
import SimpleITK as sitk
from resize import resize_image_itk


def read_img(path):
    img = sitk.ReadImage(path)
    data = sitk.GetArrayFromImage(img)
    return data



# 数据集路径
DATA_PATH = 'D:\\U_net\\'

# 数据加载
TRAIN_PATH = DATA_PATH + 'ct_scans\\'  # 训练集路径
TEST_PATH = DATA_PATH + 'lung_mask\\'  # 测试集路径
filenames = os.listdir(TRAIN_PATH)
img = sitk.ReadImage('D:\\U_net\\coronacases_org_001.nii')
for f in filenames :
    # image = read_img(TRAIN_PATH + f)
    image = sitk.ReadImage(TRAIN_PATH + f)
    print(sitk.GetArrayFromImage(image).shape)
    result = resize_image_itk(image,img,resamplemethod=sitk.sitkNearestNeighbor)
    data = sitk.GetArrayFromImage(result)
    print(data.shape)
    # fname = f.replace('.nii','.npy') #去掉nii的后缀名
    # print('finish resize')

    # np.save(file="D:\\U_net\\ct_data_second\\ct_mask\\" + fname , arr=data)    
    # print('finish this file -----' + fname  + '----------')

# 存储
# np.save(file="data.npy", arr=a)
# 
# 读取
# b= np.load(file="data.npy")


#'D:\\U_net\\ct_scans\\coronacases_org_002.nii'
#'D:\\U_net\\ct_scans\\coronacases_org_001.nii'








# seed = 10
# np.random.seed = seed


# # 样本图片大小
# IMG_WIDTH = 512
# IMG_HEIGHT = 512
# IMG_DEPTH = 200
# IMG_CHANNELS = 2



