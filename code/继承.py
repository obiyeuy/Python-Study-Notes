# 继承： is a, has a
"""
知识点：
 1 has a
   一个类中使用了另一种自定义的类型

 2 类型
   系统类型：
       str  int  float  list
       dict  tuple  set
   自定义类型：
       算是自定义的类，都可以将其当成一种类型


特点：
  1 如果类中不定义__init__,调用父类super都
  2 如果类继承父类也需要定义自己的__init__,就需要在当前类的__init__调用一下父类__init__
  3 如何调用父类__init__：
    super().__init__()
    super(类名，对象).__init__()
  4 如果父类有eat(),子类也要定义一个eat()，则会先找当前类，再找父类
    被称为override：重写（覆盖）  两函数重名
  5 子类的方法中也可以调用父类的方法
       super().方法名(参数)
"""
import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = '{}车在{}上以{}速度行驶{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的，速度：{}'.format(self.brand, self.speed)


# 创建实例化对象
r = Road('京藏高速', 12000)
audi = Car('奥迪', 120)
print(audi)
r.name = '京哈高速'
audi.get_time(r)  # 将对象当成参数传入


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('person的init')

    def run(self):
        print('{}在跑步'.format(self.name))


class Student(Person):    # 继承父类
    def __init__(self, name, age, clazz):
        print('student的init')
        super().__init__(name, age)   # 父类对象,继承父类的属性
        self.clazz = clazz


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.patients = patients


s = Student('jack', 18, 'san')
s.run()


import inspect

print(inspect.getmro(Doctor))    # 可以找到搜索顺序，使用时要导入inspect
print(Doctor.__mro__)   # 与上面作用一样

"""
  python允许多继承
  def 子类（父类1，父类2...）
      pass
  
  父类中有重名的方法，则"""


