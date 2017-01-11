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
            elif result[0] == "merge":
                if result[1] == "left": # the page is merged with its left sibling
                    self.nodes.pop(targetIdx-1)
                else: # the page is merged with its right sibling
                    self.nodes.pop(targetIdx)
                self.ptrs.pop(targetIdx)
                if self.isRoot(): # root page has no size contraint, but need to check whether size == 0
                    if self.nodes: # node size == 0
                        return "OK", result[2]
                    else:
                        self.ptrs[0].parent = None
                        return "change root", self.ptrs[0], result[2]
                else:
                    if len(self.nodes) < self.order:
                        return "nonLeafNode insufficient", result[2]
                    else:
                        return "OK", result[2]
            else: # result[0] == "nonLeafNode insufficient"
                leftNonLeafPageIdx = targetIdx - 1
                rightNonLeafPageIdx = targetIdx + 1
                if leftNonLeafPageIdx >= 0: # check left non leaf page exist, if exist, try to borrow from it
                    if len(self.ptrs[leftNonLeafPageIdx].nodes) > self.order:
                        leftNonLeafPage = self.ptrs[leftNonLeafPageIdx] 
                        targetPage.nodes.insert(0, self.nodes[targetIdx-1]) # change node value to borrowed node
                        self.nodes[targetIdx-1] = leftNonLeafPage.nodes.pop(-1) # pop the borrowed node from left page
                        targetPage.ptrs.insert(0, leftNonLeafPage.ptrs.pop(-1)) # prepend the pointer from left page
                        targetPage.ptrs[0].parent = targetPage # change the parent of appended pointer to target page
                        return "OK", result[1]
                if rightNonLeafPageIdx < len(self.ptrs): # check right non leaf page exist, if exist, try to borrow from it
                    if len(self.ptrs[rightNonLeafPageIdx].nodes) > self.order:
                        rightNonLeafPage = self.ptrs[rightNonLeafPageIdx]
                        targetPage.nodes.append(self.nodes[targetIdx]) # change node value to borrowed node
                        self.nodes[targetIdx] = rightNonLeafPage.nodes.pop(0) # pop the borrowed node from right page
                        targetPage.ptrs.append(rightNonLeafPage.ptrs.pop(0)) # append the pointer from right page
                        targetPage.ptrs[-1].parent = targetPage # change the parent of appended pointer to target page
                        return "OK", result[1]

                # neither left or right non leaf page can lend node, do merge
                if leftNonLeafPageIdx >= 0: # check left non leaf page exist, if exist, merge with it
                    leftNonLeafPage = self.ptrs[leftNonLeafPageIdx]
                    leftNonLeafPage.nodes.append(self.nodes.pop(targetIdx-1))
                    leftNonLeafPage.nodes += targetPage.nodes
                    leftNonLeafPage.ptrs += targetPage.ptrs
                    for page in targetPage.ptrs:
                        page.parent = leftNonLeafPage
                else: # due to the properity of B+ tree, if no left non-leaf page, right non-leaf page must exist
                    rightNonLeafPage = self.ptrs[rightNonLeafPageIdx]
                    rightNonLeafPage.nodes.insert(0, self.nodes.pop(targetIdx))
                    rightNonLeafPage.nodes = targetPage.nodes + rightNonLeafPage.nodes
                    rightNonLeafPage.ptrs = targetPage.ptrs + rightNonLeafPage.ptrs
                    for page in targetPage.ptrs:
                        page.parent = rightNonLeafPage
                self.ptrs.pop(targetIdx)
                if self.isRoot(): # root page has no size contraint, but need to check whether size == 0
                    if self.nodes:
                        return "OK", result[1]
                    else:
                        self.ptrs[0].parent = None
                        return "change root", self.ptrs[0], result[1]
                else:
                    if len(self.nodes) < self.order:
                        return "NonLeafPage insufficient", result[1]
                    else:
                        return "OK", result[1]
        else:
            return result

    def rangeQuery(self, rangeStart, rangeStop):
        targetIdx = self.nextTraverseIdx(rangeStart)
        targetPage = self.ptrs[targetIdx]
        return targetPage.rangeQuery(rangeStart, rangeStop)

    def isRoot(self):
        return True if self.parent is None else False

    def nextTraverseIdx(self, key):
        for idx, value in enumerate(self.nodes):
            if key < value:
                return idx
        else:
            return len(self.nodes)

    def pageStatistics(self, statistics):
        statistics["nonLeafPage"] += 1
        statistics["totalPage"] += 1
        for page in self.ptrs:
            page.pageStatistics(statistics)

    def __str__(self):
        return "{}".format(self.nodes)
