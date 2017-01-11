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
        return self.root.search(key)

    def insert(self, record):
        result = self.root.insert(record)
        if result is not None: # insert is not simple case
            self.root = NonLeafPage(self.order)
            self.root.nodes.append(result[0])
            self.root.ptrs.append(result[1])
            self.root.ptrs.append(result[2])
            for page in self.root.ptrs:
                page.parent = self.root
            print("root split, root: {}, left: {}, right: {}".format(self.root, self.root.ptrs[0], self.root.ptrs[1]))

    def delete(self, key):
        result = self.root.delete(key)
        if result is not None:
            if result is False: # no such key
                return False
            else: # need merge
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

    result = testTree.search(9)
    print("result of find 9: {}".format(result))
    result = testTree.search(100)
    print("result of find 100: {}\n".format(result))

    print("test simple delete case")
    print(testTree.root.ptrs[1].ptrs[2])
    testTree.delete(22)
    print(testTree.root.ptrs[1].ptrs[2])
    print("")

    print("test delete with borrow from left case")
    print("nonLeafNode: {}".format(testTree.root.ptrs[0]))
    print("relevant leaf pages: {} {}".format(testTree.root.ptrs[0].ptrs[1], testTree.root.ptrs[0].ptrs[2]))
    testTree.delete(8)
    print("nonLeafNode: {}".format(testTree.root.ptrs[0]))
    print("relevant leaf pages: {} {}".format(testTree.root.ptrs[0].ptrs[1], testTree.root.ptrs[0].ptrs[2]))
    print("")

    testTree.insert(LeafNode(4, 0, 17))
    print("test delete with borrow from right case")
    print("nonLeafNode: {}".format(testTree.root.ptrs[0]))
    print("relevant leaf pages: {} {}".format(testTree.root.ptrs[0].ptrs[0], testTree.root.ptrs[0].ptrs[1]))
    testTree.delete(2)
    print("nonLeafNode: {}".format(testTree.root.ptrs[0]))
    print("relevant leaf pages: {} {}".format(testTree.root.ptrs[0].ptrs[0], testTree.root.ptrs[0].ptrs[1]))
    print("")
