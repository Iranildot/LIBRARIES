//Biblioteca usada para realizar o tratamento de textos e números
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef char *string;

string grabText(string title){
    int i = 0;
    char c[1];
    string tmp;

    // Print out the message the user gave
    printf("%s", title);

    string texto = malloc(1);
    if (texto == NULL){
        printf("ERRO 1");
        return "ERRO 1"; //Erro in text variable
    }

    while ((c[0] = getchar()) != '\n'){
        //Takes the characters typed by the user and puts them in the text string
        texto[i] = c[0];

        //Increase the length of the text string
        tmp = realloc(texto, i + 2);
        if (tmp == NULL){
            free(texto);
            printf("ERRO 2");
            return "ERRO 2"; //Temporary variable (tmp) error
        }
            
        texto = tmp;
        i++;  
    }
    texto[i] = '\0';
    return texto;
}

//Gets an integer from users
int grabInt(string titulo){
    int numero = 0;
    printf("%s", titulo);
    scanf("%d", &numero);
    return numero;
}