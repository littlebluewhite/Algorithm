# ex8_3.py

month = {'January':'一月',
         'February':'二月',
         'March':'三月',
         'April':'四月',
         'May':'五月',
         'June':'六月',
         'July':'七月',
         'August':'八月',
         'September':'九月',
         'October':'十月',
         'November':'十一月',
         'December':'十二月'
         }

n = input('請輸入月份 : ')
print('{} 的中文是 {}'.format(n, month[n.title()]))
