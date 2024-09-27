def d_array_find_parent(child_index, dimension_of_heap):
    return (child_index - 1) // dimension_of_heap

def d_array_find_ith_child(parent_index, index, dimension_of_heap):
    return parent_index * dimension_of_heap + index + 1

