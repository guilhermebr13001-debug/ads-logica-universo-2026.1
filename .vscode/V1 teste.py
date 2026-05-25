def cadastrar_barras():
    barras = []

    qtd_barras = int(input("Quantas barras deseja cadastrar? "))

    for i in range(qtd_barras):
        nome = input("Nome da barra: ")
        barras.append(nome)

    return barras


def cadastrar_linhas(barras):
    linhas = []

    qtd_linhas = int(input("Quantas ligações deseja criar? "))

    for i in range(qtd_linhas):
        origem = input("Barra origem: ")
        destino = input("Barra destino: ")

        if origem in barras and destino in barras:

            resistencia = float(input("Resistência da linha: "))

            linhas.append([origem, destino, resistencia])

        else:
            print("Barra inválida!")

    return linhas


def iniciar_tensoes(barras):
    tensoes = {}

    for barra in barras:
        tensoes[barra] = 100.0

    return tensoes


def calcular_tensoes(barras, linhas, tensoes):

    # Correntes fixas do teste
    correntes = {
        barras[1]: -10.0,
        barras[2]: -5.0
    }

    erro = 1
    iteracao = 1

    while erro > 0.001:

        erro = 0

        for barra in barras[1:]:

            valor_antigo = tensoes[barra]

            numerador = correntes[barra]
            denominador = 0

            for linha in linhas:

                origem = linha[0]
                destino = linha[1]
                resistencia = linha[2]

                if origem == barra:
                    numerador += tensoes[destino] / resistencia
                    denominador += 1 / resistencia

                elif destino == barra:
                    numerador += tensoes[origem] / resistencia
                    denominador += 1 / resistencia

            novo_valor = numerador / denominador

            tensoes[barra] = novo_valor

            diferenca = abs(novo_valor - valor_antigo)

            if diferenca > erro:
                erro = diferenca

        print("Iteração", iteracao, tensoes)

        iteracao += 1

    return tensoes


def main():

    barras = cadastrar_barras()

    linhas = cadastrar_linhas(barras)

    tensoes = iniciar_tensoes(barras)

    resultado = calcular_tensoes(barras, linhas, tensoes)

    print("\nConvergiu!")
    print("Resultado final:")
    print(resultado)


main()