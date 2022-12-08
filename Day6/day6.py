def doCharsRepeat(textLine):
    for i in range(0, len(textLine)):
        if (textLine.count(textLine[i]) > 1):
            return True
    return False

def getPartOneAnswer(input):
    for i in range(0, len(input)-3):
        if doCharsRepeat(input[i:i+4]):
            continue
        else:
            return i+4
    return 0

def getPartTwoAnswer(input):
    for i in range(0, len(input)-13):
        if doCharsRepeat(input[i:i+14]):
            continue
        else:
            return i+14
    return 0

with open("input", "r") as file:
    line = file.readline()
    print("Part one")
    print(getPartOneAnswer(line))
    print("Part two")
    print(getPartTwoAnswer(line))

