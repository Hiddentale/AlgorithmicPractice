from random import randint as chooseRandomInteger


def choose_pivot(low, high):
	return chooseRandomInteger(low, high)

def partition(list_to_sort, low, high):

	chosen_pivot_index = list_to_sort[low]

	i = low + 1

	for j in range(low + 1, high + 1):
		if list_to_sort[j] <= chosen_pivot_index:
			list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
			i += 1
	final_pivot_position = i - 1

	list_to_sort[final_pivot_position], list_to_sort[low] = list_to_sort[low], list_to_sort[final_pivot_position]

	return final_pivot_position

def quicksort(list_to_sort, low, high):
	if low >= high:
		return 
	
	chosen_pivot_index = choose_pivot(low, high)

	list_to_sort[chosen_pivot_index], list_to_sort[low] = list_to_sort[low], list_to_sort[chosen_pivot_index]

	pivot_position = partition(list_to_sort, low, high)

	quicksort(list_to_sort, low, pivot_position - 1)
	quicksort(list_to_sort, pivot_position + 1, high)


def main():
	list_to_sort = [8, 7, 2, 9, 13, 1, 7, 8, 10, 6 , 3, 2, 11]
	quicksort(list_to_sort, 0, len(list_to_sort) - 1)
	print(list_to_sort)

main()