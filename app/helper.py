def check(v1, v2, v3):
    if v1 == "T" or v1 == "" or v1 == "D":
        print("Wrong Input")
        return False
    if v2 == "T" or v2 == "" or v2 == "D":
        print("Wrong Input")
        return False
    if v3 == "T" or v3 == "" or v3 == "D":
        print("Wrong Input")
        return False
    return True

def getValue(value):
    if value[0] == "T":
        return 3 * int(value[1:])
    elif value[0] == "D":
        return 2 * int(value[1:])
    else:
        return int(value)
    
def getAvg(darts):
    count = 0
    sum = 0
    for dart in darts:
        count+=1
        sum+=dart.value
    if count > 0:
        return int(sum/count)
    return 0