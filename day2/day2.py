def openFileAndClean(filename):
    f = open(filename, "r")
    fullList = f.readlines()

    cleanedList = []
    for e in fullList:
        cleanedList.append(e.strip())
    return cleanedList

def multiplyFinalHorizontalAndVertical(filename):
    cleanedList = openFileAndClean(filename)
    x = 0
    y = 0
    for command in cleanedList:
        newcommand = command.split()
        if newcommand[0] == "forward":
            y += int(newcommand[1])
        if newcommand[0] == "up":
            x -= int(newcommand[1])
        if newcommand[0] == "down":
            x += int(newcommand[1])
    return x*y

def multiplyFinalHorizontalAndVerticalWithAim(filename):
    cleanedList = openFileAndClean(filename)
    x = 0
    y = 0
    aim = 0
    for command in cleanedList:
        newcommand = command.split()
        if newcommand[0] == "forward":
            y += int(newcommand[1])
            x += int(newcommand[1])*aim
        if newcommand[0] == "up":
            aim -= int(newcommand[1])
        if newcommand[0] == "down":
            aim += int(newcommand[1])
    return x*y


print(multiplyFinalHorizontalAndVertical("input"))
print(multiplyFinalHorizontalAndVerticalWithAim("input"))