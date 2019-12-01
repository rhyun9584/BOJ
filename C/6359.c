#include <stdio.h>
#include <stdlib.h>

int main(){
    int numofcase;

    scanf("%d", &numofcase);

    for(int k = 0; k < numofcase; k++){
        int count = 0;
        int numofroom;

        scanf("%d", &numofroom);

        int room[100] = {0};

        for(int i = 0; i < numofroom; i++){
            for(int j = i + 1; j <= numofroom; j += (i + 1)){
                room[j-1] = (room[j-1] == 1)? 0 : 1;
            }
        }

        for(int i = 0; i < numofroom; i++){
            printf("%d ", room[i]);
        }
        printf("\n");

        for(int i = 0; i < numofroom; i++){
            if(room[i] == 1)
                count++;
        }

        printf("%d\n", count);
    }
    
    return 0;
}