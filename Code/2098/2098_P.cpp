#include <iostream>
using namespace std;
#define INF 987654321

int N, W[16][16], dp[16][65536]{ 0, };

int min(int a, int b) {
	return a < b ? a : b;
}

int TSP(int cur, int visited) {
	if (visited == (1 << N) - 1) {
		if (W[cur][0]) return W[cur][0];
		else return INF;
	}
	
	int &ret = dp[cur][visited];
	if (ret) return ret;
	
	ret = INF;

	for (int i = 0; i < N; i++) {
		if (!W[cur][i]) continue;
		if (visited & (1 << i)) continue;
		ret = min(ret, TSP(i,visited|(1<<i)) + W[cur][i]);
	}
	return ret;

}

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) scanf("%d", &W[i][j]);
	}
	printf("%d", TSP(0, 1));

}
