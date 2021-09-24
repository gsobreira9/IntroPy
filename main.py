# 1 - imports / bibliotecas / lista de Compras




# 2 - Classe


# 3 - Métodos e Funções
# def = definittion = definição


def print_hi(name):

    print(f'Oi, {name}')

def calcular_area_do_retangulo(largura,comprimento):
     return largura * comprimento


def calcular_area_do_quadrado (lado):
    return lado ** 2

def calcular_area_do_triangulo (largura, comprimento):
    return  largura * comprimento /2


def contagem_progressiva(fim):
    for numero in range(fim): # repetir o bloco de zero o fim
        print (numero)          # exibir o número

def apoiar_candidato(nome,vezes):
    for numero in range(vezes):
       # contador = numero +1
        #print(f'{contador} - {nome}')
        if numero < 9:
            print(f'00{numero +1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1, '-', nome)

def brincar_deplim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))



## def contagem_regressiva(inicio, fim):


# estrutura de identificação / execução do script
if __name__ == '__main__':
    print_hi('Gustavo')

# chamar a função de cáculdo da área do retangulo
    resultado =  calcular_area_do_retangulo(3,4)
    print (f'A área do retângulo é de {resultado} m²')

# chamar a função de cálculo da área do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f' A área do quadrado é de {resultado} m²')

# chamar a função de cálculo do triângulo
    resultado = calcular_area_do_triangulo(6,7)
    print(f' A área do triângulo é de {resultado} m²')

# executar contagem progressiva
    contagem_progressiva(10)

# exibir o nome do candidato várias vezes
    apoiar_candidato('Faker',99)

    # brincar de Plim
    brincar_deplim(100)