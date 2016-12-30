def getSize(record):
    cumulateSize = 4 # 4 byte is for rid
    for val in record[1:]:
        if val[0] == "\"" and val[-1] == "\"": # is a double quoted string
            cumulateSize += len(val) - 2 # a char size = 1 byte
        else: # is a number
            try:
                int(val)
            except Exception as e:
                print(e)
                return None
            cumulateSize += 4 # assume the number is a int, and int size = 4 byte
    
    return cumulateSize
