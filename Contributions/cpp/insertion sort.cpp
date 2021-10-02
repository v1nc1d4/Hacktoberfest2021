#include<bits/stdc++.h>
using namespace std;

void solve(int a[], int n){
	for(int i=0; i<n-1; i++){
		for(int j=0; j<n-i-1; j++){
			if(a[j]>a[j+1]){
				int temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;				
			}
		}
	}
}

int main(){
	int a[] = {64, 25, 12, 22, 11};
	int s = sizeof(a)/sizeof(a[0]);
	solve(a,s);
	for(int i=0; i<s; i++){
		cout<<a[i]<<" ";
	}
	return 0;
}
