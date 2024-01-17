# 输入函数input
# present=input('大圣想要什么礼物？')
# print(present)

# 从键盘区录入两个整数，计算两个整数的和
# a=int(input('请输入一个整数:'))
# b=int(input('请输入另一个整数:'))   #为str类型，需要数据转换
# =int(a)
# b=int(b)
# print(a+b)

# 算术运算符  +加法  -减法   *乘法  /除法
print(11 // 5)  # //整除运算
print(11 % 4)  # %取模运算
print(3 ** 3)  # **幂运算

# 运算符的一些特殊使用规则
print(-9 // 4)  # -3，而不是-2.向下取整
print(9 % -4)  # -3
print(-9 % 4)  # 3   余数=被除数-除数*商  ！！！！！

# 赋值运算符（从右到左）
# 支持链式赋值
a = b = c = 20  # 即a=20 b=20 c=20
print(a, id(a))
print(b, id(b))
print(c, id(c))
# 支持参数赋值
a = 20
a += 30  # 即a=a+30
print(a)
a -= 5  # 即a=a-5
print(a)  # a*=?  a/=?  a//=?  a%=?一样
# 支持系列解包赋值
a, b, c = 1, 2, 3  # 即a=1,b=2,c=3
print(c, b, a)

# 交换两个变量的值
a, b = 10, 2
print('交换之前', a, b)
a, b = b, a
print('交换之后', a, b)

# 比较运算符
a, b = 10, 20
print('a>b吗？', a > b)  # ==为等于  ！=为不等于
print('a<=b吗？', a <= b)  # 运算结果为bool类型
# !!!!!!
# =为赋值运算符，==为比较运算符    一个变量由标识，类型，值组成   ==比较的是值  比较对象的标识使用 is
a, b = 10, 10
print(a == b)  # value相同
print(a is b)  # id标识相同

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)
print(list1 is list2)  # print(list1 is not list2)  标识不相同
print(id(list1), id(list2))

# 布尔运算  and有false即为false   or有true即为true  not即为相反
a, b = 1, 2
print(a != 1 and b == 2)  # false
print(not a == 2)  # true

# in与not in(也为布尔运算）
a = 'helloworld'
print('w' in a)
print('k' not in a)

# 位运算符（将数据转成二进制进行计算） &同为1时结果为1  |同为0时结果为0  <<（左移位运算符）高位溢出舍弃，低位补0  >>（右移位运算符）低位溢出舍弃，高位补0
print(4 & 7)
print(4 | 7)
print(1 << 2)

# 运算符优先级  !!!!!
# 1.**幂  2.* /  3.+ -（算术运算）  4。<<  >>  5 &  | （位运算）  7.< >...（比较运算）  8.and  or  not（布尔运算） 9.=赋值运算符
