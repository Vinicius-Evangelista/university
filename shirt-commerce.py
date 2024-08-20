print("Bem vindo a fábrica de Camisetas do Vinicius do Nascimento Evangelista")

print("Entre com o modelo desejado:")
print("MCS - Manga Curta Simples")
print("MLS - Manga Longa Simples")
print("MCE - Manga Curta Com Estampa")
print("MLE - Manga Longa Com Estampa")

modelosEvalores = {
 "MCS" : 1.80,
 "MLS" : 2.10,
 "MCE" : 2.90,
 "MLE" : 3.20
}

def escolha_modelo():
    while True:
         modelo = input("Qual o modelo desejado? ").upper()
         if not (modelo in modelosEvalores.keys()):
             print("Escolha inválida, entre com outro modelo novamente")
         else: 
             break
    return modelosEvalores[modelo]

def num_camiseta():
    while True: 
         try: 
              camisetas = int(input("Entre com o número de camisetas: "))
              if camisetas < 20:
                return 0
              elif camisetas >= 20 and camisetas < 200:
                return camisetas * 95/100 
              elif camisetas >= 200 and camisetas < 2000:
                return camisetas * 93/100
              elif camisetas >= 2000 and camisetas < 20000:
                return camisetas * 88/100
              elif camisetas > 20000:
                 print("Não aceitamos tantas camisetas de uma vez")
         except:
             print("Input inválido!")
         print("Entre com o valor da camiseta novamente")


def frete():
    while True:
        try:
             print("1 - Frete por transportadora - R$100.00")
             print("2 - Frete por Sedex - R$200.00")
             print("0 - Retirar pedido na fábrica - R$ 0.00")
             opcao_frete = int(input())

             if opcao_frete == 1:
                 return 100
             elif opcao_frete == 2:
                 return 200
             elif opcao_frete == 0:
                 return 0 
             else:
                 print("Escolha inválida, tente novamente")
                 continue
        except:
                 print("Escolha inválida, tente novamente")
                 continue


def main():
    modelo = escolha_modelo()
    camiseta_num = num_camiseta()
    valor_frete = frete()

    print(f"Total: R$ {(modelo * camiseta_num) + valor_frete} (Modelo: {modelo} * Quantidade(com desconto): {modelo * camiseta_num} + frete: {valor_frete})")


main()