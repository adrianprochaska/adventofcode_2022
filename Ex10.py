import numpy as np

class Exercise_Ten():

    def __init__(self) -> None:
            
        self.reg = 1 # current value of register
        self.reg_hist = [self.reg]
        self.width_line = 40

    def parse_input(self, input):
        if 'noop' in input:
            self.noop()
        elif 'addx' in input:
            val_addx = int(input[5:])
            self.addx(val_addx)
        else:
            print('Something went terribly wrong!')
        # end if

        return

    def noop(self):
        # self.reg stays the same
        self.reg_hist.append(self.reg_hist[-1])
        return

    def addx(self, val_addx):
        self.reg += val_addx
        self.reg_hist.extend(
            [self.reg_hist[-1], self.reg])
        return

    def print_sum_of_strength(self):
        print(f'Sum of signal strengths: {self.sum_of_strength}')
        return

    def print_reg_and_cyc(self):
        str_2_print = 'Registry value: {:-5} Cycle {:3}'.format(
            self.reg,
            self.cyc
            )
        
        print(str_2_print)
        return

    def render(self):
        
        n_lines = range(0,self.cyc-1,self.width_line)
        for idx_start in n_lines:
            idx_end = min(self.cyc, idx_start+self.width_line)
            ary_print = np.array(self.render_matrix[idx_start:idx_end])
            print(np.array2string(ary_print, separator='', formatter={'all': lambda x: '#' if x else '.'}).replace(" [","").replace("[","").replace("]",""))
        # end for
        print()

        return

    @property
    def cyc(self):
        return len(self.reg_hist)-1
    @property
    def sum_of_strength(self):
        relevant_strengths = range(20,self.cyc-1,self.width_line)
        sum_of_strength = sum([self.reg_hist[x-1]*x for x in relevant_strengths])
        return sum_of_strength

    @property
    def render_matrix(self):
        render_matrix = list()
        # calc positions
        position = 0
        for sprite in self.reg_hist:
            range_render = [sprite-1, sprite , sprite+1]
            b_render = position in range_render
            render_matrix.append(b_render)
            
            position +=1
            if position >= self.width_line:
                position = 0
            # end if
        # end for
        return render_matrix

        

if __name__=='__main__':
    with open('In10.txt') as f:
        lines_ws = f.readlines()
        lines = list(map(str.rstrip, lines_ws))

        # create object
        Ex10 = Exercise_Ten()

        for line in lines:
            Ex10.parse_input(line)
            # Ex10.print_reg_and_cyc()

    # end with
    Ex10.print_sum_of_strength()
    Ex10.render()


    
