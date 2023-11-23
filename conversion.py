# 不同数据的数据转换

# 定义列表存储每次计算值
a_list = []


# 十进制转不同进制进制
def B(number):
    if int(number) < JZ:
        a_list.insert(0, int(number))  # 如果数据小于1 则直接存储到列表第一位
        return 0  # 返回零结束此函数
    a_list.insert(0, int(number) % JZ)  # 列表a_list存储每次计算后的余数并将数据存放在第一位
    B(str(int(number) // JZ))  # 函数返回数据类型为 str 以便下次运算


# 将数据转换为十进制
def dec(number):
    k = 1
    New_number = 0
    for i in number:
        New_number = int(i) * JZ ** (len(number) - k) + New_number
        k += 1
    return New_number


# 判断数据类型,并将数据转化为十进制
def sj(number):
    global JZ
    if number[-1] == 'D' or number[-1] == 'd':
        print('此数为十进制数')
        JZ = 10
    elif number[-1] == 'B' or number[-1] == 'b':
        print('此数为二进制数')
        JZ = 2
    elif number[-1] == 'O' or number[-1] == 'o':
        print('此数为八进制数')
        JZ = 8
    elif number[-1] == 'H' or number[-1] == 'h':
        print('此数为十六进制数')
        JZ = 16
    else:
        print('输入不合法，程序结束')
        return False
    number = number[:-1]  # 去掉单位位
    # print(dec(number))
    return dec(number)


# 输出转化后的结果
def JG():
    for i in a_list:
        if i==a_list[-1]:
            print(' ',end='')
        print(i, end='')
    a_list.clear()  # 每次输出结束后清空列表
    print(end='\n')  # 每次输出结束后换行


# 将十进制转换为其他进制
def zhuanh():
    global JZ
    print('转为为二进制：', end=' ')
    JZ = 2
    B(number)
    a_list.append('B')
    JG()
    print('转为为八进制：', end=' ')
    JZ = 8
    B(number)
    a_list.append('O')
    JG()
    print('转化为十进制：', end=' ')
    JZ = 10
    B(number)
    a_list.append('D')
    JG()
    print('转化为十六进制：', end=' ')
    JZ = 16
    B(number)
    SL(number)
    a_list.append('H')
    JG()


# 对十六进制数最后一位数进行字母转换
def SL(number):
    if int(a_list[-1]) >= 10:
        if int(a_list[-1]) == 10:
            a_list[-1] = 'a'
        elif int(a_list[-1]) == 11:
            a_list[-1] = 'b'
        elif int(a_list[-1]) == 12:
            a_list[-1] = 'c'
        elif int(a_list[-1]) == 13:
            a_list[-1] = 'd'
        elif int(a_list[-1]) == 14:
            a_list[-1] = 'e'
        elif int(a_list[-1]) == 15:
            a_list[-1] = 'f'


# 函数主体

if __name__ == '__main__':
    print('B表示二进制，O表示八进制，D表示十进制,H表示16进制')
    # 用户输入内容
    number = input("请输入一个进制数(注意带单位)：")
    # 判断数据类型,并将内容转换为十进制
    number = sj(number)
    if number:
        zhuanh()
