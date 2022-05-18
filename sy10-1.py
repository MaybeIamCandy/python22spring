'''
Sy10-1 求出所有的水仙花数，保存到Arms.txt文件。
'''

def armstrong():
    addupsum = 0
    f = open('Arms.txt', 'w', encoding='utf-8')
    for i in range(100,1000):
        num = str(i)
        for j in range(len(num)):
            addupsum += int(num[j])**3
        if addupsum == int(num):
            addupsum = 0
            f.write('{}\n'.format(num))
        else:
            addupsum = 0
            
    f.close()

armstrong()
