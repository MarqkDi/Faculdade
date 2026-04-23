#include <stdio.h>

int main () {
    int PAR, RES, NUM, i;
    for (int i=1; i <= 10; i++) {
        printf("Digite um valor: ");
        scanf ("%d", &NUM);
        RES = NUM % 2;
        if (RES == 0) {
            PAR = NUM + PAR;
            printf("E um numero PAR! \n");
        }
        else {
            printf("Nao e PAR! \n");
        }
        RES = 0;
    }
    printf("A soma dos numeros pares e: %d", RES);

    return 0;
}