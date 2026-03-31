#include <stdio.h>

int main () {
    int VALOR1, VALOR2, RESSOMA, RESSUB, RESMULT, RESMOD;
    float RESDIV;
    char OP;

    printf("Digite o primeiro valor: ");
    scanf("%d", &VALOR1);
    printf("Digite o segundo valor: ");
    scanf("%d", &VALOR2);
    //Acho que ficaria melhor se a opção de escolha fosse um numero de 1 a 5, cada um contendo sua operação, a exibição seria apenas "1 - Adição", e fazia isso com cada operador em cada linha,vejo sendo mais prático doque dessa forma digitando o operador
    printf("\n Digite + pra soma \n Digite - pra subtracao \n Digite * pra multiplicacao \n Digite / pra divisao \n Digite %% pra modulo \n Insira o operador: ");
    scanf(" %c", &OP);
    if (OP != '+' && OP != '-' && OP != '*' && OP != '/' && OP != '%') {
        printf("Operador Invalido!");
    }
    else {
        if (OP == '+') {
            RESSOMA = VALOR1 + VALOR2;
            printf("O resultado da soma e: %d \n", RESSOMA);
        }
        else if (OP == '-') {
            RESSUB = VALOR1 - VALOR2;
            printf("O resultado da subtracao e: %d \n", RESSUB);
        }
        else if (OP == '*') {
            RESMULT = VALOR1 * VALOR2;
            printf("O resultado da multiplicacao e: %d \n", RESMULT);
        }
        else if (OP == '/') {
            if (VALOR2 == 0) {
                printf("Valor invalido (Nao ha como fazer divisao por 0)");
            }
            else {
                RESDIV = (float) VALOR1 / VALOR2;
                printf("O resultado da divisao e: %f \n", RESDIV);
            }
        }
        else if (OP == '%') {
            RESMOD = VALOR1 % VALOR2;
            printf("O rsultado do modulo e: %d \n", RESMOD);
        }
    }
    return 0;
}