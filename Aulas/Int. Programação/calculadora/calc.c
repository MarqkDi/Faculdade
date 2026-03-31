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
        printf("Operador Inválido!");
    }
    else {
        if (OP == '+') {
            RESSOMA = VALOR1 + VALOR2;
            printf("O resultado da soma é: %d \n", RESSOMA);
        }
        else if (OP == '-') {
            RESSUB = VALOR1 - VALOR2;
            printf("O resultado da subtração é: %d \n", RESSUB);
        }
        else if (OP == '*') {
            RESMULT = VALOR1 * VALOR2;
            printf("O resultado da multiplicação é: %d \n", RESMULT);
        }
        else if (OP == '/') {
            if (VALOR2 == 0) {
                printf("Valor inválido (Não há como fazer divisão por 0)");
            }
            else {
                RESDIV = (float) VALOR1 / VALOR2;
                printf("O resultado da divisão é: %f \n", RESDIV);
            }
        }
        else if (OP == '%') {
            RESMOD = VALOR1 % VALOR2;
            printf("O rsultado do módulo é: %d \n", RESMOD);
        }
    }
}