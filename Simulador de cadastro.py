print("Bem vindo a empresa do camisetas do Nelson Tavares") # EXIGÊNCIA DE CÓDIGO 1

lista_funcionarios = [] # EXIGÊNCIA DE CÓDIGO 2
id_global = 2424202

def cadastrar_funcionario(id): # EXIGÊNCIA DE CÓDIGO 3
    print("-" * 8,"MENU CADASTRAR FUNCIONÁRIO","-" * 8)
    print(f"id: {id_global}")
    nome = input("Por favor entre com o nome do Funcionário: ")
    setor = input("Por favor entre com o setor do Funcionário: ")
    salario = float(input("Por favor entre com o salário do Funcionário: "))
    
    funcionarios = {
        "id":id,
        "nome": nome,
        "setor":setor,
        "salario":salario      
    }

    lista_funcionarios.append(funcionarios.copy())# EXIGÊNCIA DE CÓDIGO 7
    print("Funcionário cadastrado com sucesso!")
 
def consultar_funcionarios(): # EXIGÊNCIA DE CÓDIGO 4
    while True:
        print("-" * 8,"MENU CONSULTAR FUNCIONÁRIO","-" * 8)
        print("1 - Consultar todos os funcionários")
        print("2 - Consultar funcionário por id")
        print("3 - Consultar funcionário(s) por setor")
        print("4 - Sair")
        print(" ")
        consulta = input(">>")
    
        if consulta == "1":
            print("-"*10)
            for func in lista_funcionarios:
                print(f"id: {func['id']}")
                print(f"nome:  {func['nome']}")
                print(f"setor:  {func['setor']}")
                print(f"salário:  {func['salario']:.1f}")
                print("-"*14)
        elif consulta =="2":
            busca = input("Digite o id do funcionário: ")
            print("-"*14)
            encontrado = False
            for func in lista_funcionarios:
                if str(func["id"]) == busca:
                    print(f"id:  {func['id']}")
                    print(f"nome:  {func['nome']}")
                    print(f"setor:  {func['setor']}")
                    print(f"salário:  {func['salario']:.1f}")
                    print("-"*14)
                    encontrado=True
            if not encontrado:
                print("Funcionário não econtrado.")
        elif consulta =="3":
            setor = input("Digite o setor do(s) funcionário(s): ")
            encontrados = False
            for func in lista_funcionarios:
                if func["setor"] == setor:
                    print(f"id:  {func['id']}")
                    print(f"nome:  {func['nome']}")
                    print(f"setor:  {func['setor']}")
                    print(f"salário:  {func['salario']:.1f}")
                    print("-"*14)
                    encontrados=True
            if not encontrados:
                print("Funcionário não econtrado nesse setor.")
        elif consulta == "4":
            return
        else:
            print("Opção inválida.")

def remover_funcionario(): # EXIGÊNCIA DE CÓDIGO 5
    print("-" * 8,"MENU REMOVER FUNCIONÁRIO","-" * 8)
    remover = input("Digite o Id do funcionário a ser removido: ")
    for func in lista_funcionarios:
        if str(func["id"]) == remover:
            lista_funcionarios.remove(func)
            print("")
            print("Funcionário removido com sucesso.")
            return
        
    print("Id inválido") 

#-----------MENU--------------------- EXIGÊNCIA DE CÓDIGO 6 
while True:
    print("-" * 17,"MENU PRINCIPAL","-" * 17)
    print("Escolha a opção desejada: ")
    print("1 - Cadastrar Funcionários: ")
    print("2 - Consultar Funcionário(s): ")
    print("3 - Remover funcionário")
    print("4 - Sair")
    print(" ")
    resposta = input(">>")

    if resposta == "1" :
        cadastrar_funcionario(id_global)
        id_global +=1
    elif resposta == "2":
        consultar_funcionarios()
    elif resposta == "3":
        remover_funcionario()
    elif resposta =="4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
        print(" ")

 
           