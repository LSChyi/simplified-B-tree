from storageFile.utils import *

class Page:
    def __init__(self, recordSize):
        self.recordSize = recordSize
        self.record = []
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
            if None in self.record:
                sid = self.record.index(None)
                self.record[sid] = record
            else:
                sid = len(self.record)
                self.record.append(record)

            return sid 
        else:
            return None
