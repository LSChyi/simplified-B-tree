from storageFile.page import Page
from storageFile.utils import *
from bPlusTree.bPlusTree import bPlusTree
from bPlusTree.leafNode import LeafNode

class RelationTable:
    def __init__(self, name, keyType, recordSize):
        self.name = name
        self.pages = []
        self.keyType = keyType
        self.bPlusTree = bPlusTree(keyType)
        self.recordSize = recordSize

    def insertable(self, record):
        recordSize = 4
        if self.keyType == "Integer":
            recordSize += 4
            try:
                int(record[0])
            except Exception as e:
                print(e)
                return False
        else:
            recordSize += 10

        recordSize += restSize(record)
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

        if self.keyType == "String":
            key = record[0][:10]
        else:
            key = int(record[0])
        self.bPlusTree.insert(LeafNode(key, pid, sid))

    def search(self, key):
        if self.keyType == "String":
            key = key[:10]
        else:
            try:
                key = int(key)
            except Exception as e:
                print(e)
                return None

        record = self.bPlusTree.search(key)
        if record is not None:
            recordTuple = self.pages[record.pid].getRecord(record.sid)
            print("key: {}  restSize: {}  rid: {}".format(key, restSize(recordTuple), record.rid()))
        else:
            print("no record found")

    def rangeQuery(self, rangeStart, rangeStop):
        if self.keyType == "String":
            rangeStart = rangeStart[:10]
            rangeStop = rangeStop[:10]
        else:
            try:
                rangeStart = int(rangeStart)
                rangeStop = int(rangeStop)
            except Exception as e:
                print(e)
                return None

        records = self.bPlusTree.rangeQuery(rangeStart, rangeStop)
        for record in records:
            print("key: {}, RID: {}".format(record.value, record.rid()))

    def delete(self, key):
        if self.keyType == "String":
            key = key[:10]
        else:
            try:
                key = int(key)
            except Exception as e:
                print(e)
                return None
            
        record = self.bPlusTree.delete(key)
        if record is None:
            print("no record found, no deletion")
            return
        
        self.pages[record.pid].delete(record.sid)
        print("record deleted: {} with rid {}".format(record.value, record.rid()))

    def showPageContent(self, pageId):
        if 0 <= pageId < len(self.pages):
            self.pages[pageId].showContent()
        else:
            print("the page id does not exist")
            return

    def showStatistics(self):
        indexPageNum = self.bPlusTree.pageStatistics()["totalPage"]

        print("{} index page(s), {} data page(s)".format(indexPageNum, len(self.pages)))

    def showIndexStatistics(self):
        statistics = self.bPlusTree.pageStatistics()

        print("{} leaf page(s), {} total index page(s)".format(statistics["leafPage"], statistics["totalPage"]))
