'''
【程序功能】新建一Python程序，实现以下功能：
从键盘任意输入字符串m，对m加密，加密后为n。
加密方法：对于数字加1，如是3则处理为4，如是9处理为0，其他非数字字符保持不变。
【输入描述】包括1行，一个任意字符串，表示原密码
【输出描述】包括1行，处理后的字符串，表示加密后的密码
【输入样例】ks1690
【输出样例】ks2701
'''

li = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
newLi = []
source = input('请输入原密码：\n')

for i in source:
    if i in li:
        if not i == '9':
            newLi.append(int(i)+1)
        else:
            newLi.append(0)
    else:
        newLi.append(i)

print('转换后的密码：')
for j in newLi:
    print('{}'.format(j),sep='',end='')
