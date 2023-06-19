"""
Busca recursiva em lista
"""
def busca_rec(lista, pos, valor):
    tamanho=len(lista)
    if pos==tamanho-1:
        if lista[pos]>valor:
            contmaiores=1
        else:
            contmaiores=0
        return contmaiores
    else:
        if lista[pos]>valor:
            contmaiores=1+busca_rec(lista, pos+1,valor)
        else:
            contmaiores=0+busca_rec(lista, pos+1, valor)
        return contmaiores

lista=[10, 15, 21, 16, 17, 23]

contagem=busca_rec(lista, 0, 20)

print(contagem)

def busca(lista, valor):
    contmaiores=0
    for v in lista:
        if v>valor:
            contmaiores=contmaiores+1
    return contmaiores

contagem=busca(lista, 20)

print(contagem)