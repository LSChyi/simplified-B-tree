class LeafPage:
    def __init__(self, order):
        self.order = order
        self.nodes = []
        self.ptrs = [ None, None ]
        self.parent = None

    def search(self, key):
        for node in self.nodes:
            if node.value == key:
                return node
        else:
            return None

    def insert(self, record):
        self.nodes.append(record)
        self.nodes.sort(key=lambda x: x.value)
        if len(self.nodes) <= self.order * 2: # page not full, do simple insert
            print(self)
            return None
        else: # page is full, should split. copy up middle value
            halfIdx = len(self.nodes)//2
            copyUpValue = self.nodes[halfIdx].value
            newLeafPage = LeafPage(self.order)
            newLeafPage.nodes = self.nodes[halfIdx:]
            self.nodes = self.nodes[:halfIdx]
            self.ptrs[1], newLeafPage.ptrs[1], newLeafPage.ptrs[0] = newLeafPage, self.ptrs[1], self
            if newLeafPage.ptrs[1] is not None:
                newLeafPage.ptrs[1].ptrs[0] = newLeafPage
            newLeafPage.parent = self.parent
            print("ori: {}, new: {}".format(self, newLeafPage))
            return copyUpValue, self, newLeafPage

    def delete(self, key):
        for idx, node in enumerate(self.nodes):
            if node.value == key:
                deletedNode = self.nodes.pop(idx)
                if self.isRoot(): # if the page is root, simply delete the node
                    return "OK", deletedNode
                else:
                    if len(self.nodes) < self.order: # violate b+ tree constraint, need redistribution
                        if self.ptrs[0] is not None: # try to borrow from left sibling
                            if self.ptrs[0].canBeBorrowed(self):
                                borrowedNode = self.ptrs[0].nodes.pop(-1)
                                self.nodes.insert(0, borrowedNode)
                                return "borrow", "left", borrowedNode.value, deletedNode
                        if self.ptrs[1] is not None: # try to borrow from right sibling
                            if self.ptrs[1].canBeBorrowed(self):
                                borrowedNode = self.ptrs[1].nodes.pop(0)
                                self.nodes.append(borrowedNode)
                                return "borrow", "right", self.ptrs[1].nodes[0].value, deletedNode

                        # no extra nodes can be borrowed, merge with sibling
                        if self.ptrs[0] is not None: # try to merge with left sibling
                            if self.parent == self.ptrs[0].parent:
                                # TODO, merge with left page
                                pass
                        if self.ptrs[1] is not None:
                            if self.parent == self.ptrs[1].parent:
                                # TODO, merge with right page
                                pass
                    else: # the page node is enough, simply delete the node
                        return "OK", deletedNode
        else:
            return "OK", None # no such key

    def rangeQuery(self, rangeStart, rangeStop):
        pass

    def isRoot(self):
        return True if self.parent is None else False

    def canBeBorrowed(self, borrower):
        if (self.parent is not borrower.parent) or (len(self.nodes) <= self.order):
            return False
        else:
            return True

    def __str__(self):
        contentStr = "["
        for node in self.nodes:
            contentStr += node.__str__() + " "
        contentStr += "]"
        return contentStr
