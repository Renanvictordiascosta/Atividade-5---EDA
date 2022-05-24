# Código de classe de opção
# Importar código de classes de filas
import fila

# Classe de Opções
class Opcao:

    # Escolher uma das opções
    def escolher_opcao(self):
        from time import sleep
        opcao = 0

        # Chamada das filas
        prioridade1 = fila.FilaDePrioridade()
        prioridade2 = fila.FilaDePrioridade()

        while opcao != 6:
            print("1 - Resolução da Questão 1")
            print("2 - Resolução da Questão 2")
            print("3 - Resolução da Questão 3")
            print("4 - Resolução da Questão 4")
            print("5 - Resolução da Questão 5")
            print("6 - Sair do Sistema")
            opcao = int(input("Digite a opção desejada: "))

            # Resolução da Questão 1
            if opcao == 1:
                prioridade1 = fila.FilaDePrioridade()

                print("Resolução da Questão 1")
                sleep(2)

                print("Mostrar que a fila está vazia: ")
                prioridade1.print_fila()
                sleep(2)

                print("Inserir o primeiro elemento: ")
                prioridade1.inserir(70, 1)
                sleep(4)

                print("Inserir o segundo elemento: ")
                prioridade1.inserir(67, 2)
                sleep(4)

                print("Inserir o terceiro elemento: ")
                prioridade1.inserir(35, 2)
                sleep(4)

                print("Inserir o quarto elemento: ")
                prioridade1.inserir(48, 3)
                sleep(4)

                print("Inserir o quinto elemento: ")
                prioridade1.inserir(21, 3)
                sleep(4)

                print("Inserir o sexto elemento: ")
                prioridade1.inserir(23, 3)
                sleep(4)

                print("Inserir o sétimo elemento: ")
                prioridade1.inserir(15, 3)
                sleep(4)

                print("Mostrar essa fila nova: ")
                prioridade1.print_fila()
                sleep(4)

            # Resolução da questão 2
            elif opcao == 2:
                print("Resolução da Questão 2")
                sleep(2)

                print("Remover o primeiro elemento, em prioridade: ")
                prioridade1.remover()
                sleep(4)

                print("Remover o segundo elemento, em prioridade: ")
                prioridade1.remover()
                sleep(4)

                print("Mostrar essa nova fila, com os elementos removidos: ")
                prioridade1.print_fila()
                sleep(4)

            # Resolução da Questão 3
            elif opcao == 3:
                print("Resolução da Questão 3")
                sleep(2)

                prioridade2 = fila.FilaDePrioridade()
                print("Mostrar fila vazia: ")
                prioridade2.print_fila()
                sleep(2)

                print("Inserir o primeiro elemento: ")
                prioridade2.inserir(15, 1)
                sleep(4)

                print("Inserir o segundo elemento: ")
                prioridade2.inserir(21, 2)
                sleep(4)

                print("Inserir o terceiro elemento: ")
                prioridade2.inserir(23, 2)
                sleep(4)

                print("Inserir o quarto elemento: ")
                prioridade2.inserir(48, 3)
                sleep(4)

                print("Inserir o quinto elemento: ")
                prioridade2.inserir(35, 3)
                sleep(4)

                print("Inserir o sexto elemento: ")
                prioridade2.inserir(70, 3)
                sleep(4)

                print("Inserir o sétimo elemento: ")
                prioridade2.inserir(67, 3)
                sleep(4)

                print("Mostrar a fila com os elementos inseridos: ")
                prioridade2.print_fila()
                sleep(4)

            # Resolução da Questão 4
            elif opcao == 4:
                print("Resolução da Questão 4")
                sleep(2)

                print("Remover o primeiro elemento, em prioridade: ")
                prioridade2.remover()
                sleep(4)

                print("Remover o segundo elemento, em prioridade: ")
                prioridade2.remover()
                sleep(4)

                print("Imprimir essa nova fila, com os elementos removidos: ")
                prioridade2.print_fila()
                sleep(4)

            # Resolução da Questão 5
            elif opcao == 5:
                prioridade3 = fila.FilaDePrioridade()
                print("Mostrar fila vazia: ")
                prioridade3.print_fila()
                sleep(2)

                print("Inserir o primeiro elemento: ")
                prioridade3.inserir(70, 1)
                sleep(4)

                print("Inserir o segundo elemento: ")
                prioridade3.inserir(67, 2)
                sleep(4)

                print("Inserir o terceiro elemento: ")
                prioridade3.inserir(35, 2)
                sleep(4)

                print("Inserir o quarto elemento: ")
                prioridade3.inserir(48, 3)
                sleep(4)

                print("Inserir o quinto elemento: ")
                prioridade3.inserir(21, 3)
                sleep(4)

                print("Inserir o sexto elemento: ")
                prioridade3.inserir(23, 3)
                sleep(4)

                print("Inserir o sétimo elemento: ")
                prioridade3.inserir(15, 3)
                sleep(4)

                print("Mostrar a fila com os elementos inseridos: ")
                prioridade3.print_fila()
                sleep(4)

            elif opcao == 6:
                print("Entendemos que queira sair.")
                sleep(2)

                print("Tenha um bom dia!")
                sleep(2)

            else:
                print("A opção digitada é inválida")
                sleep(2)
                
