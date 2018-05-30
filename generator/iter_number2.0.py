__doc__ = """
iter for a number demo
only python3

迭代器可以迭代，但是可迭代的对象不是迭代器     ---- 流畅的python (Fluent Python)

"""

class IterNumber(object):
    """
    """
    def __init__(self, num):
        self.num = num
        self.index = 1
    
    def __next__(self):
        
        r = int(self.num / self.index % 10)
        if r <= 0:
            raise StopIteration
        self.index *= 10
        return r

class Number(object):
    def __init__(self, num):
        self.num = num
    
    def __iter__(self):
        return IterNumber(self.num)


if __name__ == '__main__':
    r = Number(123)
    for i in r:
        print(i)

