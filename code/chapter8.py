# # sort reverse
#
# import random
#
# numbers = []
# for i in range(8):
#     ran = random.randint(1, 20)
#     numbers.append(ran)
#
# print(numbers)
#
# numbers.reverse()
# print(numbers)  # reverse将列表翻转
# # numbers.sort()  # 默认升序，可以通过reverse参数控制升序还是降序
# # print(numbers)
#
# numbers.sort(reverse=False)
#
# a = 2
# b = 4
#
# a, b = b, a
# print(a, b)


# 字典 键值对
book = {'书名': '三体', '价格': '20', '作者': '刘慈欣'}
value = book.get('书名1', '红楼梦')
print(value)  # 没找到不会报错，会返回none;如果赋值了，就会返回默认值

value = book['书名']
print(value)  # 没找到会报错 Keyerror

for i in book:
    print(i)  # 只打印键值（key）

for i in book.values():  # 返回值(value) 注： book.values() 是一个列表
    print(i)

for i in book.keys():
    print(i)

print(book.items())  # [('书名', '三体'), ('价格', '20'), ('作者', '刘慈欣')]

for i in book.items():
    print(i)  # 结果是元组

for k, v in book.items():
    print(k, v)
    print(k)
    print(v)

book.setdefault('出版社', '人民教育出版社')  # 类似：book[key]=value 只能添加，不能修改
print(book)

book.setdefault('出版社', '人民出版社')  # 类似：book[key]=value
print(book)

dict1 = {'a': 10, 'b': 20}
book.update(dict1)  # 实现字典的合并
print(book)

result = dict.fromkeys(book)  # 创建一个新字典，以book中key不变，value赋值为none
print(result)

result = dict.fromkeys(['a', 'b'])
print(result)
