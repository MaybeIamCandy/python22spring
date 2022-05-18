from random import randint as rdt

li = []
n = 0

for i in range(10):
    li.append('')
    li[i] = rdt(0,9)
print('原始列表：{}'.format(li))

while n < len(li):
    if li[n] %2 == 1:
        li.remove(li[n])
    else:
        n += 1
print('最终结果：{}'.format(li))
