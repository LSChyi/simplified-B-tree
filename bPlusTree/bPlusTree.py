#from bPlusTree.leafPage import LeafPage
#from bPlusTree.nonLeafPage import NonLeafPage
from leafPage import LeafPage
from nonLeafPage import NonLeafPage

class bPlusTree:
    def __init__(self, keyType):
        self.keyType = keyType
        self.order =  2 # TODO, calculate real order depends on the keyType
        self.root = LeafPage(self.order)

    def search(self, key):
        pass

    def insert(self, key):
        result = self.root.insert(key)
        if result is not None: # insert is not simple case
            self.root = NonLeafPage(self.order)
            self.root.nodes.append(result[0])
            self.root.ptrs.append(result[1])
            self.root.ptrs.append(result[2])
            for page in self.root.ptrs:
                page.parent = self.root
            #print("root split, root: {}, left: {}, right: {}".format(self.root, self.root.ptrs[0], self.root.ptrs[1]))

    def delete(self, key):
        pass

    def rangeQuery(self, rangeStart, rangeStop):
        pass

if __name__ == "__main__":
    testTree = bPlusTree("integer")
    testTree.insert(6)
    testTree.insert(7)
    testTree.insert(8)
    testTree.insert(9)
    testTree.insert(10)
    testTree.insert(11)
    testTree.insert(20)
    testTree.insert(21)
    testTree.insert(22)
    testTree.insert(13)
    testTree.insert(14)
    testTree.insert(15)
    testTree.insert(1)
    testTree.insert(2)
    testTree.insert(3)
