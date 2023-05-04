import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

print('\033[35mConversor de decimal para outras bases!\033[0m\nBem-vindo 😊\n')

while True:
    print('''O que você deseja fazer?
\033[32m[1] Converter decimal.
\033[34m[2] Ver os créditos.
\033[31m[3] Sair do programa.\033[0m''')
    modo = input('Insira APENAS o número da opção que você deseja > ')

    match(modo):
        case '1':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                base = input(
                    "Você deseja converter seu decimal para qual base?\n\n\033[35m[1] Binário.\n\033[34m[2] Hexadecimal.\n\033[36m[3] Octadecimal.\033[0m\n\n> ")
                numConvertido = ''

                match (base):
                    case '1':
                        numInserido = int(input("Insira seu número decimal aqui: "))
                        numDecimal = numInserido
                        sistema = '\033[35mbinário\033[0m'
                        while numDecimal > 0:
                            numConvertido += str(numDecimal % 2)
                            numDecimal = numDecimal // 2

                    case '2':
                        numInserido = int(input("Insira seu número decimal aqui: "))
                        numDecimal = numInserido
                        sistema = '\033[34mhexadecimal\033[0m'
                        hex = [0, 1, 2, 3, 4, 5, 6, 7, 8,
                               9, 'A', 'B', 'C', 'D', 'E', 'F']
                        while numDecimal > 0:
                            numConvertido += str(hex[numDecimal % 16])
                            numDecimal = numDecimal // 16

                    case '3':
                        numInserido = int(input("Insira seu número decimal aqui: "))
                        numDecimal = numInserido
                        sistema = '\033[36moctadecimal\033[0m'
                        while numDecimal > 0:
                            numConvertido += str(numDecimal % 8)
                            numDecimal = numDecimal // 8

                    case _:
                        print(
                            '\033[31mVocê inseriu algo inválido!\033[0m\nTente novamente.')
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue

                # invertendo os números
                numInvertido = ''
                for digito in range(len(numConvertido)-1, -1, -1):
                    numInvertido += str(numConvertido[digito])
                numConvertido = numInvertido

                print(
                    f"\nO número \033[32m{numInserido}\033[0m dentro do sistema {sistema} é: {numConvertido}.")
                time.sleep(2)
                input('Enter continua...')
                os.system('cls' if os.name == 'nt' else 'clear')
                break

        case '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(
                '''Obrigado por querer nos conhecer 😁
                
Este programa está na versão \033[32m[1.5]\033[0m, foi desenvolvido por:
\033[35m> João Victor Ferreira - 3424143
\033[34m> Arthur Cardoso de Lima - 33561095
\033[33m> Guilherme Gonçalves Santos - 33009236
\033[32m> Tiago Vieira Farias - 33653500 \033[0m
Como projeto do 1° semestre de Ciência da Computação - Universidade Cruzeiro do Sul.

Envolvendo as matérias Programação de Computadores e Organização e Arquitetura de Computadores.''')
            time.sleep(4)
            input('\nDigite enter para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')

        case '3':
            print('\nObrigado por utilizar nosso programa!\n\nVolte sempre 😉')
            break

        case _:
            print(
                '\033[31m\nVocê inseriu algo inválido!\033[0m\nTente novamente.')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
