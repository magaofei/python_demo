
"""
预激协程 ---> 装饰器实现
yield from 会自动预激
"""
from coroutil import coroutine

"""
执行函数前先调用了一次 next ,使用装饰器实现比较优雅
"""
@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
        print(average)


if __name__ == '__main__':
    coro_avg = averager()
    coro_avg.send(10)
    coro_avg.send(20)
    coro_avg.send(30)