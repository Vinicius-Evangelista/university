# Menu
print("Bem vindos a loja do Vinicius do Nascimento Evangelista")
print("----------------------+       Cardápio      +---------------------+")
print("+---------------------+---------------------+---------------------+")
print("|      Tamanho        |  Bife Acebolado(BA)  |  Filé de Frango(FF)  |")
print("+---------------------+---------------------+---------------------+")
print("|         P           |       R$ 16.00       |       R$ 15.00       |")
print("+---------------------+---------------------+---------------------+")
print("|         M           |       R$ 18.00       |       R$ 17.00       |")
print("+---------------------+---------------------+---------------------+")
print("|         G           |       R$ 22.00       |       R$ 21.00       |")
print("+---------------------+---------------------+---------------------+")

# map das possiveis abreviações
abreviacoes = {
    "FF" : "Filé de Frango",
    "BA" : "Bife Acebolado"
}

# cardápio da loja de marmitas
cardapio = {
    "FF": { 
            "P": {
                15
            },
            "M": {
                17
            },
            "G" : {
                21
            }
    },
    "BA": {
        "P": {
            16
        },
        "M": {
            18
        },
        "G": {
            21
        }
    }

}

# opcoes de continuação para o usuário
opcoesContinuacao = {
    "S" : True,
    "N" : False
}

acumulador = 0

while True:
    tipoDeMarmita = input("Entre com o sabor desejado (BA/FF): ").upper() 

    if (not (tipoDeMarmita in cardapio.keys())):
        print("Sabor inválido. Tente novamente")
    else:
        tamanhoSelecionado = input("Entre com o tamnho desejado (P/M/G): ").upper()
        if(not (tamanhoSelecionado in cardapio[tipoDeMarmita])):
            print("Tamanho inválido. Tente novamente")
        else:
            valorMarmita = list(cardapio[tipoDeMarmita][tamanhoSelecionado])[0]
            acumulador += valorMarmita
            print(f"Você pediu um {abreviacoes[tipoDeMarmita]} no tamanho {tamanhoSelecionado}: R${valorMarmita}")

            continuar = False
            continuar = input("Deseja mais alguma coisa? (S/N): ").upper()
            if (not (continuar in opcoesContinuacao)):
                print("Opção inválida tente novamente.")
            else:
                if (opcoesContinuacao[continuar]):
                    continue
                else:
                    break

print(f"O valor total a ser pago: R${acumulador}")



