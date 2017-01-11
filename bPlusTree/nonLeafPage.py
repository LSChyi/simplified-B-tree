class NonLeafPage():
    def __init__(self, order):
        self.order = order
        self.nodes = []
        self.ptrs = []
        self.parent = None

    def search(self, key):
        targetIdx = self.nextTraverseIdx(key)
        targetPage = self.ptrs[targetIdx]
        return targetPage.search(key)

    def insert(self, record):
        for idx, value in enumerate(self.nodes):
            if record.value < value:
                targetIdx = idx
                break
        else:
            targetIdx = len(self.nodes)

        targetPage = self.ptrs[targetIdx]
        result = targetPage.insert(record)
        if result is not None: # insert is not simple case
            self.nodes.insert(targetIdx, result[0])
            self.ptrs.insert(targetIdx+1, result[2])
            if len(self.nodes) <= self.order * 2: # the page is not full, simple insert case
                print("nonLeafPgae: {}".format(self.nodes))
                return None
            else: # the page overflow, push the middle value
                halfIdx = len(self.nodes)//2
                pushUpValue = self.nodes[halfIdx]
                newNonLeafPage = NonLeafPage(self.order)
                newNonLeafPage.nodes = self.nodes[halfIdx+1:]
                newNonLeafPage.ptrs = self.ptrs[halfIdx+1:]
                self.nodes = self.nodes[:halfIdx]
                self.ptrs = self.ptrs[:halfIdx+1]
                for page in newNonLeafPage.ptrs:
                    page.parent = newNonLeafPage
                print("nonleaf page, ori: {}, new: {}".format(self.nodes, newNonLeafPage))
                return pushUpValue, self, newNonLeafPage

    def delete(self, key):
        targetIdx = self.nextTraverseIdx(key)
        targetPage = self.ptrs[targetIdx]
        result = targetPage.delete(key)
        if result is not None:
            if result is False:
                return False
            elif result[0] == "borrow":
                if result[1] == "left": # the page borrowed from left page
                    self.nodes[targetIdx-1] = result[2]
                else: # the page borrowed from right page
                    self.nodes[targetIdx] = result[2]
                return None
            else: # merge
                # TODO
                pass

    def rangeQuery(self, rangeStart, rangeStop):
        pass

    def isRoot(self):
        return True if self.parent is None else False

    def nextTraverseIdx(self, key):
        for idx, value in enumerate(self.nodes):
            if key < value:
                return idx
        else:
            return len(self.nodes)

    def __str__(self):
        return "{}".format(self.nodes)
