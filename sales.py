print("Bem-vindo a loja do Vinicius do Nascimento Evangelista")

print("Entre com o valor do pedido: ", end="")
valorDoPedido = float(input())

print("Entre com a quantidade de parcelas: ", end="")
quantidadeParcelas = int(input())

juros = 0

if (quantidadeParcelas < 4): 
    juros = 0
elif (quantidadeParcelas >= 4 & quantidadeParcelas < 6):
    juros = 4/100
elif (quantidadeParcelas >= 6 & quantidadeParcelas < 9):
    juros = 8/100
elif (quantidadeParcelas >= 9 & quantidadeParcelas < 13):
    juros = 16/100
else:
    juros = 32/100

valorDaParcela = round(float((valorDoPedido * (1 +  juros)) / quantidadeParcelas), 2)

print(f"O valor das parcelas é: R$ {valorDaParcela}", end="")

valorTotal = round(valorDaParcela * quantidadeParcelas, 2)
print(f"O valor Total Parcelado é: R$ {valorTotal}", end="")