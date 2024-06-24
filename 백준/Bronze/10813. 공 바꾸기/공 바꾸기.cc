#include <stdio.h>
#

int main(){
    int n, m, a, b, temp;
    int arr[101]={0, };
    scanf("%d %d", &n, &m);
    for(int i=1; i<=n; i++){
        arr[i]=i;
    }
    for(int i=1; i<=m; i++){
            scanf("%d %d", &a, &b);
        temp=arr[a];
        arr[a]=arr[b];
        arr[b]=temp;
    }

    for(int i=1; i<=n; i++)
        printf("%d ",arr[i]);

    return 0;
}