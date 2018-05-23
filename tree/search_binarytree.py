# -*- coding: utf-8 -*-
# author: zhonghua
# filename: search_binarytree.py
# create: 2016/3/29
# version: 1.0

# 二叉树查找
# 1.生成二叉树
# 2.遍历查找

class Node:
    def __init__(self, data, left, right):
        self._data = data
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None

    def make_tree(self, node):
        self._root = node

    def insert(self, node):
        def insert_node(tree_node, node):
            if tree_node._data >= node._data:
                if tree_node._left is None:
                    tree_node._left = node
                else:
                    insert_node(tree_node._left, node)
            else:
                if tree_node._right is None:
                    tree_node._right = node
                else:
                    insert_node(tree_node._right, node)
        insert_node(self._root, node)

    def search(self, data):
        def search_node(tree_node, data):
            if tree_node._data == data:
                print('success.')
                return
            elif tree_node._data >= data:
                if tree_node._left is None:
                    return
                else:
                    search_node(tree_node._left, data)
            else:
                if tree_node._right is None:
                    return
                else:
                    search_node(tree_node._right, data)
        search_node(self._root, data)

    def pre_order(self):
        lst = []
        def order(node):
            lst.append(node._data)
            if node._left is not None:
                order(node._left)
            if node._right is not None:
                order(node._right)
        order(self._root)
        print(lst)

    def in_order(self):
        lst = []
        def order(node):
            if node._left is not None:
                order(node._left)
            lst.append(node._data)
            if node._right is not None:
                order(node._right)
        order(self._root)
        print(lst)

    def post_order(self):
        lst = []
        def order(node):
            if node._left is not None:
                order(node._left)
            if node._right is not None:
                order(node._right)
            lst.append(node._data)
        order(self._root)
        print(lst)

if __name__ == '__main__':
    lst = [12, 9, 7, 19, 3, 8, 52, 106, 70, 29, 20, 16, 8, 50, 22, 19]
    tree = BinaryTree()
    # 生成二叉树
    for (i, j) in enumerate(lst):
        node = Node(j, None, None)
        if i == 0:
            tree.make_tree(node)
        else:
            tree.insert(node)
    # 二叉树查找
    tree.search(70)
    # 二叉树遍历，前序、中序、后序
    tree.pre_order()
    tree.in_order()
    tree.post_order()
