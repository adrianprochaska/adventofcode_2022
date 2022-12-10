import numpy as np

n_win = 4 # window size

def start_of_packet(input, n_win=4):
    
    for idx, value in enumerate(input):
        str_window = input[idx:idx+n_win]
        if len(set(str_window)) == n_win:
            break

        
    idx_final = idx+n_win
    print('Start of packet with window size ' + str(n_win) + ' after: ' + str(idx_final))
    return idx_final


with open('In6.txt') as f:
    for line in f:
        start_of_packet(line)
        start_of_packet(line, 14)



