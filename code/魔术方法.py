# 魔术方法
# __init__():初始化魔术方法
# 触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）

# __new__():实例化的魔术方法
# 在实例化时触发

# __call__():允许一个类的实例像函数一样被调用：x(a, b) 调用 x.__call__(a, b)
# 触发时机：将对象当成函数使用时，会默认调用此函数中内容

# __del__():析构魔术方法
# 触发时机：当对象没有用时（没有任何变量引用）的时候被触发

# __str__():
# 触发时机:打印对象名时自动触发，调用__str__里的内容
# 注意：一定要添加return

"""
__del__:
  1 对象赋值
   p = Person()
   p1 = p
   说明：p和p1共同指向一个地址

  2 删除地址的引用
  del p1 删除p1对地址的引用

  3 查看对地址的引用次数
    import sys
    sys.getrefcount(p)   ref为引用   get ref count

  4 当一块空间没有了任何引用，默认执行__del__


"""

import sys


class Person:
    def __init__(self, name):
        print('----->init', self)  # <__main__.Person object at 0x000001442874FCA0>
        self.name = name

    def __new__(cls, *args, **kwargs):  # 向内存要空间----->地址
        print('----->new')
        position = object.__new__(cls)
        print(position)  # <__main__.Person object at 0x000001442874FCA0>
        return position  # 地址

    def __call__(self, *args, **kwargs):
        print('------->call')


p = Person('jack')
print(p)  # <__main__.Person object at 0x000001442874FCA0>
p()  # 会默认执行__call__()函数
p.__call__()  # 与上面一样


# __del__

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):  # 一般自己不写，会覆盖默认的垃圾回收机制，有可能内存释放不干净，主要了解知识
        print('------------del')


p = Person('rose')
p1 = p  # 将地址赋给p1和p2   想查看地址被引用的数量就要导入sys
p2 = p
print('p1', p1.name)
print('p2', p2.name)

p1.name = 'tom'  # 改动的是地址中的，因此p2与p访问时全都是修改后的
print(p.name)
print(p2.name)

print(sys.getrefcount(p))  # 4   # 调用此函数时会再引用一次此地址，因此要默认减一

del p1  # 删除一次便调用一次__del__()
print(sys.getrefcount(p))  # 3
print('删除p1后打印：', p.name)

del p2
print(sys.getrefcount(p))  # 2
print('删除p2后打印：', p.name)

# del p
# # print(sys.getrefcount(p))   # name 'p' is not defined
# # print('删除p后打印：', p.name)     # 当一块空间没有了任何引用，默认执行__del__
#                                    # 故先print('------------del')，再print(5)


print(5)


# 若地址还有引用，就会先执行所有代码，因为python自带垃圾回收机制，即释放内存
# 所以python解释器最后再回收所有在本次执行过程中使用到的空间，则p所在内存被释放，引用也被断开，此时是__del__的触发时机
# 即先print(5),再print('------------del')，且两次del 最后只打印一次------------del


# __str__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名:' + self.name + ',年龄:' + str(self.age)


p = Person('tom', 10)
print(p)

# 单纯打印对象名称，出来的是一个地址，地址对于开发者来说没有多大意义
# 如果想在打印对象名时能够给开发者更多一些信息量
