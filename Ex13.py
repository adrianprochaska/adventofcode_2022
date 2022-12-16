import numpy as np

def parse_input(input):
    list_of_string = list(map(str.rstrip, f.readlines()))
    counter = 0

    l_input_ptI = []
    l_input_ptII = []
    n_line = 3
    while counter < int(len(list_of_string)/n_line)+1:
        idx_start = counter * n_line
        list1 = eval(list_of_string[idx_start])
        list2 = eval(list_of_string[idx_start+1])

        l_input_ptI.append(
            [list1, list2]
        )
        l_input_ptII.append(list1)
        l_input_ptII.append(list2)
        counter+=1
    # end while

    return l_input_ptI, l_input_ptII

def compare_pair(pair):
    mini_pair1 = pair[0]
    mini_pair2 = pair[1]
    n_iter = min(len(mini_pair1), len(mini_pair2))
    if len(mini_pair1)< len(mini_pair2):
        b_correct = True
        b_length_decision = True
    elif len(mini_pair1) > len(mini_pair2):
        b_correct = False
        b_length_decision = True
    else:
        b_correct = -1
        b_length_decision = False
    b_break = False
    for idx in range(n_iter):
        b_isempty1 = len(mini_pair1) < 1
        b_isempty2 = len(mini_pair2) < 1
        if b_isempty1:
            b_correct = True
            b_break = True
        elif b_isempty2:
            b_correct = False
            b_break = True
        elif b_isempty1 and b_isempty2:
            print()
        else:
            mini_mini_pair1 = mini_pair1[idx]
            mini_mini_pair2 = mini_pair2[idx]
            b_isint1 = isinstance(mini_mini_pair1, int)
            b_isint2 = isinstance(mini_mini_pair2, int)
            b_both_int = b_isint1 and b_isint2
            if b_both_int:
                if mini_mini_pair1 == mini_mini_pair2:
                    continue
                else:
                    b_correct = mini_mini_pair1 < mini_mini_pair2
                    b_break = True 
            else:
                # any ran out of elements?

                if b_isint1:
                    l_pair1 = [mini_mini_pair1]
                    l_pair2 = mini_mini_pair2
                elif b_isint2:
                    l_pair1 = mini_mini_pair1
                    l_pair2 = [mini_mini_pair2]
                else:
                    l_pair1 = mini_mini_pair1
                    l_pair2 = mini_mini_pair2
                # end if
                b_correct_loc, b_break = compare_pair([l_pair1, l_pair2])
                if b_correct_loc != -1:
                    b_correct = b_correct_loc
                # end if
            # end if
        # end if
        if b_break:
            break
        # end if
    # end for
    if b_length_decision:
        b_break = True
    # end if

    return b_correct, b_break

def compare_pairs(l_input):
    list_of_bool = []
    n_correct = 0
    for pair in l_input:
        b_correct, b_break = compare_pair(pair)
        list_of_bool.append(b_correct)
        # print(list_of_bool)
        # print()
        # pass
    # end for
    for idx, val in enumerate(list_of_bool):
        if val:
            n_correct += idx+1
        # end if
    # end for

    return n_correct

def sort_all(l_input):
    divider_packets = [[[2]],[[6]]]
    n_low = 1
    n_mid = 1
    n_high = 1
    for line in l_input:
        b_correct, b_break = compare_pair([line, divider_packets[0]])
        if b_correct:
            n_low += 1
        else:
            b_correct, b_break = compare_pair([line, divider_packets[1]])
            if b_correct:
                n_mid += 1
            else:
                n_high += 1
            # end if
        # end if
    # end for
    n_solution = (n_low)*(n_low+n_mid)
    return n_solution

with open('In13.txt') as f:
    l_input_ptI, l_input_ptII = parse_input(f)
# end with
n_correct = compare_pairs(l_input_ptI)

print('Sum of index of correct pairs: ' + str(n_correct))


n_solution = sort_all(l_input_ptII)
print('Product of index of sorted decoder keys : ' + str(n_solution))