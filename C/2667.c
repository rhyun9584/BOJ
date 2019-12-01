#include <stdio.h>
#include <stdlib.h>

int N;

void numbering(int arr[][25], int i, int j, int* count){
    if(arr[i][j] != 1)
        return;

    arr[i][j] = 0;

    if(i > 0) // go left
        numbering(arr, i-1, j, count);
    if(i < N-1) //go right
        numbering(arr, i+1, j, count);
    if(j > 0) //go up
        numbering(arr, i, j-1, count);
    if(j < N-1) //go down
        numbering(arr, i, j+1, count);
    
    ++*count;
}

void sort(int arr[], int count){
    for(int i = 1; i < count; i++){
        for(int j = i; j > 0; j--){
            if(arr[j] < arr[j-1]){
                int temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
            }
        }
    }
}

int main(){
    int allcount = 0;
    int count = 0;
    int arr[25][25];
    int num[170];

    scanf("%d", &N);

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            int temp;
            scanf("%1d", &temp);
            arr[i][j] = temp;
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(arr[i][j] == 1){
                count = 0;
                numbering(arr, i, j, &count);
                
                num[allcount] = count;
                allcount++;
            }
        }
    }    
    
    printf("%d\n", allcount);
    sort(num, allcount);
    
    for(int i = 0; i < allcount; i++){
        printf("%d\n", num[i]);
    }

    return 0;
}