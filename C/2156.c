#include <stdio.h>

int max(int x, int y){
    if(x > y)
        return x;
    else
        return y;
}

int main(){
    int N;
    int grape[10001] = {0};
    int drink[10001] = {0};

    scanf("%d", &N);

    for(int i = 1; i <= N; i++){
        scanf("%d", &grape[i]);
    }

    drink[1] = grape[1];
    drink[2] = grape[2] + grape[1];

    for(int i = 3; i <= N; i++){
        drink[i] = max(drink[i-2] + grape[i], drink[i-3] + grape[i-1] + grape[i]);
        drink[i] = max(drink[i-1], drink[i]);
    }

    printf("%d\n", drink[N]);

    return 0;
}