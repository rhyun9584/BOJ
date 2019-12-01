#include <stdio.h>
#include <math.h>

int IsPrime(int n){ // 1 is Y, 0 is N
    int sqrn = (int)sqrt(n);
    for(int i = 2; i <= sqrn; i++){
        if((n % i) == 0)
            return 0;
    }
    return 1;
}

void Goldbach(int n){
    for(int i = 3; i <= (n/2); i += 2){
        if(IsPrime(i)){
            if(IsPrime(n - i)){
                printf("%d = %d + %d\n", n, i, n - i);
                return;
            }
        }
    }

    printf("Goldbach's conjecture is wrong.\n");
}

int main(){
    int N;
    scanf("%d", &N);
    
    while(N != 0){
        Goldbach(N);

        scanf("%d", &N);
    }

    return 0;
}