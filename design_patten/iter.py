"""
迭代器设计模式
"""
class Number():
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return NumberIter(self.value)
    
class NumberIter():

    def __init__(self, value):
        self.value = value
        self.index = 1

    def __next__(self):
        r = self.value // self.index % 10
        if r < 1:
            raise StopIteration
        self.index *= 10
        return r

    def __iter__(self):
        return self

if __name__ == '__main__':
    r = Number(123)
    for i in r:
        print(i)

