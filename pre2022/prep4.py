from __future__ import annotations  # UGLY ASS MFKR


class Node:
    def __init__(self, key: int, left: Node = None, right: Node = None, parent: Node = None):
        self.left = left
        self.right = right
        self.parent = parent
        self.max_depth = 0 if parent is None, else parent.max_depth + 1
        self.val = key

    def __repr__(self):
        return f"<Node {self.val}>"

    def insert(self, key):
        if key > self.val:
            if self.right is None:
                self.right = Node(key)
            else:

                self.right.insert(key)
        elif key < self.val:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)


    def print_traversal(self, order=''):
        if self.left is not None:
            self.left.print_tree()
        print(self)
        if self.right is not None:
            self.right.print_tree()

    def search(self, key):
        if key == self.val:
            return self
        elif key > self.val:
            if self.right is None:
                return 'Not Found'
            return self.right.search(key)
        elif key < self.val:
            if self.left is None:
                return 'Not Found'
            return self.left.search(key)
        else:
            return 'Not Found'


    def max_depth_tree(self):

        left_depth = 0
        right_depth = 0

        if self.right is None and self.left is None:
            return 1
        if self.left is not None:
            left_depth = self.left.max_depth_tree()
        elif self.right is not None:
            righ_tdepth = self.right.max_depth_tree()

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1


    def find_node(self, k):
        if self.val > k:
            if self.right:
            else:
                return 0
        elif self.val < k:
        elif self.val == k:

        return node

ee = Node(8)

ee.insert(1)
ee.insert(3)
ee.insert(6)
ee.insert(4)
ee.insert(7)
ee.insert(13)
ee.insert(14)
ee.insert(10)
print('max depth')
print(ee.max_depth_tree())
import ipdb; ipdb.set_trace()
