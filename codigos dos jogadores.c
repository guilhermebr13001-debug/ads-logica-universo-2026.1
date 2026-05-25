#include <stdio.h>

struct Jogador {
    int numero;
    float peso;
    float altura;
    char inicial;
};

int main() {
    struct Jogador jogadores[3];

    // Leitura dos dados
    for(int i = 0; i < 3; i++) {
        printf("Jogador %d\n", i + 1);

        printf("Numero da camisa: ");
        scanf("%d", &jogadores[i].numero);

        printf("Peso: ");
        scanf("%f", &jogadores[i].peso);

        printf("Altura: ");
        scanf("%f", &jogadores[i].altura);

        printf("Inicial do nome: ");
        scanf(" %c", &jogadores[i].inicial); // espaço antes do %c é importante

        printf("\n");
    }

    int indiceMaisBaixo = 0;
    int indiceMaisPesado = 0;

    // Comparações
    for(int i = 1; i < 3; i++) {
        if(jogadores[i].altura < jogadores[indiceMaisBaixo].altura) {
            indiceMaisBaixo = i;
        }

        if(jogadores[i].peso > jogadores[indiceMaisPesado].peso) {
            indiceMaisPesado = i;
        }
    }

    // Resultados
    printf("Inicial do jogador mais baixo: %c\n", jogadores[indiceMaisBaixo].inicial);
    printf("Numero do jogador mais pesado: %d\n", jogadores[indiceMaisPesado].numero);

    return 0;
}