# -*- coding:utf-8 -*-
import xlwt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

number = 0
f = open('result6.txt','r')
for i in f.readlines():
    # 存入xls
    if number < 60000:
        ws.write(number, 0, i.strip().split(' ')[0].decode('utf-8'))
        ws.write(number, 1, i.strip().split(' ')[1].decode('utf-8'))
        number += 1


wb.save('shape_reduction2.13_5.xls')