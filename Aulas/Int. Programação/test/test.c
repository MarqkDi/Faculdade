#include <stdio.h>

int main() {
    int IDADE, ALTURACM;
    float PESO, ALTURA, ALTURAPOL, IMC, TMBH, TMBM, IDEALBRH, IDEALBRM, IDEALDEVH, IDEALDEVM, IDEALROBH, IDEALROBM;
    char GENERO;

    printf("Insira sua idade: ");
    scanf("%d", &IDADE);
    printf("Insira seu peso (KG): ");
    scanf("%f", &PESO);
    printf("Insira sua altura (M): ");
    scanf("%f", &ALTURA);
    printf("Insira seu gênero (H/M): ");
    scanf(" %c", &GENERO);

    ALTURACM = ALTURA * 100;
    ALTURAPOL = ALTURACM / 2.54;
    IMC = PESO / (ALTURA * ALTURA);
    TMBH = 66.5 + (13.75 * PESO) + (5.003 * ALTURACM) - (6.75 * IDADE);
    TMBM = 655.1 + (9.563 * PESO) + (1.850 * ALTURACM) - (4.676 * IDADE);
    IDEALBRH = ALTURACM - 100;
    IDEALBRM = ALTURACM - 105;
    IDEALDEVH = 50 + 2.3 * (ALTURAPOL - 60);
    IDEALDEVM = 45.5 + 2.3 * (ALTURAPOL - 60);
    IDEALROBH = 52 + 1.9 * (ALTURAPOL - 60);
    IDEALROBM = 49 + 1.7 * (ALTURAPOL - 60);

    printf("Seu IMC é: %.2f \n", IMC);
    if (IMC < 18.5) {
        printf ("Você está abaixo do peso! Procure um nutricionista. \n");
    }
    else if (IMC >= 18.5 && IMC < 24.9) {
        printf ("Você está no peso ideal! Continue assim. \n");
    }
    else {
        printf ("Você está acima do peso! Procure um nutricionista. \n");
    }
    if (GENERO != 'H' && GENERO != 'h') {
        printf ("Sua Taxa Metabólica Basal é: %.2f", TMBM);
        printf ("Seu Peso Ideal segundo a fórmula de Broca é: %.2f \n", IDEALBRM);
        printf ("Seu Peso Ideal segundo a fórmula de Devine é: %.2f \n", IDEALDEVM);
        printf ("Seu Peso Ideal segundo a fórmula de Robinson é: %.2f \n", IDEALROBM);
    }
    else {
        printf ("Sua Taxa Metabólica Basal é: %.2f", TMBH);
        printf ("Seu Peso Ideal segundo a fórmula de Broca é: %.2f \n", IDEALBRH);
        printf ("Seu Peso Ideal segundo a fórmula de Devine é: %.2f \n", IDEALDEVH);
        printf ("Seu Peso Ideal segundo a fórmula de Robinson é: %.2f \n", IDEALROBH);
    }
    return 0;
}