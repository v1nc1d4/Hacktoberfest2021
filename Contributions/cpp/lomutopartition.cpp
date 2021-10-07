#include<bits/stdc++.h>
using namespace std;
void swap(int *x, int *y)
{
    int *t;
    t = x;
    x = y;
    y = t;
}

int lp(int a[],int l,int h)
{
    int p=a[h];
    int i=l-1;
    for(int j=l;j<=h-1;j++)
    {
        if(a[j]<p)
        {
            i++;
            swap(a[j],a[i]);
        }
    }
    swap(a[h],a[i+1]);

    return i+1;
}

int main()
{
    int a[] = {2, 1, 3, 56, 43, 67, 22, 88, 55, 76, 2};
    int n = sizeof(a) / sizeof(a[0]);
    cout<<lp(a, 0,n-1)<<"\n";
    for (auto x : a)
        cout << x << " ";
    return 0;
}