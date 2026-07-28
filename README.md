# EP2 - Show do Milhão em Python

Projeto desenvolvido para a disciplina de Design de Software (Insper).

O objetivo deste projeto é implementar uma versão simplificada do jogo **Show do Milhão**, utilizando conceitos fundamentais de Python, como listas, dicionários, funções, modularização e manipulação de dados.

## Funcionalidades

- Organização automática das questões por nível de dificuldade;
- Validação da base de questões;
- Sorteio aleatório de perguntas;
- Sorteio de perguntas inéditas;
- Sistema de ajuda (eliminação de alternativas incorretas);
- Sistema de pulos;
- Progressão de dificuldade:
  - Fácil
  - Médio
  - Difícil
- Sistema de premiação crescente;
- Opção de parar o jogo e levar o prêmio conquistado;
- Encerramento automático em caso de erro ou vitória.

## Estrutura do projeto

```
.
├── funcoes.py
├── main.py
├── lib_questoes.py
└── README.md
```

### `funcoes.py`

Arquivo contendo todas as funções utilizadas durante o jogo.

Funções implementadas:

- `transforma_base()`
- `valida_questao()`
- `valida_questoes()`
- `sorteia_questao()`
- `sorteia_questao_inedita()`
- `questao_para_texto()`
- `gera_ajuda()`

### `lib_questoes.py`

Arquivo contendo o banco de questões utilizado pelo jogo.

Cada questão possui o seguinte formato:

```python
{
    "titulo": "...",
    "nivel": "facil",
    "opcoes": {
        "A": "...",
        "B": "...",
        "C": "...",
        "D": "..."
    },
    "correta": "A"
}
```

### `programa.py`

Arquivo principal responsável pela execução do jogo.

## Como executar

Certifique-se de possuir o Python 3 instalado.

No terminal, execute:

```bash
python main.py
```

ou

```bash
python3 main.py
```

## Regras do jogo

- O jogador inicia com:
  - **3 pulos**
  - **2 ajudas**

- As perguntas são sorteadas aleatoriamente.

- Nenhuma pergunta é repetida durante a partida.

- Cada ajuda elimina uma ou duas alternativas incorretas.

- Cada questão aceita apenas uma ajuda.

- Ao acertar uma pergunta, o jogador pode:
  - continuar jogando;
  - parar e levar o prêmio conquistado.

- Caso erre qualquer pergunta, o jogo termina sem prêmio.

## Premiação

| Questão | Prêmio |
|---------:|-------:|
| 1 | R$ 1.000 |
| 2 | R$ 5.000 |
| 3 | R$ 10.000 |
| 4 | R$ 30.000 |
| 5 | R$ 50.000 |
| 6 | R$ 100.000 |
| 7 | R$ 300.000 |
| 8 | R$ 500.000 |
| 9 | R$ 1.000.000 |

## Conceitos utilizados

- Funções
- Modularização
- Listas
- Dicionários
- Estruturas de repetição (`for` e `while`)
- Estruturas condicionais (`if`, `elif`, `else`)
- Biblioteca `random`
- Validação de dados
- Manipulação de strings

## Autor

João Pedro de Paiva Greco

Projeto desenvolvido para fins acadêmicos na disciplina de Design de Software (Insper).