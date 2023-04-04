#include <iostream>
#include <math.h>
#include <stack>
using namespace std;
#define pii pair<int, int>
#define INF 2147483647

int N, W, dp[1001][1001]{ 0, }, ans = INF;
pii work[1001], dp2[1001][1001];
stack<int> stk;

int dist(pii a, pii b) {
	return abs(a.first - b.first) + abs(a.second - b.second);
}

int main() {
	scanf("%d%d", &N, &W);
	for (int i = 1; i <= W; i++) scanf("%d%d", &work[i].first, &work[i].second);

	dp[1][0] = dist({ 1,1 }, work[1]);
	dp[0][1] = dist({N,N}, work[1]);
	dp[0][0] = dp[1][1] = INF;
	dp2[1][0] = dp2[0][1] = { 0,0 };

	
	for (int i = 2; i <= W; i++) {
		dp[i][i] = INF;
		for (int j = 0; j < i; j++) {
			if (j < i - 1) {
				dp[i][j] = dp[i - 1][j] + dist(work[i], work[i - 1]);
				dp[j][i] = dp[j][i - 1] + dist(work[i], work[i - 1]);
				dp2[j][i] = { j, i - 1 };
				dp2[i][j] = { i - 1,j };
			}
			else {
				int min1 = INF, min2 = INF, idx1, idx2;
				for (int h = 0; h < i - 1; h++) {
					if (!h) {
						int d1 = dist({ 1,1 }, work[i]), dN = dist({ N,N }, work[i]);
						if (dp[h][j] + d1 < min1) { min1 = dp[h][j] + d1, idx1 = h; }
						if (dp[j][h] + dN < min2) { min2 = dp[j][h] + dN, idx2 = h; }
					}
					else
					{
						int dh = dist(work[h], work[i]);
						if (dp[h][j] + dh < min1) { min1 = dp[h][j] + dh, idx1 = h; }
						if (dp[j][h] + dh < min2) { min2 = dp[j][h] + dh, idx2 = h; }
					}
				}
				dp[i][j] = min1, dp[j][i] = min2;
				dp2[i][j] = { idx1,j };
				dp2[j][i] = { j ,idx2 };
			}
		}
	}
	int anx, any;
	for (int i = 0; i <= W; i++) {
		if (ans > dp[W][i]) { ans = dp[W][i]; anx = W, any = i; }
		if (ans > dp[i][W]) { ans = dp[i][W], anx = i, any = W; }
	}
	printf("%d\n", ans);
	
	while (anx || any) {
		if (anx > any) stk.push(1);
		else stk.push(2);
		int tmpx = anx;
		anx= dp2[tmpx][any].first;
		any = dp2[tmpx][any].second;
	}

	while (!stk.empty()) {
		printf("%d\n", stk.top());
		stk.pop();
	}

}
