

"""
"""

def if_demo(value):
    foo = 1
    bar = 2

    value -= 1
    k_dict = [foo, bar]
    k = k_dict[value]

    # k = 0
    # if value == foo:
    #     k = foo
    # elif value == bar:
    #     k = bar
        
    print(k)

    


if __name__ == '__main__':
    if_demo(2)