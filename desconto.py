# Programa: Sistema de Desconto Progressivo
# Autor: Gustavo Ikeda
# Objetivo: Calcular o desconto aplicado em uma compra
# conforme as regras estabelecidas.

# Solicita ao usuário o valor total da compra
valor_compra = float(input("Digite o valor total da compra (R$): "))

# Inicializa a variável de desconto
desconto = 0.0

# Estrutura condicional para aplicar as regras de desconto
if valor_compra < 200:
    desconto = 0.05  # 5%
elif valor_compra >= 200 and valor_compra < 300:
    desconto = 0.10  # 10%
else:
    desconto = 0.15  # 15%

# Calcula o valor do desconto em reais
valor_desconto = valor_compra * desconto

# Calcula o valor final a pagar
valor_final = valor_compra - valor_desconto

# Exibe os resultados
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f} ({desconto*100:.0f}%)")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
