
class CustomStr(str):

    def __init__(self, string):
        self.string = string
    
if __name__ == '__main__':
    a = CustomStr('1213')
    print(type(a))