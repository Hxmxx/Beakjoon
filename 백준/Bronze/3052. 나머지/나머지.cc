#include <stdio.h>

int main(void) {

    int n, sum=0;
    int arr[10];

    for(int i=0; i<10; i++) {
        scanf("%d", &n);
        arr[i] = (n % 42);
    }

    for(int i=0; i<10; i++) {
        int cnt=0; // 초기화
        for(int j=i+1; j<10; j++) {
            if(arr[i] == arr[j]) cnt++;
        }
        if (cnt == 0) sum++;
    }

    printf("%d", sum);

    return 0;
}

