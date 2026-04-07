#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
  int CH, i, NT;
  printf("-------Integração de todos meus sistemas de calculo-------");
  printf("Escolha um sistema:");
  printf("1 - Calculo de média");
  printf("2 - Calculo de média ponderada");
  printf("3 - Tabuada");
  printf("4 - Descobrir se um número é primo");
  printf("5 - Descobrir se um número é par");
  printf("6 - Calculadora");
  printf("7 - Jogo de Adivinhação");
  printf("0 - Sair");
  scanf("%d", &CH);
  if (CH == 0) {
    printf("Até a próxima 👋");
  }
  else if (CH == 1) {
    printf("Este programa suporta apenas o calculo da media de dois valores! ⚠");
    
  }
}