# ex12_2.py
def mymax(nLst):
    if len(nLst) == 2:
        return nLst[0] if nLst[0] > nLst[1] else nLst[1]
    tmp_max = mymax(nLst[1:])
    return nLst[0] if nLst[0] > tmp_max else tmp_max

data = [1, 5, 9, 2, 8, 100, 81]
print('data         = ', data)
print('data的最大值 = ', mymax(data))






        
def recursiveMax(nList):
    if len(nList) == 2:
        return nList[0] if nList[0] > nList[1] else nList[1]
    tmp_max = recursiveMax(nList[1:])
    return nList[0] if nList[0] > tmp_max else tmp_max




