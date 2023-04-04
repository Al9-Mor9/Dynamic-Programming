#include <stdio.h>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

int A, num;
vector<int> LCS;
vector<int> nums;
vector<int> order;
stack<int> ans;

int main() {
	scanf("%d", &A);

	for (int i = 0; i < A; i++) {
		scanf("%d", &num);	
		nums.push_back(num);
		if (LCS.empty() || LCS.back() < num) { LCS.push_back(num); }
		else {
			vector<int>::iterator iter = lower_bound(LCS.begin(), LCS.end(), num);
			*iter = num;
		}
		vector<int>::iterator iter = lower_bound(LCS.begin(), LCS.end(), num);
		order.push_back(iter - LCS.begin()+1);

	}
	int size = LCS.size();
	printf("%d\n", size);
	
	for (int i = A - 1; i >= 0; i--) {
		if (order[i] == size) {
			ans.push(nums[i]);
			size--;
		}
	}

	while (!ans.empty()) {
		printf("%d ", ans.top());
		ans.pop();
	}


}
