sum = 0

def getPriority(letter):
    ascii = ord(letter)
    if ascii >= 97 and ascii <= 122:
        return ascii - 96
    elif ascii >= 65 and ascii <= 90:
        return ascii - 38
    else:
        return 0

with open("input") as file:
    lines = file.readlines()
    length = len(lines)
    for i in range(0, length):
        lineLength = len(lines[i])
        leftPart = lines[i][0 : int(lineLength/2)]
        rightPart = lines[i][int(lineLength/2) : int(lineLength)]
        print(leftPart)
        print(rightPart)
        for k in range(0, int(lineLength/2)):
            if rightPart.__contains__(leftPart[k]):
                rightPart = rightPart.replace(leftPart[k], '')
                sum += getPriority((leftPart[k]))
                print(leftPart[k])

print(sum)