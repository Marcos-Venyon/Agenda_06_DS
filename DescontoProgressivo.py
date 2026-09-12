# Solicita ao usuário que digite o valor da compra e converte a entrada para um número decimal (float)
valor = float(input("Digite o valor da compra: "))

# Verifica se o usuário digitou um valor negativo, o que não faria sentido para uma compra
if valor < 0:
    print("Valor inválido. Digite um valor positivo.")

# Se o valor for maior ou igual a zero, mas menor que 200, entra nesta condição
elif valor < 200.00:
    print("Desconto de 5% aplicado.")
    # Multiplicar por 0.95 é uma forma rápida de calcular o valor já com 5% de desconto
    valor = valor * 0.95 

# O Python só chega aqui se o valor for maior ou igual a 200. 
# Então, verifica se é menor que 300 para aplicar a regra do meio.
elif valor < 300.00:
    print("Desconto de 10% aplicado.")
    # Multiplica por 0.90 para calcular o valor com 10% de desconto
    valor = valor * 0.90 

# Se o valor não foi menor que 200 nem menor que 300, ele obrigatoriamente é 300 ou mais.
else:
    print("Desconto de 15% aplicado.")
    # Multiplica por 0.85 para calcular o valor com 15% de desconto
    valor = valor * 0.85 

# Garante que o print do valor final só aconteça se a entrada original não tiver sido negativa
if valor >= 0:
    # O ":.2f" formata o número para exibir sempre duas casas decimais (ex: 225.00)
    print(f"O valor final da compra é: R$ {valor:.2f}.")