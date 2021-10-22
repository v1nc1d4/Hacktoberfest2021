#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
    // Dynamic Programming (Memoization)
    int MCM(int t[][102], int arr[], int i, int j, int n){
        // if array has only one matrix
        if(i >= j){
            return 0;
        }

        if(t[i][j] != -1){
            return t[i][j];
        }

        int mn = INT_MAX;
        for(int k=i; k<j; k++){
            int temp = MCM(t, arr, i, k, n) + MCM(t, arr, k+1, j, n) + (arr[i-1] * arr[k] * arr[j]);
            if(temp < mn){
                mn = temp;
            }
        }
        t[i][j] = mn;
        return t[i][j];

    }
};

int main() {
    // Here you can alter the matrix size
    int t[102][102];
    memset(t, -1, sizeof(t));
    Solution obj;
    int size;
    cout<<"Enter the number of matrices: ";
    cin>>size;
    int arr[size+1];
    // Example for entering array elements:
    //[10 20 30 40 30] lets say this is the array
    // A1 = 10 x 20
    // A2 = 20 x 30
    //A3 = 30 x 40
    //A4 = 40 x 30
    cout<<"Enter the array elements: ";
    for(int i=0; i<size+1; i++){
        cin>>arr[i];
    }

    int ans = obj.MCM(t, arr, 1, size, size+1);
    cout<<"Answer is: "<<ans<<endl;

    return 0;
}
