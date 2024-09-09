def bubble_sort(array_to_sort):

    length_of_array = len(array_to_sort)
    
    for j in reversed(range(length_of_array)):

        still_unsorted = False

        for i in range(0, j):
            if array_to_sort[i] > array_to_sort[i + 1]:
                array_to_sort[i], array_to_sort[i + 1] = array_to_sort[i + 1], array_to_sort[i]
                still_unsorted = True
        if not still_unsorted:
            break
        
    return array_to_sort

bubble_sort([1, 2, 3, 4, 5, 6])