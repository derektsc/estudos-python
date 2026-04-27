#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoas = [{'nome': "Derek", 'idade': 25, 'Cidade': "São Paulo"},
            {'nome': "Matheus", 'idade': 29, 'Cidade': "São Paulo"},
            {'nome': "Sharon", 'idade': 24, 'Cidade': "São Paulo"},
            {'nome': "Manuela", 'idade': 17, 'Cidade': "São Paulo"},
            ]
#2 - Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.
for pessoa in pessoas:
    del pessoa['Cidade']
    if pessoa['nome'] == "Derek":
        pessoa['idade'] = 20
        pessoa['profissão'] = "Desenvolvedor"
        print(pessoa)


#3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
numeros = {}
for i in range (1, 6):
    numeros[i] = i ** 2
print(numeros)

#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
if 'nome' in pessoas:
    print("chave existe")
else:
    print("Chave não existe")

#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = "python é legal e python é fácil"

palavras = frase.split()
frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)