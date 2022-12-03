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
    i = 0
    while i in range(0, len(lines)):
        for letterID in range(0, len(lines[i])):
            letter = lines[i][letterID]
            if lines[i+1].__contains__(letter) and lines[i+2].__contains__(letter):
                lines[i+1] = lines[i+1].replace(letter, '')
                lines[i+2] = lines[i+2].replace(letter, '')
                sum += getPriority(letter)
                print(letter)
        i += 3

print(sum)