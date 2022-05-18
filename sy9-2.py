days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days4 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def whichday(n):
    month_addup = 0

    if int(userInput[0]) %4 == 0:
        daysDict = days4
    else:
        daysDict = days

    for i in range(int(userInput[1])-1):
        month_addup += daysDict[i]
    month_addup += int(userInput[2])
    print('{0}年{1}月{2}日是{0}年的第{3}天'.format(userInput[0],userInput[1],userInput[2],month_addup))

userInput = input('输入年月日，以空格分隔：').split(' ')
whichday(userInput)