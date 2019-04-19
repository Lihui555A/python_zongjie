import numpy as np
#这个数组是几唯其实就是你想拿数组中某个具体的元素是需要在这个数组外加几个【】

k=np.array((1,2,3,4))
print(type(k))
#结果  [1 2 3 4]

#其实就是个大的列表，其中的元素没有逗号间隔，然后如果是矩阵的话，那么其中的元素都是一个一个的小列表，只要涉及到行数超过1了，那么里边就有小【】了
#array=np.array([[1,2,3],
  #             [2,3,4]])


#print(array)
#结果：
'''[[1 2 3]
 [2 3 4]]'''
#print(array.ndim)#维度 结果：2
#print(array.shape)#几行几列  结果：(2, 3)
#print(array.size)#几个元素  结果：6


#a=np.array([1,2,3])
#print(a)#深生成的数组元素中没有逗号
#结果：[1 2 3]

#b=np.zeros((4,4))#s生成全部为零的4行4列的矩阵
#print(b)
#结果：
'''[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]'''

#c=np.ones((4,4))#生成全部为一的4行4列的矩阵，需要主要的是括号里一定要记得加上小括号
#print(c)
#结果：
'''[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]'''

#d=np.empty((4,4))
#print(d)
#结果：其实是一堆接近0的数
'''[[1.17023457e-311 1.17023457e-311 1.35637083e-202 1.17003390e-311]
 [1.17003390e-311 0.00000000e+000 0.00000000e+000 0.00000000e+000]
 [0.00000000e+000 0.00000000e+000 0.00000000e+000 0.00000000e+000]
 [0.00000000e+000 0.00000000e+000 0.00000000e+000 0.00000000e+000]]'''


#e=np.arange(10,20,2)#括号里第一个起始值，第二个结束值，第三个步长
#print(e)
#结果：[10 12 14 16 18]



f=np.arange(12).reshape((3,4))#这个玩意跟range挺像的，都是不包含最后一个数字，然后reshape是重新定义这个矩阵的长和宽
#print(f)
#结果：
'''[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]'''
#h=np.linspace(1,10,12).reshape((3,4))
#i=h-f #两个相同形状的矩阵相减
#print(i)
#结果：对应元素相减
'''[[ 1.          0.81818182  0.63636364  0.45454545]
 [ 0.27272727  0.09090909 -0.09090909 -0.27272727]
 [-0.45454545 -0.63636364 -0.81818182 -1.        ]]'''



#g=np.linspace(1,10,20)#生成等差数列，1是起始值，10是结束值，20表示生成20个等长的
#print(g)
#结果：
'''[ 1.          1.47368421  1.94736842  2.42105263  2.89473684  3.36842105
  3.84210526  4.31578947  4.78947368  5.26315789  5.73684211  6.21052632
  6.68421053  7.15789474  7.63157895  8.10526316  8.57894737  9.05263158
  9.52631579 10.        ]'''




#j=np.random.random((2,4))#生成0到1之间的两行四列的矩阵
#print(j)
#结果：
'''[[0.08007992 0.93672403 0.93441046 0.23695113]
 [0.3281258  0.15921329 0.83635536 0.98611021]]'''
#print(np.random.random(10))#这样的话生成的数组就是一维的
#因为这个random.random的取值范围已经确定了，所以只需要写个数就可以了
#l=np.logspace(0,100,10)#生成对数数组
#print(l)
#结果：
'''[1.00000000e+000 1.29154967e+011 1.66810054e+022 2.15443469e+033
 2.78255940e+044 3.59381366e+055 4.64158883e+066 5.99484250e+077
 7.74263683e+088 1.00000000e+100]'''


#m=np.zeros((3,1))
#print(m)
#结果：
'''[[0.]
 [0.]
 [0.]]'''

#n=np.zeros(10)#括号里不写规格，只写数字表示只有一行10个元素
#print(n)
#结果：[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]


#n=np.ones((1,3))
#print(n)
#结果：[[1. 1. 1.]]
#m=np.ones(3)#可与上面的有个比较，括号里不写规格的话，出来就是一维向量，如果写规格的话就是二维的
#print(m)
#结果：[1. 1. 1.]


#o=np.identity(5)#生成单位矩阵，括号里的是生成多大的
#print(o)
#结果：
'''[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]'''


#数组与数值的算术运算
#q=np.array((1,2,3,4,5))
#print(q*2)   #结果：[ 2  4  6  8 10]
#print(q/2)   #结果：[0.5 1.  1.5 2.  2.5]
#print(q//2)  #结果：[0 1 1 2 2]
#print(q**3)#数组中每个元素都成自己的三次方  #结果：[  1   8  27  64 125]


#数组与数组的算术运算
#r=np.array((1,2,3))
#m=np.arange(1,10,1).reshape((3,3))
#print(r*m)#注意这个乘法是从上到下着，对应元素的相乘，不是现实中矩阵的乘法
#结果：
'''[[ 1  4  9]
 [ 4 10 18]
 [ 7 16 27]]'''
#print(m*r)
#结果：
'''[[ 1  4  9]
 [ 4 10 18]
 [ 7 16 27]]'''
#print(m/r)#这个除法也是挨着从上到下一个一个的对应元素相除，当然如果两个矩阵形状相同那么就对应的元素相除就可以了
#结果;
'''[[1.  1.  1. ]
 [4.  2.5 2. ]
 [7.  4.  3. ]]'''
#print(r/m)
#结果;   #不论是大的除以小的还是小的除以大的，都是拿出被除数的每行去跟除数的每行进行相除
'''[[1.         1.         1.        ]
 [0.25       0.4        0.5       ]
 [0.14285714 0.25       0.33333333]]'''


#二维数组转至
# r=np.arange(9).reshape((3,3))
# print(r)
#print(r.T)
#print(r.transpose())#也是矩阵的转至
#二维 一行三列转至后变为二维 三行一列
#transpose()对于多维数组来说，是怎么操作的，拿一个三维数组a来说，我们如果想取其中的某一个确定的元素得这样a【2】【1】【3】，表示拿第二堆里的第二行的第三列那个数据假如说这数是9，我们把2,2,3，这三个数的索引表示为0,1,2，然后在a.transpose（）
#transpose后边的括号里如果啥也写的话，那么这个就9就到了a.transpose()这个新得到的数组的【3】【1】【2】这个位置上了，当然如果我们在transpose的括号里填了数字，比如果填了（1,2,0）这个表示把上边个索引为0，1,2，的对应的2,2,3改为2，3，2，就是把9放到a.transpose()的2,3,2那个位置上
#向量的内积
#s=np.arange(1,4,1)#如果是一维向量且形状相同，则对应元素相乘再相加
#t=np.arange(2,5,1)
#u=s.dot(t)#计算  向量内积
#print(u)#结果：20
#print(s*t) #结果：[ 2  6 12]
#v=np.dot(s,t) #另外一种表示方法：
#print(v)  结果 ：20
#print(np.dot(s.T,t))#注意这里一维向量转置后跟没转是一样的，所以乘起来的结果不变   结果：20
#w=np.arange(1,10,1).reshape((3,3))#这就有点扯了，前面是大矩阵，后边是一维向量，那么做乘法的时候就是拿大矩阵的每一行去跟一维向量去乘，在乘的过程中，对应元素相乘再相加，然后这算是结果的一个元素，具体有结果中有几个元素那得看大矩阵有几行
#print(w.dot(s))
#结果：[14 32 50]
#总结一下，其实w.dot(s) 就是拿w中的每个元素，就是一个向量，跟后边的向量做内积，然后根据w中几个向量得到几个内积值
#print(s.dot(w))#但是要是一维向量在前，大矩阵在后就不一样了，就得按照正常的矩阵的乘法去乘了
#结果：[30 36 42]




#这里必须总结一下，这个*号只适用与一个矩阵和一个向量，或者两个向量之间，并且的这个矩阵的列数和向量的列数要一样，两个向量的列数也要一样，这个要求是必须要做到的，
#如果这样即使他们换了位置也是可以运算的并且运算的结果不变
#而对于dot运算来说，如果是两个矩阵且左列等于右行，则按照正常的矩阵乘法进行运算，如果两个矩阵不是上述的形状则不能运算，如果是矩阵和向量的话得看向量在哪边，
#如果向量在右边则矩阵每行和向量对应元素相乘然后相加算一个元素，最后的元素的个数取决于原矩阵的行数，如果向量在左边，那就得按照正常的矩阵的乘法进行运



# #数组元素访问
# a=np.arange(9).reshape((3,3))
# print(a)
# print(a[1][2])
# print(a[1,2])#都是拿出二维数组中某个具体位置上的值,括号里逗号前是一个维度
# print(a[:][0])
# #b=np.arange(9)
#print(b[[1,2]])#这里需要注意的是在一维数组上一次性拿多个值的时候方框里放的是个列表，列表里的元素是下标,出来的数据带框
#print(len(b))
#print(a[2,:])#这个表示打印出数组矩阵第二行所有的数
#print(a[:，1])#打印出第一列的所有的数  这两个玩意都是针对矩阵来说的
#print(a[:,0])
# #print(a[:][0])注意这个和上一行是不一样的
# print(a[[1]])#但是括号中间加上了列表的话就是针对整个数组了，如果整个数组中是一个一维向量的话出来的就是你选择的多个元素，如果整个数组中是个矩阵，那么这个玩意可以拿出矩阵的多行
# #index=np.random.randint(0,10,5)
#print(index)#此时的index是个列表
#y=np.array(np.random.randint(1,100,10))
#print(a[index])#可以一次性根据下标拿取数组中的多个值，当然也可以只拿取一个值
#对数组进行函数运算
#print(np.sin(y))求数组的每个元素的正玄值
#print(np.sin(w))
#print(np.cos(y))#求数组的每个元素的余弦值
#print(np.cos(w))
#print(np.round(np.cos(w)))
#z=np.random.random(10)#生成0到1之间的10个随机数
#print(z)
#print(np.floor(z))#向下取整
#print(np.ceil(z))#向上取整

#对矩阵不同维度上的元素进行计算
#a=np.arange(0,10).reshape((2,5))#生成二维数组
#print(a)
#print(np.sum(a))#z对数组所有元素求和
#print(np.sum(a,axis=0))#对数组纵向求和，其实就是矩阵每列求和，自己可以这样理解，axis就是横轴的意思，它＝0表示矩阵的每行元素中间没有axis拦着了，就可以竖着相加了
#print(np.sum(a,axis=1))#对数组横向求和，就是矩阵的每行求和
#print(np.mean(a))#z对数组所有元素求平均数
#print(a.mean())#求数组中的平均数
#print(np.average(a))#都是求平均数
#print(np.median(a))#求数组的中位数
#print(np.cumsum(a))#得到的新数组的元素的个数个原数组的个数以一样的，只不过新的数组的里的元素的值都是原来元素的值的累加
#print(np.mean(a,axis=0))#对数组纵向求平均数，其实就是矩阵每列求平均数，自己可以这样理解，axis就是横轴的意思，它＝0表示矩阵的每行元素中间没有axis拦着了，就可以竖着相加了
#print(np.mean(a,axis=1))
#weight=[0.3,0.7]
#print(np.average(a,axis=0,weights=weight))#计算矩阵纵向加权之后的和
#print(np.max(a))#找数组中元素最大的那个
#print(np.max(a,axis=0))#找数组中纵向元素最大的那个
#另外一种创建数组的方法
#b=np.random.randint(0,10,size=(3,3))
#print(np.std(b))#求一个数组的标准差，
#先解释一下啥叫标准差，首先像标准差，方差等概念都是对数组来说的，具体来说就是，一堆数字中求他们的标准差，
#和方差，标准差的求法，就是先算这堆数字的平均数，然后让每个数字去减这个平均数，然后每个差值再平方，然后
#把这些平方后的数加起来然后求平均，得到一个数，然后这个数再开方
#print(np.std(a,axis=1))#求矩阵的每行的标准差
#print(np.sort(a,axis=0))#把矩阵中的每列里的元素按照升序的方法排序

#改变数组的大小，两种方法一种是reshape这个是返回一个新数组，还有一种方法是改变自身
c=np.arange(10)
c.shape=2,5
# print(c)
# #c.shape=5,-1#-`1表示自动计算
# print(c.shape)
# print(str(c[1]))
# print(len(str(c[1])))
# print(type(str(c[1])))
#切片操作
#print(c[::-1])#反向切片  就是把最上面那行放到最下面，把最下面那行放到最上面，原来倒数第二行放到整数第二行，其他的都是这样
#print(c[::2])#隔一行取一个元素
#print(c[:4])#取前四个元素

# d=np.aranss
#布尔运算
#f=np.random.random(10)
#print(f>0.5)#比较元素中是否每个元素的值都大于0.5，返回的是个列表里边都是ture和false[False  True  True False False  True False False False False]
#print(f[f>0.5])#获取f中大于0.5的元素#
#g=np.random.random(10)
#print(f>g)#比较两个数组的对应元素的大小
#print(f[f>g])#获取f中对应元素大于g的元素值
#print(f==g)
#print(f[f==g])

#广播
#一个列向量和一个行向量干的活
#h=np.arange(0,60,10).reshape(-1,1)
#i=np.arange(0,6)
#print(h+i)#每行每个元素与后者每列每个元素相加
#print(h*i)

#分段函数
#j=np.random.randint(0,10,10)
#print(np.where(j<5))返回的是j中小于5的索引
#print(j[np.where(j<5)])打印出j中小于5的值
#print(np.where(j<5,0,1))#看j中那些元素的值小于5.小于5的返回0，大于5的返回1
#结果： [0 0 0 0 1 1 0 0 1 0]
#print(np.clip(j,5,9))#这个是干啥的呢，是让数组中所有小于5的数变成5，所有大于9的数都变成9，处于5和9之间的数就保持不变
#结果：[6 9 6 5 7 6 5 5 5 5]
#print(np.piecewise(j,[j<4,j>7],[lambda j:j*2,lambda j:j*3]))#小于4的元素乘以2，大于7的元素乘以3，其他元素变成0
#结果：[ 4  2  0 24  4  0  0 27  4  2]
#计算数组中最小值的索引
#print(np.argmax(j))#结果; 7
#print(np.argmin(j))#计算数组中最大值的索引



#h=np.random.randint(1,29,12).reshape((3,4))
#for row in h:#用for循环去遍历数组中的行，然后如果想遍历列的话直接把原数组转至一下然后遍历就可以了
#    print(row)
#结果：
'''[15 15 12 21]
[ 4 12 11 12]
[26 11 27 27]'''
#print(h.flatten())#这个函数是把多维的数组转为一维数组
#结果：[15 15 12 21  4 12 11 12 26 11 27 27]
#for item in h.flat:#这个循环是把多维数组中的所有的元素都遍历出来
#    print(item)
#结果：
'''15
15
12
21
4
12
11
12
26
11
27
27'''
#数组的合并
# m=np.arange(5)
# n=np.arange(5)
# print(np.vstack((m,n)))#这个是把原来两个数组进行一个上下合并，括号里可以放多个数组
# print(np.hstack((m,n)))#这个是把原来的连个数组左右进行一个合并就是放到一行里
# print(n[:,np.newaxis])#可以把一维数组变成二维数组，相当于就是添加了一个维度
# print(np.concatenate((n,m,n,m),axis=0))#多个数组横向进行合并，




#数组的分割
#l=np.arange(12).reshape((3,4))
#print(np.split(l,2,axis=1))#对列进行二等分，这个split只能等分，什么意思，比如说按列分，即axis=1，你们矩阵的总列数必须是括号里第二个参数的整数倍，如果按行分，即axis=0那矩阵的总行数必须是括号里第二个参数的整数倍
#那如果想不等分的话要怎么办呢
#print(np.array_split(l,3,axis=1))#就是把列给分成了不等的三份
#print(np.vsplit(l,3))
#print(np.hsplit(l,4))#注意了昂，这里也是要等分的，具体的细节再看
#数组的改值和赋值
#p=np.arange(5)
#p[0]=9
#print(p)
#p[1:3]=[10,89]
#print(p)
#q=p
#r=q
#print(r)#赋值之后是不变得，但是如果不想一样怎么办呢
#s=p.copy()
#print(s)#现在s的值跟p是一样的，但是如果接下来再改变p的值。s是不会变得


#矩阵运算、
#alist=[3,5,7]
#a_mat=np.matrix(alist)  #生成矩阵
#b=np.array(alist).reshape(1,3)  #这样我也能生成矩阵
#print(a_mat.T)
#print(b.T)  #两个都能生成矩阵的转至

#ctuple=(1,2,3)
#c_mat=np.matrix(ctuple)
#print(a_mat*c_mat.T)  #  结果：[[34]]

#d_mat=np.matrix([[1,5,3],[2,9,6],[3,1,9]])#创建二维矩阵
#print(d_mat)
#print(d_mat.argmax(axis=0))#返回一个列表,列表里有三个元素，分别是三个列的最大值的下标
#agrmax(axis=0)这个玩意用到三维数组是这么回事
'''
[[[4 5 5]
  [9 6 3]
  [2 6 6]]

 [[5 6 8]
  [6 8 4]
  [7 9 7]]]
  拿第一堆的第一个4和第二堆的第一个5比大小，很显然5大，那么索引就是1，然后拿第一堆的5和第二堆的6比。很显然6大，所以索引是1
  其实就是对应的元素相比，然后索引就是看第几堆
'''
#print(d_mat.argsort(axis=0))#返回的是一个矩阵，矩阵中的元素是原矩阵中每列元素的下标按照原矩阵中每列的值升序的后样子
#print(d_mat.diagonal())#矩阵对角线元素
#d_mat.sort(axis=1)#把矩阵中的每行按升序排序
#print(d_mat)
#d_mat.sort(axis=0)#把矩阵中的每列按照升序排序
#print(d_mat)



#numpy.append(arr, values, axis=None):

#简答来说，就是arr和values会重新组合成一个新的数组，做为返回值。而axis是一个可选的值

#当axis无定义时，是横向加成，返回总是为一维数组！

# Examples
# --------
# >> > np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])



# import numpy as np
# aa= np.zeros((1,8))
# bb=np.ones((3,8))
# c = np.append(aa,bb,axis = 0)
# print(c)    #这个表示两个数组的，其中axis是有值的，那么在axis=0的时候两个数组的列数要相同然后摞在一起

# [[ 0.  0.  0.  0.  0.  0.  0.  0.]
#  [ 1.  1.  1.  1.  1.  1.  1.  1.]
#  [ 1.  1.  1.  1.  1.  1.  1.  1.]
#  [ 1.  1.  1.  1.  1.  1.  1.  1.]]


# import numpy as np
# aa= np.zeros((3,8))
# bb=np.ones((3,1))
# c = np.append(aa,bb,axis = 1)
# print(c)     #这个表示两个数组的，其中axis是有值的，那么在axis=1的时候两个数组的行数要相同然后排在一起，新的在后边


# [[ 0.  0.  0.  0.  0.  0.  0.  0.  1.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  1.]
#  [ 0.  0.  0.  0.  0.  0.  0.  0.  1.]]
# aa= np.array([0,0,0,0])    #这个玩意就有点扯了，如果是一维的向量这样往起摞的话是摞不起来的，只能横着放
# bb= np.array([1,1,1,1])
# c = np.append(aa,bb,axis = 0)
# print(aa)
# print(c)
#总结一下对于数组的切片取值操作
#对于一位一维的数组来说，
# a=np.array([1,2,3,4,5,6,7,8])
# print(a[[1,2,3]])  #方括号里带个列表，列表里放的是想要的元素的索引值，
# print(a[1:4]) #这个是想要的区间
# print(a[1:])#这个是想要的范围
# print(a[:5])#这个也是想要的范围
# #总结一下关系数组元素访问后的维度变化的要点拿以下例子来说吧
'''
a=[[[6 9 3]
  [6 2 7]
  [6 5 8]]

 [[5 1 8]
  [1 6 2]
  [8 4 1]]


'''
#print(a[1,2,1])#这个拿出来的是个具体的值，没有维度
#print(a[:,2,1])#直接上要点吧，别那么多废话了，只有逗号中间有具体的数字，不是：连接的那种，数组就会降维，有几个数字就会降低几个维度,
