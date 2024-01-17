# s1 = 'hello'
# s2 = 'hello'
# s3 = 'hello1'
#
# print(id(s1))
# print(id(s2))
# print(id(s3))
# print(s1 is s2)  # is 是比较地址
# print(s2 is s3)
#
# print(s1[1])  # 正数，从0开始
# print(s1[-4])  # 倒数，从-1开始
#
# print(len(s1))

'''
索引机制
1.0~len(s)-1
2.-lem(s)~-1
'''

'''
切片：字符串，列表
格式：字符串变量[start:end]
 字符串变量[start:end:step]   注：step>0,从左往右取；step<0,从右往左取
'''

# s = 'ABCDEF'
# print(s[1:4])  # 包前不包后 BCD 按索引值
# print(s[0:5])
# print(s[:5])  # 一样，均为ABCDE
#
# print(s[-3:-1])  # DE 包前不包后 要按顺序写
# print(s[-3:])  # DE
#
# print(s[1:-1])  # 与s[1:5]一样
#
# print(s[:])
# print(s)  # s[:]与s 字符串与地址均一样
#
# print(id(s[:]))
# print(id(s))
# print(s[1::2])
#
# # 字符串变量[start:end:step]
# # 注：step > 0, 从左往右取；step < 0, 从右往左取
# s = 'ABCDEFG'
# print(s[::1])
# print(s[::-2])  # GECA
# print(s[0:6:-2])  # 取不到
# print(s[6:0:-2])  # GEC

# path = 'https://stackoverflow.com/users/signup?ssrc=product_home'
#
# # find,index,rfind,rindex,count
# # find:从左往右查找，遇到第一个相同的则返回第一个字母的位置，没找到则返回-1 （可以找多个字符）
# # rfind:right find; rindex:right index
# # count:找有几个相同的，返回个数
# # index:与find相同，但没找到会报错
#
# i = path.find('?')
# print(i)
# i = path.find('users')
# print(i)
#
# j = path.count('/')
# print(j)

'''
判断：startswith,endswith,isalpha,isdigit,isalnum,isspace,isupper,islower
返回值均为布尔类型
isalpha:是否为纯字母 isdigit:纯数字 isalnum:字母或数字 isspace:是否为空白字符串 isupper:大写字母 islower:小写字母
'''

# s = 'signup?ssrc=product_home'
# s1 = s.startswith('sign')
# print(s1)
#
# s2 = s.endswith('home')
# print(s2)
# print(s.isalpha())


s = '小李说：小红是**，小红她就是**'
s1 = s.replace('小红', '小明')  # 全替换
print(s1)
s2 = s.replace('小红', '小明', 1)  # 替换，指定次数
print(s2)

# spilt,rspilt,spiltlines,partition,rpartition
#  spilt('分隔符,maxspilt)   将结果存在列表中   可指定最多切割次数
# spiltlines:按行切割
a = '小红 小明 小李'
a1 = a.split('小红')
print(a1)



























