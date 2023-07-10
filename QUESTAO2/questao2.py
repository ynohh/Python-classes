import csv

#Metodo bubble sort otimizado

def bubble_sort(array):
    fim_repeticao = len(array) - 1
    ultima_troca = 0
    ordenado = False
    while (not ordenado):
        ordenado = True
        for i in range(0, fim_repeticao): # percorre o vetor do início até onde ocorreu a última troca\n",
            if array[i][1] > array[i + 1][1]: #precisa trocar os elementos de posição\n",
                aux = array[i]
                array[i] = array[i + 1]
                array[i + 1] = aux
                ordenado = False
                ultima_troca = i    

    #atualizar o fim da repetição para otimizar\n",
    fim_repeticao = ultima_troca


with open("./data.csv", "r") as file:
    reader = csv.reader(file)
    data = [row for row in reader]
    data.pop(0)
    data = [[row[0], int(row[1])] for row in data]

    bubble_sort(data)
    for row in data:
        print(row)