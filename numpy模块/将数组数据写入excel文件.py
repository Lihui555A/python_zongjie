import xlwt
import numpy as np
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('test', cell_overwrite_ok=True)
#sheet.write(0, 0, 'x值')  # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
#sheet.write(0, 1, 'y')
a=np.random.randint(1,100,48).reshape(6,8)
b=a.flatten()
c=np.random.randint(1,100,48).reshape(6,8)
d=c.flatten()
v=0
for i in b :
    sheet.write(v,0,str(i))
    v+=1
v=0
for i in d :
    sheet.write(v,1,str(i))
    v+=1



book.save(r'b.xlsx')