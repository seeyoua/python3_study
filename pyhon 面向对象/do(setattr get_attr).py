
"""
hasattr
    判断 object对象是否存在属性
    getattr 获取object的属性
    setattr 设置 object的属性
result:True
        True
        True
        True
        False
"""
class A(object):
    name = "python"
    def func(self):
        print("A 类的方法")
    @classmethod
    def func02(cls):
        print("A 类方法")

    @staticmethod
    def func03():
        print("A 类的静态方法")

print(hasattr(A,'func'))
print(hasattr(A,"name"))
print(hasattr(A,"func02"))
print(hasattr(A,"func03"))
print(hasattr(A,"func05"))

#设置属性
t = A()
setattr(t,"age",20)
print(getattr(t,'age'))


"""
__call__  将实例象想函数一样调用
"""


class DistanceForm(object):
    def __init__(self,name):
        self.name =name

    def __call__(self, *args, **kwargs):
        return self.instance()
    def instance(self):
        print(self.__dict__)
        return 20

d = DistanceForm("admin")
print(d())


"""
__call__ 方法装饰器
"""

import time

class Counter(object):

    def __init__(self,func):
        self.func = func
        self.start_time = time.time()

    def __call__(self, *args, **kwargs):
        res=self.func(*args,**kwargs)
        end_time = time.time()
        print((int(self.start_time)-int(end_time))*1000)
        return res


@Counter
def foo():
    time.sleep(2)
    pass


foo()
print(foo.__dict__)
print(foo.start_time)






