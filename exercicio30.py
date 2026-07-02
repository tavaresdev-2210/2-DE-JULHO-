nome = input ("Digite o seu nome:")
idade = input ("Digite a sua idade:")
#nunca esquecer que com o if é necessário dos 4 espaços ou o 'TAB'
if nome and idade: 
    print("Seu nome é Lucas")
    print("Seu nome invertido é:",nome[::-1])
    #neste caso o python entende que é pra começar no ultimo caracter , e vai de -1 em -1 
    #começando de trás para a frente 
    print("Seu nome contém (ou não)espaços:",''in nome)
    #Aqui seria a situação da string fechada e a string aberta, para saber se ha ou não espaço 
    #String aberta = False, String Fechada = True
    print("Seu nome tem ",len(nome),"letras")
    #Neste caso o len serve para contar quantos caracteres existem dentro da string, e o letras
    #vem após dando complemento a frase no terminal 
    print("A primeira letra do seu nome é:",nome[0])
    print("A última letra do seu nome é:",nome[-1])
    print("Desculpe,você deixou campos vazios")

"""
01234
Lucas
-12345
Utilizamos a virgula pois o python precisa separar a string da variável
"""


