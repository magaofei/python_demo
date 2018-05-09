
__doc__ = """
动态调用方法
"""
import sys

def fun1(foo, bar):
    print(foo, bar)


class Fun():

    def fun2(self, foo, bar):
        print(foo, bar)

if __name__ == '__main__':
    data = {'foo': 1, 'bar': 2}
    args = ','.join((str(v) for k, v in data.items()))
    # print(args)
    # eval('fun1(' + args + ')')
    getattr(, 'fun1')(1, 2)

    args = data

    f = Fun()
    getattr(f, 'fun2')(**args)





