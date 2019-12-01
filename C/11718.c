#include <stdio.h>

int main(){
    char ch = 0;

    while(1){
        ch = getchar();
        if(ch == EOF)
            break;
        putchar(ch);
    }    

    return 0;
}