from bPlusTree.bPlusTreeNode import bPlusTreeNode
import math

class bPlusTreeLeafNode(bPlusTreeNode):

    def __init__(self, parent, order, pageMgr):
        bPlusTreeNode.__init__(self, parent, order, pageMgr)
        # Parent class increases node count but this is a leaf
        self.pageMgr.decNodeCount()
        self.pageMgr.incLeafCount()
        self._valueNode = []
        self._neighborPtr = None

    def setNeighbor(self, neighbor):
        self._neighborPtr = neighbor

    def propogateOverflow(self, propKey, childPtr):
        # Helper function for insert()
        self._parent.propogateOverflow(propKey, childPtr)

    def insert(self, record):
        # record should be a (key, rid) pair
        length = len(self._keyNode)
        hasInserted = False

        # First insert the key
        for i in range(0, length):
            if self._keyNode[i] > record.key:
                self._keyNode.insert(i, record.key)
                self._valueNode.insert(i, record.rid)
                hasInserted = True
                break
        if (hasInserted == False):
            self._keyNode.append(record.key)
            self._valueNode.append(record.rid)
            hasInserted = True

        # Check if the node has overflowed
        if length == self._order:
            halfIdx = math.floor(self._order)
            propKey = self._keyNode[halfIdx]
            newLeaf = bPlusTreeLeafNode(self._parent, self._order)
            newLeaf._keyNode = self._keyNode[halfIdx:]
            newLeaf._valueNode = self._valueNode[halfIdx:]
            self._keyNode = self._keyNode[0:halfIdx]
            self._valueNode = self._valueNode[0:halfIdx]
            self._neighborPtr = newLeaf
            # Propogate the overflow to the parent
            self.propogateOverflow(propKey, self)

        # DEBUG Only
        if length > self._order:
            print("Something went wrong.")

    def propogateUnderflow(self):
        # Helper function for delete()
        # TODO

    def delete(self, record):
        # TODO
        # First check if the key exists
        if key in self._keyNode:
            idx = self._keyNode.index(key)
        else:
            print("Attempting to delete record with invalid key.")
            return

        del self._keyNode[idx]
        del self._valueNode[idx]

        # If this is the root node, it's ok
        if self.checkRoot() == True:
            return

        # Check if there are enough elements left
        length = len(self._keyNode)
        if length >= math.floor(self._order/2):
            return
        else:
            # Check if redistribution is possible
            neighborLength = len(self._neighborPtr._keyNode)
            if (neighborLength - 1) >= math.floor(self._order/2):
                redistKey = self._neighborPtr._keyNode.pop(0)
                redistValue = self._neighborPtr._valueNode.pop(0)
                self._keyNode.append(redistKey)
                self._valueNode.append(redistValue)
                # Change parent node's key
                parentPtrIdx = self._parent._ptrNode.index(self)
                self._parent._valueNode[parentPtrIdx] = self._neighborPtr._keyNode[0]
            # Merge if redistribution fails
            else:
                # TODO

    def find(self, key):
        if key in self._keyNode:
            idx = self._keyNode.index(key)
            return self._valueNode[idx]
        else:
            print("Key can not be found in the B+ tree.")
            return

    def range(self, key1, key2, listRid):
        # Returns all key1 <= x < key2
        # Once it reaches the appropriate leaf node scan the neighboring leaf nodes until key > key2

        length = len(self._keyNode)

        for i in range(0, length):
            if self._keyNode[i] >= key1:
                if self._keyNode[i] < key2:
                    listRid.append(self._valueNode[i])
                else:
                    return

        # Keep checking the leaf nodes to the right
        if (self._neighborPtr != None):
            self._neighborPtr.range(key1, key2, listRid)