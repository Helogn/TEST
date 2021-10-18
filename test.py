# 2021-10-8
# He Jiang
# a = 36
# b = str(a)
# print("MPHY0030 " + b + " people" )



# 2021-10-11
# Fighter = ["F22","F31","J20","T50"]
# Cay = {"001A":"CN","NIM":"USA","Enterprise":"USA"}
# Tanker = ("T34","99A","T14")
# print(Fighter[2])
# print(Tanker[1])
# print(Cay["001A"])


# def image(number,name = "He Jiang"):
#     output_number = number * number
#     name = "BBB"
#     return output_number, name

# b = 10
# a = image(b)
# print(type(a))
# print(a[1])

#keyword argument:an argument preceded by an identifier////different from positional
#
#keyword
#

# def function (name,*argument,**keyword,):
#     print("The tanker's name is "+ name)
#     for arg in argument:

#         print("this position will output argument: "+ arg)

#     print("\n")

#     for arg1 in keyword:
#         print("this position will output keyword "+ arg1)

# a = function("T34","RUSSIA","1941-6-22",tanker = "wow!")

#scope and Namespace： Namespaces are given directly


#---------------------namespace---------------------
#
# def name_scale():
#     g = 3
#     def hhh():
#         nonlocal g
#         g = 12
#         print(g)
#     global hh
#     hhh()

# name_scale()


#-------------------Class

# class Tanker:
#     def __init__(self = "sss"):
#         self.a = "T34"
#         self.b = "T90"

# a = Tanker()
# print(a.a)
# print(a)



#-------2021-10-18-----------

import numpy as np
import matplotlib.pyplot as plt
from math import sin

image = np.array([4,7,5,3,3])
# print(image)
# print(type(image))

# plt.plot([1,2,3],[2,5,7])
# plt.show()
# plt.plot(image,image*image)
# # plt.show()
# print(image*image)
# x = 4
# print(sin(x))

# list_a = list(image)
# print(type(image))
# a = np.ones([4,4,2])
# # print(type(a)
# print(a)
# print(len(a))
# sizz = np.shape(a)
# print(type(sizz))
# print("size = " + str(sizz))
# print(sizz)

ENG = ('s','w','rr')
print(ENG)
print(ENG[1])