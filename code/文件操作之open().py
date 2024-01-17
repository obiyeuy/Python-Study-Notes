'''

文件上传
保存log

系统函数
open(file,mode,buttering,encodeing)

读：
  open(path/filename,'rt')---->返回值：stream（管道）  # rt为默认

  container=stream.read()---->读取管道中内容

  注意：如果path/filename有误，就会报错
       如果是图片，就不能使用默认的读取方式，mode=’rb‘

  总结：
  read()
  readline()   一行一行读
  readlines()   按行读，并放在一个列表中
  readable()   是否可读


写：
   open(r'C:\gg\gg.txt','w')    # 在同一次流中的第一次写时会先清空文件
   mode是'w',就是写
   writelines(Iterable) 没有换行效果  需要自己加\n

如果mode='a'   则为追加，即不会先清空文件  (append)


'''


# 读
stream = open(r'C:\gg\gg.txt')  # 加r是声明不用字符串转义，否则如\t会被转义为tab键
                                # 其它方法  1:'C:\\gg\\gg.txt'  2:'C:/gg/gg.txt'
# container=stream.read()
# print(container)

result = stream.readable()  # 判断是否可以读取  True  False
print(result)

# while True:
#     line = stream.readline()   # 注意：read读过一次后，stream就没有东西了，而radline是读取一行内容
#     print(line)
#     if not line:
#         break


lines = stream.readlines()   # 将内容按行读取，然后存在一个列表中
print(lines)
# 将内容按行取出
for i in lines:
    print(i)

# stream = open(r'C:\Users\YYB\Pictures\Saved Pictures\Screenshot_20220929_132954.jpg','rb')  # 图片需按二进制读取
#
# container = stream.read()
# print(container)


# # 写
# stream = open(r'C:\gg\gg.txt', 'w')   # 在同一次流中的第一次写时会先清空文件
#
# s = '''
# 你好！
#    欢迎来到我的世界
# '''
#
# result = stream.write(s)
# print(result)
#
# result = stream.write('\nplay')
# stream.close()  # 释放资源
#
# print(result)


stream = open(r'C:\gg\gg.txt', 'a')

s = '''
  你好！
    欢迎来到我的世界
 '''

result = stream.write(s)
print(result)
















