import xlrd   #可以在PyCharm下面的terminal里面pip list一下，查看是否已经安装xlrd包
data=xlrd.open_workbook('a.xlsx')  #'***'内部为excel路径，test是文件名称
table=data.sheet_by_index(0)  #参数0表示读取excel中的sheet1
nrows=table.nrows    #数行数
ncols=table.ncols    #数列数

print(nrows,ncols)#打印出sheet1中有数据的行数和列数

print(table.row_values(0))   #输出第一行
print(table.col_values(0))   #输出第一列
list=[]
for i in range(nrows):
    print(table.row_values(i))#输出每一行的值,里边的数都是浮点型的