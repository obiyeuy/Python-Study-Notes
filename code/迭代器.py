# 可迭代对象：生成器  元组 列表 集合 字典  字符串
# 可迭代对象 (iterable) 是一种 能逐一返回其成员项 的对象，常包括：
# 所有内置序列对象 (字符串、列表、元组)
# 部分内置非序列对象 (字典、集合、文件对象等)
# 其他支持迭代协议的对象 (定义有 __iter__() 方法)
# 其他支持序列协议的对象 (定义有 __getitem__() 方法)

from collections.abc import Iterable  # 3.7以前的版本是collection，无.abc

# 判断一个对象是可迭代的
list1 = [1, 3, 43, 34, 3, 23, 34, 342]
f = isinstance(list1, Iterable)
print(f)

f = isinstance('acsd', Iterable)
print(f)

l = ((x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 == 1)
f = isinstance(l, Iterable)
print(f)


"""
可以被next()函数调用并不断返回下一个值的对象被称为迭代器：Iterator  （生成器是迭代器的一种）
迭代器特点：迭代器只能往前不能后退

可迭代的 是不是肯定就是 迭代器
list是可迭代的，但不是迭代器

list--->iter(list)--->迭代器next()   #iter()可以将一些变为迭代器
"""

list1 = [1,2,3,4,5]
list1 = iter(list1)   # 将可迭代的而不是迭代器的对象变为迭代器
f = isinstance(list1, Iterable)
print(f)

















