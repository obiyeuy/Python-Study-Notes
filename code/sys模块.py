"""
当你导入一个模块时，python解析器对模块位置的搜索顺序是：
1 当前目录
2 不在当前目录，就会搜索在shell变量PYTHONPATH下的每个目录
3 如果都找不到，就会查看默认路径。UNIX下，默认路径一般为/uer/local/lib/python/。
  模块搜索路径存储在system模块的sys.path变量中。变量包含当前目录，PYTHONPATH和由安装过程决定的默认路径
"""


import sys
print(sys.path)   # 显示搜索路径






