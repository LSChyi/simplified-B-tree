from storageFile.utils import *

class Page:
    def __init__(self, recordSize):
        self.recordSize = recordSize
        self.records = []
        self.emptySize = 512 - 4 # a int for tracking how many records inside this page

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
        sid = None
        if self.emptySize >= self.recordSize:
            self.emptySize -= (self.recordSize + 4)
            if None in self.records:
                sid = self.records.index(None)
                self.records[sid] = record
            else:
                sid = len(self.records)
                self.records.append(record)

            return sid 
        else:
            return None

    def getRecord(self, idx):
        return self.records[idx]

    def delete(self, idx):
        self.records[idx] = None

    def showContent(self):
        print("Number of slots: {}, number of occupied slots: {}, number of empty slots: {}".format(len(self.records), len([ x for x in self.records if x is not None ]), len([ x for x in self.records if x is None ])))
        print(" sid  key")
        for index, record in enumerate(self.records):
            if record is not None:
                print("[{:>3}] {} {}".format(index, record[0], record[1:]))
            else:
                print("[{:>3}] {}".format(index, record))
