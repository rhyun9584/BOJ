#include <stdio.h>

int R, C; // row, column

void AirFlow(int arr[][50], int A){
    int addArr[50][50] = {0};

    for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
            if(arr[i][j] > 0){
                int addNum = arr[i][j] / 5;
                int count = 0;

                if(i > 0 && arr[i-1][j] >= 0){
                    addArr[i-1][j] += addNum;
                    count++;
                }
                if(i < R - 1 && arr[i+1][j] >= 0){
                    addArr[i+1][j] += addNum;
                    count++;
                }
                if(j > 0 && arr[i][j-1] >= 0){
                    addArr[i][j-1] += addNum;
                    count++;
                }
                if(j < C - 1 && arr[i][j+1] >= 0){
                    addArr[i][j+1] += addNum;
                    count++;
                }  

                arr[i][j] -= addNum * count;
            }
        }
    }

    for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
            if(arr[i][j] >= 0){
                arr[i][j] += addArr[i][j];
            }
        }
    }
}

void _GoRight(int arr[][50], int i, int j, int A, int flag);
void _GoLeft(int arr[][50], int i, int j, int A, int flag);
void _GoUp(int arr[][50], int i, int j, int A, int flag);
void _GoDown(int arr[][50], int i, int j, int A, int flag);

void _GoRight(int arr[][50], int i, int j, int A, int flag){
    if(j == C - 1){
        if(flag){// upper
            _GoUp(arr, i - 1, j, A, flag);
        }
        else{
            _GoDown(arr, i + 1, j, A, flag);
        }
    }
    else{
        _GoRight(arr, i, j + 1, A, flag);
    }
    arr[i][j] = arr[i][j-1];
}
void _GoLeft(int arr[][50], int i, int j, int A, int flag){
    if(j == 0){
        if(flag){// upper
            _GoDown(arr, i + 1, j, A, flag);
        }
        else{
            _GoUp(arr, i - 1, j, A, flag);
        }
    }
    else{
        _GoLeft(arr, i, j - 1, A, flag);   
    }
    arr[i][j] = arr[i][j+1];
}
void _GoUp(int arr[][50], int i, int j, int A, int flag){
    if(flag){ // upper
        if(i == 0){
            _GoLeft(arr, i, j - 1, A, flag);
        }
        else{
            _GoUp(arr, i - 1, j, A, flag);
        }
    }
    else{ // lower
        if(i != A + 2){
            _GoUp(arr, i - 1, j, A, flag);
        }
    }
    arr[i][j] = arr[i+1][j];
}
void _GoDown(int arr[][50], int i, int j, int A, int flag){
    if(flag){ // upper
        if(i != A - 1){
            _GoDown(arr, i + 1, j, A, flag);
        }
    }
    else{
        if(i == R - 1){
            _GoLeft(arr, i, j - 1, A, flag);
        }
        else{
            _GoDown(arr, i + 1, j, A, flag);
        }
    }
    arr[i][j] = arr[i-1][j];
}

void AirCleaner(int arr[][50], int A){
    _GoRight(arr, A, 1, A, 1);
    arr[A][1] = 0;

    _GoRight(arr, A+1, 1, A, 0);
    arr[A+1][1] = 0;

    /*
    is upper
        go right until j = C - 1 (i = A)
        go up until i = 0 (j = C-1)
        go left until j = 0 (i = 0)
        go down until i = A - 1 (j = 0)

    is lower
        go right until j = C - 1 (i = A+1)
        go down until i = R - 1 (j = C-1)
        go left until j = 0 (i = R-1)
        go up until i = A + 2 (j = 0)

    and 전 위치의 값을 받아오기 if -1 then 0
    */
}

int main(){
    int T;
    int sum = 0;
    int cleanerRow; // Cleaner in [cleanerRow,0] ~ [cleanerRow+1,0]
    int arr[50][50];

    scanf("%d %d %d", &R, &C, &T);
    
    for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
            int temp;
            scanf("%d", &temp);
            arr[i][j] = temp;

            if(temp == -1)
                cleanerRow = i-1;
        }
    }

    for(int i = 0; i < T; i++){
        AirFlow(arr, cleanerRow);
        AirCleaner(arr, cleanerRow);

        // for debug
        /*
        printf("\n");
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                printf("%d ", arr[i][j]);
            }
            printf("\n");
        }
        */
    }

    for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
            if(arr[i][j] > 0)
                sum += arr[i][j];
        }
    }

    printf("%d\n", sum);

    return 0;
}