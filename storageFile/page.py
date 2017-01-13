from storageFile.utils import *

class Page:
    def __init__(self, recordSize):
        self.recordSize = recordSize
        self.records = []
        self.emptySize = 512 - 4 # a int is for tracking how many records inside this page
        self.maxSlotN = self.emptySize // (self.recordSize + 2)

    @staticmethod
    def isValidSize(size):
        if size <= 0:
            print("record size should larger then 0")
            return False
        elif size < 4:
            print("the size is too small that rid can not be stored")
            return False
        elif size == 4:
            print("the size is too small that only rid can be stored")
            return False
        elif size >= 508:
            print("the size is too big that can not be sotred in one page")
            return False
        else:
            return True

    def insert(self, record):
        if self.emptySize >= (self.recordSize + 2):
            self.emptySize -= (self.recordSize + 2)
            if len(self.records) < self.maxSlotN:
                sid = len(self.records)
                self.records.append(record)
            else:
                sid = self.records.index(None)
                self.records[sid] = record

            return sid 
        else:
            return None

    def getRecord(self, idx):
        return self.records[idx]

    def delete(self, idx):
        key = self.records[idx][0]
        self.records[idx] = None
        self.emptySize += (self.recordSize + 2)
        return key

    def showContent(self):
        print("Number of slots: {}, number of occupied slots: {}, number of empty slots: {}".format(len(self.records), len([ x for x in self.records if x is not None ]), len([ x for x in self.records if x is None ])))
        print(" sid  key")
        for index, record in enumerate(self.records):
            if record is not None:
                print("[{:>3}] {} {}".format(index, record[0], record[1:]))
            else:
                print("[{:>3}] {}".format(index, record))
