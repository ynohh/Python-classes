#Função que calcula as medias de orçamento/gasto por tipo de projeto
def calcMediaPorTipo(lista_dados, tipo_projeto):
    lista = lista_dados
    tp_proj = tipo_projeto
    count = 0
    orcamento = 0
    gasto = 0
    for l in lista:
        atributos=l.split(',')
        if atributos[1] == tp_proj:
            count = count + 1
            orcamento = orcamento + int(atributos[3])
            gasto = gasto + int(atributos[4])
    mediaOrcamento = orcamento / count        
    mediaGasto = gasto / count
    print("\n-----------------------")
    print("Médias dos Projetos: {}".format(tp_proj))
    print("Média de ORÇAMENTO foi {}".format(mediaOrcamento))     
    print("Média de GASTO foi {}".format(mediaGasto))     
    
#Função que calcula se o valor gasto com o projeto foi maior que o orçamento
def valorMaiorOrcamento(lista_dados):
    lista = lista_dados
    count = 0
    for l in lista:
        atributos=l.split(',')
        if atributos[4] > atributos[3]:
            count = count + 1
    return "\n{} projetos tiveram o valor maior que o ORÇAMENTO".format(count)


#Função que mostra os dados dos projetos e o valor do orçamento por hora.
def valorOrcadoPorHora(lista_dados):
    lista = lista_dados
    for l in lista:
        print('-----------------------')
        atributos=l.split(',')
        print('Código Projeto:', atributos[0])
        print('Tipo Projeto:', atributos[1])
        print('Duração Total:', atributos[2])
        print('Valor Orçado:', atributos[3])
        print('Valor Gasto:', atributos[4])  
        atributos=l.split(',')
        print("Valor do orçamento por hora: {}".format(int(atributos[3]) / int(atributos[2])))

