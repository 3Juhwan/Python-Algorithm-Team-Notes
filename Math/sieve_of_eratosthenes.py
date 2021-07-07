import math

n = 1000    # 2부터 n까지의 숫자 중 소수 판별
array = [True for _ in range(n + 1)]    # 0, 1을 제외한 모든 수를 True로 초기화

for i in range(2, int(math.sqrt(n)) + 1):    # 2부터 n의 제곱근까지 탐색
    if array[i] == True:    # i가 소수인 경우
        # i를 제외한 i의 모든 배수 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i] == True:
        print(i, end=' ')