#include "tnt.h"

int main(void){

    string name = grabText("What is your name? ");
    int years = grabInt("How old are you? ");

    printf("%s\n", name);
    printf("%d\n", years);

    free(name);
}