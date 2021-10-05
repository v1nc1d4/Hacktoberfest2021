#include<bits/stdc++.h>
#include<string>
using namespace std;
#define int long long


void solve()
{
	
	int n;
	cin >> n ;
	int a[n];
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}
	for (int i = 0; i < n - 1; i++)
	{
		int min = i;

		for (int j = i + 1; j < n; j++)
		{
			if (a[j] < a[min])
			{
				min = j;
			}
		}
		if (min != i)
		{
			swap(a[i], a[min]);
		}
	}
	for (int i = 0; i < n; i++)
	{
		cout << a[i] << " ";
	}
	cout << endl;




}


signed main()

{
	solve();



}


/* Time Complexity
  Best Case : O(n*n)
  Average Case : O(n*n)
  Worst Case : O(n)
 
  Space Complexity : O(1)
 */


/* Sample Input 
  7
  5 3 4 1 2 9 7
  Sample Output
  1 2 3 4 5 7 9
*/
