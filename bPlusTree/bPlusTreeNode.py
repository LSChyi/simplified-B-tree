import math

class bPlusTreeNode():

    def __init__(self, parent, order):
        # Using Wikipedia's definition of order, so node must have at least order/2 keys
        self._order = order
        self._parent = parent
        self._keyNode = []
        self._ptrNode = []

    def checkRoot(self):
        if self._parent == None:
            return True
        else:
            return False

    def propogateOverflow(self, propKey, childPtr):
        # If this was originally a root node, create the parent node first
        if self.checkRoot == True:
            newNode = bPlusTreeNode(None, self._order)
            self._parent = newNode

        length = len(self._keyNode)
        hasInserted = False

        # First insert the key
        for i in range(0, length):
            if self._keyNode[i] > record.key:
                self._keyNode.insert(i, propKey)
                self._ptrNode.insert(i+1, childPtr)
                hasInserted = True
                break
        if (hasInserted == False):
            self._keyNode.append(propKey)
            self._valueNode.append(childPtr)
            hasInserted = True

        # Check if the node has overflowed
        if length == self._order:
            halfIdx = math.floor(self._order)
            propKey = self._keyNode[halfIdx]
            newNode = bPlusTreeNode(self._parent, self._order)
            # No copy up
            newLeaf._keyNode = self._keyNode[halfIdx+1:]
            newLeaf._ptrNode = self._valueNode[halfIdx+1:]
            self._keyNode = self._keyNode[0:halfIdx]
            self._ptrNode = self._valueNode[0:halfIdx]
            # Propogate the overflow to the parent
            self.propogateOverflow(propKey, self)

    def insert(self, record):
        # Find the next node to trasverse
        # record should be a (key, rid) pair
        length = len(self._keyNode)
        hasFoundPtr = False

        for i in range(0, length):
            if self._keyNode[i] > record.key:
                self._ptrNode[i].insert(record)
                hasFoundPtr = True
                break

        if hasFoundPtr == False:
            self._ptrNode[length].insert(record)
            hasFoundPtr = True

    def delete(self, record):
        # TODO

    def find(self, key):
        # Find the next node to trasverse
        length = len(self._keyNode)
        hasFoundPtr = False

        for i in range(0, length):
            if self._keyNode[i] > key:
                self._ptrNode[i].find(key)
                hasFoundPtr = True
                break

        if hasFoundPtr == False:
            self._ptrNode[length].find(key)
            hasFoundPtr = True

    def range(self, key1, key2, listRid):
        # TODO
        # Find smallest unit > key1 then use _neighborPtr in the leaf node until key > key2 is reached