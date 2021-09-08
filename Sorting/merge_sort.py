arr = [5, 34, 4, 23, 4, 5, 3]

''' Merge Sort '''
def merge(left, right):
    i, j = [0] * 2
    sorted_list = []

    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    if len(left) > i:
        sorted_list.extend(left[i:])

    if len(right) > j:
        sorted_list.extend(right[j:])

    return sorted_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])

    return merge(left_list, right_list)

print(merge_sort(arr))

'''OUTPUT

[3, 4, 4, 5, 5, 23, 34]

'''