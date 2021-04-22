


class Node():

    def __init__(self, some_number: int):
        self.node_data = some_number

    def sum_node_data(self):
        raise NotImplementedError("Must implement abstract method")

    def __str__(self):
        return str(self.node_data)


class Leaf(Node):

    def __init__(self, node_data):
        self.node_data = node_data

    def sum_node_data(self):
        return self.data

    def __str__(self):
        return str(self.node_data)


class Internal(Node):

    def __init__(self, node_data: int, left: Node, right: Node):
        self.node_data = node_data
        self.left_node = left
        self.right_node = right

    def sum_node_data(self):
        if isinstance(self, Leaf) or (self.left_node == None and self.right_node == None):
            return self.node_data
        else:
            leftData = Internal.sum_node_data(self.left_node)
            rightData = Internal.sum_node_data(self.right_node)
            total = leftData + rightData + self.node_data
            return total

    def __str__(self):
        if isinstance(self, Leaf) or (self.left_node == None and self.right_node == None):
            return self.node_data
        else:
            leftData = Internal.__str__(self.left_node)
            rightData = Internal.__str__(self.right_node)
            string_to_return = "<" + str(self.node_data) + ", " + str(leftData) + ", " + str(rightData) + " >"
            return string_to_return


def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    l4 = Leaf(20)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    a_bigger_root = Internal(15, i, root)
    print(root.sum_node_data())
    print(l1)
    print(root)
    print(a_bigger_root)
    print(a_bigger_root.sum_node_data())


if __name__ == '__main__':
    main()
