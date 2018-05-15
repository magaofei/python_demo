from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity


# 上下文
class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

# 策略: 抽象基类
class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """ 返回折扣金额(正值) """


# 第一个具体策略
class FidelityPromo(Promotion):
    """ 为积分1000或以上的顾客提供5%的折扣 """
    
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


# 第二个具体策略
class BuikItemPromo(Promotion):
    """  单个商品为20或以上时提供10%折扣 """
    
    def discount(self, order):
        discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


# 第三个具体策略
class LargeOrderPromo(Promotion):
    """ 订单中的不同商品达到10个或以上时提供7%折扣 """

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

    




if __name__ == '__main__':
    joe = Customer('John Doe', 0)