arr = [1, 2, 3, 4, 5, 6, 7]
tree = [0] * 16

'''Prefix Sum with Segment Tree'''
def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]


def getSum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return getSum(start, mid, node*2, left, right) + getSum(mid+1, end, node*2+1, left, right)


def update(start, end, node, index, dif):
    if index < start or index > end:
        return -1
    tree[node] += dif
    if start == end:
        return -1
    mid = (start + end) // 2
    update(start, mid, node*2, index, dif)
    update(mid+1, end, node*2+1, index, dif)


init(0, len(arr)-1, 1)

print(tree)
print(getSum(0, len(arr)-1, 1, 2, 5))

'''OUTPUT

[0, 28, 10, 18, 3, 7, 11, 7, 1, 2, 3, 4, 5, 6, 0, 0]
18 (3+4+5+6)

'''