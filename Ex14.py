import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

class Ex14():
    def __init__(self, f) -> None:
        self.origin = np.array([0, 500])
        self.lowest_point = 0
        self.sand_counter = 0
        self.parse_input(f)

        
        
        self.origin_tf = tuple(self.origin - np.array([self.idx_start_row, self.idx_start_col]))

    def parse_input(self, f):
        lines = list(map(str.rstrip, f.readlines()))
        lines_sep = list(map(lambda x : x.split(' -> '), lines))
        idx_rock = [[list(map(int, xx.split(','))) for xx in x] for x in lines_sep]        
        

        max_row = self.origin[0]
        min_row = self.origin[0]
        max_col = self.origin[1]
        min_col = self.origin[1]

        for line in idx_rock:
            for coordinate in line:
                max_col = max(max_col, coordinate[0])
                min_col = min(min_col, coordinate[0])
                max_row = max(max_row, coordinate[1])
                min_row = min(min_row, coordinate[1])
            # end for 
        # end for

        n_row = max_row-min_row+1+1
        n_add_cols = 2*n_row
        n_col = max_col-min_col+1+2*n_add_cols
        self.idx_start_row = min_row
        self.idx_start_col = min_col-n_add_cols

        self.state = np.zeros((n_row, n_col), dtype=int)

        transform_row = lambda x : x-self.idx_start_row
        transform_col = lambda x : x-self.idx_start_col
        transform_coord = lambda x : [transform_col(x[0]), transform_row(x[1])]

        for line in idx_rock:
            for idx in range(len(line)-1):
                idx_start = transform_coord(line[idx])
                idx_end = transform_coord(line[idx+1])
                idx_row = range(
                    min(idx_start[1],idx_end[1]),
                    max(idx_start[1],idx_end[1])+1
                    )
                idx_col = range(
                    min(idx_start[0],idx_end[0]),
                    max(idx_start[0],idx_end[0])+1
                    )
                self.state[idx_row, idx_col] = 1
                self.print_state()
            # end for 
        # end for
        return
    
    def start_simulation(self):
        print_count = 0
        while not np.any(self.state[-1,:]):
            print_count += 1
            self.simulate_sand()

            if print_count%20==0:
                self.print_state()
            # end if
        # end while
        self.sand_counter -= 1
        return

    def continue_simulation_ptII(self):
        print_count = 0
        while not self.state[self.origin_tf]:
            print_count += 1
            self.simulate_sand()

            if print_count%20==0:
                self.print_state()
            # end if
        # end while
        self.sand_counter -= 1
        return

    def simulate_sand(self):
        # start in origin column
        self.sand_counter += 1
        self.sand_physics(self.origin_tf)
        return

    def sand_physics(self, idx_sand_start):
        b_finished = False
        idx_row = idx_sand_start[0]
        idx_col = idx_sand_start[1]

        col = self.state[:,idx_col]
        
        idx_nonzero = np.argwhere(col!=0)
        idx_nonzero_filt = idx_nonzero>idx_row
        if not any(idx_nonzero_filt):
            idx_first_nonzero = np.array([self.state.shape[0]+1])
        else:
            idx_first_nonzero = np.min(idx_nonzero[idx_nonzero_filt])
        # end if
        idx_zeros = np.flip(np.transpose(np.argwhere(col==0)))
        idx_zeros_clean = idx_zeros[
            (idx_zeros >= idx_row) & (idx_zeros < self.state.shape[0]) & (idx_zeros < idx_first_nonzero)]
        if len(idx_zeros_clean)>1:
            idx_possible_rest = int(
                idx_zeros_clean[
                np.argmax(
                    np.diff(
                        idx_zeros_clean
                    )
                )]
            )
        else:
            idx_possible_rest = int(idx_zeros_clean)
        # end if

        if idx_possible_rest == self.state.shape[0]-1:
            self.state[idx_possible_rest,idx_col] = 2
            b_finished = True
        else:
            value_left_right = [
                self.state[idx_possible_rest+1,idx_col-1],
                self.state[idx_possible_rest+1,idx_col+1]
            ]
            if value_left_right[0] == 0:
                idx_sand = [idx_possible_rest+1, idx_col-1]
            elif value_left_right[1] == 0:
                idx_sand = [idx_possible_rest+1, idx_col+1]
            else:
                # set state and finish
                self.state[idx_possible_rest, idx_col] = 2
                b_finished = True
            # end if
        # end if
        if not b_finished:
            idx_sand_new = self.sand_physics(idx_sand)
        else:
            idx_sand_new = idx_sand_start
        # end if
        return idx_sand_new, b_finished

    def do_ptI(self):
        self.start_simulation()
        self.print_state()
        self.print_sand_counter()
        return

    def do_ptII(self):
        self.sand_counter += 1
        
        self.continue_simulation_ptII()
        
        self.print_state()
        self.print_sand_counter()
        return

    @property
    def b_abyss(self):
        pass

    def print_state(self):
        # print(np.array2string(self.state, separator='', formatter={'all': lambda x: str(x) if x!=0 else '.'}).replace(" [","").replace("[","").replace("]",""))
        # print()
        pass

    def print_sand_counter(self):
        print('Number of sand corns: ' + str(self.sand_counter))

if __name__=='__main__':
        
    with open('In14.txt') as f:
        Exercise14 = Ex14(f)
    # end with

    Exercise14.do_ptI()
    Exercise14.do_ptII()

# end if