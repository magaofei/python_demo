"""
递归打印每个文件
"""

import os

PATH = '/Users/mark/GitHub/python_demo'
def find_walk():
    for root, dirs, files in os.walk(PATH):
        for file in files:
            print(os.path.join(root, file))
            # pass

def find(file_path):
    """
    递归便利
    """
    files = os.listdir(file_path)
    for file in files:
        file_d = os.path.join(file_path, file)
        # 是目录 继续递归
        if os.path.isdir(file_d):
            find(file_d)
        else:
            print(file_d)

if __name__ == '__main__':
    # find(PATH)
    find_walk()