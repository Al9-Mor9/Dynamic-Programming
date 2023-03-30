#include <iostream>
using namespace std;

int N;
long long A[2000];
long long dp[2000][2000];
long long ans = 0;

long long max(long long a, long long b) {
	return a > b ? a : b;
}

long long min(long long a, long long b){
    return a < b ? a : b;
}

int main(){

	scanf("%d", &N);
	for (int i = 0; i < N; i++){
		scanf("%lld", &A[i]);
	}

    for (int len = 0; len < N; len++){
        for (int i = 0; i < N; i++) {
			int j = (i + len) % N;
            if (len == 0) dp[i][j] = A[i];
            else if (len == 1) dp[i][j] = max(A[i], A[j]); 
			else {
                pair<int, int> case1, case2; //맨 앞에거 가져 갔다고 하자
                if (A[i+1] > A[j]) case1 = {(i + 2) % N, j};
                else case1 = {(i + 1) % N, (j - 1 + N) % N};

                if (A[i] > A[j-1]) case2 = {(i + 1) % N, j - 1};
                else case2 = {i, (j - 2 + N) % N };

                dp[i][j] = max(dp[i][i] + dp[case1.first][case1.second], dp[j][j] + dp[case2.first][case2.second]); 
            }
			if (len == N - 1) ans = max(ans, dp[i][j]); 
		}
	}
	printf("%lld", ans);	

}
