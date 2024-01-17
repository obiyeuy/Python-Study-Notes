# class Student:
#     # 类属性
#     name = "yyb"
#     age = 10
#
#
# yyb = Student()
# print(yyb.name)
#
# yyb.gender = '男'  # 对象属性，属于它自己的
# print(yyb.gender)   # 先找自己空间的，没找到再到上层(模型 即类)去找


# 类中方法：动作
# 种类：普通方法   类方法  静态方法   魔术方法

"""
普通方法格式：
def 方法名(self,参数,参数)：
    pass 
"""


class Phone:
    # 方法

    # 魔术方法之一：__名字__() 被称为魔术方法
    def __init__(self, brand, price):  # 初始的，初始化    # 用于解决报阴影的部分   # self为当前对象的地址
        print('-----------------init')  # 系统会默认执行魔术方法,不需要调用
        self.brand = brand  # 将对象标准化，即都有brand,price
        self.price = price  # 注意这些属性定义在对象中，即类中没有这些属性   则Phone.price会报错

    def call(self):  # 对象在调用时，将对象本身传进去了
        print(self)
        print('正在访问通讯录')
        for person in self.address_book:
            print(person.items())
        print('打电话')
        print('留言:', self.note)  # 有阴影是因为不一定所有对象都有note

    def play(self, game):
        print('用{}打{}'.format(self.brand, game))


yyb = Phone('huawei', 3000)
# 1 找有没有一块空间是Phone
# 2 利用Phone类，向内存申请一块和Phone类一样的空间：0x000001C08535F250
# 3 去Phone中找有没有__init__，如果没有则执行将开辟内存给对像名:yyb
# 4 如果有，则会进入执行里面的动作，将内存地址赋值给对象yyb
print(yyb)
yyb.note = '我是留言'  # 传入note才能调用call(),否则报错
yyb.address_book = [{'18282772794': 'yyb'}, {'12323434t43431': 'hhhh'}]
yyb.call()
yyb.play('galgame')

# Phone.price      #type object 'Phone' has no attribute 'price'


# 类方法

"""
特点：
  1 定义需要依赖装饰器@classmethod
  2 类方法中参数不是一个对象，而是类
  3 类方法中只可以使用类属性   # 不依赖于对象，没有对象也可以调用类方法
  4 类方法中不能使用普通方法
  
  
作用：
  因为只能访问类属性与类方法，所以可以在对象创建之前，如果需要完成一些动作（功能），使用类方法

"""


class Person:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')

    def eat(self):
        print('eat')
        self.run()

    @classmethod
    def test(cls):
        print('------')
        print(cls)
        # print(cls.name)  报错
        # print(self.name)
        # self.run()    与上面报错原因相同


Person.test()  # 类方法直接调用
# Person.run()   # Person.run() missing 1 required positional argument: 'self'
# 即没有对象传入，不可调用


# 补充类方法

"""
静态方法：很类似类方法
   1 需要装饰器@staticmethod
   2 静态方法是无需传递参数(cls,self)
   3 也只能访问类的属性与方法，对象的是无法访问的
   4 加载时机同类方法
   
   
总结：
 类方法  静态方法
  不同：
   1 装饰器不同
   2 类方法有参数，静态方法没有
  
  相同：
   1 只能访问类属性与方法
   2 都可以通过类名调用访问
   3 都可以在创建对象之前使用，因为不依赖于对象
  
普通方法与两者区别：
 不同：
  1 没有装饰器
  2 普通方法永远要依赖对象，因为每个普通方法都有一个self
  3 只有创建了对象才可以调用普通方法，否则无法调用
  
"""


class Person:
    # age = 18
    __age = 18  # 将age属性私有

    def __init__(self, name):
        self.name = name

    def show(self):
        print(Person.age)

    @classmethod
    def update_age(cls):
        cls.__age = 20  # 私有后在类方法中改
        print('----->类方法')

    @classmethod
    def show_age(cls):
        print('修改后年龄：', cls.__age)

    @staticmethod
    def test():
        print('------>静态方法')
        # print(self.name)   # 语法错误
        print(Person.__age)


Person.update_age()  # age已经更新成功，但外界无法查看
Person.show_age()  # 利用这个类方法可以查看
Person.test()
# Person.age = Person.age + 1     # 私有前可以这样改类属性，私有后报错type object 'Person' has no attribute 'age'
# print(Person.age)

# p = Person()
# p.age = p.age+1
# print(p.age)




















