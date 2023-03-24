#include <iostream>
using namespace std;

int H, W, N;
int town[1001][1001];
int dp[1001][1001];

int main(){
	scanf("%d%d%d", &H, &W, &N);
	for (int i = 1; i <= H; i++){
		for (int j = 1; j <= W; j++){
			scanf("%d", &town[i][j]);
			//0 아래쪽, 1 오른쪽
		}
	}

	dp[1][1] = N-1; 
	for (int i = 1; i <= H; i++){
		for (int j = 1; j <= W; j++){
			if (i == 1 && j == 1) continue;
			int fromUp = dp[i-1][j];
			if (fromUp % 2 && town[i-1][j] == 0) dp[i][j] += fromUp/2 + 1;
			else  dp[i][j] += fromUp/2;

			int fromLeft = dp[i][j-1];
			if (fromLeft % 2 && town[i][j-1] == 1) dp[i][j] += fromLeft/2 + 1;
			else dp[i][j] += fromLeft/2;
		}
	}

	for (int i = 1; i <= H; i++){
		for (int j = 1; j <= W; j++) {
			if (dp[i][j] % 2) town[i][j] = 1 - town[i][j];
		}
	}


	int x = 1, y = 1;
	while (x != H + 1 && y != W + 1){
		if (town[x][y]) y++;
		else x++;
	}

	printf("%d %d", x, y);
}
