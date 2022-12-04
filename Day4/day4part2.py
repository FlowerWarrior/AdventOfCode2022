finalNum = 0
with open("input", "r") as file:
    lines = file.readlines()
    for line in lines:
        ranges = line.split(',')
        elf1start = int(ranges[0].split('-')[0])
        elf1end = int(ranges[0].split('-')[1])
        elf2start = int(ranges[1].split('-')[0])
        elf2end = int(ranges[1].split('-')[1])
        if (elf1end >= elf2start and elf1start <= elf2end):
            finalNum += 1
            continue

print(finalNum)