

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
    
    
    