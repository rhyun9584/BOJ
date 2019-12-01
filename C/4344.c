#include <stdio.h>

int main(){
    int C;
    scanf("%d", &C);

    for(int i = 0; i < C; i++){
        int num;
        float upper = 0;
        scanf("%d", &num);

        int score[1000];

        float sum = 0;

        for(int j = 0; j < num; j++){
            int temp;
            scanf("%d", &temp);

            score[j] = temp;
            sum += temp;
        }

        float avg = sum / num;

        for(int j = 0; j < num; j++){
            if(score[j] > avg)
                upper++;
        }
        printf("%.3f%%\n", (upper / num) * 100);
    }

    return 0;
}