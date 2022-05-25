'''
【程序功能】编写程序，随机密码生成。
在字母和数字组成的列表中随机生成8个6位数密码。
'''

import random

li = []
pwd = []
c = 0

for i in range(48, 58):
    li.append(chr(i))
for i in range(65, 91):
    li.append(chr(i))
for i in range(97, 123):
    li.append(chr(i))

print('随机产生的8个6位数密码为：')
while c < 8:
    c += 1
    pwd = random.sample(li, 6)
    pwd.append('\n')
    for j in range(len(pwd)):
        print(pwd[j], sep='', end='')
