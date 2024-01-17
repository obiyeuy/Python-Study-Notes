#转义字符与原字符
print('hello\nworld')    #\n-->newline换行
print('hello\tworld')   #四个字母为一个制表位  \t可补足空缺或重开制表位
print('hello\rworld')   #\r-->return回车 world覆盖hello
print('hello\bworld')   #\b为退一个格

#反斜杠\\  单引号'  双引号"
print('http:\\\\www.baidu.com')   #第一个\为反斜线，第二个\为转义符号
print('老师说：\'大家好\'')   #\用于区分说话的引号与输出引号

#原字符（让转义字符不起作用）在字符串前加r或R
print(r'hello\nworld')
#注意事项：最后一个字符不能是\,但最后两个可以是\\
#print(r'hello\nworld\')
print(r'hello\nworld\\')


#print函数
#输出数字、字符串、含运算符的表达式
print('helloworld')
print(3+3*4)

#输出到文件中  注意点1指定的盘符存在  2使用file=fp
#fp=open('D:/text.txt','a+')  #a+如果文件不存在就创建，存在就在文件后追加
#print('helloworld',file=fp)
#fp.close()

#不进行换行（输出内容在一行中）
print('hello','world','Python')

#八位一字节 8bit=1byte  1024byte=1kb  1024kb=1mb  1024mb=1gb  1024gb=1tb
print(chr(0b100111001011000))  #100111001011000为乘的二进制编码 注意：前必须加0b
print(ord('乘'))   #此函数可找出符号的十进制表示

#变量  name=马里亚 标识、类型、值
name='马里亚'
print(name)
#print(‘标识’，id(name))    ？？？
#print('类型'，type(name))
#print('值'，name)

#变量的定义与使用  多次赋值后，会指向新的空间
#数据类型  整数类型-->int-->18   浮点数类型-->float-->3.1415  布尔类型-->bool(boolean)-->true false   字符串类型-->str

#整数：十进制（默认进制） 二进制加0b  八进制加0o  十六进制加0x
print('十进制',116)
print('二进制',0b10001110)
print('八进制',0o2354)
print('十六进制',0x75abe)

#浮点数：二进制存储可能不精确，导致误差
print(1.1+2.2)  #3.3000000000000003
print(1.1+2.1)  #3.2
#解决方法:导入模块 如下
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型（true-->1  false-->0）
f1=True
f2=False
print(f1+2+f2)  #布尔值可转成整数

#字符串类型：不可变的字符序列
#不同数据类型数据连接时，应数据类型相互转换
name='张三'
age=20
print(type(name),type(age))  #说明name与age数据类型不同
print('我叫'+name+'，今年'+str(age)+'岁')  #当将str类型与int类型连接时，报错，解决方案：类型转换

f1=10  #int
f2=98.8  #float
f3=False  #bool
#str()均可 f1 f2 f3
#int()可将str转为int，字符串为数字（整数）串   将float转为int，舍去小数部分  将bool转为1与0
#float()将bool转为1.0或0.0  将int转为10.0(如f1)  str中文字无法转，数字可以


