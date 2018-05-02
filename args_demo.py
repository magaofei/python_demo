
def tag(name, *content, cls=None, **attrs):
    """ generatr HTML Tag """

    """ 赋值cls标签 """
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % 
        (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


def func1(*arg, **kwargs):
    # print(arg)
    # print(type(arg))

    print('print(arg)')
    for i in arg:
        print(i)
    print('kwargs')
    print(kwargs.get('foo'))

    # print(*arg)
    # print(type(*arg))

    # print(kwargs)
    foo = kwargs.get('foo')
    # print(foo)
    # print(**kwargs)

def func2(*arg):
    print(__name__)
    print(arg)


if __name__ == '__main__':

    # func1([1, 2, 3, 4], foo=1, bar=2)
    # # print(r1)
    # d = [i for i in range(10)]
    # d2 = (i for i in range(10))
    # print(type(d2))
    # r = func2(d)
    # print(r)
    # print(*d)

    """ tag('br')                   <br /> """
    """ tag('br', 'hello')          <br>hello</br> """

    """ tag('p', 'hello', id=33)    <p id="33">hello</p>  """
    """ tag('p', 'hello', 'world', cls='sidebar')  
    <p class="sidebar">hello</p> 
    <p class="sidebar">world</p> """
    r = tag('p', 'hello', 'world', cls='sidebar')
    print(locals())
    print(globals())
    print(r)


    