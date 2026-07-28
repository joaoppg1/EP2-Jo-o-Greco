nome = input('Qual é o seu nome?:')
nome = nome.upper()
print(f'Perfeito, {nome}! Você tem direito a pular 3 questões e pedir ajuda em 2 questões!')
print('Você pode escolher dentre as opções: A, B, C, D, ajuda, pula ou parar.')
input('\nAperte ENTER para continuar')
print('\nVamos começar! Aqui vai a primeira questão!')
print('\nVamos começar com questões do nível FACIL!')
input('\nAperte ENTER para continuar...')

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
        resposta = input('\nQual sua resposta?! ')
        