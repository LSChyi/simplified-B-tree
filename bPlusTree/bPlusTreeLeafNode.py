from bPlusTree.bPlusTreeNode import bPlusTreeNode

class bPlusTreeLeafNode(bPlusTreeNode):

    def __init__(self, parent, order):
        bPlusTreeNode.__init__(self, order)
        self._valueNode = []
        self._neighborPtr = None

    def setNeighbor(self, neighbor):
        self._neighborPtr = neighbor

    def propogateOverflow(self, propKey, childPtr):
        # If this was originally a root node, create the parent node first
        if self.checkRoot == True:
            newNode = bPlusTreeNode(None, self._order)
            self._parent = newNode

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


    def delete(self, record):
        # TODO

    def find(self, key):
        if key in self._keyNode:
            idx =  self._keyNode.index(key)
            return self._valueNode[idx]
        else:
            print("Key can not be found in the B+ tree.")
            return

    def range(self, key1, key2, listRid):
        # TODO
        # Once it reaches the appropriate leaf node scan the neighboring leaf nodes until key > key2