nome = input ("Digite o seu nome:")
idade = input ("Digite a sua idade:")
#nunca esquecer que com o if é necessário dos 4 espaços ou o 'TAB'
if nome and idade: 
    print("Seu nome é Lucas")
    print("Seu nome invertido é:",nome[::-1])
    print("Seu nome contém (ou não)espaços:",''in nome)
    print("Seu nome tem ",len(nome),"letras")
    print("A primeira letra do seu nome é:",nome[0])
    print("A última letra do seu nome é:",nome[-1])
    print("Desculpe,você deixou campos vazios")



