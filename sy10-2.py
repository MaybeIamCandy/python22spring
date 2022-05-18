'''
Sy10-2 把你最喜欢的一首唐诗宋词写到file1.txt文件中，
并统计file1.txt文件中包含的字符数和行数。
'''

li = []
ListLen = 0
encoding = 'utf-8'
fileName = 'file1.txt'
userInput = input('输入诗词，一次输入一行\n输入空行表示结束输入：')

while userInput != '':
    li.append('{}\n'.format(userInput))
    userInput = input('输入诗词，一次输入一行\n输入空行表示结束输入：')
    
print('输入结果：\n{}'.format(li))

#data = '春未老，风细柳斜斜。试上超然台上望，半壕春水一城花。烟雨暗千家。\n寒食后，酒醒却咨嗟。休对故人思故国，且将新火试新茶。诗酒趁年华。\n（苏轼《望江南·超然台作》）'
#data = '谁念西风独自凉？萧萧黄叶闭疏窗。沉思往事立残阳。\n被酒莫惊春睡重，赌书消得泼茶香。当时只道是寻常。\n（纳兰性德《浣溪沙·谁念西风独自凉》）'

f = open(fileName, 'w', encoding=encoding)
for i in range(len(li)):
    f = open(fileName, 'a', encoding=encoding)
    f.write(li[i])
    ListLen += len(li[i])
    if '\n' in li[i]:
        ListLen -= 1 #不计算加上的换行符\n

#f = open('file1.txt', 'r', encoding='utf-8')
f.close()

print('字符数：{}，行数：{}'.format(ListLen,len(li)))
