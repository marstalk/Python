

def find_smallest(arr):
    smallest_value = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_index = i
    return smallest_index


def collection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


print(collection_sort([2,4,5,8,9,2,3,4,8,2,45,6,88,6,1,76]))