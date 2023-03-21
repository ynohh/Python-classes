num_part = int(input('Qual o número de particpantes da pesquisa? \n'))
cont = 1
cont_android = 0
cont_ios = 0
cont_outros = 0
cont_nao_primeiro = 0
cont_nao_segundo = 0
cont_nao_terceiro = 0
lista_nivel = []
lista_sisop = []
lista_temcel = []
lista_ram = []
lista_memoria = []
totalram = 0
totalmemoria = 0
valido=False

while cont <= num_part:
    while not valido:
        valido=False
        ano_escolar = input('Qual ano/série do participante {}? (Primeiro, Segundo, Terceiro) \n'.format(cont))
        if ano_escolar == 'Primeiro' or ano_escolar == 'Segundo' or ano_escolar == 'Terceiro' or ano_escolar == 'primeiro' or ano_escolar == 'segundo' or ano_escolar == 'terceiro':
            valido=True
    valido=False
    while not valido:
        valido=False
        tem_cell = input('Possui celular?(S/N)')
        if tem_cell == 'S' or tem_cell == 's':
            sisop = input('Qual o sistema operacional do seu celular? (Android/Ios/Outro)')
            qtd_ram = int(input('Qual a quantidade de ram do seu aparelho?'))
            memoria = int(input('Qual a quantidade de memória interna do seu aparelho?'))
            if sisop == 'Android':
                cont_android = cont_android+ 1
                valido=True
            elif sisop == 'Ios' or sisop == 'ios':
                cont_ios = cont_ios + 1
                valido=True
            else:
                cont_outros = cont_outros + 1
                valido=True
        elif tem_cell == 'N' or tem_cell == 'n':
            if ano_escolar == 'Primeiro' or ano_escolar == "primeiro":
                cont_nao_primeiro = cont_nao_primeiro + 1
            elif ano_escolar == 'Segundo' or ano_escolar == "segundo":
                cont_nao_segundo = cont_nao_segundo + 1
            else:
                cont_nao_terceiro = cont_nao_terceiro + 1
            sisop = ''
            qtd_ram = 0
            memoria = 0
            valido = True
    valido=False
    lista_nivel.append(ano_escolar)
    lista_temcel.append(tem_cell)
    lista_sisop.append(sisop)
    lista_ram.append(qtd_ram)
    lista_memoria.append(memoria)

    cont = cont + 1

contram=0
for ram in enumerate(lista_ram):
    ramv=ram[1]
    ind=ram[0]
    if lista_temcel[ind]=='S' or lista_temcel[ind]=='s':
        totalram = totalram + ramv
        contram=contram+1

mediaram = totalram / contram

contmem=0
for mem in enumerate(lista_memoria):
    memv = mem[1]
    ind = mem[0]
    if lista_temcel[ind] == 'S' or lista_temcel[ind] == 's':
        totalmemoria = totalmemoria + memv
        contmem=contmem+1
mediamemoria = totalmemoria / contmem

num_IOS = lista_sisop.count('ios') + lista_sisop.count('Ios')
num_AND = lista_sisop.count('Android') + lista_sisop.count('android')
num_out = lista_sisop.count('Outro') + lista_sisop.count('outro')

num_pri = lista_nivel.count('primeiro') + lista_nivel.count('Primeiro')
num_seg = lista_nivel.count('segundo') + lista_nivel.count('Segundo')
num_ter = lista_nivel.count('terceiro') + lista_nivel.count('Terceiro')

percentual_IOS = num_IOS * 100 / num_part
percentual_AND = num_AND * 100 / num_part
percentual_OUT = num_out * 100 / num_part

percentual_primeiro_ano = 0
percentual_segundo_ano = 0
percentual_terceiro_ano = 0

if num_pri != 0:
    percentual_primeiro_ano = cont_nao_primeiro * 100 / num_pri
if num_seg != 0:
    percentual_segundo_ano = cont_nao_segundo * 100 / num_seg
if num_ter != 0:
    percentual_terceiro_ano = cont_nao_terceiro * 100 / num_ter


print(f'\nSão {num_part} alunos participando da pesquisa!\n')

# Formatação usando \n para quebra de linha e 2f para que sejam mostradas duas decimais
print(f'O percentual de sistema operacional dos alunos:\nIos: {percentual_IOS:.2f}%\n'
      f'Android: {percentual_AND:.2f}%\nOutros: {percentual_OUT:.2f}%')
print(f'O percentual de alunos que não possui aparelho celular em cada ano é:'
      f'\nPrimeiro: {percentual_primeiro_ano:.2f}%\nSegundo: {percentual_segundo_ano:.2f}%'
      f'\nTerceiro: {percentual_terceiro_ano:.2f}%')
print(f'A média geral de memória ram do aparelho dos alunos é {mediaram:.2f}!')
print(f'A média geral de memória interna do aparelho dos alunos é {mediamemoria:.2f}!')