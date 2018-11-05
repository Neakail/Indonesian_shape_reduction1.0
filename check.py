# import glob
# import json
# filenames = glob.glob('/home/linnankai/PycharmProjects/ind_news/*/*')
# for i in filenames:
#     if 'model' not in i:
#         with open(i,'r+') as f:
#             datas = json.load(f)
#             for data in datas:
#                 if ' atakan ' in data['body']:
#                     print data
#                     raw_input()
a = '12345678'
print a[-2:]
print a[3:-2]