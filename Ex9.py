import numpy as np

class Exercise_Nine():

    def __init__(self) -> None:
            
        self.ary_size = 501
        self.len_rope = 10
        loc_start = np.floor(self.ary_size/2)
        self.state = np.ones((self.len_rope, 2), dtype=int) * int(loc_start)
        # self.loc_head = np.array([loc_start, loc_start], dtype=int)
        # self.loc_tail = np.array([loc_start, loc_start], dtype=int)
        self.ary_visit = np.zeros((self.ary_size,self.ary_size), dtype=bool)
        self.ary_visit[tuple(self.state[1,:])] = True

    def update_tail(self, head, tail):
        # check if head and tail are not touching
        dir = head-tail
        if any(abs(dir)>1):
            # dominant direction
            dir_new = np.int_(dir/max(abs(dir)))
            # update tail: one step agains moving direction
            tail_new = head-dir_new
            
            

            # update tail
            # self.loc_tail = tail

        else:
            # do nothing
            tail_new = tail
            pass
        # end if

        return tail_new

    def move_anywhere(self, move):
        # move
        state_new = self.state
        # self.loc_head += move

        # update tail
        for idx, value in enumerate(state_new):
            if idx == 0:
                state_new[idx,:] += move

            else:
                state_new[idx,:] = self.update_tail(state_new[idx-1,:],value)
                self.state = state_new
                # update the array of visited places
            # end if
        # end for
                
        self.ary_visit[tuple(state_new[-1,:])] = True
        

    def parse_input(self, input):
        str_dir, steps = input.split()

        if str_dir == 'L':
            ary_dir = np.array([-1, 0])
        if str_dir == 'R':
            ary_dir = np.array([1, 0])
        if str_dir == 'U':
            ary_dir = np.array([0, 1])
        if str_dir == 'D':
            ary_dir = np.array([0, -1])
        # end if

        for i in range(int(steps)):
            self.move_anywhere(ary_dir)
            # self.visualise_rope()

    def print_n_visit(self):
        n_visit = sum(sum(self.ary_visit))

        print(str(n_visit) + ' points were visited.')

    def visualise_result(self):
        ary_print = np.transpose(self.ary_visit)
        print(np.array2string(ary_print, separator='', formatter={'all': lambda x: 'x' if x else '.'}).replace(" [","").replace("[","").replace("]",""))
        print()

    def visualise_rope(self):
        ary_print = np.zeros(self.ary_visit.shape, dtype=int)
        for count, knot in reversed(list(enumerate(self.state))):
            ary_print[tuple(knot)] = count+1
        # end for
        ary_print = np.flipud(np.transpose(ary_print))
        print(np.array2string(ary_print, separator='', formatter={'all': lambda x: '.' if x == 0 else str(x-1)}).replace(" [","").replace("[","").replace("]",""))
        print()

if __name__=='__main__':
    with open('In9.txt') as f:
        lines_ws = f.readlines()
        lines = list(map(str.rstrip, lines_ws))

        # create object
        Ex9 = Exercise_Nine()

        for line in lines:
            Ex9.parse_input(line)

    # end with
    Ex9.print_n_visit()


    
