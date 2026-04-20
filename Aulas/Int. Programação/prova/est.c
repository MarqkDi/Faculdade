#include <stdio.h>

int main () {
    float NOTA1, NOTA2, MEDIA;
    printf("Digite uma nota: ");
    scanf("%f", &NOTA1);
    printf("Digite uma segunda nota: ");
    scanf("%f", &NOTA2);
    if ((NOTA1 > 10) || (NOTA1 < 0) || (NOTA2 > 10) || (NOTA2 < 0)) {
        printf("Nota inválida!");
    }
    else {
        MEDIA = (NOTA1 + NOTA2) / 2;
        printf("Sua média foi %.2f! \n", MEDIA);
        if (MEDIA >= 7) {
            printf("Você passou!");
        }
        else if ((MEDIA >= 6) && (MEDIA < 7)) {
            printf("Você está de recuperação!");
        }
        else {
            printf("Você reprovou!");
        }
    }
    return 0;
}