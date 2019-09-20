"""
带有固定参数的函数装饰器
"""

import time
from functools import wraps

"""
 函数带参数的装饰器
"""
def total_time(f):
    @wraps(f)
    def wapper(*args,**kwargs):
        start_time = time.time()
        resutl=f(*args,**kwargs)
        print(resutl)
        end_time = time.time()
        execution_time = (end_time-start_time)*100
        print("time is %d ms" % execution_time)
        return resutl
    return wapper

@total_time
def func(a,b):
    print("be on")
    res = a+b
    time.sleep(1)
    print("result is %d ms"%(a+b))

func(1,2)
print(func.__name__)


import random

def author(func):
    def wrapper(*args,**kwargs):
        while True:
            user = input("input your name >>>:").strip()
            pwd  = input("input your password>>>:").strip()
            if user == "abcd" and pwd == "1234":
                print("login sucessful")
                func(*args,**kwargs)
                break
            else:
                print("login failed")

    return wrapper

@author
@total_time
def index():
    time.sleep(2)
    print("welcome to index page ")


"""
带参数的装饰器
"""

from inspect import signature

def typeassert(*args,**kwargs):
    def wrapper(func):
        sig = signature(func)
        bytes = sig.bind_partial(*args,**kwargs).arguments
        @wraps(func)
        def inner(*args,**kwargs):
            for name,obj in sig.bind(*args,**kwargs).arguments.items():
                if name in bytes:
                    if not isinstance(obj,bytes[name]):
                        raise TypeError('"%s" must be "%s"' % (name,bytes[name]))
            func(*args,**kwargs)
        return inner

    return wrapper


""""
logger 的等级设置
"""
def logger(*args,**kwargs):
    def wrapper(func):
        level = kwargs.get("level")
        @wraps(func)
        def inner(*args,**kwargs):
            if level==3 and isinstance(args[0],int):
                print("log debug is level is dangerous{}".format(str(args[0])))
                func(*args)
        return inner
    return wrapper


@logger(level=3)
def func(b):
    print("hello word")
func(4)

def params_check(*args,**kwargs):
    def wrapper(func):
        sig = signature(func)
        bytes = sig.bind_partial(*args,**kwargs).arguments
        @wraps(func)
        def inner(*args,**kwargs):
            for name,obj in sig.bind(*args,**kwargs).arguments.items():
                if name in bytes:
                    if not isinstance(obj,bytes[name]):
                        raise TypeError("类型错误")
            func(*args,**kwargs)
        return inner

    return wrapper




@typeassert(int,str,list)
def f(a,b,c):
    print(a,b,c)

f(1,'abc',[1,2,3,4])

func_sig = signature(f)
print(func_sig.bind(1,"2",[1,2,4]).arguments)

print(f.__dict__)







