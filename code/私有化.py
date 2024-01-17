# 私有化
# 封装：1 私有化属性  2 定义公有set和get方法
# __属性：就是将属性私有化，访问范围仅仅限于类中

"""
好处：
  1 隐藏属性不被外界随意修改
  2 也可以修改，通过函数
    def setXXX(self, xxx):
        3 筛选赋值的内容（过滤）
        if xxx符合条件:
            赋值
        else:
            提示
  4 如果想获取一个具体的属性
    使用get方法
    def getXXX(self):
        return self.__xxx
"""


# class Student:
#     # __age = 18   # 类属性
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.__score = 59
#
#     # 定义公有set和get方法
#     # set是为了赋值
#     def setAge(self, age):
#         if age > 0 and age <= 120:
#             self.__age = age
#         else:
#             print('年龄不在规定范围内')
#
#     # get是为了取值
#     def getAge(self):
#         return self.__age
#
#     def setName(self, name):
#         if len(name) == 6:
#             self.__name = name
#         else:
#             print('名字必须六位')
#
#     def getName(self):
#         return self.__name
#
#     def setScore(self, score):
#         self.__score = score
#
#     def getScore(self):
#         return self.__score
#
#     def __str__(self):
#         return '姓名：{}，年龄：{}，分数：{}'.format(self.__name, self.__age, self.__score)
#
#
#
# p = Student('yyb',18)
# print(p)
# # print(p.__score)   # 'Student' object has no attribute '__score'
# p.__score = 95
# p.setAge(19)
# print(p)
# print(p.getAge())
#
# print(dir(Student))
#
# print(dir(p))
# print(p._Student__age)   # 伪装私有，底层将其改名，所以没有访问的属性才访问不到，因此这样也可以访问。但不支持，一般用set与get





# 在开发中看到一些私有化处理：装饰器

class Student:
    # __age = 18   # 类属性

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 先有getxxx
    @property
    def age(self):
        return self.__age

    # 再有setxxx(依赖于get)
    @age.setter
    def age(self, age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print('年龄不在规定范围内')


    # # 定义公有set和get方法
    # # set是为了赋值
    # def setAge(self, age):
    #     if age > 0 and age <= 120:
    #         self.__age = age
    #     else:
    #         print('年龄不在规定范围内')
    #
    # # get是为了取值
    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return '姓名：{}，年龄：{}'.format(self.name, self.__age)


s = Student('yjh', 9)
# 私有化赋值
# s.setAge(30)
# print(s.getAge())
print(s.__dir__())   # '_Student__age', 'age'
s.age = 19
print(s.age)
s.age = 130   # 不在范围内
print(s.age)













