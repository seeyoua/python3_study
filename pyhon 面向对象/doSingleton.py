"""
python3 单例模式

"""
from functools import wraps
#普通的单列模
def singtleton(cls):
    _instance ={}
    @wraps(cls)
    def _singleton(*args,**kwargs):
        if cls  not in _instance:
            _instance[cls] = cls(*args,**kwargs)
        return _instance[cls]
    return _singleton

@singtleton
class A(object):
    def __init__(self):
        self.name = "A"

a= A()
b= A()


#类的单利模式
from threading import Thread
import threading
import time
class Singleton(object):
    #_instance_lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        _instance_lock = threading.Lock()
        if not hasattr(Singleton,"_instance"):
            with _instance_lock as lock:
                Singleton._instance = Singleton
        return Singleton._instance

    def __init__(self,name=None):
        self.name ="Singleton class"

    @classmethod
    def instance(cls,*args,**kwargs):
        if not hasattr(Singleton,"_instance"):
            with cls._instance_lock as lock:
                Singleton._instance = Singleton(*args,**kwargs)
        return Singleton._instance


def  test():
    a = Singleton()
    print(id(a))


def test2():
    a= Singleton.instance()
    print(id(a))

for i in range(2):
    t = Thread(target=test(),args=())
    t.start()


time.sleep(5)
# obj = Singleton.instance()
# print(id(obj))
obj2 =Singleton()
print(id(obj2))