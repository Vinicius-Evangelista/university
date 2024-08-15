print("Bem-vindo a loja do Vinicius do Nascimento Evangelista")

print("Entre com o valor do pedido: ")
valorDoPedido = float(input())

print("Entre com a quantidade de parcelas: ")
quantidadeParcelas = int(input())


juros = 0

if (quantidadeParcelas < 4): 
    juros = 0
elif (quantidadeParcelas >= 6 & quantidadeParcelas < 9):
    juros = 8/100
elif (quantidadeParcelas >= 9 & quantidadeParcelas < 13):
    juros = 16/100
else:
    juros = 32/100



valorDaParcela = (valorDoPedido * (1 +  juros)) / quantidadeParcelas

valorTotal = valorDaParcela * quantidadeParcelas

print(valorTotal)