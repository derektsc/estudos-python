#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

number_list = [1,2,3,4,5,6,7,8,9,10]
name_list = ["Derek", "Fulano", "Ciclano", "Beutrano"]
year_list = [2000, 2026]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
def create_list():
    items = []
    for i in range(3):
        element_input = input(f"Construa sua lista, digite o {i+1} elemento: ")
        items.append(element_input)
    return items
    
def show_list(created_items):    
    for item in created_items:
        print(item)

created_items = create_list()
show_list(created_items)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
numeros = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for numero in numeros:
    if numero % 2 == 1:
        soma += numero
print(soma)

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
numeros2 = [1,2,3,4,5,6,7,8,9,10]
def revert_list(lista):
    left = 0
    right = len(lista) - 1

    while left < right:
        lista[left], lista[right] = lista[right], lista[left]

        left += 1
        right -=1

    return lista
revert_list(numeros2)
print(numeros2)

#Ou dessa forma:
for numeros3 in range(10,0,-1):
    print(numeros3)

#numeros2.sort(reverse = True) sem loop daria para fazer dessa forma
#print(numeros2)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
digit_number = int(input("Digite um número: "))
for tabuada in range(0, 11, +1):
    multi = digit_number * tabuada
    print(f"{digit_number} * {tabuada} = {multi}")

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
list_number = [1,2,3,4,5]
def soma_numbers(numbers):
    soma2 = 0
    for number in numbers:
        try:
            soma2 += number
        except:
            print("Valor invalido")
    return soma2
resultado = soma_numbers(list_number)
print(resultado)

#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

list_number2 = [10,10,10,10]
def media_soma_lista(numbers):
    try:
        soma = soma_numbers(numbers)
        media = soma / len(numbers)
    except:
        print("Valores invalidos")
    return media

resultado_media = media_soma_lista(list_number2)
print("Média: ", resultado_media)