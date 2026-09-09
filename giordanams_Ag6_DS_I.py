# ============================================================
# Programa: Sistema de Desconto Progressivo
# Curso: Desenvolvimento de Sistemas
# Descrição: Calcula o valor do desconto e o total a pagar
#            com base no valor bruto da compra.
# ============================================================

def calcular_desconto():
    # Solicita o valor total da compra ao usuário e converte para float
    try:
        valor_compra = float(input("Digite o valor total da compra (R$): "))
        
        # Validação para evitar valores negativos
        if valor_compra < 0:
            print("Por favor, insira um valor válido e positivo.")
            return

        # Definição do percentual de desconto com base nas regras do sistema
        if valor_compra < 200.00:
            porcentagem_desconto = 0.05  # 5% de desconto
        elif valor_compra < 300.00:
            porcentagem_desconto = 0.10  # 10% de desconto
        else:
            porcentagem_desconto = 0.15  # 15% de desconto

        # Processamento: cálculo do desconto e valor final a pagar
        valor_desconto = valor_compra * porcentagem_desconto
        valor_final = valor_compra - valor_desconto

        # Exibição dos resultados formatados em moeda nacional (R$)
        print("\n--- RESUMO DA COMPRA ---")
        print(f"Valor original: R$ {valor_compra:.2f}")
        print(f"Desconto aplicado ({int(porcentagem_desconto * 100)}%): R$ {valor_desconto:.2f}")
        print(f"Valor total a pagar: R$ {valor_final:.2f}")
        print("------------------------")

    except ValueError:
        print("Erro: Digite apenas números válidos (ex: 150.50).")

# Execução do programa
if __name__ == "__main__":
    calcular_desconto()