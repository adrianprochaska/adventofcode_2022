global directories
global pointer
global current_dict
global list_dir_sizes

directories = {'files' : [], 'dirs':{}, 'size':0, 'total_size':0}
current_dict = directories
pointer = ''
list_dir_sizes = []

def move_in(str_dir):
    global directories
    global pointer
    global current_dict
    global list_dir_sizes

    print('move in')
    current_dict['dirs'][str_dir] = {'files' : [], 'dirs':{}, 'size':0, 'total_size':0}
    current_dict = current_dict['dirs'][str_dir]
    pointer += '/' + str_dir

def move_out():
    global directories
    global pointer
    global current_dict
    global list_dir_sizes

    print('move out')
    # calc file size
    current_dict['size'] = sum([x[1] for x in current_dict['files']])

    # calc total size
    dirs_size = sum([current_dict['dirs'][keys]['total_size'] for keys in current_dict['dirs']])
    current_dict['total_size'] = dirs_size + current_dict['size']

    list_dir_sizes.append(current_dict['total_size'])

    # pointer

    pointer_old = pointer.split('/')
    pointer_old.pop()
    if len(pointer_old)>0:
        pointer_old.pop(0)
    pointer = ''
    current_dict = directories
    for dir_letter in pointer_old:
        current_dict = current_dict['dirs'][dir_letter]
        pointer += '/' + dir_letter
    # end for


def get_dir():
    pass

def total_size():
    pass

def create_dir():
    pass

def add_file(str_input):
    global directories
    global pointer
    global current_dict
    global list_dir_sizes

    size, name = str_input.split()
    current_dict['files'].append([name, int(size)])

def move_out_total():
    while len(pointer) > 0:
        move_out()
    # end while
    move_out()

with open('In7.txt') as f:
    list_of_lines = list(map(str.rstrip, f.readlines()))
    while len(list_of_lines) > 0:
        current_command = list_of_lines.pop(0)
        if not '$' == current_command[0]:
            print('Something went terribly wrong.')
        # end if

        if 'cd' in current_command:
            # this is a moving command
            if '/' in current_command:
                # do nothing, this is the starting command
                pass
            elif '..' in current_command:
                # moving out
                move_out()
            else:
                # get the directory letter and move in
                dir_command = current_command.split()
                move_in(dir_command[-1])
            # end if


        elif 'ls' in current_command:
            # This is a list command
            # get all the console output

            # ignore all the dirs
            while len(list_of_lines) > 0 and not list_of_lines[0][0] == '$':
                str_cur_file = list_of_lines.pop(0)
                if not 'dir' in str_cur_file:
                    add_file(str_cur_file)

                else:
                    # do nothing
                    pass
                # end if
            # end while
        # end if
    # end while
    move_out_total()

print(list(enumerate(list_dir_sizes)))
list_dir_sizes.sort()

print(sum([x for x in list_dir_sizes if x<100000]))

allowed_used_space = 70000000-30000000
necessary_space = directories['total_size']-allowed_used_space

dir_size_to_delete = next(x for x in list_dir_sizes if x>= necessary_space)
print(dir_size_to_delete)
pass
