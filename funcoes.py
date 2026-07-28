def transforma_base(lista_questoes):
    dic_final = {}
    for questao in lista_questoes:
        if questao['nivel'] not in dic_final:
            dic_final[questao['nivel']] = [questao]
        else:
            dic_final[questao['nivel']].append(questao)
    return dic_final