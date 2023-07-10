#Leitura do arquivo
with open('C:\\Users\\m131564\\Downloads\\Python-classes-main\\PROVA\Prova2\\projetos.csv', 'r', encoding='utf8') as file:
    next(file)
    lst_lines=[line[:-1:] for line in file]
