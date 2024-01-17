# 内置函数range()
'''第一种创建方式'''
r = range(10)  # 默认从0开始，默认1为步长
print(r)  # range(0,10)
print(list(r))  # [0,1,2,...,9]

'''第二种方式，给两个参数'''
r = range(1, 10)
print(list(r))

'''第三种创建方式，给三个数'''
r = range(2, 10, 2)
print(list(r))

# 循环结构 while  for-in
# while
'''a=1
while a<10:
    print(a)
    a+=1'''

# 计算0-4的累加和
'''初始化变量为0'''
sum = 0
b = 0
while b < 5:
    sum += b
    b += 1
print('和为', sum)

# for-in循环
for a in range(10):
    print(a)

# 结束循环break
'''for item in range(3):
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')'''

'''a=0
while a<3:
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a+=1'''

# 流程控制语序continue(用于结束当前循环，进入下一次循环，通常与分支结构中的if一起使用)
for item in range(1, 51):
    if item % 5 == 0:
        print(item)

for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)

# 嵌套循环
for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='\t')
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, end='\t')
    print()

# 二重循环中的break和continue用于控制本层循环
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j, end='\t')
    print()
