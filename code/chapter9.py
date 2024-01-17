'''
set 无序，不许重复
list 有顺序，可以重复
'''

'''
import random

code_list = set()
s = '1234568907qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
while True:
    code = ''
    for i in range(4):
        r = random.choice(s)
        code += r
    code_list.add(code)

    if len(code_list) == 5:
        break

print(code_list)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

a = set1.union(set2)  # set1|set2
b = set1.intersection(set2)  # set1&set2
c = set1.difference(set2)  # set1-set2

print(a, b, c)

# list-->dict
# 特殊要求：
list1 = [('a', [2,1,4]), ('b', 3)]
print(dict(list1))
'''

'''
# 列表推导式
# 格式1：[i for i in 可迭代的]
listA = [i for i in range(1, 21)]
print(listA)

listB = [i * 2 for i in range(1, 51)]
print(listB)

# 格式2：[i for i in 可迭代的 if 条件]
listC = [i for i in range(1, 101) if i % 2 == 0]
print(listC)

list1 = ['12', 'play', '34', 'jump', 'fly', '42', 'float', 'playground']
list2 = [j for j in list1 if j.isalpha()]
print(list2)

# 格式3：[结果1 if 条件 else 结果2 for 变量 in 可迭代的]
list3 = [word.title() if word.startswith('p') else word.upper() for word in list1]
print(list3)
'''

'''
装包与拆包：
函数装包：
def 函数(*args):     (可变参数)
    pass

拆包：
list,tuple,set
调用的时候
函数(*list)   # 一颗*拆元组，列表的包
'''

'''
# (可变参数) 两颗*

def show_books(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


show_books()  # 返回字典
show_books(book_name='西游记', author='吴承恩', number=5)  # 前面为key，后面为value

book = {'book_name': '西游记', 'author': '吴承恩', 'number': 5}
show_books(**book)  # 两颗*拆字典包
'''


def show_books(*args, **kwargs):      # '''  ''' 会自动跳出变量与return
    '''

    :param args:
    :param kwargs:
    :return:
    '''
    print(args)  # ()
    print(kwargs)  # {}


book = {'book_name': '西游记', 'author': '吴承恩', 'number': 5}
show_books('龙少', '小飞', **book)

print(book, 'hello', sep='--')








