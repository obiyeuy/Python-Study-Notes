'''
a = 1324  # 全局变量


def max():
    global a  # 加global后，a-=10中a才会与全局变量联系，才能使用
    a -= 10  # 只有不可变的类型才需要添加global  可变的类型不需要添加global
    print('a =', a)  # 不可变：改变变量的值时会改变地址  e.g. 类型 int float str bool tuple
    # 可变：里面内容发生改变，但地址没有发生改变  e.g.  类型 list dict set


max()
'''


# 查看全局变量
# print(globals())


def outer():
    c = 100

    def inner():  # 1、函数中在嵌套一个函数，被嵌套的函数里 (成为内部)，是可以使用外部（上一层的函数）变量，但不能修改，类似全局跟局部变量。
        b = 200  # 2、而 global 是修改全局变量的，并不适用于这种，这种函数嵌套函数需要用nonlocal。
        # b+=c  # 内部函数可以调用外部函数的参数
        # print('内部函数',b)
        nonlocal c  # 注意nonlocal修改的是你上一层函数的变量
        c += b
        print('内部函数', b)

    print(c)
    inner()


outer()

# 闭包定义
# 1 闭包就是外部函数中定义一个内部函数 (嵌套)
# 2 内部函数引用外部函数中的变量
# 3 外部函数的返回值是内部函数


# return 结束函数的调用(之后的语句都不会执行)，并返回一个值或多个值
