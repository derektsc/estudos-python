#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
numero = int(input("Selecione um número: "))
if numero % 2 == 0:
    print("O número é Par")
else:
    print("O número é Impar")

#Outra maneira de fazer a condicional só que inline
resultado = "Par\n" if numero % 2 == 0 else "Impar\n"
print(resultado)

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.
idade = int(input("Qual a sua idade? "))
if 0 <= idade <= 12:
    print("Você é uma criança\n")
elif 13 <= idade <= 18:
    print("Voce é um Adolescente\n")
else:
    print("Você é um adulto\n")

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
user_name = "derek"
password = "123"
def login():
    user_name_input = str(input("Digite seu nome de usuario: "))
    password_input = str(input("Digite sua senha: "))

    if user_name_input == user_name and password_input == password:
        print("Você logou!\n")
    else:
        print("O login ou senha estão errados!\n")

login()

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

def classificar_quadrante(x, y):
    if x > 0 and y > 0:
        return("Primeiro quadrante")
    elif x < 0 and y > 0:
        return("Segundo quadrante")
    elif x < 0 and y < 0:
        return("Terceiro quadrante")
    elif x > 0 and y < 0:
        return("Quarto quadrante")
    else:
        return("O ponto está localizado no eixo ou origem")

def coordenadas():
    x = int(input("Digite a coordenada X"))
    y = int(input("Digite a coordenada Y"))

    resultado = classificar_quadrante(x,y)
    print(resultado)

coordenadas()