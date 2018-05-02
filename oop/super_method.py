

class Person(object):
    def __init__(self):
        print("Person init")


class Student(Person):

    def __init__(self):
        super().__init__()
        print("Student init")


if __name__ == '__main__':
    s = Student()
    