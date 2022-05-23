'''
【程序功能】新建一Python程序，实现以下功能：
输入5个成绩，按照优秀、良好、合格、不合格进行评级
260分（含）以上为优秀，240分（含）以上为良好
200分（含）以上为合格，200分以下为不合格
【输入描述】包含1行，5个整数，表示5个成绩
【输出描述】包含1行，1个字符串
输出对应的成绩等级（优秀，良好，合格，不合格）
【输入样例】288 250 150 220 240
【输出样例】优秀 良好 不合格 合格 良好
'''

print('输入5个成绩，用空格分隔：')
li = []
userInput = input().split()

for i in range(len(userInput)):
    if int(userInput[i]) >= 260:
        li.append('优秀')
    elif 240 <= int(userInput[i]) < 260:
        li.append('良好')
    elif 200 <= int(userInput[i]) < 240:
        li.append('合格')
    elif int(userInput[i]) < 200:
        li.append('不合格')

print('对应的成绩等级为：')
for j in range(len(li)):
    print('{}'.format(li[j]), end=' ')

