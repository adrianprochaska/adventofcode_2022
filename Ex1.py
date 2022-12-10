all_elves = []
one_elf = 0
with open('In1.txt') as f:
    for line in f:
        line = line.rstrip()
        if not (line == ''):
            one_elf += int(line)
        else:
            all_elves.append(one_elf)
            one_elf = 0

all_elves.sort()
print('max value: ' + str(max(all_elves)))

print('sum of the first three:')
print(sum(all_elves[-3:]))