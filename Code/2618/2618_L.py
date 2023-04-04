import sys
sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
w = int(sys.stdin.readline())
q = [list(map(int, sys.stdin.readline().split())) for _ in range(w)]
dp = [[2e6] * (w + 1) for _ in range(w + 1)]
dp[0][0] = 0
history = [[''] * (w + 1) for _ in range(w + 1)]

dist1 = [[0] * (w + 1) for _ in range(w + 1)]
dist2 = [[0] * (w + 1) for _ in range(w + 1)]

q1 = [[1, 1]] + q
q2 = [[n, n]] + q
for i in range(w + 1):
    for j in range(i, w + 1):
        dist1[i][j] = abs(q1[i][0] - q1[j][0]) + abs(q1[i][1] - q1[j][1])
        dist2[i][j] = abs(q2[i][0] - q2[j][0]) + abs(q2[i][1] - q2[j][1])

for i in range(1, w + 1):
    dp[i][0] = dp[i-1][0] + dist1[i-1][i]
    dp[0][i] = dp[0][i-1] + dist2[i-1][i]
    history[i][0] = history[i-1][0] + '1'
    history[0][i] = history[0][i-1] + '2'    
    dp[i][i] = 0


for i in range(2, w + 1):
    # dp[i][i-1], dp[i-1][i]을 정의해야함. 
    for j in range(0, i - 1):
        if dp[i][i-1] > dp[j][i-1] + dist1[j][i]:
            dp[i][i-1] = dp[j][i-1] + dist1[j][i]
            tmp1 = j
        if dp[i-1][i] > dp[i-1][j] + dist2[j][i]:
            dp[i-1][i] = dp[i-1][j] + dist2[j][i]
            tmp2 = j
        history[i][i-1] = history[tmp1][i-1] + '1'
        history[i-1][i] = history[i-1][tmp2] + '2' 
        
    for j in range(i + 1, w + 1):
        dp[j][i-1] = dp[j-1][i-1] + dist1[j-1][j]
        dp[i-1][j] = dp[i-1][j-1] + dist2[j-1][j]
        history[j][i-1] = history[j-1][i-1] + "1"
        history[i-1][j] = history[i-1][j-1] + "2"

if dp[w][w-1] > dp[w-1][w]:
    hist = history[w-1][w]
else:
    hist = history[w][w-1]

print(min(dp[w][w-1], dp[w-1][w]))
for s in hist:
    print(s)