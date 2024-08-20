print("Bem vindos a empresa do Vinicius do Nascimento Evangelista")

lista_de_funcionarios = []

id_global = 4676461

def cadastrar_funcionario(id):
    funcionario = {
        "id" : id,
        "nome" : "",
        "setor" : "",
        "salario" : 0
    }

    print("--------- CADASTRAR FUNCIONÁRIOS ----------")
    funcionario["nome"] = input("Por favor entre com o nome do funcionário: ")
    funcionario["setor"] = input("Por favor entre com o setor do funcionário: ")
    funcionario["salario"] = input("Por favor entre com o salário do funcionário: ")
    
    lista_de_funcionarios.append(funcionario.copy())

def consultar_funcionarios():
    while True:
        print("--------- CONSULTAR FUNCIONÁRIOS ----------")
        print("1 - Consultar todos os funcionário")
        print("2 - Consultar Funcionários por Id")
        print("3 - Consultar Funcionários por setor")
        print("4 - Retornar")
        opcao = int(input())

        if opcao == 1:
            for funcionario in lista_de_funcionarios:
                print("-----------------------------------")
                print(f"id : {funcionario['id']}")
                print(f"nome: {funcionario['nome']}")
                print(f"setor: {funcionario['setor']}")
                print(f"salário: {funcionario['salario']}")
                print("-----------------------------------")
        elif opcao == 2:
            id = int(input("Digite o id do funcionário: "))
            for funcionario in lista_de_funcionarios:
                if funcionario["id"] == id: 
                    print("-----------------------------------")
                    print(f"id : {funcionario['id']}")
                    print(f"nome: {funcionario['nome']}")
                    print(f"setor: {funcionario['setor']}")
                    print(f"salário: {funcionario['salario']}")
                    print("-----------------------------------")
        elif opcao == 3:
            setor = input("Digite o setor do funcionário: ")
            for funcionario in lista_de_funcionarios:
                if funcionario["setor"] == setor: 
                    print("-----------------------------------")
                    print(f"id : {funcionario['id']}")
                    print(f"nome: {funcionario['nome']}")
                    print(f"setor: {funcionario['setor']}")
                    print(f"salário: {funcionario['salario']}")
                    print("-----------------------------------")
        elif opcao == 4:
            break
        else:
            print("Opção inválida")
 

def remove_funcionario():
    while True:
        print("--------- CONSULTAR FUNCIONÁRIOS ----------")
        id = int(input("Digite o id do funcionário a ser removido: "))

        for funcionario in lista_de_funcionarios:
            if funcionario["id"] == id:
                lista_de_funcionarios.remove(funcionario)
                print("Funcionário removido com sucesso!")
                return 

        print("id inválido!")
         
def main():
    while True:
        print("--------- MENU PRINCIPAL ----------")
        print("1 - Cadastrar funcionário")
        print("2 - Consultar funcionário(s)")
        print("3 - Remover funcionários")
        print("4 - Sair")
        opcao = int(input())

        if opcao == 1: 
            global id_global 
            id_global += 1
            cadastrar_funcionario(id_global)
        elif opcao == 2:
            consultar_funcionarios()
        elif opcao == 3:
            remove_funcionario()
        elif opcao == 4:
            break
        else:
            print("Opção inválida!")

main()