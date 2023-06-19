import random

#Função que criar o dicionário com valores aleatórios e define o seu status
def dicio_gerar_vagas():
    dicio_vagas = {}
    for letras in ['A', 'B', 'C']:
        for numero in range(1, 11):
            vaga = letras + str(numero)
            ocupada = random.random() > 0.5
            dicio_vagas[vaga] = 'Ocupada' if ocupada else 'Liberada'
    return dicio_vagas

#Função que contará  e mostrará o número de vagas ocupadas ou liberadas
def contador_de_vagas(dicio_vagas, status_vaga):
    contador = 0
    for vaga in dicio_vagas.values():
        if vaga == status_vaga:
            contador += 1
    return contador

#Programa principal que vai chamar as funções
vagas = dicio_gerar_vagas()
print("Situação das vagas:")
print(vagas)
print("Número de vagas que estão OCUPADAS:", contador_de_vagas(vagas, 'Ocupada'))
print("Número de vagas que estão LIBERADAS:", contador_de_vagas(vagas, 'Liberada'))