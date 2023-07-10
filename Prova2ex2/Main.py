import BubbleSort

lista_compras = []
c = 0

while c < 10:
    valor = int(input("Valor da compra: "))
    if valor < 1 or valor > 500:
        print("Valor não permitido")
    else:
        lista_compras.append(valor)
    c = c + 1

#implementado o menoto Bubble sort OTIMIZADO    
BubbleSort.bubble_sort(lista_compras)

#Iterando a lista e apresentado os valores ordenados 
for l in lista_compras:
    print(l)