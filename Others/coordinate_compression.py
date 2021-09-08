arr = [1, 999999, 3, 82828, 4]

''' Coordinate Compression '''
def coordinate_compression(arr):
    x = list(sorted(set(arr)))
    x = {x[i]: i for i in range(len(x))}
    return [x[i] for i in arr]

print(coordinate_compression(arr))

'''OUTPUT

[0, 4, 1, 3, 2]

'''