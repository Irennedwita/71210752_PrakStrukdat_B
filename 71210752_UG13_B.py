class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, self)
            else:
                self.right.insert(data)
        else:
            return False
        return True

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

class BinaryTree:
    def __init__(self):
        self._root = Node(0,None)

    def add(self, data):
        if self._root.left is None and data % 2 != 0:
            self._root.left = Node(data,self._root)
        elif self._root.right is None and data % 2 == 0:
            self._root.right = Node(data,self._root)
        else:
            if data % 2 != 0:
                self._root.left.insert(data)
            else:
                self._root.right.insert(data)
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.getLeft())
            print(node.getData(), end= ' ')
            self.inorder(node.getRight())

    def nodes(self):
        print("Order Tree :")
        self.inorder(self._root)

Btree = BinaryTree()
Btree.add(5)
Btree.add(4)
Btree.add(3)
Btree.add(9)
Btree.add(8)
Btree.add(6)
Btree.add(7)
Btree.add(11)
Btree.add(10)
Btree.nodes()