#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b){
    int num1 = *(int*)a;
    int num2 = *(int*)b;

    if(num1 < num2)
        return -1;
    if(num1 > num2)
        return 1;

    return 0;
}

int main(){
    int N;
    scanf("%d", &N);

    int arr[100000] = {0};

    for(int i = 0; i < N; i++){
        scanf("%d", &arr[i]);
    }
        
    qsort(arr, N, sizeof(int), compare);

    long long count = arr[0] - 1;
    arr[0] = 1;

    for(int i = 1; i < N; i++){
        if(arr[i] == arr[i-1])
            continue;

        count += arr[i] - arr[i - 1] - 1;
        arr[i] = arr[i-1] + 1;
    }

    printf("%lld\n", count);

    return 0;
}