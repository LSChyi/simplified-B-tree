from storageFile.relationTable import RelationTable
from storageFile.page import Page

def emptyFn(*params):
    pass

def RFn(*params):
    commandParams = params[0]
    databaseTables = params[1]
    if len(commandParams) != 3:
        print("number of parameters not match")
        return

    tableName = commandParams[0]
    if tableName in [ table.name for table in databaseTables ]:
        print("table already exists")
        return

    keyType = commandParams[1]
    if keyType.lower() not in [ "integer", "int", "string", "str" ]:
        print("type not support")
        return

    try:
        recordSize = int(commandParams[2])
    except Exception as e:
        print(e)
        return
    if not Page.isValidSize(recordSize):
        return
    
    databaseTables.append(RelationTable(tableName, keyType, recordSize))
    print("{} relation table created".format(tableName))
