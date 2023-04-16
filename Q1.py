import os

nomePortos = []
estadoPortos = []	
print("Digite 1 para adicionar um porto")
print("Digite 2 para editar um porto")
print("Digite 3 para remover um porto")
print("Digite 4 para listar os portos")
print("Digite 5 para sair")
opcao = int(input())
os.system('cls' if os.name == 'nt' else 'clear')

while opcao != 5:
    if opcao < 1 or opcao > 5:
        print("Opção inválida! Digite novamente:")
        opcao = int(input())
    else:
        if opcao == 1:
            nomePorto = input("Digite o nome do porto: ")
            nomePortos.append(nomePorto)
            estadoPorto = input("Digite o estado desse porto: ")
            estadoPortos.append(estadoPorto)
            print("\nPorto adicionado com sucesso!\n")
        elif opcao == 2:
            if len(nomePortos) > 0:
                print("Portos disponíveis para editar:")
                for i in range(len(nomePortos)):
                    print(f"{i+1} - {nomePortos[i]} - {estadoPortos[i]}")
                portoEditar = int(input("Digite o número do porto que deseja editar: "))
                if portoEditar > 0 and portoEditar <= len(nomePortos):
                    nomePorto = input("Digite o novo nome do porto: ")
                    estadoPorto = input("Digite o novo estado desse porto: ")
                    nomePortos[portoEditar-1] = nomePorto
                    estadoPortos[portoEditar-1] = estadoPorto
                    print("\nPorto editado com sucesso!\n")
                else:
                    print("Número inválido!")
            else:
                print("Não há portos disponíveis para editar!")
        elif opcao == 3:
            if len(nomePortos) > 0:
                print("Portos disponíveis:")
                for i in range(len(nomePortos)):
                    print(f"{i+1} - {nomePortos[i]} - {estadoPortos[i]}")
                portoRemover = int(input("Digite o número do porto que deseja remover: "))
                if portoRemover > 0 and portoRemover <= len(nomePortos):
                    nomePortos.pop(portoRemover-1)
                    estadoPortos.pop(portoRemover-1)
                    print("\nPorto removido com sucesso!\n")
                else:
                    print("Número inválido!")
            else:
                print("Não há portos disponíveis para remover!")
        elif opcao == 4:
            if len(nomePortos) > 0:
                print("Portos disponíveis:")
                for i in range(len(nomePortos)):
                    print(f"{i+1} - {nomePortos[i]} - {estadoPortos[i]}")
            else:
                print("Não há portos disponíveis!")
        elif opcao == 5:
            break
        print("Digite 1 para adicionar um porto")
        print("Digite 2 para editar um porto")
        print("Digite 3 para remover um porto")
        print("Digite 4 para listar os portos")
        print("Digite 5 para sair")
        opcao = int(input())
        os.system('cls' if os.name == 'nt' else 'clear')
