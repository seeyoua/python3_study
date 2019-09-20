"""
1、Cretor 简单的工厂方法的核心，包含所有的程序的所需要的业务逻辑，当客户类client时候委托工厂类创建产品类
2、product 可以是接口或者抽象类、是具体子类的超类或者共同的接口。
3、Concreteproduct 实现product的接口 或者继承抽象类product
不支持开闭原则
"""

from abc import ABC,abstractmethod

class Creator(object):
    @staticmethod
    def get_product(option):
        product = None
        if option == 1:
            product = ConcreateProduct1()
        elif option ==2:
            product = ConcreateProduct2()
        return product

class Product(ABC):
    @abstractmethod
    def get_product_info(self):
        raise NotImplementedError

class ConcreateProduct1(Product):
    def get_product_info(self):
        return "ConcreateProduct01"

class ConcreateProduct2(Product):

    def get_product_info(self):
        return "concreateProduct02"

class Client(object):
    @staticmethod
    def main():
        otptions = int(input('please select>>>:'))
        print(Creator.get_product(otptions).get_product_info())

# Client.main()

"""
 完善工厂方法 ，支持开闭原则
"""

class Creator01(object):
    @staticmethod
    def factory(self):
        pass
class CreateA(Creator01):
    @staticmethod
    def factory():
        return ConProduct01()
class CreateB(Creator01):
    @staticmethod
    def factory():
        return ConProduct02()

class Product01(ABC):
    def get_info(self):
        pass

class ConProduct01(Product01):
    def get_info(self):
        return "conProduct01"

class ConProduct02(Product01):
    def get_info(self):
        return "conProduct02"

class Client01(object):

    @staticmethod
    def main():
        options = int(input("select params >>:"))
        if options == 1:
            creator = CreateA()
        else:
            creator = CreateB()
        product = creator.factory()
        print(product.get_info())

""""
注释:
    两个模式的中心不同。工厂方法模式的中心是抽象工厂类或者接口，而简单工厂方法模式的中心是一个实的工厂类（Concrete Factory Class）。
    在简单工厂模式类中，工厂方法是静态（Static）的，而在工厂模式中工厂方法是动态的（Dynamic）。
    简单工厂模式不支持开闭原则，工厂方法模式支持开闭原则。在简单工厂模式中，如果要增加一个新的产品类，相应地在工厂类中也要增加一个条件语句，用于创建一个新的产品类对象。也就是说，必须修改工厂类的源代码。因此简单工厂模式不支持开闭原则。
    在工厂方法模式中，增加新产品，只需在Product类的结构体中增加一个实类，并且在工厂类的层次结构体中增加一个增加一个相应的能产生该新产品类对象的实类。这种模式无需修改或者重新编译抽象的工厂方法类与已经存在的具体的工厂方法类。这样，在无需修改或者重新编译已经存在的代码的情况下，可以添加新的产品类（当然也必须同时添加工厂方法类）。因此工厂方法模式支持开闭原则。
    在简单工厂模式中，必要的创建对象的逻辑判断包含在工厂类中；在工厂方法模式中，工厂类不必包含创建对象的逻辑判断。
    在以下任何一种情况下，可以使用工厂方法模式。
    
    创建某些类的对象的逻辑比较复杂，并且有很多条件分支，而且还可能增加新的条件。
    一个类不能预先准确地知道它必须创建一个层次类中的哪个子类对象。
    一个类使用它的子类决定所要创建的对象。
    需要封装创建类的对象的逻辑，使得这些逻辑局部化。
    工厂方法模式的优点如下：
    
    工厂方法模式将创建对象的逻辑与任务交给了工厂类。
    工厂方法模式支持开闭原则
"""

if __name__ == '__main__':
    Client01.main()



