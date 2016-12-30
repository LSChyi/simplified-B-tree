class bPlusTreeNode():

    def __init__(self, order):
        # Using Wikipedia's definition of order, so node must have at least order/2 keys
        self._order = order
        self._isRoot = false
        self._keyNode = [None] * order
        self._ptrNode = [None] * (order + 1)

    def setRoot(self):
        self._isRoot = true

    def insert(self, record):
        # TODO
        # record should be a (key, rid) pair

    def delete(self, record):
        # TODO

    def find(self, key1):
        # TODO

    def range(self, key1, key2, listRid):
        # TODO
        # Find smallest unit > key1 then use _neighborPtr in the leaf node until key > key2 is reached

class bPlusTreeLeafNode(bPlusTreeNode):

    def __init__(self, order):
        bPlusTreeNode.__init__(self, order)
        self._valueNode = [None] * order
        self._neighborPtr = None

    def setNeighbor(neighbor):
        self._neighborPtr = neighbor

    def range(self, key1, key2, listRid):
        # TODO
        # Once it reaches the appropriate leaf node scan the neighboring leaf nodes until key > key2

class bPlusTree():

    def __init__(self, order):
        self._root = bPlusTreeNode(order)
        self._order = order

    def insert(self, record):
        _root.insert(record)

    def delete(self, record):
        _root.delete(record)

    def find(self, key1):
        _root.find(key1)

    def range(self, key1, key2, listRid):
        _root.range(key1, key2, listRid)
