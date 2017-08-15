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

    def findSuccessor(self):
        succ = None
        if self.isLeaf():
            return None

        if self.hasRightChild():
            return self.rightChild.findMin()

        if self.parent and self.hasLeftChild():
            return self.parent

    def findMin(sef):
        if self.hasLeftChild():
            return self.leftChild.findMin()

        else:
            return self

    def sliceOut(self):             # the successor node never has a left child.
        if self.parent and self.hasRightChild():
            if self.isLeftChild():
                self.parent.leftChild = self.rightChild

            else:
                self.parent.rightChild = self.rightChild

    def traverse(self):
        # ! in-order traverse prints out an sotred list.
        if self.hasLeftChild():
            self.leftChild.traverse()
        print(self.payload)
        if self.hasRightChild():
            self.rightChild.traverse()


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self):
        if self.root:
            self._put(key, val, self.root)

        else:
            self.root = TreeNode(key, val)

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)

            else:
                currentNode.leftChild = TreeNode(key, val, parent = currentNode)

        else:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent = currentNode)


    def __setitem__(self, k, v):
        self.put(k, v)
