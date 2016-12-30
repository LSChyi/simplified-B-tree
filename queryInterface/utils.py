from storageFile.relationTable import RelationTable
from storageFile.page import Page
import re

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
    else:
        if keyType.lower() in [ "integer", "int" ]:
            keyType = "Integer"
        else:
            keyType = "String"

    try:
        recordSize = int(commandParams[2])
    except Exception as e:
        print(e)
        return
    if not Page.isValidSize(recordSize):
        return
    
    databaseTables.append(RelationTable(tableName, keyType, recordSize))
    print("{} relation table created".format(tableName))

def IFn(*params):
    commandParams = params[0]
    databaseTables = params[1]

    tableName = commandParams[0]
    table = None
    for dataTable in databaseTables:
        if tableName == dataTable.name:
            table = dataTable
            break
    else:
        print("relation table '{}' not found".format(tableName))
        return

    dataToInsert = []
    rawDataStr = " ".join(commandParams[1:])
    dataStrRows = re.split(r'(?!\B"[^"]*);(?![^"]*"\B)', rawDataStr)
    for row in dataStrRows:
        parsedData = re.split(r'\s|(".+?")', row)
        parsedData = [ s for s in parsedData if s is not None and s is not '' ]
        if table.insertable(parsedData):
            dataToInsert.append(parsedData)
        else:
            return

    for data in dataToInsert:
        table.insert(data)

    print("{} record(s) stored".format(len(dataToInsert)))

def pFn(*params):
    commandParams = params[0]
    databaseTables = params[1]

    if len(commandParams) != 2:
        print("number of parameters not match")
        return

    tableName = commandParams[0]
    table = None
    for dataTable in databaseTables:
        if tableName == dataTable.name:
            table = dataTable
            break
    else:
        print("relation table '{}' not found".format(tableName))
        return

    try:
        pageId = int(commandParams[1])
    except Exception as e:
        print(e)
        return

    table.showPageContent(pageId) 

def cFn(*params):
    commandParams = params[0]
    databaseTables = params[1]

    if len(commandParams) != 1:
        print("number of parameters not match")
        return

    tableName = commandParams[0]
    for dataTable in databaseTables:
        if tableName == dataTable.name:
            dataTable.showStatistics()
            break
    else:
        print("relation table '{}' not found".format(tableName))
        return
