import numpy as np
ary_isin = 0
with open('In4.txt') as f:
    lines = f.readlines()
    lines_rs = list(map(str.rstrip, lines))
    lines_dash = list(map(lambda x : x.replace(',','-').split('-'), lines_rs))
    int_nums = np.array([list(map(int, x)) for x in lines_dash])

    ### Part I ###

    ary_2in1 = np.bitwise_and(int_nums[:,0] <= int_nums[:,2], int_nums[:,1] >= int_nums[:,3])
    ary_1in2 = np.bitwise_and(int_nums[:,0] >= int_nums[:,2], int_nums[:,1] <= int_nums[:,3])

    ary_isin = ary_1in2|ary_2in1


    ### Part 2 ###
    # ranges of line 1 are greater than the ones of line 2
    ary_1gt2 = (int_nums[:,0] > int_nums[:,3])
    # ranges of line 1 are greater than the ones of line 1
    ary_2gt1 = (int_nums[:,2] > int_nums[:,1])
    ary_no_overlap = ~(ary_1gt2|ary_2gt1)

print('Number of completely contained ranges: ' + str(sum(ary_isin)))

print('Number of overlapping ranges: ' + str(sum(ary_no_overlap)))



