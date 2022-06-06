'''
 【程序功能】产生100个随机的两位整数，
 将其中的偶数写到文件odd.txt中，
 10个一行，并在最后输出偶数的个数。
【输出样例】odd.txt的文件内容：见图
'''

from random import randint as rdt

k = 0
li = []
for i in range(100):
    li.append(rdt(10,100))

for i in range(len(li)):
    if li[i] % 2 == 0:
        print(li[i], end=' ')
        k += 1
        if k % 10 == 0:
            print()
print('\n产生的100个随机数中偶数一共有：{}个'.format(k))
