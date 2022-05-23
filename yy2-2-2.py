'''
【函数设计题】编写一个med(nums)的函数，nums为一个列表。
med(nums)的功能是求一组数的中位数。
中位数是指所有数（n个）按从小到大顺序排列后，处于中间位置的值。
如果n是奇数，则取最中间的一个数作为中位数；
如果n是偶数，则取最中间两个数的平均值作为中位数。
【函数定义要求】定义一个函数med(nums)，参数nums为一组实数，
函数返回这组数的中位数。
【输入描述】1行。一组实数，用空格分隔。
【输出描述】1行。一个数，中位数。
【输入样例】80 88 76 95 80 99
【输出样例】85.5
【函数调用】调用的程序代码与自定义函数写在一个程序里，
运行后，输入以空格分隔的一组数，输出中位数。
'''

def med(nums):
    nums.sort()
    length = len(nums)
    if (length %2) == 1:
        i = length // 2
        j = nums[i]
    else:
        j = (int(nums[length//2])+int(nums[length//2-1]))/2
    # print(nums)
    return j

nums = input('请输入用空格分隔的若干个数字：\n').split()
print(med(nums))
