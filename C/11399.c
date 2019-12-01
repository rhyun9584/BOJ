#include <stdio.h>
#include <stdlib.h>

int compare(const void* first, const void* second){
    if(*(int*)first > *(int*)second)
        return 1;
    else if(*(int*)first < *(int*)second)
        return -1;
    else
        return 0;

}

int main(){
    int N;
    int sum = 0;
    int P[1001] = {0};

    scanf("%d", &N);

    for(int i = 0; i < N; i++){
        scanf("%d", &P[i]);
    }

    qsort(P, N, sizeof(int), compare);

    for(int i = 0; i < N; i++){
        sum += P[i] * (N-i);
    }

    printf("%d\n", sum);

    return 0;
}