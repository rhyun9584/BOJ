#include <stdio.h>

void findres(long long result[][9], int a){
    if(result[a-1][0] > 0)
        return;

    if(result[a-2][0] == 0)
        findres(result, a-1);
    
    for(int i = 0; i < 9; i++){
        for(int j = i ; j < 9; j++){
            result[a-1][i] += result[a-2][j];
        }
        //printf("result[%d][%d]: %d\n", a-1, i, result[a-1][i]);
    }
}

int main() {
    int T;
    int num[1001] = {0};
    long long result[65][9] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 0};

    scanf("%d", &T);

    for(int i = 0; i < T; i++){
        scanf("%d", &num[i]);
    }

    for(int i = 0; i < T; i++){
        long long sum = 1;

        findres(result, num[i]);

        for(int j = 0; j < num[i]; j++){
            for(int k = 0; k < 9; k++){
                sum += result[j][k];
            }
        }
        printf("%lld\n", sum);
    }

    return 0;
}