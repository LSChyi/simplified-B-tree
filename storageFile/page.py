class Page:
    def __init__(self, pid, recordSize):
        self.pid = pid
        self.recordSize = recordSize
        self.record = []

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
