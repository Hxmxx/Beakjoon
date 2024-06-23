#include <stdio.h>
#

int main(){
    int n, m, a, b, num;
    int arr[101]={0,};
    scanf("%d %d", &n, &m);

    for(int i=1; i<=m; i++){
        scanf("%d %d %d", &a, &b, &num);
        for(int j=a; j<=b; j++) arr[j]=num;
    }

    for(int i=1; i<=n; i++) printf("%d ", arr[i]);

    return 0;
}