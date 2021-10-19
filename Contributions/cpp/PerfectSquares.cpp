// Leetcode Problem 279

#include<bits/stdc++.h>
using namespace std;

 int numSquares(int n) {
          int dp[n + 1];
           dp[0] = 0;
           for(int i=1;i<=n;i++){
            dp[i] = INT_MAX;
            for(int j=1;j*j<=i;j++){
                dp[i] = min(dp[i], dp[i-j*j]+1);
            }
        }
        return dp[n];
    }

int main() {
	// your code goes here
	int n ;
	 cin>>n;
	 cout << numSquares(n);
	return 0;
}
