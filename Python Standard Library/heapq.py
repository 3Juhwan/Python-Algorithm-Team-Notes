import heapq

def heapsort(iterable):
    h = []
    result = []
    
    for value in iterable:
        heapq.heappush(h, value)
        
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

'''OUTPUT

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

'''최대힙은 다음과 같이 코드를 수정

    ...
        heapq.heappush(h, -value)
    
    ...
        result.append(-heapq.heappop(h))

'''