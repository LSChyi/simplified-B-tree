from storageFile.page import Page

class RelationTable:
    currentPid = 0

    def __init__(self, name, keyType, recordSize):
        self.name = name
        self.page = [ Page(RelationTable.currentPid, recordSize) ]
        RelationTable.currentPid += 1
        self.bPlusTree = None # TODO, initialize a empty B+ tree
        self.keyType = keyType
        self.recordSize = recordSize
