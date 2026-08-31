# Exercício 03

# 1 - Função escreve_ola
def mostrar_ola():
    print("ola exercício 03")


# 2 - Expressões lógicas

# a) A and B
def expressao_and(valor_a, valor_b):
    return valor_a and valor_b


# b) A or B
def expressao_or(valor_a, valor_b):
    return valor_a or valor_b


# c) not A
def expressao_not(valor_a):
    return not valor_a


# d) B and C
def expressao_and_bc(valor_b, valor_c):
    return valor_b and valor_c


# e) A or B and C
def expressao_or_and(valor_a, valor_b, valor_c):
    return valor_a or (valor_b and valor_c)


# 3 - Calculadora de operações

# Função de soma
def adicionar(numero_a, numero_b):
    return numero_a + numero_b


# Função de subtração
def diminuir(numero_a, numero_b):
    return numero_a - numero_b


# Função de multiplicação
def multiplicar(numero_a, numero_b):
    return numero_a * numero_b


# Função de divisão
def dividir(numero_a, numero_b):
    return numero_a / numero_b


# Duas chamadas de teste para cada função
print(adicionar(3, 4))
print(adicionar(7, 9))

print(diminuir(3, 4))
print(diminuir(7, 9))

print(multiplicar(3, 4))
print(multiplicar(7, 9))

print(dividir(3, 4))
print(dividir(7, 9))


# 4 - Validação de dados

# Verifica se o nome possui pelo menos 3 caracteres
# e se a idade está entre 18 e 100 anos
def conferir_usuario(nome_usuario, idade_usuario):
    return len(nome_usuario) >= 3 and 18 <= idade_usuario <= 100


# Duas chamadas de teste
print(conferir_usuario("Arthur", 13))
print(conferir_usuario("Carlos", 20))


# 5 - Estatísticas de uma lista

# Criação de uma lista contendo 10 números inteiros
numeros = [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# A) Apresente a quantidade de elementos da lista
print(len(numeros))

# B) Apresente o maior valor
print(max(numeros))

# C) Apresente o menor valor
print(min(numeros))

# D) Apresente a soma dos valores
print(sum(numeros))

# E) Apresente a média dos valores
print(sum(numeros) / len(numeros))

# F) Apresente o primeiro elemento utilizando índice
print(numeros[0])

# G) Apresente o último elemento utilizando índice
print(numeros[-1])

# H) Utilize slicing para apresentar os três primeiros elementos
print(numeros[:3])

# Apresente os três últimos elementos
print(numeros[-3:])

# Apresente os elementos que estão nas posições pares
print(numeros[::2])


# I) Atualize o valor de pelo menos dois elementos
numeros[2] = 15
numeros[6] = 31

print(numeros)


# J) Utilize append() para adicionar dois novos números
numeros.append(11)
numeros.append(12)

print(numeros)


# K) Utilize pop() para remover um elemento
numeros.pop(2)

print(numeros)


# L) Apresente a lista resultante após todas as operações
print(numeros)


# 6 - Cadastro de produto

# Criação de uma tupla representando um produto
produto_info = ("notebook", 3500.00, 10, "informática")

# Apresenta o nome
print(produto_info[0])

# Apresenta o preço
print(produto_info[1])

# Apresenta a quantidade
print(produto_info[2])

# Apresenta a categoria
print(produto_info[3])


# Função que calcula o valor total do estoque
def calcular_estoque(produto):
    preco_produto = produto[1]
    quantidade_produto = produto[2]
    return preco_produto * quantidade_produto


print(calcular_estoque(produto_info))


# 7 - Coordenadas

# Criação da tupla com as coordenadas
coordenadas = (10, 20, 30)

# Desempacotamento dos valores
coordenada_x, coordenada_y, coordenada_z = coordenadas


# Função que recebe x, y e z e retorna a soma
def somar_coordenadas(valor_x, valor_y, valor_z):
    return valor_x + valor_y + valor_z


print(somar_coordenadas(coordenada_x, coordenada_y, coordenada_z))


# 8 - Cadastro de aluno

# Criação do dicionário do aluno
cadastro_aluno = {
    "nome": "Pedrin",
    "idade": 20,
    "curso": "ADS",
    "nota1": 8.0,
    "nota2": 7.5
}

# Apresenta o nome
print(cadastro_aluno["nome"])

# Apresenta a idade
print(cadastro_aluno["idade"])

# Apresenta o curso
print(cadastro_aluno["curso"])

# Apresenta as notas
print("Nota 1:", cadastro_aluno["nota1"])
print("Nota 2:", cadastro_aluno["nota2"])


# Função que calcula a média do aluno
def obter_media(aluno):
    primeira_nota = aluno["nota1"]
    segunda_nota = aluno["nota2"]
    return (primeira_nota + segunda_nota) / 2


# Apresenta a média
print(obter_media(cadastro_aluno))


# 9 - Conversão de temperatura

# Converte Celsius para Fahrenheit
def transformar_celsius(temperatura_celsius):
    resultado = (temperatura_celsius * 9 / 5) + 32
    return resultado


# Converte Fahrenheit para Celsius
def transformar_fahrenheit(temperatura_fahrenheit):
    resultado = (temperatura_fahrenheit - 32) * 5 / 9
    return resultado


# Testes das funções
print(transformar_celsius(0))
print(transformar_fahrenheit(48))


# 10 - Registro de uma viagem

# Criação da tupla com os dados da viagem
dados_viagem = ("Maranhão", 7, "Trem", 35.00)

# A) Apresenta a tupla completa
print(dados_viagem)

# B) Apresenta a quantidade de elementos
print(len(dados_viagem))

# C) Verifica se "Ônibus" está presente na tupla
print("Ônibus" in dados_viagem)

# D) Cria uma nova tupla acrescentando a hospedagem
nova_viagem = dados_viagem + ("Hotel 3 Estrelas",)

# E) Apresenta a nova tupla
print(nova_viagem)


# 11 - Cadastro de produto

# Função que recebe os dados e cria um dicionário
def cadastrar_produto(
    nome_produto,
    categoria_produto,
    preco_produto,
    quantidade_produto,
    codigo_produto
):
    registro = {
        "nome": nome_produto,
        "categoria": categoria_produto,
        "preco": preco_produto,
        "quantidade": quantidade_produto,
        "codigo": codigo_produto
    }

    # 1. Imprime o dicionário completo
    print(registro)

    # 2. Imprime cada informação individualmente
    print("nome:", registro["nome"])
    print("categoria:", registro["categoria"])
    print("preco:", registro["preco"])
    print("quantidade:", registro["quantidade"])
    print("codigo:", registro["codigo"])

    # 3. Calcula o valor total em estoque
    total_estoque = registro["preco"] * registro["quantidade"]

    print("Valor total em estoque deste produto é de:", total_estoque)


# Chamada da função
cadastrar_produto("Pinhão", "Comida", 2.50, 37676, "0987")


# 12 - Área de um círculo

# Função que recebe o diâmetro e retorna o raio
def calcular_raio(diametro):
    return diametro / 2


# Função que calcula a área do círculo utilizando a função do raio
def calcular_area(diametro):
    raio = calcular_raio(diametro)
    area = 3.14 * (raio ** 2)
    return area


# Duas chamadas de teste
print(calcular_area(23))
print(calcular_area(34))
