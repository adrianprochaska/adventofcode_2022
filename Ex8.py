import numpy as np

def calc_scenic_val(this_tree, view):
    if len(view)>1:
        idx_view = this_tree > view
        scenic_cumsum = np.cumsum(idx_view)
        scenic_val = next((scenic_cumsum[idx] for idx, val in enumerate(idx_view) if val == 0), len(view)-1)+1
    else:
        scenic_val=1
    return scenic_val

ary_trees = np.genfromtxt('In8.txt', delimiter=1, dtype=int)

# generate array of boolean values with the borders as one
ary_bool = ary_trees > 10
ary_bool[:,0] = True
ary_bool[:,-1] = True
ary_bool[0,:] = True
ary_bool[-1,:] = True

n_row, n_col = ary_trees.shape

ary_scenic = np.zeros((n_row,n_col))


for row in range(1,n_row-1):
    for col in range(1, n_col-1):
        this_tree = ary_trees[row,col]
        # are all left smaller
        b_lft = all(this_tree > ary_trees[row,:col])
        # are all right smaller
        b_rgt = all(this_tree > ary_trees[row,col+1:])
        # are all above smaller
        b_abv = all(this_tree > ary_trees[:row,col])
        # are all below smaller
        b_blw = all(this_tree > ary_trees[row+1:,col])
        
        # is any of the booleans true
        b_visible = b_lft or b_rgt or b_abv or b_blw

        ary_bool[row,col] = b_visible

        ### Part II ###
        # Scenic score
        # left
        sc_lft = calc_scenic_val(this_tree,ary_trees[row,range(col-1,-1,-1)])
        # right
        sc_rgt = calc_scenic_val(this_tree,ary_trees[row,range(col+1,n_col)])
        # above
        sc_abv = calc_scenic_val(this_tree,ary_trees[range(row-1,-1,-1),col])
        # below
        sc_blw = calc_scenic_val(this_tree,ary_trees[range(row+1,n_row),col])

        scenic_final = sc_lft * sc_rgt * sc_abv * sc_blw

        ary_scenic[row,col] = scenic_final

n_visible = sum(sum(ary_bool))

print(str(n_visible) + ' trees are visible!')

max_scenic = ary_scenic.max()

print(str(max_scenic) + ' is the maximum scenic score!')

pass