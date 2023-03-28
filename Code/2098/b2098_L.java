package Beakjun;
import java.io.*;
import java.util.*;

public class b2098 {

	static int n;
	static final int INF = 1000000 * 16;
	static int[][] dp;
	static int[][] arr;
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		n = Integer.parseInt(br.readLine());
		arr = new int [n][n];
		dp = new int[n][(1<<n)-1];
		
		for (int i = 0; i < n; i ++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j ++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		// -1로 전 구간 초기화
		for (int i = 0; i < n; i ++) {
			Arrays.fill(dp[i], -1);
		}
		// 현재 노드와 방문한 장소 넣어주기
		bw.write(dfs(0, 1)  +"\n");		
		bw.flush();
		br.close();
		bw.close();
		
	}
	// 현재 cur 노드에서, visit를 방문하고 난 상태를 의미
	static int dfs(int cur, int visit) {
		
		// 모든 도시에 도착한 경우 5개 도시 -> 11111
		// 다 들렸기 때문에 이제 0으로 돌아가는 경로를 계산해야한다.
		if (visit == (1<<n) - 1) {
			// 현재 노드에서 0 으로 가는 경로가 없다면 INF 반환.
			if (arr[cur][0] == 0) {
				return INF;
			} else {
				return arr[cur][0];				
			}
		}
		
		// 첫 방문이 아니라면, 값을 반환해주자. 처음 진행시 모두 첫 방문이므로 가장 깊숙히 들어감.
		if (dp[cur][visit] != -1) {
			return dp[cur][visit];
		} else {
			dp[cur][visit] = INF;
		}
				
		// 어디로 갈지 정하기
		for(int i = 0; i < n; i ++) {
			// i번 노드를 방문하지 않았고, 가는 경로가 있다면, 
			if ((visit & (1 << i)) == 0 && arr[cur][i] !=0 ) {
				// 최소값을 갱신해주자.
				// dfs(i, visit | (1 << i)) : i를 방문했을 때 값과 현재 INF를 갱신하자.
				// 어짜피 다른 i1, i2로 가도 나머지 다 돌고 1로 갈 때까지의 최소값을 반환하므로, 
				// 다른 경로를 비교해 봐도 된다. 
				// 즉 여기서 dp[cur][visit]는 cur에서 visit외에 곳을 방문하고 들어가는 최소 거리로 정의 할 수 있다.
				dp[cur][visit] = Math.min(dp[cur][visit], dfs(i, visit | (1 << i)) + arr[cur][i]);
			}
		}
		return dp[cur][visit];
	}
}




