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

def moveCrate(fromColumn, toColumn, crates):
    currentColumn = crates[fromColumn];
    char = currentColumn[len(currentColumn)-1]
    del crates[fromColumn][len(currentColumn)-1]
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
        for j in range(0, cratesToMove):
            crates = moveCrate(int(lineParts[3]) - 1, int(lineParts[5]) - 1, crates)
    return crates

# Main
with open("input", "r") as file:
    inputLines = file.readlines()
    visualEndLine = findEndOfVisual(inputLines)
    crates = getCratesList(inputLines, visualEndLine)
    crates = executeMoveCommands(inputLines, crates, visualEndLine)

    print(getTopCrates(crates))