import sys
from pprint import pprint
sys.stdin = open('init.txt', 'r')
#####
w, h = map(int, input().split())

# 뒤에 2개는 상태인자. 방향전환 가능여부와 바라보는방향
dp = [[[[0, 0], [0, 0]] for _ in range(w)] for _ in range(h)]

# pprint(dp)

# init
for col in range(1, w):
    dp[0][col][1][1] = 1
for row in range(1, h):
    dp[row][0][1][1] = 1
pprint(dp)

for i in range(1, w):
    for j in range(1, h):
        # 방향전환이 가능하고 북쪽 방향을 보는 애들은 남쪽에서 쭉 온 애들이랑 남족에서 왔는데 방향전환 불가능하던 애들.
        dp[i][j][0][0] = (dp[i - 1][j][0][0] + dp[i - 1][j][1][0]) % 100000
        # 방향전환 가능하고 동쪽 보는애드은 동쪽에서 쭉왔거나 동쪽에서 왔는데 방향전환 불가능해서 쭉온애들
        dp[i][j][0][1] = (dp[i][j - 1][0][1] + dp[i][j - 1][1][1]) % 100000
        # 방향전환 불가능한데 북쪽보는 애들은 남쪽에서 올라온 애들중에 동쪽 보고 있던 애들
        dp[i][j][1][0] = (dp[i - 1][j][0][1]) % 100000
        # 방향전환 불가능한데 동쪽보는 애들은 동쪽에서 왔는데 원래 북쪽 보던애들.
        dp[i][j][1][1] = (dp[i][j - 1][0][0]) % 100000
        pass
ans = sum(dp[h-1][w-1][0]) + sum(dp[h-1][w-1][1])       # 도착지점에서의 모든 경우의 수의 합
print(ans % 100000)
