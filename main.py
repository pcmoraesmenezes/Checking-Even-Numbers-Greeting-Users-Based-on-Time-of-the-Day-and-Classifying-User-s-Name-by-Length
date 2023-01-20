"""
Faça um programa que peça ao usuario para digitar um valor inteiro.
Verificar se o numero digitado é par ou impar
Caso o usuario digite um numero que não é inteiro informe ao usuario que não é um numero inteiro
"""
print("Digite um numero inteiro para começarmos")
numero = input()
if numero.isdigit():
    if int(numero) % 2 == 0:
       print("Você digitou um numero par!!")
    else:
       print("Você digitou um numero impar!!")
else:
    print("Você não digitou um numero inteiro")
"""
Faça um programa que pergunte a hora ao usuario, baseando no horario descrito passe uma saudação plausivel
EX: 0.0 - 11 bom dia. 12-17 boa tarde e 18-23 boa noite
"""
(horas) = input("Informe que horas são: ")
if 0 <= float(horas) < 11:
    print("Bom dia")
elif 11 <= float(horas) < 18:
    print("Boa tarde!")
elif 18<= float(horas) < 24:
    print("Boa noite!") 
"""
Faça um programa que peça o primeiro nome do usuario, caso o nome do usuario tenha 4 digitos, informe que ele tem o nome curto
caso o nome tiver 5-6 letras informe que seu nome é normal, e caso ele tenha +6 letras informe que ele tem um nome grande

"""
print("Olá, informe o seu primeiro nome!")
nome = input()
if len(nome) <= 4:
    print("O seu nome é pequeno!")
elif len(nome) >=5 and  len(nome) <=6:
    print("O seu nome tem tamanho normal")
elif len(nome) >6:
    print("O seu nome é grande meu chapa!")