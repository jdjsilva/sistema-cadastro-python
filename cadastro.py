cadastros = []

while True:
    print("n=== SISTEMA DE CADASTRO")
    print("1 - Cadastrar pessoa")
    print("2 - Ver cadastros")
    print("3 - Sair")

    opção = input("Escolha a sua opção: ")

    if opção == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")

        pessoa = {
            "nome": nome, 
            "idade": idade
        }

        cadastros.append(pessoa)
        print("Cadastro realizado!")

    elif opção == "2":
        if len(cadastros) == 0:
            print("Nenhum cadastro ainda.")
        else:
            print("\n --- LISTA DE CADASTROS ---")
            for i, pessoa in enumerate(cadastros, start=1):
                print(f"{i}. {pessoa['nome']} - {pessoa['idade']} anos")
    
    elif opção == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
                                                        