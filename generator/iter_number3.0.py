__doc__ = """
iter for a number demo
only python3

"""

class Number(object):

    def __init__(self, num):
        self.num = num
        self.nums = []
        index = 1
        r = 2
        
        while r > 1:
            r = self.num // index % 10
            self.nums.append(r)
            index *= 10
    
    def __iter__(self):
        for n in self.nums:
            yield n


if __name__ == '__main__':
    r = Number(123)
    for i in r:
        print(i)

