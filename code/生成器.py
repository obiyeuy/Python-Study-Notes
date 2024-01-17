"""
通过列表生成式，我们可以直接创建一个列表 ： L = [ x2 for x in range(5)]
咱们运行这个列表，一般的电脑还是可以的，但是，如果我改成这样呢： L = [ x2 for x in range(5000000)]
相信这个大家运行时，就会很慢,CPU估计会疯狂的飙升，因为这个列表占用很大的内存
如果，我们的需求，仅仅是求前几个元素的结果呢！（这边只是举个列子，可能我们遇到的问题，不只只取前面几个元素的结果）
那空间不是白白浪费了。如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。这时就会用到生成器了。

生成器：这种一边循环一边计算的机制，称为生成器（generator）


得到方式：
1第一种方法很简单，只要把一个列表生成式的 [ ] 改成 ( )
有返回(type())可以看出，一个列表生成式的 [ ] 改成 ( )返回的就不再是一个列表了，而是一个生成器（generator）

生成器值的获取：
因为，生成器保存的是算法，可以每次调用 next()或generator.__next__() ，就计算出 下一个元素的值，直到计算到最后一个元素
没有更多的元素时，抛出 StopIteration 的异常

因为生成器也是可迭代对象。
所以，我们创建了一个生成器后，基本上永远不会调用 next() ，
而是通过 for 循环来迭代它，并且不需要关心 StopIteration 异常。

2如果推算的算法比较复杂，用类似列表生成式的 for 循环无法实现的时候，还可以用函数来实现。
 yeild的用法  只要出现yield，就是一个生成器

"""

# 1
l = ((x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 == 1)
print(type(l))
# for i in range(17):
#     print(next(l))      # next()与l.__next__()相同

while True:
    try:
        print(next(l))
    except:
        print('没有更多元素了')
        break

# 2
# 斐波那契数列
"""
步骤
1定义一个函数，函数中使用yield关键字
2调用函数，接受函数结果
3得到的结果就是生成器
4借助与next(),__next__()得到元素
"""


# def func():
#     n = 0
#     while True:
#         n +=1
#         # print(n)    # 把print(b)改为yield b就成为生成器了
#         yield n   # return n  + 暂停
#
# g = func()
# print(next(g))

def fib(length):
    a, b = 0, 1
    n = 0

    while n < length:
        yield b
        a, b = b, a + b
        n += 1
    return '没有更多元素'


# g = fib(5)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


"""
生成器方法：
   __next__()
   send(value) :向每次生成器调用中传值  注意：第一次调用send()必须为send(None)
"""


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp:', temp)
        i += 1
    return '没有更多元素'


g = gen()
print(g.send(None))
n1 = g.send('呵呵')
print('n1', n1)
n2 = g.send('哈哈')
print('n2', n2)











