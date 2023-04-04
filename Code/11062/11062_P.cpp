#include <iostream>
using namespace std;

int T, N;
int card[1000];
int dp[1000][1000];

int max(int a, int b){
	return a > b ? a : b;
}

int main(){
	scanf("%d", &T);
	while (T--){
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%d", &card[i]);
			for (int j = 0; j < N; j++){
				dp[i][j] = 0;
			}
		}

		for (int len = 0; len < N; len++){
			for (int start = 0; start + len < N; start++){
				if (!len){
					if (N % 2 == 1) dp[start][start] = card[start];
				}
				else if ((N - len) % 2 == 1) {//근우 턴  
					dp[start][start + len] = max(dp[start + 1][start + len] + card[start],
												dp[start][start + len - 1] + card[start + len]);
				}
				else {
					dp[start][start + len] = min(dp[start + 1][start + len], dp[start][start + len - 1]);
				}

			}
		}	
		printf("%d\n", dp[0][N-1]);
	}
}
