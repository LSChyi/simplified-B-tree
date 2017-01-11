class LeafPage:
    def __init__(self, order):
        self.order = order
        self.nodes = []
        self.ptrs = [ None, None ]
        self.parent = None

    def search(self, key):
        pass

    def insert(self, key):
        self.nodes.append(key)
        self.nodes.sort()
        if len(self.nodes) <= self.order * 2: # page not full, do simple insert
            #print(self)
            return None
        else: # page is full, should split. copy up middle value
            halfIdx = len(self.nodes)//2
            copyUpValue = self.nodes[halfIdx]
            newLeafPage = LeafPage(self.order)
            newLeafPage.nodes = self.nodes[halfIdx:]
            self.nodes = self.nodes[:halfIdx]
            self.ptrs[1] = newLeafPage
            newLeafPage.ptrs[0] = self
            newLeafPage.parent = self.parent
            #print("ori: {}, new: {}".format(self, newLeafPage))
            return copyUpValue, self, newLeafPage

    def delete(self, key):
        pass

    def rangeQuery(self, rangeStart, rangeStop):
        pass

    def isRoot(self):
        return True if self.parent is None else False

    def __str__(self):
        return "{}".format(self.nodes)
