a = [
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
]

''' rotate_martrix_elements_clockwise '''
def rotate_martrix_elements_clockwise(graph, info):
    r, c, s = info
    lx, ly, rx, ry = r-s-1, c-s-1, r+s-1, c+s-1

    while lx < rx and ly < ry:
        t1, t2, t3 = graph[lx][ry], graph[rx][ry], graph[rx][ly]
        for y in range(ry, ly, -1):
            graph[lx][y] = graph[lx][y-1]
        for x in range(rx, lx, -1):
            graph[x][ry] = graph[x-1][ry]
        graph[lx+1][ry] = t1
        for y in range(ly, ry):
            graph[rx][y] = graph[rx][y+1]
        graph[rx][ry-1] = t2
        for x in range(lx, rx):
            graph[x][ly] = graph[x+1][ly]
        graph[rx-1][ly] = t3
        lx, ly, rx, ry = lx+1, ly+1, rx-1, ry-1
        
    return graph

matrix = rotate_martrix_element_clockwise(a, (4, 5, 2))

for row in matrix:
    print(row)
    
''' OUTPUT

[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 3, 4, 5, 6]
[1, 2, 3, 4, 4, 5, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 5, 6, 6, 7]
[1, 2, 4, 5, 6, 7, 7]
[1, 2, 3, 4, 5, 6, 7]

'''