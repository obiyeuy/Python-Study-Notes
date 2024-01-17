'''
原文件：
目标文件：

open 只能复制具体的一个文件

要复制多个文件，需要导入os模块

 os.path:
   os.path.dirname(__file__)   # 得到当前文件所在目录的位置(绝对路径)
   os.path.join(path,'','','',...)    # 返回的是一个拼接后的新路径(可以接多个，每多一个就多一层)
   os.path.isabs(path)     判断是否是绝对路径     !!!注意：不会去判断path路径是否存在！
   os.path.split(path)   # 切一刀，放在元组中
   os.path.splitext(path)   # 分割文件与拓展名
   os.path.getsize(path)   # 返回文件字节数


with open(path,mode) as name:    #name为stream通道的名字
    name.write('Hello, world!')     #这种格式无需关闭，自动释放内存
              否则如下
             f = open(path,mode)
             f.write('Hello, world!')
             f.close()
'''

# with open(r'C:\Users\YYB\Pictures\Saved Pictures\beauty.jpg', 'rb') as stream:
#     container = stream.read()   # 读取文件内容
#
# with open(r'C:\Users\YYB\Pictures\Camera Roll\beauty.jpg', 'wb') as wstream:    # 注意'wb'
#     wstream.write(container)


import os

# print(os.path)
# path = os.path.dirname(__file__)
# print(path)  # 得到当前文件所在目录的位置(绝对路径)   __file__:当前文件


# with open(r'C:\Users\YYB\Pictures\Saved Pictures\beauty.jpg', 'rb') as stream:
#     container = stream.read()   # 读取文件内容
#
#     file = stream.name
#     filename = file[file.rfind('\\')+1:]   # 截取文件名，即beauty.jpg
#
#     path = os.path.dirname(__file__)
#     path1 = os.path.join(path, filename)
# with open(path1, 'wb') as wstream:    # 注意'wb'
#     wstream.write(container)


# r = os.path.isabs(r'C:\Users\YYB\Pictures\Saved Pictures\beauty.jpg')
# print(r)
#
# #  相对路径
# r = os.path.isabs('../images/beauty.jpg')    # ../表示当前文件的上一级  code
# print(r)
#
# r = os.path.isabs('images/beauty.jpg')    # 找与文件复制.py同级的images里面找beauty.jpg
# print(r)


path = os.path.abspath('beauty.jpg')
print(path)

path = os.getcwd()    # 类似os.path.dirname(__file__)
print(path)

path = r'C:\Users\YYB\Pictures\Saved Pictures\beauty.jpg'

result = os.path.split(path)   # 切一刀，放在元组中
print(result)
print(result[1])

result = os.path.splitext(path)   # 分割文件与拓展名
print(result)














