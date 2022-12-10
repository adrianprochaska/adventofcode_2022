def calc_winning(input):
    # index allocation
    n_wins = 0
    n_draw = 0
    n_rck = 0
    n_pap = 0
    n_sci = 0
    for line in input:
        line = line.rstrip()
        if 'X' in line:
            n_rck += 1
            if 'C' in line:
                n_wins += 1
            elif 'A' in line:
                n_draw += 1
        elif 'Y' in line:
            n_pap += 1
            if 'A' in line:
                n_wins += 1
            elif 'B' in line:
                n_draw += 1
        elif 'Z' in line:
            n_sci += 1
            if 'B' in line:
                n_wins += 1
            elif 'C' in line:
                n_draw += 1
                
                
    n_points = 6*n_wins + 3*n_draw + 1*n_rck + 2*n_pap + 3*n_sci
    
    return n_points

def calc_winning_ptII(input):
    # index allocation
    n_wins = 0
    n_draw = 0
    n_rck = 0
    n_pap = 0
    n_sci = 0
    for line in input:
        line = line.rstrip()
        if 'X' in line:
            if 'A' in line:
                n_sci += 1
            elif 'B' in line:
                n_rck += 1
            else:
                n_pap += 1

        elif 'Y' in line:
            n_draw += 1
            if 'A' in line:
                n_rck += 1
            elif 'B' in line:
                n_pap += 1
            else:
                n_sci += 1

        elif 'Z' in line:
            n_wins += 1
            if 'A' in line:
                n_pap += 1
            elif 'B' in line:
                n_sci += 1
            else:
                n_rck += 1

               
                
    n_points = 6*n_wins + 3*n_draw + 1*n_rck + 2*n_pap + 3*n_sci
    
    return n_points


with open('In2.txt') as f:
    lines = f.readlines()
    n_win = calc_winning(lines)

    n_win2 = calc_winning_ptII(lines)

    print(n_win)
    print()
    print(n_win2)

