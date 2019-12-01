#include <stdio.h>

int main(){
    int X;

    scanf("%d", &X);

    if(X < 100){
        printf("%d\n", X);
    }
    else{
        int count = 99;

        for(int i = 100; i <= X; i++){
            int a = i / 100;
            int b = (i / 10) % 10;
            int c = i % 10;

            if((a - b) == (b - c))
                count++;
        }

        printf("%d\n", count);
    }

    return 0;
}