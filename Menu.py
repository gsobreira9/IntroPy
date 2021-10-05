

    # 1 - imports / bibliotecas

    # 2 - Classe

    # 3 -  Métodos e Funções
    # def = definition = definição
def print_hi(name):
        print(f'Oi, {name}')  # a partir do Python 3
        print('Oi, ' + name)  # antes do Python 3

def calcular_area_do_retangulo(largura, comprimento):
        return largura * comprimento

def calcular_area_do_quadrado(lado):
        return lado ** 2

def calcular_area_do_triangulo(largura, comprimento):
        return largura * comprimento / 2

def contagem_progressiva(fim):
        for numero in range(fim):  # repetir o bloco de zero até o fim
            print(numero)  # exibir o número

def apoiar_candidato(nome, vezes):
        for numero in range(vezes):
            # contador = numero + 1
            # print(f'{contador} - {nome}')

            if numero < 9:
                print(f'00{numero + 1} - {nome}')
            elif numero < 99:
                print(f'0{numero + 1} - {nome}')
            else:
                print(numero + 1, '-', nome)

def brincar_de_plim(fim):
        for numero in range(fim):
            if numero % 4 == 0:
                print('PLIM!')
            else:
                print('{:0>3}'.format(numero))

def sair():
        print('Obrigado e Volte Sempre')
def exibir_menu(escolha):
        opcao = {
            1: print_hi('José'),
            2: calcular_area_do_retangulo(8, 9),
            3: calcular_area_do_quadrado(7),
            4: calcular_area_do_triangulo(5, 4),
            5: contagem_progressiva(10),
            6: apoiar_candidato('Sabado', 10),
            7: brincar_de_plim(20),
            8: sair()
        }
        return opcao.get(escolha, 'Opção Inválida')

    # estrutura de identificação / execução do
if __name__ == '__main__':
        continua = True

        # while continua:
        print('#####################################')
        print('#                                   #')
        print('#    M E N U   D E   O P Ç Õ E S    #')
        print('#                                   #')
        print('#    1 - Olá Mundo                  #')
        print('#    2 - Área do Retângulo          #')
        print('#    3 - Área do Quadrado           #')
        print('#    4 - Área do Triângulo          #')
        print('#    5 - Contagem Progressiva       #')
        print('#    6 - Apoiar Candidato           #')
        print('#    7 - Brincar de Plim            #')
        print('#                                   #')
        print('#    Z - Sair                       #')
        print('#                                   #')
        print('#####################################')

        escolha = input("Escolha sua opção")
        # print(f'A sua escolha foi: {escolha}')
        exibir_menu(escolha)
