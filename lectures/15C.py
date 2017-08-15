class TreeNode(object):
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.val = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent

    def hasleftchild(self):
        return self.leftchild

    def hasrightchild(self):
        return self.rightchild

    def isleftchild(self):
        return self.parent and self.parent.leftchild == self

    def isrightchild(self):
        return self.parent and self.parent.rightchild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightchild or self.leftchild)

    def hasanychildren(self):
        return not self.leaf()

    def hasbothchildren(self):
        return self.hasrightchild() and self.hasleftchild()

    def findsuccessor(self):
        if self.isLeaf():
            return None

        if self.hasrightchild():
            return slef.rightchild.findmin()

        if self.parent and self.hasleftchild():
            return self.parent

    def findmin(self):
        if self.hasleftchild():
            return self.leftchild.findmin()
        else:
            return self

    def sliceout(self):
        if self.parent and self.hasrightchild():
            if self.isleftchild():
                self.parent.leftchild = self.rightchild
            else:
                self.parent.rightchild = self.rightchild

    def inorder_traverse(self):
        if self.hasleftchild():
            self.leftchild.inorder_traverse()
        print(self.val)
        if self.hasrightchild():
            self.rightchild.inorder_traverse()

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)

        else:
            self.root = TreeNode(key, val)
            self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasleftchild():
                self._put(key, val, currentNode.leftchild)
            else:
                currentNode.leftchild = TreeNode(key, val, parent = currentNode)

        elif key > currentNode.key:
            if currentNode.hasrightchild():
                self._put(key, val, currentNode.rightchild)
            else:
                currentNode.rightchild = TreeNode(key, val, parent = currentNode)

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

        elif currentNode.key > key:
            return self._get(key, currentNode.leftchild)

        else:
            return self._get(key, currentNode.rightchild)

    def __setitem__(self, k, v):
        self.put(k, v)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodetoremove = self._get(key, self.root)
            if nodetoremove:
                self.remove(nodetoremove)
                self.size -= 1
            else:
                raise KeyError("Key is not in tree!")

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0

        else:
            raise KeyError("Key is not in tree!")


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


def main():
    bst = BinarySearchTree()
    input_data = (17,5,25,2,11,29,38,9,16,7,8)
    for i in input_data:
        bst.put(i, i)

    bst.root.inorder_traverse()
    print('remove 5')
    bst.delete(5)
    bst.root.inorder_traverse()
    print('put 39')
    bst.put(39, 39)
    bst.root.inorder_traverse()

main()
