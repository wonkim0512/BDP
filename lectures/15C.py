class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent

    def hasleftchild(self):
        return self.leftchild is not None

    def hasrightchild(self):
        return self.rightchild is not None

    def isleftchild(self):
        return self.parent and self.parent.leftchild is self

    def isrightchild(self):
        return self.parent and self.parent.rightchild is self

    def isroot(self):
        return not self.parent

    def isleaf(self):
        return not (self.leftchild or self.rightchild)
        #return not (self.hasleftchild() or self.hasrightchild())

    def hasanychildren(self):
        return not self.isleaf()

    def hasbothchildren(self):
        return self.hasleftchild() and self.hasrightchild()

    def replacenodedata(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.leftchild = lc
        self.rightchild = rc
        if self.hasleftchild():
            self.leftchild.parent = self

        if self.hasrightchild():
            self.rightchild.parent = self

    def findsuccessor(self):
        succ = None
        if self.isleaf():
            return None

        if self.hasrightchild():
            return self.rightchild.findmin()

        if self.parent and self.isleftchild:
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

    def traverse(self):
        if self.hasleftchild():
            return self.leftchild.traverse()

        print(self.payload)

        if self.hasrightchild():
            return self.rightchild.traverse()

class BST:
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

        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasleftchild():
                self._put(key, val, currentNode.leftchild)

            else:
                currentNode.leftchild = TreeNode(key, val, parent = currentNode)

        else:
            if currentNode.hasrightchild():
                self._put(key, val, currentNode.rightchild)

            else:
                currentNode.rightchild = TreeNode(key, val, parent = currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def _get(self, key, currentNode):
        if not currentNode:
            return None

        elif currentNode.key == key:
            return currentNode

        elif currentNode.key > key:
            return self._get(key, currentNode.leftchild)

        else:
            return self._get(key, currentNode.rightchild)


    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True

        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0

        else:
            raise KeyError

        def __delitem__(self, key):
            self.delete(key)

        def remove(self, currentNode):
            if currentNode.isleaf():
                if currentNode.isleftchild():
                    currentNode.parent.leftchild = None

                else:
                    currentNode.parent.right = None

            elif currentNode.hasbothchildren():
                succ = currentNode.findsuccessor()
                succ.sliceout()
                currentNode.key = succ.key
                currentNode.payload = succ.payload

            elif currentNode.hasleftchild():
                if currentNode.isleftchild():
                    currentNode.parent.leftchild = currentNode.leftchild
                else:
                    currentNode.parent.leftchild = currentNode.leftchild

            else:
                if currentNode.isleftchild():
                    currentNode.parent.rightchild = currentNode.rightchild
                else:
                    currentNode.parent.rightchild = currentNode.rightchild

def main():
    b = BST()
    ad = (17, 5, 25, 2, 11, 29, 38, 9, 16, 7, 8)
    for i in ad:
        b.put(i, i)
    b.root.traverse()
    print('remove 5')
    b.delete(5)
    b.root.traverse()
    print("put 39")
    b.put(39, 39)
    b.root.traverse()

if __name__ == "__main__":
    main()
