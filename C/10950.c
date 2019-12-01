#include <stdio.h>

int main(){
    int case;
    scanf("%d", &case);
    
    int a, b;
    for(int i = 0; i < case; i++){
        scanf("%d %d", &a, &b);
        printf("%d\n", a + b);
    }
    return 0;
}