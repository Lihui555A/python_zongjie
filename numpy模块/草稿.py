



# import numpy as np
# import cv2 as cv
#
# a=np.random.randint(1,100,48).reshape((3,4,4))
#
#
# print('-----------------')
# b=np.random.randint(1,100,60).reshape((3,4,5))
#
# print('--------------')
# list1=[]
# list2=[]
# list3=[]
# for i in a :
#     list1.append(i)
# for i in b:
#     list2.append(i)
# for i in range(len(list1)):
#     c=np.hstack((list1[i],list2[i]))
#     list3.append(c)
#     print(c)
# d=np.zeros((3,4,9))
# for i in range(len(list3)):
#     d[i,:,:]=list3[i]
#
#
#
# def com_cha(a,b):
#     a=np.array(a)
#     b=np.array(b)
#     list1 = []
#     list2 = []
#     list3 = []
#     for i in a:
#         list1.append(i)
#     for i in b:
#         list2.append(i)
#     for i in range(len(list1)):
#         c = np.hstack((list1[i], list2[i]))
#         list3.append(c)
#     d = np.zeros((3, 4, 9))
#     for i in range(len(list3)):
#         d[i, :, :] = list3[i]
#     return d
# e=np.arange(12).reshape((3,4))
# print(np.vsplit(e,3))