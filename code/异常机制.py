# 异常处理
"""
格式1：
try:
   可能出现异常的代码
except:
    如果有异常执行的代码    # try 与 except 必须需要， finally 可要可不要
[finally:
    无论是否存在异常都会执行的代码]


格式2：
try:
   可能出现异常的代码
except:
    如果有异常执行的代码
else:
    没有异常才会执行的代码块



情况一：
  try:
     有可能产生多个异常
  except 异常类型1：
      print('')
  except 异常类型2：
      print('')
  except Exception:
      pass      # 注意顺序，大类放在下面

情况二：   获取Exception的错误原因
try:
     有可能产生多个异常
  except 异常类型1：
      print('')
  except 异常类型2：
      print('')
  except Exception as err:
      print('',err)




"""

"""
def func():
    try:
        n1 = int(input('输入一个数字：'))
        n2 = int(input('输入另一个数字：'))
        result = n1 / n2
        print(result)
    except ValueError:  # 匹配判断从try上往下
        print('必须输入数字')
    except ZeroDivisionError:
        print('除数不为0')
    except Exception as rr:    # as ...  报出出错原因
        print('出错了', rr)
"""


def func():
    stream = None
    try:
        stream = open(r'C:\Users\YYB\Pictures\Saved Pictures\beauty.jpg')
        container = stream.read()
        print(container)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('---finally---')
        if stream:
            stream.close()
        return 3 


print(func())
















