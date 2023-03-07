num_of_part = int(input("Qual é o número de participantes que irão participar da pesquisa? "))
count = 0
count_ios = 0
count_android = 0
count_else = 0
count_have = 0
first_year = 0
second_year = 0
third_year = 0
dont_have_smartphone = 0
while count <= num_of_part:
    count += 1

    reg_year = input("Em qual ano/série vocês está matriculado? (Primeiro, segundo, terceiro) ")
    if reg_year.lower() == "primeiro":
        first_year += 1 
    elif reg_year.lower() == "segundo":
        second_year += 1   
    else:
        third_year += 1

    have_smartphone = input("Você possui celular ou smartphone? ")
    if have_smartphone.lower() == 's':
        count_have += 1
        ops_system = input("Qual o sistema operacional do seu celular/smartphone? (IOS, Android, outro) ")
        if ops_system.lower() == 'ios':
            count_ios += 1
        elif ops_system.lower() == 'android':
            count_android += 1
        else:
            count_else += 1
            
        ram_size = int(input("Qual a quantidade de RAM e de armazenamento interno disponível? "))
    else:
        dont_have_smartphone += 1


print("Students at the first year: {}".format(first_year))
print("Students at the second year: {}".format(second_year))
print("Students at the third year: {}".format(third_year))


print("The number of students that have a smartphone is: {}".format(count_have))
print("The number of students that don't have a smartphone is: {}".format(dont_have_smartphone))
print("The number of students that have IOS: {}".format(count_ios))
print("The number of students that have Android: {}".format(count_android))
print("The number of students that have other OS: {}".format(count_else))