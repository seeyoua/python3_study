"""
1、Cretor 简单的工厂方法的核心，包含所有的程序的所需要的业务逻辑，当客户类client时候委托工厂类创建产品类
2、product 可以是接口或者抽象类、是具体子类的超类或者共同的接口。
3、Concreteproduct 实现product的接口 或者继承抽象类product
"""


from abc import ABC,abstractmethod

class Creator(object):
    @staticmethod
    def get_product(option):
        product = None
        if option == 1:
            product = ConcreateProduct1()

class Product(ABC):
    @abstractmethod
    def get_product_info(self):
        raise NotImplementedError

class ConcreateProduct1(ABC):
    "con"
    pass


class ConcreateProduct2():
    pass

