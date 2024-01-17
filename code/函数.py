# isinstance(变量,类型)  #判断变量是不是这个类型

from functools import reduce

print('{}{}{}'.format('AA', 'BB', 'cc'))
print('{name}{sex}{age}'.format(name='张三', sex='男', age=19))
print("{2}, {0}".format(*"abc"))  # c, a
print("{0} {1} {0}".format("aa", "bb"))  # aa bb aa

result = "-".join(['aas', '12', 'A'])  # join为拼接，将列表按""内容拼接，返回为字符串类型
print(result)

# filter()函数用于过滤序列，过滤掉不符合条件的元素，返回符合条件的元素组成新列表。
# filter()语法如下：
# filter(function,iterable)
#
# function -- 判断函数。
# iterable -- 可迭代对象

# 序列中的每个元素作为参数传递给函数进行判断，
# 返回True或者False，最后将返回True的元素放到新列表中
#
# 和map一样，filter函数在Python3中返回一个惰性计算的filter对象或迭代器。我们不能通过index访问filter对象的元素，也不能使用len()得到它的长度

list1 = [('tom', 19), ('tony', 20), ('bob', 15), ('rose', 23), ('jack', 22)]
r = filter(lambda x: x[1] > 20, list1)  # 注:filter的匿名函数必须是bool类型，只有结果为True的才是符合过滤条件的
print(list(r))

s = map(lambda x: x[0].title(), list1)
print(list(s))

t = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 注：reduce不在内置库中，要先导入库   from functools import reduce
print(t)                                        # 函数必须是有两个参数

# 以上为高阶函数，因为以其他函数为参数

# zip()
a = ['a', 'b', 'c', 'd']
b = ['1', '2', '3', '4']
c = list(zip(a, b))
print(c)

# [('a', '1'), ('b', '2'), ('c', '3'), ('d', '4')]
# 很明显，对于我们的两个list，a和b，list(zip(a, b))生成了一个列表。
# 在这个列表中，每个元素是一个tuple；对于第i个元组，它其中的内容是(a[i-1], b[i-1])。
# 这样的操作，与压缩软件的“压缩”十分接近。如果我们继续在zip()中加入更多的参数，
# 比如zip(a, b, c, d)，那么在将它转换成list之后，结果当然就是[(a[0], b[0], c[0], d[0]), (a[1], b[1], c[1], d[1]), ..., (a[n-1], b[n-1], c[n-1], d[n-1])]。
