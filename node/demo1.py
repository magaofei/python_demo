class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value
        self.left = left    # Left child
        self.right = right  # Right child


    def create_tree(self, node):
        data = raw_input('->')
        
    
    def pre_order(self, node):
        """  根 左 右  """
        if node is not None:
            print(node.value)
            pre_order(self.left)
            pre_order(self.right)


    def mid_order(self):
        """  左 根 右  """
        print(self.value)

    def back_order(self):
        """ 左 右 根  """
        print(self.value)


if __name__ == '__main__':
    n = Node()