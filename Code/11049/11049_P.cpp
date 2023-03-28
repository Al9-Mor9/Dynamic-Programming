#include <iostream>
using namespace std;

int N;
int matrix[501];
int dp[500][500]{ 0, };


int main() {

	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d %d", &matrix[i], &matrix[i+1]);
	}

	for (int j = 0; j < N; j++) {
		for (int i = 0; i < N; i++) {
			for (int mid = 0; mid < j; mid++) {
				if (i + mid < N - 1) {
					int min = dp[i][i + mid] + dp[mid + i +1][i+j] + matrix[i]*matrix[i+mid+1]*matrix[i+j+1];
					if (!dp[i][i + j]) dp[i][i + j] = min;
					else if (dp[i][i + j] > min) dp[i][i + j] = min;
				}
				else break;
			}
		}
	}
	
	printf("%d\n", dp[0][N - 1]);



}
