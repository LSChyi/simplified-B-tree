from storageFile.pageMgr import PageMgr

class RelationTable:
    def __init__(self, name, keyType):
        self.name = name
        self.page = PageMgr(keyType)
        self.bPlusTree = None # TODO, initialize a empty B+ tree
        self.keyType = keyType
