#include <stdio.h>

int main(){
    int desch;                  // destination channel
    int numofwrong;             // # of wrong button
    int currentch = 100;
    int movecount = 0;
    int button[10] = {0};  // 1 is wrong button flag

    scanf("%d", &desch);
    scanf("%d", &numofwrong);

    for(int i = 0; i < numofwrong; i++){
        int temp;
        scanf("%d", &temp);
        button[temp] = 1;
    }



    return 0;
}