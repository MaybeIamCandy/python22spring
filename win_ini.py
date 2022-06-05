'''
【程序功能】C:\Windows目录中有一个win.ini文本文件，存放了安装Windows系统的配置参数。
统计该文件中每一个单词出现的次数，把结果按词频降序排序并保存到windata.txt文件中。(18分)
'''

f = open(r'C:\Windows\win.ini', 'r')
li = f.read().lower().split()

new_dict = {}.fromkeys(li,0)

for i in li:
    new_dict[i] += 1
li_sorted = sorted(new_dict.items(),key=lambda k:k[1],reverse=True)

f = open('windata.txt', 'w')

for i in range(len(li_sorted)):
    f.write('{:>10}: {:<4}\n'.format(li_sorted[i][0],li_sorted[i][1]))
f.close()
print('运行结束')