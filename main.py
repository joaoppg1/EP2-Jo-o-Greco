nome = input('Qual é o seu nome?:')
nome = nome.upper()
print(f'Perfeito, {nome}! Você tem direito a pular 3 questões e pedir ajuda em 2 questões!')
print('Você pode escolher dentre as opções: A, B, C, D, ajuda, pula ou parar.')
input('\nAperte ENTER para continuar')
print('\nVamos começar! Aqui vai a primeira questão!')
print('\nVamos começar com questões do nível FACIL!')
input('\nAperte ENTER para continuar...')

from funcoes import transforma_base
from funcoes import valida_questao
from funcoes import valida_questoes
from funcoes import sorteia_questao
from funcoes import sorteia_questao_inedita
from funcoes import questao_para_texto
from funcoes import gera_ajuda

from lib_questoes import quest
premios = [
    1000,
    5000,
    10000,
    30000,
    50000,
    100000,
    300000,
    500000,
    1000000
]
questoes_por_nivel = transforma_base(quest)
pulos = 3
ajudas = 2
premio = 0
numero_questao = 1
questoes_sorteadas = []
jogo_acontecendo = True

while jogo_acontecendo:

    if numero_questao <= 3:
        nivel = 'facil'

    elif numero_questao <= 6:
        nivel = 'medio'

    else:
        nivel = 'dificil'

    questao = sorteia_questao_inedita(questoes_por_nivel, nivel, questoes_sorteadas)

    respondendo = True
    ajuda_usada_na_questao = False
    pulou = False
    while respondendo and jogo_acontecendo:
        print(questao_para_texto(questao, numero_questao))
        resposta = input('\nQual sua resposta?: ')
        if resposta == questao['correta']:
            premio = premios[numero_questao - 1]
            print(f'Resposta correta! Seu prêmio atual é de R$ {premio:.2f}')
            respondendo = False
            if premio == 1000000:
                print(f'PARABÉNS, {nome.upper()}!')
                print('Você venceu o jogo!')
                print(f'Seu prêmio final é de R$ {premio:.2f}')
                jogo_acontecendo = False
            else:
                decisao = input('\nDigite "parar" para sair com o prêmio ou "continuar" para continuar: ')

                while decisao != 'parar' and decisao != 'continuar':
                    print('Opção inválida!')
                    decisao = input('Digite "parar" ou "continuar": ')

                if decisao == 'parar':
                    print(f'Você parou com o prêmio de R$ {premio:.2f}!')
                    jogo_acontecendo = False

                else:
                    numero_questao += 1
                    if numero_questao == 4:
                        print('Agora vamos para questões do nível MEDIO!')

                    elif numero_questao == 7:
                        print('Agora vamos para questões do nível DIFICIL!')
                        input('Aperte ENTER para continuar...')
        elif resposta == 'ajuda':
            if ajuda_usada == True:
                print('Você já pediu ajuda nesta questão!')
            elif ajudas == 0:
                print('Você não tem mais ajudas disponíveis!')
            else:
                print(gera_ajuda(questao))
                ajudas -= 1
                ajuda_usada = True
                print(f'Você ainda possui {ajudas} ajuda(s).')
        elif resposta == 'pula':
            if pulos == 0:
                print('Você não tem mais pulos disponíveis!')
            else:
                pulos -= 1
                print('Você pulou a questão!')
                print(f'Você ainda possui {pulos} pulo(s).')
                respondendo = False
                input('Aperte ENTER para continuar...')
        