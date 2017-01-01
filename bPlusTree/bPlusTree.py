from bPlusTree.bPlusTreeNode import bPlusTreeNode
from bPlusTree.bPlusTreeLeafNode import bPlusTreeLeafNode
from bPlusTree.pageMgr import pageMgr

class bPlusTree():

    def __init__(self, order):
        self.pageMgr = pageMgr()
        self._root = bPlusTreeLeafNode(None, order)
        self._order = order

    def insert(self, record):
        _root.insert(record)

    def delete(self, record):
        _root.delete(record)

    def find(self, key1):
        _root.find(key1)

    def range(self, key1, key2, listRid):
        _root.range(key1, key2, listRid)
