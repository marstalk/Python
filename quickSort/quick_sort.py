

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for i in range(1, len(arr)):
            if arr[i] <= pivot:
                less.append(arr[i])
            else:
                greater.append(arr[i])
    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([2,5,8,24,46,79,134,790,22,34,6,76,]))