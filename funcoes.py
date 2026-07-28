def transforma_base(lista_questoes):
    dic_final = {}
    for questao in lista_questoes:
        if questao['nivel'] not in dic_final:
            dic_final[questao['nivel']] = [questao]
        else:
            dic_final[questao['nivel']].append(questao)
    return dic_final

def valida_questao(questao):
    retorno = {} 
    
    # Verificando se as chaves existem
    if 'titulo' not in questao:
        retorno['titulo'] = 'nao_encontrado'

    if 'nivel' not in questao:
        retorno['nivel'] = 'nao_encontrado'

    if 'opcoes' not in questao:
        retorno['opcoes'] = 'nao_encontrado'

    if 'correta' not in questao:
        retorno['correta'] = 'nao_encontrado'

    # Verificando se a questão tem exatamente 4 chaves
    contagem_chaves = 0

    for chave in questao.keys():
        contagem_chaves += 1

    if contagem_chaves != 4:
        retorno['outro'] = 'numero_chaves_invalido'
    
    # Verificando se o título é válido
    if 'titulo' in questao:
        if questao['titulo'].strip() == '':
            retorno['titulo'] = 'vazio'
    
    # Verificando se o nível é válido
    if 'nivel' in questao:
        if questao['nivel'] != 'facil' and questao['nivel'] != 'medio' and questao['nivel'] != 'dificil':
            retorno['nivel'] = 'valor_errado'
    
    # Verificando as opções
    if 'opcoes' in questao:
        contagem_chaves = 0

        for chave in questao['opcoes'].keys():
            contagem_chaves += 1

        if contagem_chaves != 4:
            retorno['opcoes'] = 'tamanho_invalido'

        elif 'A' not in questao['opcoes'] or 'B' not in questao['opcoes'] or 'C' not in questao['opcoes'] or 'D' not in questao['opcoes']:
            retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        else:
            opcoes_vazias = {}

            for letra, resposta in questao['opcoes'].items():
                if resposta.strip() == '':
                    opcoes_vazias[letra] = 'vazia'

            if opcoes_vazias != {}:
                retorno['opcoes'] = opcoes_vazias
    
    # Verificando a alternativa correta
    if 'correta' in questao:
        if questao['correta'] != 'A' and questao['correta'] != 'B' and questao['correta'] != 'C' and questao['correta'] != 'D':
            retorno['correta'] = 'valor_errado'
    
    return retorno

def valida_questoes(lista_questoes):
    lista_final = []
    for questao in lista_questoes:
        lista_final.append(valida_questao(questao))
    return lista_final

import random

def sorteia_questao(questoes, nivel):
    return random.choice(questoes[nivel])

def sorteia_questao_inedita(questoes, nivel, questoes_sorteadas):
    questao = sorteia_questao(questoes, nivel)

    while questao in questoes_sorteadas:
        questao = sorteia_questao(questoes, nivel)

    questoes_sorteadas.append(questao)
    return questao

def questao_para_texto(questao, id):
    texto = '----------------------------------------\n'
    texto += f'QUESTAO {id}\n'
    texto += f'{questao["titulo"]}\n'
    texto += 'RESPOSTAS:\n'
    texto += f'A: {questao["opcoes"]["A"]}\n'
    texto += f'B: {questao["opcoes"]["B"]}\n'
    texto += f'C: {questao["opcoes"]["C"]}\n'
    texto += f'D: {questao["opcoes"]["D"]}\n'
    return texto

def gera_ajuda(questao):
    alternativas_erradas = []

    correta = questao['correta']

    for letra, resposta in questao['opcoes'].items():
        if letra != correta:
            alternativas_erradas.append(resposta)

    quantidade = random.randint(1, 2)
    sorteadas = random.sample(alternativas_erradas, quantidade)

    dica = 'DICA:\nOpções certamente erradas: '

    if quantidade == 1:
        dica += sorteadas[0]
    else:
        dica += sorteadas[0] + ' | ' + sorteadas[1]

    return dica


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