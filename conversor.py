import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

print('\033[35mConversor de decimal para outras bases!\033[0m\nBem-vindo 😊\n')

while True:
    print('''O que você deseja fazer?
\033[32m[1] Converter decimal.
\033[0m[2] Ver os créditos.
\033[31m[3] Sair do programa.\033[0m''')
    modo = input('Insira APENAS o número da opção que você deseja > ')

    match(modo):
        case '1':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                base = input(
                    "Você deseja converter seu decimal para qual base?\n\n\033[35m[1] Binário.\n\033[34m[2] Hexadecimal.\n\033[36m[3] Octadecimal.\033[0m\n\n> ")
                numInserido = int(
                    input("Insira seu número decimal aqui: "))
                numDecimal = numInserido
                numConvertido = ''

                match (base):
                    case '1':
                        sistema = '\033[35mbinário\033[0m'
                        while numDecimal > 0:
                            numConvertido += str(numDecimal % 2) 
                            numDecimal = numDecimal // 2
                    
                    case '2':
                        sistema = '\033[34mhexadecimal\033[0m'
                        hex = [0, 1, 2, 3, 4, 5, 6, 7, 8,
                               9, 'A', 'B', 'C', 'D', 'E', 'F']
                        while numDecimal > 0:
                            numConvertido += str(hex[numDecimal % 16])
                            numDecimal = numDecimal // 16

                    case '3':
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
                
                if sistema == '\033[34mhexadecimal\033[0m' or sistema == '\033[36moctadecimal\033[0m':
                    numInvertido = ''
                    for digito in range(len(numConvertido)-1, -1, -1):
                        numInvertido += str(numConvertido[digito])
                    numConvertido = numInvertido

                print(
                    f"\nO número \033[32m{numInserido}\033[0m dentro do sistema {sistema} é: {numConvertido}.")
                time.sleep(5)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
        
        case '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(
                'Obrigado por querer nos conhecer 😁\n\nEste programa está na versão \033[32m[1.5]\033[0m, foi desenvolvido por:\n> \033[35mJoão Victor Ferreira - 34241434\033[0m\n> Arthur Cardoso\n>\n\nComo projeto do 1° semestre de Ciência da Computação - Universidade Cruzeiro do Sul.\n\nEnvolvendo as matérias Programação de Computadores e Organização e Arquitetura de Computadores.')
            time.sleep(8)
            os.system('cls' if os.name == 'nt' else 'clear')

        case '3':
            print('\nObrigado por utilizar nosso programa!\n\nVolte sempre 😉')
            break

        case _:
            print('\033[31mVocê inseriu algo inválido!\033[0m\nTente novamente.')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue