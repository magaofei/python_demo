__doc__ = """
iter for a number demo
only python3

生成器表达式

"""

def gen_number(number):
    index = 1
    value = index + 1

    length = len(str(number))
    for i in range(length):
        if value < 1:
            return

        value = number // index % 10
        index *= 10
        yield value

if __name__ == '__main__':
    number = 1234
    f = (x for x in gen_number(number))
    for i in f:
        print(i)
