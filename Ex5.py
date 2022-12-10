import numpy as np

with open('In5.txt') as f:
    lines = f.readlines()
    lines_rs = lines
    '1' in lines_rs[3]
    # find line of numbers
    idx_num = next(idx for idx, line in enumerate(lines_rs) if '1' in line)

    # find index of numbers
    num_line = lines_rs[idx_num]
    idx_stack = [idx for idx, value in enumerate(num_line) if value.isdigit()]

    # find letters in lines above 
    stacks = []
    stacks_ptII = []
    for value in idx_stack:
        list_of_letters = []
        for k in range(idx_num-1, -1, -1):
            chr_letter = lines_rs[k][value]
            if chr_letter.isalpha():
                list_of_letters.append(chr_letter)
            else:
                break
            # end if
        # end for
        stacks.append(list_of_letters)
        stacks_ptII.append(list_of_letters.copy())
    # end for 

    # loop over moves
    for k in range(idx_num+2, len(lines_rs)):
        # print(k)
        # get number of items
        n_move, n_from, n_to = [int(value) for value in lines_rs[k].split() if value.isdigit()]
        
        n_from -= 1
        n_to -= 1
        ### Part I ###
        # stack from x to y
        stacks[n_to].extend(reversed(stacks[n_from][-n_move:]))
        stacks[n_from] = stacks[n_from][:-n_move]
        ### Part I ###
        # stack from x to y
        stacks_ptII[n_to].extend(stacks_ptII[n_from][-n_move:])
        stacks_ptII[n_from] = stacks_ptII[n_from][:-n_move]
    # end for

str_final = ''
for list_loc in stacks:
    str_final += list_loc[-1]

str_final_ptII = ''
for list_loc in stacks_ptII:
    str_final_ptII += list_loc[-1]

print(str_final)

print(str_final_ptII)
