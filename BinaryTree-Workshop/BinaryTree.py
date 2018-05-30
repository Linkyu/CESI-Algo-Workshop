class Node(object):
    def __init__(self, weight: int, left, right):
        self.weight = weight
        self.left = left
        self.right = right

    def insert(self, i):
        if i < self.weight:
            if self.left:
                self.left.insert(i)
            else:
                self.left = Node(i, None, None)
        elif i > self.weight:
            if self.right:
                self.right.insert(i)
            else:
                self.right = Node(i, None, None)
