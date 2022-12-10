import string

dict_values = dict((value, idx+1) for idx, value in enumerate(list(string.ascii_letters)))

### Part I ###

priorities = []

with open('In3.txt') as f:
    for line in f:
        line = line.rstrip()
        half = int(len(line)/2)
        str_half1 = line[0:half]
        str_half2 = line[-half:]

        letter_in_both = next((x for x in str_half1 if x in str_half2), False)

        priorities.append(dict_values[letter_in_both])

print(sum(priorities))

### Part II ###

priorities_2 = []

with open('In3.txt') as f:
    count = 0
    lines = []
    for line in f:
        line = line.rstrip()
        count += 1
        lines.append(line)
        if count == 3:
            count = 0
            char_in_both = lambda str1, str2 : {x for x in str1 if x in str2}

            line_1_in_2 = char_in_both(lines[0],lines[1])
            line_2_in_3 = char_in_both(lines[1],lines[2])
            letter_in_all = char_in_both(line_1_in_2, line_2_in_3)
            priorities_2.append(dict_values[letter_in_all.pop()])

            lines = []

print(sum(priorities_2))

