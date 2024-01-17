# 列表推导式 字典推导式 集合推导式
# 旧的列表---》新的列表

# 1列表推导式： 格式：[表达式 for 变量 in 旧列表] 或者[表达式for变量 in旧列表 if条件]
# number = [24, 2, 42, 5, 2, 6, 7]
# result = [number for number in number if number < 7]
# print(result)
#
# name = ['tom', 'tony', 'jone', 'rose', 'jake']
# result = [name.capitalize() for name in name if len(name) > 3]  # 首字母大写
# print(result)
#
# list = [number for number in range(1, 101) if number % 3 == 0 and number % 5 == 0]
# print(list)
#
# """
# def func():
#     newlist = []
#     for i in range(5):
#         if i%2==0:
#             for j in range(10):
#                 if j%2==1:
#                     newlist.append((i,j))
#     return newlist
# print(func())
# """
#
# newlist = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 == 1]
# print(newlist)
#
# list = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]
# newlist = [i[2] for i in list]
# print(newlist)
#
# newlist = [i[2] if i[2]<6 else i[2]+1 for i in list]
# print(newlist)


# 集合推导式  {} 类似于列表推导式，在其上加了去除重复项
list1 = [1, 3, 4, 2, 4, 3, 2, 434, 3, 3, 3, 2132, 3, 3, 43, 12]

set = {x for x in list1}
print(set)

# 字典推导式
dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}

newdict = {value: key for key, value in dict.items()}
print(newdict)
