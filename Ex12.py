import numpy as np
def some_fun():
    pass

def parse_input(input):
    l_lines_nl = f.readlines()
    l_lines = list(map(str.rstrip, l_lines_nl))
    heightmap = np.zeros((len(l_lines), len(l_lines[0])), dtype=int)
    reachmap = heightmap

    for idx, line_n in enumerate(l_lines) :
        line = line_n.rstrip()
        heightmap[idx,:] = np.array(list(map(lambda x : ord(x)-96, line)))
    # end for

    idx_start = heightmap == -13
    idx_end = heightmap == -27

    heightmap[idx_start] = 1
    heightmap[idx_end] = 26

    return heightmap, idx_start, idx_end
def possible_idx(heightmap, idx_start):
    ary_dirs = np.array([[1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]])
    dirs = ary_dirs+idx_start
    shape_hm = heightmap.shape
    
    idx_possible_dirs = np.bitwise_and(
            np.bitwise_and(dirs[:,0] >= 0, dirs[:,0] <= shape_hm[0]-1),
            np.bitwise_and(dirs[:,1] >= 0, dirs[:,1] <= shape_hm[1]-1)
            )
            
    possible_dirs = dirs[idx_possible_dirs]
    
    for count, idx_step in reversed(list(enumerate(possible_dirs))):
        if heightmap[tuple(idx_start)] - heightmap[tuple(idx_step)] > 1:
            possible_dirs = np.delete(possible_dirs, count, 0)
        # end if
    # end for

    return possible_dirs

def optimal_way(heightmap, idx_start, idx_end):
    ary_steps = -1*np.ones(heightmap.shape)
    ary_steps[idx_end] = 0
    step = 0
    while not ary_steps[idx_start] != -1:
        last_steps = np.transpose(np.array(np.where(ary_steps==step)))
        step += 1

        for idx in last_steps:
            idx_possible = possible_idx(heightmap, idx)
            for current_step in idx_possible:
                if ary_steps[tuple(current_step)] == -1:
                    ary_steps[tuple(current_step)] = step
                # end if
        # end for
        # print(np.array2string(ary_steps[:,:], separator='', formatter={'all': lambda x: str(x) if x!=-1 else '.'}).replace(" [","").replace("[","").replace("]",""))
        # pass
        # print()
        if step%10==0:
            print(step)
        # end if
    # end while
    min_steps = ary_steps[idx_start]
    min_steps_direct = min(ary_steps[np.bitwise_and(heightmap==1, ary_steps!=-1)])
    return min_steps, min_steps_direct

with open('In12.txt') as f:
    heightmap, idx_start, idx_end = parse_input(f)
    min_steps, min_steps_direct = optimal_way(heightmap, idx_start, idx_end)

    print('Minimum number of steps from start: ' + str(min_steps))
    print('Minimum number of steps from start: ' + str(min_steps_direct))