#include <stdio.h>
#include<math.h>
int main(void) {
    int t,n[20],x,i;	// your code goes here
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    scanf("%d",&n[i]);
    for(i=1;i<=t;i++){
    x=sqrt(n[i]);
        printf("%d\n",x);
    }
	return 0;
}

