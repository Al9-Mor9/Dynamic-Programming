import sys
sys.stdin = open('input.txt', 'r')
#####
n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n+1)]
mx = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i-1][j-1] == 1:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        mx = max(mx, dp[i][j])

print(mx**2)
