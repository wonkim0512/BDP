class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild is not None

    def hasRightChild(self):
        return self.rightChild is not None

    def isLeftChild(self):
        return self.parent and self.parent.leftChild is self

    def isRightChild(self):
        return self.parent and self.parent.rightChild is self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return not self.isLeaf()

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

<<<<<<< HEAD
    def findsuccessor(self):
        if self.isLeaf():
            return None

        if self.hasrightchild():
            return slef.rightchild.findmin()

        if self.parent and self.hasleftchild():
            return self.parent
=======

>>>>>>> ecb4187e0d5c15e2e79dfcdac8b86b83fcc85e3a



class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                currentNode.leftChild._put(self, key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent = currentNode)

        else:
            if currentNode.hasRightChild():
                currentNode.rightChild._put(self, key, val, currentNode.rightChild)
            else:
                current.rightChild = TreeNode(key, value, parent = currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload

            else:
                return None

        return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None

        elif currentNode.key == key:
            return currentNode

        elif currentNode.key < key:
            return self._get(key, currentNode.leftChild)

        else:
            return self._gey(key, currentNode.rightChild)

    


<<<<<<< HEAD

    def remove(self, currentNode):
        if currentNode.isLeaf:
            if currentNode.isleftchild():
                self.parent.leftchild = None

            else:
                self.parent.rightchild = None

        elif currentNode.hasbothchildren():
            succ = currentNode.findsuccessor()
            succ.sliceout()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        elif currentNode.hasleftchild():
            if currentNode.isleftchild():
                currentNode.parent.leftchild = currentNode.leftchild
            if currentNode.isrightchild():
                currentNode.parent.rightchild =currentNode.leftchild

        else:
            if currentNode.isleftchild():
                currentNode.parent.leftchild = currentNode.rightchild
            if currentNode.isrightchild():
                currentNode.parent.rightchild = currentNode.rightchild
=======
>>>>>>> ecb4187e0d5c15e2e79dfcdac8b86b83fcc85e3a


def main():
    b = BinarySearchTree()
    ad = (17, 5, 25, 2, 11, 29, 38, 9, 16, 7, 8)
    for i in ad:
        b.put(i, i)
    b.root.traverse()
    print('remove 5')
    b.delete(5)
    b.root.traverse()

if __name__ == "__main__":
    main()
