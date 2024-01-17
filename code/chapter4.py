# 程序的流程控制

# 程序的组织结构（顺序结构，选择结构，循环结构）
# 顺序结构

# python一切皆对象，所有对象都有一个布尔值
# 使用bool（）可获取对象布尔值
print(bool(False))  # False:False  数值0  None  空字符串  空列表  空元组  空字典  空集合   其他对象布尔值均为True

# 选择结构
# 单分支结构
'''money=1000 #余额
s=int(input('请输入取款金额:'))  #取款金额
#判断金额是否充足
if money>=s:
    money=money-s
    print('取款成功，余额为:',money)'''

# 双分支结构
'''num=int(input('请输入一个整数:'))
#条件判断
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')'''

# 多分支结构
'''score=int(input('请输入一个成绩:'))
if score>=90 and score<=100:  #或90<=score<=100
    print('A级')
elif score>=80 and score<90:
    print('B级')
elif score>=70 and score<80:
    print('C级')
elif score>=0 and score<70:
    print('D级')
else:
    print('对不起，成绩有误！')'''

# 嵌套if
'''answer=input('您是会员吗？y/n')
money=float(input('请输入您的购物金额:'))
if answer=='y':
    if money>=200:
        print('付款金额为:',money*0.8)
    elif money>=100:
        print('付款金额为:',money*0.9)
    else:
        print('付款金额为:',money)
else:
    print('非会员，金额为:',money)'''

# 条件表达式 if else简式
a = int(input('请输入一个整数:'))
b = int(input('请输入另一个整数:'))
print('使用条件表达式进入比较')
print((a, '大于等于', b) if a >= b else (a, '小于', b))

# pass语句：什么都不做，只是一个占位符，用到需要写语句的地方
