#     匿名函数
# 在Python中，使用lambda表达式创建匿名函数，其语法格式如下：
# result = lambda[arg1[,arg2,...,argn]]:expression
# result：用于调用lambda表达式。
# [arg1[,arg2,…,argn]]：可选参数，用于指定要传递的参数列表，多个参数使用逗号“,”分隔。
# expression：必选参数，用于指定一个实现具体功能的表达式，如果有参数，那么在该表达式中将应用这些参数。
# 注意： 使用lambda表达式时，参数可以有多个，用逗号“,”分隔，但是表达式只能有一个，即只能返回一个值，而且也不能出现其他非表达式语句（如for或while）。


'''
def foo():
    print('foo')


def fun():
    print('fun')


foo = fun  # fun 函数名  fun() 调用函数    注：函数也是参数，将fun赋给foo
foo()
'''




# 装饰器是给现有的模块增添新的小功能，可以对原函数进行功能扩展，而且还不需要修改原函数的内容，也不需要修改原函数的调用。
# 装饰器的使用符合了面向对象编程的开放封闭原则。
# 开放封闭原则主要体现在两个方面：
# 1 对扩展开放，意味着有新的需求或变化时，可以对现有代码进行扩展，以适应新的情况。
# 2 对修改封闭，意味着类一旦设计完成，就可以独立其工作，而不要对类尽任何修改
'''
def decorator(func):
    def wrapper():          
        func()
        print('刷漆')
        print('买家具')
    return wrapper

@decorator
def house():
    print('毛坯房')

house()
'''


'''
def decorator(func):
    def wrapper(*args,**kwargs):          # wrapper函数的参数为*args和**kwargs，表示可以接受任意参数,这时我们就可以调用我们的装饰器了。
        func(*args,**kwargs)
        print('刷漆')
        print('买家具')
    return wrapper


@decorator
def home(address):
    print('房子在{}'.format(address))


home('fle')
'''


'''
# 带返回值的装饰器
def decorator(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print('刷漆')
        print('买家具')
        return func(*args,**kwargs)   # 返回值为原函数的返回值  (原函数有返回值，装饰器也要有返回值)
    return wrapper


@decorator
def house():
    print('毛坯房')
    return 50000

house()
r=house()
print(r)
'''
























