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
        if result[0] is not "OK":
            if result[0] == "borrow":
                if result[1] == "left": # the page borrowed from left page
                    self.nodes[targetIdx-1] = result[2]
                else: # the page borrowed from right page
                    self.nodes[targetIdx] = result[2]
                return "OK", result[3]
            else: # result[0] == merge
                if result[1] == "left": # the page is merged with its left sibling
                    self.nodes.pop(targetIdx-1)
                else: # the page is merged with its right wibling
                    self.nodes.pop(targetIdx)
                self.ptrs.pop(targetIdx)
                if self.isRoot(): # root page has no size contraint, but need to check whether size == 0
                    if self.nodes: # node size == 0
                        # TODO
                        pass
                    else:
                        return "OK", result[2]
                else:
                    if len(self.nodes) < self.order:
                        pass
                    else:
                        return "OK", result[2]
        else:
            return result

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
