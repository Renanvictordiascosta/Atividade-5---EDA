# Código limpo, apenas para execução
# Importação de opções
import opcoes

# Tratamento de erros
try:
    escolher_opcao = opcoes.Opcao()
    escolher_opcao.escolher_opcao()

# Em caso de interromper a operação
except KeyboardInterrupt:
    from time import sleep
    print("\nEntendo que queira encerrar sua operação.")
    sleep(2)
    print("Tenha um bom dia")
    sleep(2)

# Em caso de valor ser inválido
except ValueError:
    from time import sleep
    print("\nO valor digitado é inválido!")
    sleep(2)


# Em caso do tipo ser inválido
except TypeError:
    from time import sleep
    print("\nO valor digitado é inválido!")
    sleep(2)
