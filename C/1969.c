#include <stdio.h>

#define A 65
#define C 67
#define G 71
#define T 84

int FindMax(int arr[]){
    int maxcount = 0;
    for(int i = 1; i < 4; i++){
        if(arr[maxcount] < arr[i])
            maxcount = i;
    }
    
    switch(maxcount){
        case 0:
            return A;
        case 1:
            return C;
        case 2:
            return G;
        case 3:
            return T;
    }
}

int main(){
    int N, M;
    char DNA[1000][50] = {0};
    int newDNA [50] = {0};
    int sum = 0;

    scanf("%d %d", &N, &M);
    getchar();
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            DNA[i][j] = getchar();
        }
        getchar();
    }

    for(int i = 0; i < M; i++){
        int count[4] = {0}; // A, C, G, T 
        for(int j = 0; j < N; j++){
            switch(DNA[j][i]){
                case A:
                    count[0]++;
                    break;
                case C:
                    count[1]++;
                    break;
                case G:
                    count[2]++;
                    break;
                case T:
                    count[3]++;
                    break;
                default: break;
            }
        }

        newDNA[i] = FindMax(count);
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            if(DNA[i][j] != newDNA[j])
                sum++;
        }
    }
    
    for(int i = 0; i < M; i++){
        printf("%c", newDNA[i]);
    }
    printf("\n%d\n", sum);

    return 0;
}