#include <stdio.h>

int main(){
    int N;
    int count[10] = {0}; 

    scanf("%d", &N);

    while(N != 0){
        int num = N % 10;
        count[num]++;
        N /= 10;
    }

    for(int i = 9; i >= 0; i--){
        for(int j = 0; j < count[i]; j++){
            printf("%d", i);
        }
    }    

    printf("\n");
    return 0;
}