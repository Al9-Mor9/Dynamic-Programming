import sys
from pprint import pprint
sys.stdin = open('init.txt', 'r')
#####
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 0이상 20 이하
dp = [[0] * 21 for _ in range(n)]
# 8에 경우의 수 1 - 첫 번째 경우의 수는 반드시 포함
dp[0][arr[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j]:    # 경우의 수가 존재하면
            if 0 <= j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            if 0 <= j - arr[i] <= 20:
                dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[n - 2][arr[n - 1]])
