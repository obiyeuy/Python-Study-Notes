import random

s = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
file = input('输入文件名：')
# 判断扩展名
if file.endswith('jpg') or file.endswith('gif') or file.endswith('png'):
    # 判断文件名字
    i = file.rfind('.')
    name = file[:i]
    # len(name)
    if len(name) < 6:
        # 随机生成字母和数字的组合
        filename = ''
        for j in range(6):
            index = random.randint(0, len(s) - 1)
            filename += s[index]
        file = filename + file[i:]
    print('成功上传%s文件' % file)
else:
    print('文件格式错误，上传失败！')
