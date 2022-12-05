def findEndOfVisual(input):
    for i in range(0, len(input)):
        if (len(input[i]) < 2):
            continue
        if (input[i][0:2] == " 1"):
            return i

def getCratesList(input, endLine):
    numLine = input[endLine].split()
    columnCount = int(numLine[len(numLine)-1])
    crates = []
    for i in range(0, columnCount):
        column = []
        for j in range(endLine-1, -1, -1):
            char = input[j][i*4+1]
            if (char != " "):
                column.append(char)
        crates.append(column)
    return crates

def moveCrates(cratesCount, fromColumn, toColumn, crates):
    currentColumn = crates[fromColumn]
    cratesStart = len(currentColumn)-cratesCount
    cratesEnd = len(currentColumn)
    for i in range(cratesStart, cratesEnd):
        char = currentColumn[cratesStart]
        del crates[fromColumn][cratesStart]
        crates[toColumn].append(char)
    return crates

def getTopCrates(crates):
    topcrates = ""
    for crate in crates:
        topcrates += crate[len(crate)-1]
    return topcrates

def executeMoveCommands(input, crates, visualEndLine):
    commandsStartLine = visualEndLine + 2
    for i in range(commandsStartLine, len(input)):
        lineParts = input[i].split()
        cratesToMove = int(lineParts[1])
        crates = moveCrates(cratesToMove, int(lineParts[3]) - 1, int(lineParts[5]) - 1, crates)
    return crates

# Main
with open("input", "r") as file:
    inputLines = file.readlines()
    visualEndLine = findEndOfVisual(inputLines)
    crates = getCratesList(inputLines, visualEndLine)
    crates = executeMoveCommands(inputLines, crates, visualEndLine)

    print(getTopCrates(crates))