
"""
默认不调用父类的 __init__
需要手动调用
"""
class Person(object):
    def __init__(self):
        print("Person init")


class Student(Person):

    def __init__(self):
        super().__init__()
        print("Student init")

class StaticDemo(object):

    @staticmethod
    def test_static(self):
        pass

    def normal(self):
        pass

if __name__ == '__main__':
    # s = Student()
    pass

    # StaticDemo.test_static()
    
    
class Child(Person):

    def __init__(self):
        super().__init__()
        print("Child init")

class H(Student, Child):
    def __init__(self):
        """
        Person init
        Child init
        Student init
        从最基类开始, 继承多个类时, 倒序初始化, 从参数右边开始
        """
        super().__init__()
        print("H init")

if __name__ == '__main__':
    # s = Student()
    h = H()

    