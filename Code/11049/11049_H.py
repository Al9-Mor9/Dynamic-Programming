import sys
from pprint import pprint

sys.stdin = open('input.txt', 'r')
#####
import sys
input = sys.stdin.readline
inf = float('inf')
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]

for i in range(1, n):  # row / col이 아닌 대각선을 반복한다고 생각
    for j in range(0, n - i):  # 대각선에서 몇 번째 열?
        print(i, j)
        if i == 1:  # 차이가 1밖에 나지 않는 칸은 직접 곱하여 넣음
            dp[j][j + i] = arr[j][0] * arr[j][1] * arr[j + i][1]
            continue

        dp[j][j + i] = inf
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + arr[j][0] * arr[k][1] * arr[j + i][1])

        # for z in dp:
        #     print(z)
        # print()
print(dp[0][n - 1])  # 맨 오른쪽 위