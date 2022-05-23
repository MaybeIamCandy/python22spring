'''
Sy10-3 scores.txt文件存放着某班学生的计算机课成绩，
包含学号、姓名、平时成绩、期末成绩四列(数据之间以Tab[\t]键分隔)。
请根据平时成绩占40%，期末成绩占60%的比例计算总评成绩，
并按学号、总评成绩两列写入另一个文件scored.txt中。
同时在屏幕上输出学生总人数，按总评成绩计算
90分(含)以上、75 (含) ~90分、9分、60 (含) ~75分、60分以下
各成绩区间的人数和班级总平均分(取小数点后两位)。
'''

c = 0
a,b,z,d = 0,0,0,0
class_total = 0

f = open('scores.txt', 'r', encoding='gb2312')
li = f.readlines()
li.remove(li[0])
f.close()

with open('scored.txt', 'w+', encoding='utf-8') as f:
    for i in li:
        c += 1
        splited = i.split('\t')
        #print(splited)
        total = int(splited[2])*0.4+int(splited[3])*0.6
        class_total += total
        #print(splited[0],total)
        f.write('{}\t{}\n'.format(splited[0],total))
        
        if total >= 90:
            a += 1
        elif 75 <= total < 90:
            b += 1
        elif 60 <= total < 75:
            z += 1
        elif total < 60:
            d += 1
    print('学生总人数{}人\n90分及以上{}人\n75-90分之间{}人\n60-75分之间{}人\n60分及以下{}人\n班级均分{:.2f}'.format(len(li),a,b,z,d,class_total/len(li)))
