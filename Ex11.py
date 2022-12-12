import math
class Monkey():
    def __init__(self, l_item, operation, test_divisor, tgt_true, tgt_false) -> None:
        self.n_inspect = 0
        self.new_items = l_item
        self.old_items = []
        self.operation = operation
        self.test_divisor = test_divisor
        self.test = lambda x : self.test_fun(x, test_divisor)
        self.tgt_true = tgt_true
        self.tgt_false = tgt_false

        return 
    
    def take_turns(self):
        self.old_items = self.new_items
        self.new_items = []
        
        if len(self.old_items) > len(set(self.old_items)):
            print('Items are non unique!')
        # end if

        # operation on all 
        self.old_items = list(map(self.operation, self.old_items))

        # general relief of worry level
        # self.old_items = list(map(lambda x : int(x/3), self.old_items))

        # test worry level
        l_test_results = list(map(self.test, self.old_items))

        
        
        # decide on new targets
        l_targets = list(map(
            lambda x : self.tgt_true if x else self.tgt_false,
            l_test_results
            ))

        # increase n_inspect counter and release old items
        self.n_inspect += len(self.old_items)
        l_pass_items = self.old_items
        self.old_items = []

        return l_pass_items, l_targets

    def test_fun(self, test_dividend, test_divisor):
        remainder = test_dividend % test_divisor
        b_result = remainder == 0
        if b_result:
            result = test_dividend
        else:
            result = remainder

        return b_result

    def add_new_item(self, worry_lvl):
        self.new_items.append(worry_lvl)
        return

    def print_current_state(self):

        pass

class Game():
    def __init__(self, input) -> None:
        self.general_divisor = 1
        self.monkeys = self.input_parser(input)
        self.counter_rounds = 0
        
        return 

    def input_parser(self, input):
        monkey_count = 0
        monkeys = []
        n_lines_per_monkey = 7
        general_divisor = 1
        while monkey_count < int(len(input)/n_lines_per_monkey):
            idx_strt = monkey_count *n_lines_per_monkey
            
            str_items = input[idx_strt+1]
            items = list(map(int, str_items.split(': ')[1].split(', ')))
            
            str_operation = input[idx_strt+2]
            operation = eval(
                'lambda old : {}'.format(
                    str_operation.split('new = ')[1]
                )
            )
            
            str_divisor = input[idx_strt+3]
            test_divisor = int(str_divisor.split('by ')[1])

            tgt_fun = lambda x : int(x.split('monkey ')[1])
            str_tgt_true = input[idx_strt+4]
            tgt_true = tgt_fun(str_tgt_true)
            
            str_tgt_false = input[idx_strt+5]
            tgt_false = tgt_fun(str_tgt_false)

            monkeys.append(Monkey(
                items, 
                operation, 
                test_divisor, 
                tgt_true, 
                tgt_false
                ))
            
            general_divisor *= test_divisor

            monkey_count += 1
        # end while
        self.general_divisor = general_divisor
        return monkeys

    def play_round(self):
        for monkey in self.monkeys:
            l_test_results, l_targets = monkey.take_turns()
            self.pass_items(l_test_results, l_targets)
        # end for
        self.counter_rounds += 1
        # self.print_state()
        return
        
    def pass_items(self, l_test_results, l_targets):
        for tgt, worry_lvl in zip(l_targets, l_test_results):
            remainder = worry_lvl%self.general_divisor
            worry_lvl_mod = remainder if remainder > 1 else worry_lvl
            self.monkeys[tgt].add_new_item(worry_lvl_mod)
        # end for
        return


    def play_rounds(self, n_round):
        counter = 0
        while counter < n_round:
            self.play_round()
            # self.print_state()
            counter += 1
        # end while
        return
    
    def print_n_result(self):
        print(
            'Level of monkey business {:9}'.format(
                self.lvl_monkey_business
            ))
        return

    @property
    def lvl_monkey_business(self):
        lvl_monkey_business = 1
        l_inspect = []
        for monkey in self.monkeys:
            l_inspect.append(monkey.n_inspect)
        # end for
        l_inspect.sort(reverse=True)
        lvl_monkey_business = l_inspect[0]*l_inspect[1]
        return lvl_monkey_business

    def print_state(self):
        print('Played rounds: {:2}'.format(
            self.counter_rounds
        ))
        str_2_print = ''
        for idx, monkey in enumerate(self.monkeys):
            str_2_print += 'Monkey {:2}: '.format(idx)
            for item in monkey.new_items:
                str_2_print += '{:3}, '.format(item)
            # end for
            str_2_print = str_2_print[:-2] + '\n'
        # end for
        str_2_print += '\n'
        print(str_2_print)
        return
        
if __name__ == '__main__':
    with open('In11.txt') as f:
        lines_dirty = f.readlines()
        lines = list(map(str.rstrip, lines_dirty))
        Ex11 = Game(lines)
    # end with
    Ex11.play_rounds(10000)
    Ex11.print_n_result()
# end if