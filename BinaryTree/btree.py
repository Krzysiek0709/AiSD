from typing import Any, Callable


class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None

    def PrintTree(self):
        if self.left_child:
            self.left_child.PrintTree()
        print(self.value)
        if self.right_child:
            self.right_child.PrintTree()


    def is_leaf(self):
        return self.left_child == None and self.right_child == None


    def add_left_child(self,value:Any):
        if self.left_child is None:
            self.left_child = BinaryNode(value)
        else:
            self.left_child.add_left_child(value)


    def add_right_child(self,value:Any):
        if self.right_child is None:
            self.right_child = BinaryNode(value)
        else:
            self.right_child.add_right_child(value)


root = BinaryNode(20)
root.add_left_child(5)
root.add_right_child(6)
root.add_left_child(4)
root.add_left_child(15)
root.PrintTree()
