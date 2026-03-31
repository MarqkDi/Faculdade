#include <stdio.h>

int main() {
    int FREQ;
    float NOTA1, NOTA2, MEDIA;

    printf("Digite a primeira nota do aluno: ");
    scanf("%f", &NOTA1);
    printf("Digite a segunda nota do aluno: ");
    scanf("%f", &NOTA2);
    printf("Digite a frequencia do aluno (%%): ");
    scanf("%d", &FREQ);
    if (NOTA1 < 1 || NOTA1 > 10 || NOTA2 < 1 || NOTA2 > 10) {
        printf("A nota inserida e invalida!");
    }
    else if (FREQ < 0 || FREQ > 100) {
        prinf("A frequencia insrida é invalida!");
    }
    else {
        MEDIA = (NOTA1 + NOTA2) / 2;
        if (MEDIA >= 7 && FREQ >= 75) {
            printf("O aluno está aprovado com uma media de %f e uma frequencia de %d", MEDIA, FREQ);
        }
        else if (MEDIA >= 5 && FREQ < 75) {
            prinf("O aluno esta de recuperacao com uma media de %f e uma frequencia de %d", MEDIA, FREQ);
        }
        else if (MEDIA < 5 || FREQ < 75) {
            printf("O aluno foi reprovado pois tem uma media de %f e uma frequencia de %d", MEDIA, FREQ);
        }
    }
}