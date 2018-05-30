class Node(object):
    def __init__(self, weight: int, left, right):
        self.weight = weight
        self.left = left
        self.right = right

    def __str__(self):
        return self.weight

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

    def print_infix(self) -> [int]:
        return (self.left.print_infix() if self.left else []) + [self.weight] + (self.right.print_infix() if self.right else [])

    def print_prefix(self) -> [int]:
        return [self.weight] + (self.left.print_prefix() if self.left else []) + (self.right.print_prefix() if self.right else [])

    def print_postfix(self) -> [int]:
        return (self.left.print_postfix() if self.left else []) + (self.right.print_postfix() if self.right else []) + [self.weight]


# Main
values = [21, 9, 12, 34, 36, 35, 5, 8, 1, 25]
root = Node(values[0], None, None)

for value in values[1:]:
    root.insert(value)

print("values:  " + str(values))
print("infix:   " + str(root.print_infix()))
print("prefix:  " + str(root.print_prefix()))
print("postfix: " + str(root.print_postfix()))
