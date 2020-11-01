from xlwt import *

w = Workbook()
ws = w.add_sheet('test')
ws.write(0,0,"data1")

row = 1
col = 1
ws.write(row, col,'data')

w.save('testExcel.xls')
