'''
Sy10-4 统计“I Have a Dream”一文中每一个单词出现的次数，输出词频最高的20个单词，并保存到DreamwordCount.txt文件中。
'''

f = open('Dream.txt', 'r')
li = f.read().lower().split()
#print(li)

new_dict = {}.fromkeys(li,0)

for i in li:
    new_dict[i] += 1
li_sorted = sorted(new_dict.items(),key=lambda k:k[1],reverse=True)

f = open('DreamwordCount.txt', 'w', encoding='utf-8')

for i in range(20):
    f.write('{:>10}: {:<4}\n'.format(li_sorted[i][0],li_sorted[i][1]))

f.close()
print('运行结束')
