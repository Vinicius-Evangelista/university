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
         modelo = input("Qual o modelo desejado?").upper()
         if not (modelo in modelosEvalores.keys()):
             print("Escolha inválida, entre com outro modelo novamente")
         else: 
             break
    return modelosEvalores[modelo]

def num_camiseta(modelo):
    try: 
         camisetas = int(input("Entre com o número de camisetas: "))
         if camisetas < 20:
             return 0
         elif camisetas >= 20 & camisetas < 200:
             return 5/100
         elif camisetas >= 200 & camisetas < 2000:
             return 7/100
         elif camisetas >= 2000 & camisetas < 20000:
             return 12/100
         else:
            print("Não aceitamos tantas camisetas de uma vez")
    except:
        print("Input inválido!")

