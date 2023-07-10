import Leitura_dados
import Modulo_Funcoes

print("--------------------------")
print("1 - Calcular média de orçamento e gastos por tipo de projeto")
print("2 - Contar projetos com orçamento estourado")
print("3 - Mostrar valor orçado por hora")
print("4 - Sair")
op = int(input("Escolha uma das opções acima:"))


while op != 4:
    lista_dados = Leitura_dados.lst_lines
    if op == 1:
        print(Modulo_Funcoes.calcMediaPorTipo(lista_dados, " 'Desenvolvimento de software'"))
        print(Modulo_Funcoes.calcMediaPorTipo(lista_dados, " 'Desenvolvimento software'"))
        print(Modulo_Funcoes.calcMediaPorTipo(lista_dados, " 'Implantação software'"))
        print(Modulo_Funcoes.calcMediaPorTipo(lista_dados, " 'Revisão de processos'"))
    elif op == 2:
        print(Modulo_Funcoes.valorMaiorOrcamento(lista_dados))
    elif op == 3:
        print(Modulo_Funcoes.valorOrcadoPorHora(lista_dados))
    else:
        print("Opção inválida!")
    print("--------------------------")
    print("1 - Calcular média de orçamento e gastos por tipo de projeto")
    print("2 - Contar projetos com orçamento estourado")
    print("3 - Mostrar valor orçado por hora")
    print("4 - Sair")
    op = int(input("Escolha uma das opções acima:"))


