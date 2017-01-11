#from bPlusTree.leafPage import LeafPage
#from bPlusTree.nonLeafPage import NonLeafPage
from leafPage import LeafPage
from nonLeafPage import NonLeafPage
from leafNode import LeafNode

class bPlusTree:
    def __init__(self, keyType):
        self.keyType = keyType
        self.order =  2 # TODO, calculate real order depends on the keyType
        self.root = LeafPage(self.order)

    def search(self, key):
        pass

    def insert(self, record):
        result = self.root.insert(record)
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
    testTree.insert(LeafNode(7, 0, 1))
    testTree.insert(LeafNode(6, 0, 2))
    testTree.insert(LeafNode(8, 0, 3))
    testTree.insert(LeafNode(9, 0, 4))
    testTree.insert(LeafNode(10, 0, 5))
    testTree.insert(LeafNode(11, 0, 6))
    testTree.insert(LeafNode(20, 0, 7))
    testTree.insert(LeafNode(21, 0, 8))
    testTree.insert(LeafNode(22, 0, 9))
    testTree.insert(LeafNode(23, 0, 10))
    testTree.insert(LeafNode(13, 0, 11))
    testTree.insert(LeafNode(14, 0, 12))
    testTree.insert(LeafNode(15, 0, 13))
    testTree.insert(LeafNode(1, 0, 14))
    testTree.insert(LeafNode(2, 0, 15))
    testTree.insert(LeafNode(3, 0, 16))
