def openFileAndClean(filename):
    f = open(filename, "r")
    fullList = f.readlines()

    cleanedList = []
    for e in fullList:
        cleanedList.append(int(e.strip()))
    return cleanedList

def findNumberOfIncreased(filename):
    cleanedList = openFileAndClean(filename)


    counter = 0
    for i in range(len(cleanedList)):
        if i!=0 and cleanedList[i] > cleanedList[i-1]:
            counter += 1 

    return counter


def findNumberOfSumIncreased(filename):
    cleanedList = openFileAndClean(filename)

    counter = 0
    for i in range(len(cleanedList)):
        if i>2 and cleanedList[i]+cleanedList[i-1]+cleanedList[i-2] > cleanedList[i-1]+cleanedList[i-2]+cleanedList[i-3]:
            counter += 1 

    return counter


print(findNumberOfIncreased("input1"))
print(findNumberOfSumIncreased("input1"))