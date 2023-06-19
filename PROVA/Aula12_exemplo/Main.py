{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "### Definição das funções para ordenção"
      ],
      "metadata": {
        "id": "RjYUjByiSFqx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Bubble sort\n",
        "def bubble_sort( array ):\n",
        "  for j in range(0,len(array)):\n",
        "    for i in range(0,len(array)-1): \n",
        "      if array[i] > array[i+1]: #precisa trocar os elementos de posição\n",
        "        aux = array[i]\n",
        "        array[i] = array[i+1]\n",
        "        array[i+1] = aux"
      ],
      "metadata": {
        "id": "p0v7z9BcoyuT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Bubble sort otimizado\n",
        "def bubble_sort( array ):\n",
        "  fim_repeticao = len(array)-1\n",
        "  ultima_troca = 0\n",
        "  ordenado = False\n",
        "  while (not ordenado):\n",
        "    ordenado = True\n",
        "    for i in range(0,fim_repeticao): # percorre o vetor do início até onde ocorreu a última troca\n",
        "      if array[i] > array[i+1]: #precisa trocar os elementos de posição\n",
        "        aux = array[i]\n",
        "        array[i] = array[i+1]\n",
        "        array[i+1] = aux\n",
        "        ordenado = False\n",
        "        ultima_troca = i\n",
        "        \n",
        "    #atualizar o fim da repetição para otimizar\n",
        "    fim_repeticao = ultima_troca"
      ],
      "metadata": {
        "id": "koqoXQ6oe5F3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Insertion sort\n",
        "#Percorre o vetor da posição \"proximo\" em direção ao início\n",
        "#até achar a posição correta aquele elemento que está na \"proximo\"\n",
        "def insertion_sort( array ):\n",
        "  proximo = 1 #elemento a ser classificado\n",
        "  while proximo < len(array):\n",
        "    elemento_em_analise = array[proximo] # guarda o elemento que estamos classificando\n",
        "    index = proximo\n",
        "    # achar a posição correta do elemento que estamos classificando\n",
        "    # vai empurrando os valores para frente, ocupando as posições\n",
        "    while index > 0 and elemento_em_analise < array[ index-1 ]:\n",
        "      array[ index ] = array[ index-1 ]\n",
        "      index -= 1\n",
        "    array[index] = elemento_em_analise #coloca o elemento diretamente na posição correta\n",
        "    proximo += 1      "
      ],
      "metadata": {
        "id": "cCbXNa23g4e-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Selection sort\n",
        "#Verifica até o final do vetor (iniciando pela posição zero) qual é o menor elemento\n",
        "#então coloca este elemento na posição de destino, que é posição zero. \n",
        "#Avança a posição de destino e repete o processo\n",
        "def selection_sort( array ):\n",
        "  for destino in range(0,len(array)):\n",
        "    origem = destino\n",
        "    # Menor é o do destino atual que será incrementado\n",
        "    menor = array[destino]\n",
        "\n",
        "    #procura o menor elemento (no restante do vetor) e guarda a sua posição\n",
        "    for i in range(destino+1,len(array)):\n",
        "      if array[i] < menor:\n",
        "        menor = array[i]\n",
        "        origem = i\n",
        "\n",
        "    # coloca o menor elemento (origem) na sua posição final (destino)\n",
        "    aux = array[destino]\n",
        "    array[destino] = array[origem]\n",
        "    array[origem] = aux"
      ],
      "metadata": {
        "id": "jDwABm3BjHLZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Merge sort\n",
        "def merge_sort( array ):\n",
        "  if len(array) > 1:\n",
        "    ret = np.empty( len(array), dtype=int )\n",
        "    meio = len(array) // 2      \n",
        "    esquerda = merge_sort( np.copy( array[:meio] ))\n",
        "    direita = merge_sort( np.copy( array[meio:] ))\n",
        "    i = j = k = 0\n",
        "    while j < len(esquerda) and k < len(direita):\n",
        "      if esquerda[j] < direita[k]:\n",
        "        ret[i] = esquerda[j]\n",
        "        j += 1\n",
        "      else:\n",
        "        ret[i] = direita[k]\n",
        "        k += 1 \n",
        "      i += 1\n",
        "\n",
        "    for z in range(j,len(esquerda)):\n",
        "      ret[i] = esquerda[z]\n",
        "      i += 1\n",
        "    \n",
        "    for z in range(k,len(direita)):\n",
        "      ret[i] = direita[z]\n",
        "      i += 1\n",
        "    return ret\n",
        "  else:        \n",
        "    return array"
      ],
      "metadata": {
        "id": "rDv9dqkdBMCG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Quick sort\n",
        "def quick_sort( array ):\n",
        "  if len(array) > 1:        \n",
        "    pivo = len(array) // 2\n",
        "    print(pivo)\n",
        "    valor = array[pivo]\n",
        "    print(valor)\n",
        "    esquerda = quick_sort( np.array([i for i in array if i<valor], dtype=int))\n",
        "    meio     = np.array([i for i in array if i==valor], dtype=int) \n",
        "    direita  = quick_sort( np.array([i for i in array if i>valor], dtype=int))\n",
        "    ret = np.concatenate((esquerda,meio,direita), axis=0)\n",
        "    return ret\n",
        "  else:\n",
        "    return array"
      ],
      "metadata": {
        "id": "y7LHNQWQ1pqD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Quick sort\n",
        "def quick_sort_b( array ):\n",
        "  if len(array) > 1:        \n",
        "    pivo = len(array) // 2\n",
        "    valor = array[pivo]\n",
        "    esquerda = quick_sort( [i for i in array if i<valor] )\n",
        "    meio     = [i for i in array if i==valor]\n",
        "    direita  = quick_sort( [i for i in array if i>valor])\n",
        "    ret = esquerda+meio+direita\n",
        "    return ret\n",
        "  else:\n",
        "    return array"
      ],
      "metadata": {
        "id": "N2NVpAY8is2Y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Cria os arrays para ordenação dos dados"
      ],
      "metadata": {
        "id": "qaXebZODUH8p"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "b2YPLLntdbVy"
      },
      "outputs": [],
      "source": [
        "# Carregando um vetor com x números aleatórios\n",
        "import numpy as np\n",
        "import random\n",
        "x=10000\n",
        "\n",
        "arrayOriginal = np.array([random.randint(0,100000) for i in range(0,x)], dtype=int)\n",
        "arrayOriginal"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Criar um vetor com 10 números\n",
        "import numpy as np\n",
        "array = np.empty(10 ,dtype=int)\n",
        "\n",
        "array[0] = 1000\n",
        "array[1] = 20\n",
        "array[2] = 30\n",
        "array[3] = 40\n",
        "array[4] = 50\n",
        "array[5] = 60\n",
        "array[6] = 70\n",
        "array[7] = 800\n",
        "array[8] = 90\n",
        "array[9] = 100"
      ],
      "metadata": {
        "id": "KTkEoxECmXaw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Executa cada método, analisando o desempenho"
      ],
      "metadata": {
        "id": "qpHbr9a2UhaR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Chamar ordenação bubble sort\n",
        "%timeit bubble_sort( arrayOriginal )\n",
        "#for i in range(0,len(arrayOriginal)):\n",
        "#  print( str(i)+\" -> \"+str(arrayOriginal[i]) )"
      ],
      "metadata": {
        "id": "5IPY7st0icP3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dados = list(arrayOriginal)\n",
        "#dados = tuple(arrayOriginal)"
      ],
      "metadata": {
        "id": "vwzEXNNdUpT0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%timeit bubble_sort( dados )"
      ],
      "metadata": {
        "id": "Nn4f2OfVUzJ8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Chamar ordenação insertion sort\n",
        "%timeit insertion_sort( arrayOriginal )\n",
        "#for i in range(0,len(arrayOriginal)):\n",
        "#  print( str(i)+\" -> \"+str(arrayOriginal[i]) )"
      ],
      "metadata": {
        "id": "imx8myFEpeSM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Chamar ordenação selection sort\n",
        "%timeit selection_sort( arrayOriginal )\n",
        "#for i in range(0,len(arrayOriginal)):\n",
        "#  print( str(i)+\" -> \"+str(arrayOriginal[i]) )"
      ],
      "metadata": {
        "id": "tSJROXp1w7Oy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Chamar ordenação merge sort\n",
        "arrayord = merge_sort( arrayOriginal )\n",
        "#for i in range(0,len(arrayord)):\n",
        "#  print( str(i)+\" -> \"+str(arrayord[i]) )"
      ],
      "metadata": {
        "id": "EEbb67T7I5eo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Chamar ordenação quick sort\n",
        "%timeit quick_sort( arrayOriginal )\n",
        "#for i in range(0,len(arrayOriginal)):\n",
        "#  print( str(i)+\" -> \"+str(arrayOriginal[i]) )"
      ],
      "metadata": {
        "id": "D3twJxiN2pX-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Chamar ordenação quick sort\n",
        "%timeit quick_sort_b( arrayOriginal )\n",
        "#for i in range(0,len(arrayOriginal)):\n",
        "#  print( str(i)+\" -> \"+str(arrayOriginal[i]) )"
      ],
      "metadata": {
        "id": "-0TTK0_rUAwk"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}