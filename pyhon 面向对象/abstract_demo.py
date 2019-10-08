from collections.abc import Sized

"""
python 中没有提供抽象累的方法，但是提供了内置模块abc来摸模拟实现抽象类

class Sized(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __len__(self):
        return 0

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            return _check_methods(C, "__len__")
        return NotImplemented
Color都没有继承Sized，可是为什么会返回True，这些就可以想到鸭子类型(是动态类型的一种风格)
"""


class ColorObject(object):

    def __init__(self,color_list):
        self.color = color_list

    def __len__(self):
        return len(self.color)


color = ColorObject(['red'])

result = isinstance(color, Sized)
print(result)


#抽象类无法实例化
import abc

class BaseObj(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, value):
        print(value)

    @abc.abstractmethod
    def set(self, key, value):
        print(key,value)

#obj = BaseObj() #实例化报错


#强制子类实现的方法
class Dog(BaseObj):

    def get(self, value):
        return value

    def set(self, key, value):
        pass


d = Dog()
print(d.get('name'))

"""
    鸭子类型
"""


class A(object):
    def part(self):
        print(A)


class B(A):
    def part(self):
        print(B)


class C(A):
    def part(self):
        print(C)


class D(A):
    def part(self):
        print(D)


class E(object):
    def part(self):
        print(E)


class F(object):
    pass


e = E()
a = A()
"""
    鸭子类型：A,B两个类,没有任何关系,独立两个,但是里面的功能相似，其实列方法的名称相同(
    如下：两个子类都是实现了login，和注册功能。
    )
"""

class WebDemo(object):

    def login(self):
        print('login alipay')

    def register(self):
        print('register alipay')


class WebDemoCopy(object):
    def login(self):
        print('login wechat')

    def register(self):
        print('register wechat')

web = WebDemo()
web01 = WebDemo()

#两次返回都为Ture
print(isinstance(web, WebDemo))
print(isinstance(web01, WebDemo))

"""
    多态:继承父类为前提，相同的实列方法名称，显示不同的属性
"""


### 父类的约束不是强制性的,不重写父类的 pay函数 也可以调用子类本身的函数,完成支付功能

class Payment:

    def pay(self,money):
        raise  Exception('子类必须继承父类pay方法')   # 当子类执行接口函数时,调用函数名与父类不一致,父类pay函数主动抛出一个异常


class QQ(Payment):
    def pay(self,money):
        print(f'支付了 {money}')


class Ali(Payment):
    def pay(self,money):
        print(f'支付了 {money}')


class WeChat(Payment):
    def pay(self,money):
        print(f'支付了 {money}')

# 定义接口

def pay(obj,money):
    obj.pay(money)


q=QQ()          # 实例化对象
al=Ali()
w=WeChat()

pay(q, 200)
pay(al, 100)
pay(w, 1200)     # 由于









