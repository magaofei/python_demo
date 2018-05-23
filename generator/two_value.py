def simple_coro2(a):
    print('-> Started: a = ', a)
    b = yield a
    print('-> Received: b = ', b)
    c = yield a + b
    print('-> Received: c =', c)

my_coro2 = simple_coro2(14)
from inspect import getgeneratorstate
"""  协程未启动   """
print(getgeneratorstate(my_coro2))

"""  向前执行协程到第一个 yield 表达式(预激协程) 产出 a 的值,并且暂停"""
next(my_coro2)

"""  GEN_SUSPENDED 协程在 yield 表达式处暂停  """
print(getgeneratorstate(my_coro2))

"""  把数字28发给暂停的协程, 计算 yield 表达式,得到28, 然后把那个数字绑定给b, 打印, 然后协程暂停, 等待为 c 赋值  """
my_coro2.send(28)

"""  把数字99发给暂停的协程, 计算 yield 表达式,得到99,然后把那个数绑定给 c ,打印, 然后协程终止, 生成器抛出 StopIteration 异常  """
my_coro2.send(99)
