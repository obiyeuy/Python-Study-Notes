# 开发模式：单例模式

# 单例模式有 3 个特点：
    # 单例类只有一个实例对象；
    # 该单例对象必须由单例类自行创建；
    # 单例类对外提供一个访问该单例的全局访问点；


class Singleton:
    # 私有化  单例的地址都存在于__instance
    __instance = None
    name = 'jack'

    # __new__开辟空间，重写父类
    def __new__(cls):
        print('-------------new')
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance


s = Singleton()
s1 = Singleton()

print(s)
print(s1)














