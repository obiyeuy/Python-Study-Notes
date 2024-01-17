import os

dir = os.getcwd()
print(dir)

all = os.listdir(r'C:\gg')  # 返回指定目录下的所有文件与文件夹，保存到列表中
print(all)

# 创建文件夹
if not os.path.exists(r'C:\gg1'):
    f = os.mkdir(r'C:\gg1')
    print(f)    #？？？

f = os.rmdir(r'C:\gg1')    # 只能删除空文件夹
print(f)

# f = os.removedirs(r'C:\gg1')
# print(f)
#
# os.remove(绝对路径)


# 切换目录
f = os.chdir(r'C:\gg')   # 将默认目录切换
print(f)

path = os.getcwd()
print(path)





