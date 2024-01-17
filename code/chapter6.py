'''
# 格式化输出
money = 894.96
print('赚了%f元' % money)
print('赚了%.2f元' % money)

n = 1342
result = bin(n)
print(result)  # 二进制 0b

result = oct(n)
print(result)  # 八进制 0o

result = hex(221)
print(result)  # 十六进制 0x
'''

# 位运算
'''
& 与运算
| 或运算
^ 异或运算
print(~5)  # 对5的二进制取反 ~
'''

# import random
#
# count = 0
#
# while True:
#     money = int(input('充值：'))
#     if money % 10 == 0:
#         print('充值成功')
#         break
#     else:
#         print('充值失败')
#         money = 0
#
# answer = input('是否玩游戏(y/n)')
# while money >= 5 and answer == 'y':
#     ran = random.randint(1, 6)
#     money -= 5
#     if ran >= 4:
#         ran = "大"
#     else:
#         ran = '小'
#     guess = input('猜大小：')
#     count += 1
#     if guess == ran:
#         print('猜对了')
#         money += 2
#         print(money)
#     else:
#         print('猜错了')
#         print(money)
#     answer = input('是否玩游戏(y/n)')
# else:
#     print(money)
#     print(count)
#

#
# for i in range(10):
#     if i % 3 == 0:
#         # break
#         continue
#     else:
#         print(i)


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         mup = i * j
#         print('%d*%d=%d\t' % (j, i, mup), end="")
#     print()


# range(stop) 0~stop-1
# range(start,stop) start~stop-1
# range(start,stop,step)
