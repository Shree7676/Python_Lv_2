"""
Shivam just completed his binary search tree and now he wants to add few additional methods
like in_order_traversal(), post_order_traversal(), min(), max() and getLevel(). 
Help Shivam in adding all these methods for binary search tree.

Inorder Traversal: 10 20 30 100 150 200 300
Preorder Traversal: 100 20 10 30 200 150 300
Postorder Traversal: 10 30 20 150 300 200 100

          100
    20         200
10      30  150     300


"""
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def preorder_traversal(self):
        elements=[]
        elements.append(self.data)

        if self.left:
            elements+=self.left.preorder_traversal()

        if self.right:
            elements+=self.right.preorder_traversal()

        return elements

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def postorder_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.postorder_traversal()
        if self.right:
            elements+=self.right.postorder_traversal()
        elements.append(self.data)
        return elements

    def min_value(self):
        list=self.in_order_traversal()
        return list[0]

    def max_value(self):
        list=self.in_order_traversal()
        return list[-1]

    # Function to calculate the minimum depth of the tree Pending

def build_tree(elements):
    print("Building tree with these elements:",elements)
    self = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
         self.add_child(elements[i])

    return  self

if __name__ == '__main__':

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("preorder_traversal gives this sorted list:",numbers_tree.preorder_traversal())
    print("postorder_traversal gives this sorted list:",numbers_tree.postorder_traversal())
    print("Min value:",numbers_tree.min_value())
    print("Max value:",numbers_tree.max_value())
    numbers_tree2 = build_tree([100, 20, 10, 30, 200, 150, 300])
    print("In order traversal gives this sorted list:",numbers_tree2.in_order_traversal())
    print("preorder_traversal gives this sorted list:",numbers_tree2.preorder_traversal())
    print("postorder_traversal gives this sorted list:",numbers_tree2.postorder_traversal())
    print("Min value:",numbers_tree2.min_value())
    print("Max value:",numbers_tree2.max_value())
"""
                     17
            4                20
        1       9       18           23
                                            34
io>> 1  4   9   17  18  20  23  34
Pre> 17 4   1   9   20  18  23  34
post 1  9   4   18  34  23  20  17   
"""