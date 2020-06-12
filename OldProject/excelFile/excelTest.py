import xlrd

date = xlrd.open_workbook("项目进度表.xlsx")
# print(date.sheet_names())     #获取Excel内表名
# print(type(date.nsheets))     #获取表单数量

dateOne = date.sheet_by_name("20200601-20200605")
# print(dateOne.name)   #表名
# print(dateOne.ncols)  #列数
print(dateOne.nrows)
# print(dateOne.number)     #表索引
print(dateOne.cell_value(rowx=0, colx=0))     #获取单个单元格内容
print(dateOne.cell(0, 0).ctype)
# print(dateOne.row_values(rowx=2))   #读取一行
# print(dateOne.col_values(colx=2, start_rowx=1))     #读取一列
# a = dateOne.col_values(colx=2, start_rowx=1)
# print(type(a))
# a = filter(None, a)
# print(list(a))
# a = "-".join(list(a))  #列表内字符串组合
# print(a)
# a = []
# for i in range(2, dateOne.nrows+1):
#     c = dict(dateOne.row_values(rowx=i))
#     print(c)