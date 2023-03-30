'''
4 4
0100
0111
1110
0010
'''

n, m = map(int, input().split())    # n은 행, m은 열
arr = []
for _ in range(n):
    s = input()
    arr.append(list(map(int, list(s))))
# 주어진 값들 2차원 배열로 만들기
# => [[0, 1, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 0, 1, 0]]

# 앞서 만들었던 2차원 배열보다 x,y 값이 1씩 큰 2차원 배열 생성
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

side = 0                    # 한 변의 최대 길이를 저장할 변수 

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i - 1][j - 1] == 1:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
 
            if dp[i][j] > side:     # 만약 이미 구한 최대변 보다 큰 값이 나오면 갱신
                side = dp[i][j]
print(side**2)
# 최종적인 dp 모습
# [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 1, 2, 0], [0, 0, 0, 1, 0]]
