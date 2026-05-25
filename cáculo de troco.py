def calcular_troco():
    """Calcula o troco de uma compra."""
    
    print("=== CALCULADORA DE TROCO ===\n")
    
    try:
        valor_compra = float(input("Digite o valor da compra: R$ "))
        valor_pago = float(input("Digite o valor pago: R$ "))
        
        if valor_compra < 0 or valor_pago < 0:
            print("Erro! Os valores não podem ser negativos.")
            return
        
        if valor_pago < valor_compra:
            diferenca = valor_compra - valor_pago
            print(f"\n Falta R$ {diferenca:.2f} para completar o pagamento.")
            return
        
        troco = valor_pago - valor_compra
        
        print(f"\n--- Resultado ---")
        print(f"Valor da compra: R$ {valor_compra:.2f}")
        print(f"Valor pago: R$ {valor_pago:.2f}")
        print(f"Troco: R$ {troco:.2f}")
        
        # Decomposição do troco em notas e moedas
        if troco > 0:
            print(f"\n--- Decomposição do troco ---")
            calcular_notas_moedas(troco)
    
    except ValueError:
        print("Erro! Digite valores numéricos válidos.")

def calcular_notas_moedas(valor):
    """Decomposição do troco em notas e moedas brasileiras."""
    
    # Notas e moedas em reais
    denominacoes = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    nomes = {
        100: "notas de R$ 100",
        50: "notas de R$ 50",
        20: "notas de R$ 20",
        10: "notas de R$ 10",
        5: "notas de R$ 5",
        2: "notas de R$ 2",
        1: "moedas de R$ 1",
        0.50: "moedas de R$ 0,50",
        0.25: "moedas de R$ 0,25",
        0.10: "moedas de R$ 0,10",
        0.05: "moedas de R$ 0,05",
        0.01: "moedas de R$ 0,01"
    }
    
    valor = round(valor, 2)
    
    for denominacao in denominacoes:
        quantidade = int(valor / denominacao)
        
        if quantidade > 0:
            valor = round(valor - (quantidade * denominacao), 2)
            print(f"  {quantidade}x {nomes[denominacao]}")