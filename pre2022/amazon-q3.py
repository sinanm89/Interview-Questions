# given a binary tree (unordered list)
# find least common ancestor of n1, n2 where n1, n2 can be any value of a node
# (find common father furthest away from the root)

# find 2 values n1, n2 by traversing left and right. store values in hash dict
# when both values are found

N1 = 4
N2 = 6


class Node:

    left = None
    right = None
    data = None
    root = None

    root = None
    n1, n2 = N1, N2

    def __init__(self, *args, **kwargs):
        self.left = kwargs.get("left")
        self.right = kwargs.get("right")
        self.data = kwargs.get("data")
        self.root = kwargs.get("root")

    def __repr__(self):
        return "<Node {0} || {1} , {2}>".format(
            self.data,
            self.left.data if self.left else None,
            self.right.data if self.right else None
        )

    def found_values(self, distance_to_root):
        if self.root is None:
            return distance_to_root
        return self.root.found_values(distance_to_root + 1)

    def find_values(self):
        out = 0
        if self.left is not None:
            self.left.root = self
            out += self.left.find_values()
        if self.right is not None:
            self.right.root = self
            out += self.right.find_values()

        if self.data == N1:
            out += self.found_values(0)
        elif self.data == N2:
            out += self.found_values(0)
        return out

#        1
#   2    |      3
# 4 | 5  |  6   |  7
#           | 8

r = Node(
    data=1,
    left=Node(data=2, left=Node(data=4), right=Node(data=5)),
    right=Node(
        data=3,
        left=Node(data=6, right=Node(data=8)),
        right=Node(data=7))
)
out = r.find_values()
print(out)
