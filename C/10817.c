#include <stdio.h>

int main(){
    int num[3];
    scanf("%d %d %d", &num[0], &num[1], &num[2]);
    
    int t;
    if(num[0] > num[1]){
        t = num[0];
        num[0] = num[1];
        num[1] = t;
    }
    if(num[1] > num[2]){
        t = num[1];
        num[1] = num[2];
        num[2] = t;
    }
    if(num[0] > num[1]){
        t = num[0];
        num[0] = num[1];
        num[1] = t;
    }
    
    printf("%d", num[1]);
    return 0;
}