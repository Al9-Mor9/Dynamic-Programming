import sys
sys.stdin = open("input.txt", "r")
w, h = map(int, sys.stdin.readline().split())

dp = [[[0] * 4 for _ in range(h)] for _ in range(w)]
for i in range(w): dp[i][0][0] = 1
for i in range(h): dp[0][i][1] = 1
    
for i in range(1, w):
    for j in range(1, h):
        dp[i][j][0] = int((dp[i-1][j][0] + dp[i-1][j][2])%1e5)
        dp[i][j][1] = int((dp[i][j-1][1] + dp[i][j-1][3])%1e5)
        dp[i][j][2] = dp[i-1][j][1]
        dp[i][j][3] = dp[i][j-1][0]

for i in dp:
    print(i)

print(int(sum(dp[w-1][h-1])%1e5))
