from storageFile.page import Page
from storageFile.utils import *

class RelationTable:
    def __init__(self, name, keyType, recordSize):
        self.name = name
        self.pages = [ Page(recordSize) ]
        self.bPlusTree = None # TODO, initialize a empty B+ tree
        self.keyType = keyType
        self.recordSize = recordSize

    def insertable(self, record):
        if self.keyType == "Integer":
            try:
                int(record[0])
            except Exception as e:
                print(e)
                return False

        recordSize = getSize(record)
        if recordSize is not None:
            if recordSize <= self.recordSize:
                return True
            else:
                print("the record size is too big")
                return False
        else:
            return False

    def insert(self, record):
        pid, sid = None, None
        for index, page in enumerate(self.pages):
            sid = page.insert(record) # if insert success, return sid; if not, return None
            if sid is not None:
                pid = index
                break
        else:
            pid = len(self.pages)
            self.pages.append(Page(self.recordSize))
            sid = self.pages[-1].insert(record)

        # TODO insert into B+ tree

    def showStatistics(self):
        indexPageNum = 0 # TODO get index page number from B+ tree

        print("{} index page(s), {} data page(s)".format(indexPageNum, len(self.pages)))
