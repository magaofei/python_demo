names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]


def demo_1():
    longest_name = None
    max_letters = 0
    for i in range(len(names)):
        count = letters[i]
        if count > max_letters:
            longest_name = names[i]
            max_letters = count
    
    print(longest_name)


def demo_2():
    longest_name = None
    max_letters = 0

    for i, name in enumerate(names):
        count = letters[i]
        if count > max_letters:
            longest_name = name
            max_letters = count

def demo_3():
    """
    zip 函数将两个相关联的列表的元素每次遍历时放到一个元组中
    前提： 长度需一致， 否则使用 itertools 里 zip_longest
    """
    longest_name = None
    max_letters = 0

    for name, count in zip(names, letters):
        if count > max_letters:
            longest_name = name
            max_letters = count

