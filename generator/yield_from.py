"""
yield from
"""

def chain(*iterable):
    
    for it in iterable:
        for i in it:
            yield i

def chain_from(*iterable):
    for it in iterable:
        yield from it

if __name__ == '__main__':
    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))

    print(list(chain_from(s, t)))
