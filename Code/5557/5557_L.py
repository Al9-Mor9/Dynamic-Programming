import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
target = arr[-1]

dp = [[0] * 21 for _ in range(n)]
dp[0][arr[0]] = 1

for i in range(n - 2):
    for j in range(21):
        if dp[i][j]:
            if arr[i + 1] + j <= 20:
                dp[i + 1][arr[i + 1] + j] += dp[i][j]
            if - arr[i + 1] + j >= 0:
                dp[i + 1][- arr[i + 1] + j] += dp[i][j]
print(dp[n-2][target])

# for visualize
print(' ' * 6,end='')
for i in range(21):
    print(" %-2s" % i, end = '')

for i in range(n):
    print("\n %-2s" % arr[i], end=' : ')
    for j in range(21):
        if dp[i][j]:
            print(" %-2s" % dp[i][j], end = '')
        else:
            print(" - ", end = '')