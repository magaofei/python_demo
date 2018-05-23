"""
使用协程计算平均值
"""
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

coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(20)
coro_avg.send(30)
