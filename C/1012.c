#include <stdio.h>

int M, N;

void adjacency(int arr[][50], int x, int y){
    arr[x][y] = 0;

    if(x > 0 && arr[x-1][y]) adjacency(arr, x-1, y);
    if(x < M-1 && arr[x+1][y]) adjacency(arr, x+1, y);
    if(y > 0 && arr[x][y-1]) adjacency(arr, x, y-1);
    if(y < N-1 && arr[x][y+1]) adjacency(arr, x, y+1);
}

int main(){
    int T;
    int K;
    int X, Y;
    int count;
    int field[50][50] = {0};

    scanf("%d", &T);

    for(int i = 0; i < T; i++){
        count = 0;
        
        scanf("%d %d %d", &M, &N, &K);

        for(int i = 0; i < K; i++){
            scanf("%d %d", &X, &Y);
            field[X][Y] = 1;
        }

        for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                if(field[i][j]){
                    count++;
                    adjacency(field, i, j);
                }
            }
        }

        printf("%d\n", count);
    }

    return 0;
}