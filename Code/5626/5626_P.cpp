#include <iostream>
using namespace std;
#define mod 1000000007

int N;
int h[10000];
long long dp[2][10000];

int min(int a, int b){
    return a < b ? a : b;
}

int main(){
    scanf("%d", &N);
    for (int i = 0; i < N; i++){
        scanf("%d", &h[i]);
        if ((!i || i == N - 1) && h[i] > 0) {
            printf("0");
            return 0;
        }
    }
    for (int i = 0; i < N; i++){
        if (!i) dp[1][0] = 1;
        else if (h[i] > -1){
            if (!h[i]) dp[1][h[i]] = dp[0][h[i]] + dp[0][h[i]+1];
            else dp[1][h[i]] = dp[0][h[i]-1] + dp[0][h[i]] + dp[0][h[i]+1];
            dp[1][h[i]] %= mod;
        }
        else {
            for (int j = 0; j < N; j++){
                if (j) {
                    dp[1][j + 1] += dp[0][j];
                    dp[1][j + 1] %= mod;
                    dp[1][j] += dp[0][j];
                    dp[1][j] %= mod;
                    dp[1][j - 1] += dp[0][j];
                    dp[1][j - 1] %= mod;
                }
                else {
                    dp[1][j + 1] += dp[0][j];
                    dp[1][j + 1] %= mod;
                    dp[1][j] += dp[0][j];
                    dp[1][j] %= mod;
                }
            }
        }
        for (int j = 0; j < 10000; j++) {
            dp[0][j] = dp[1][j];
            dp[1][j] = 0;
        } 
    }
    printf("%lld", dp[0][0]);
}
