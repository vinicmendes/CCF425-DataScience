# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dK7nMhFk6aU2TW9-qtOZUdhhy-ujFWor

> Introdução à Ciência dos Dados \
> Ciência da Computação – UFV/Florestal


* **Nome:** Vinícius de Oliveira Mendes
* **Matrícula:**  3881

# Aula Prática 01
##  Conhecendo o Ambiente e Manipulando Estruturas de Uma Dimensão

**Objetivo:** Conhecer o ambiente de desenvolvimento \
**Pré-requisitos:** Linguagem de programação Python \
**Meta:** Ao final da prática, o aluno será capaz de iniciar o ambiente de desenvolvimento e executar comandos na linguagem Python para manipular uma estrutura de dados de uma dimensão.

----

## Introdução

A ferramenta de desenvolvimento a ser utilizada é chamada Jupyter Notebook. Com ela, é possível executar comandos para análises de dados isoladamente, sem precisar executar todo o código sempre que for preciso fazer algum ajuste. Você pode instalar localmente na sua máquina o [Jupyter Notebook](https://jupyter.org) ou utilizar o [Google Colab](https://colab.research.google.com).

A principal API de desenvolvimento que será utilizada é chamada de [Pandas](https://pandas.pydata.org). Com ela, é possível manipular estruturas de dados complexas para análises de dados.

Dentro da API Pandas, uma estrutura 1-dimensional é a Series. Uma Serie é similar a um arranjo nas linguagens de programação, com algumas características particulares que a torna mais poderosa que as estruturas de arranjos e listas tradicionais.

Seguindo o roteiro abaixo, você deverá utilizar o Jupyter Notebook ou Google Colab para manipular algumas estruturas do tipo Series.

Para instalar as ferramentas e as bibliotecas necessárias, você pode seguir o tutorial que está no PVANet.
"""

### NÃO REMOVA ESSA CÉLULA! ####
!pip install learntools_dados_ufv

#### Não altere essa célula!!! ####
import pandas as pd
import random

from learntools_dados_ufv.core import binder; binder.bind(globals())
from learntools_dados_ufv.ccf425.pratica_1 import *

"""## 1. Gere uma Serie com 500 valores inteiros aleatórios entre -1000 e 1000
Armazene-o na variável `series`. 

Chame a função `q1.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q1.hint()`
"""

# q1.hint()
rand = (random.sample(range(-1000,1000),500))
series = pd.Series(rand)
print(series)

q1.check()

"""## 2. Recupere o maior valor da Série
Armazene-o na variável `series_max`. 

Chame a função `q2.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q2.hint()`
"""

# q2.hint()

series_max = max(series)
print(series_max)

q2.check()

"""## 3. Recupere o menor valor da Série
Armazene-o na variável `series_min`.

Chame a função `q3.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q3.hint()`
"""

# q3.hint()

series_min = min(series)
print(series_min)

q3.check()

"""## 4. Recupere somente os valores positivos da Série
Armazene-os na variável `series_positives`.

Chame a função `q4.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q4.hint()`
"""

# q4.hint()

series_positives = series[series > 0]
print(series_positives)

q4.check()

"""## 5. Recupere somente os valores ímpares da Série
Armazene-os na variável `series_odds`.

Chame a função `q5.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q5.hint()`
"""

# q5.hint()

series_odds = series[series % 2 != 0]
print(series_odds)

q5.check()

"""## 6. Recupere somente os valores das posições/índices de 50 a 100 (inclusive) da Série
Armazene-os na variável `series_range`.

Chame a função `q6.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q6.hint(n)` onde n é o número da dica.
"""

# q6.hint()

series_range = series[50:101]
print(series_range)

q6.check()

"""## 7. Recupere a quantidade de valores pares da Série
Armazene-o na variável `series_even_size`.

Chame a função `q7.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q7.hint(n)` onde n é o número da dica.
"""

# q7.hint()

series_even_size = len(series[series % 2 ==0])
print(series_even_size)

q7.check()

"""## 8. Recupere a quantidade de valores da Série maiores que 500
Armazene-o na variável `series_high_values_size`.

Chame a função `q8.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q8.hint()` onde n é o número da dica.
"""

# q8.hint()

series_high_values_size = len(series[series > 500])
print(series_high_values_size)

q8.check()

"""## 9. Recupere os valores simultaneamente maiores que 500 e menores que 700 da Série
Armazene-o na variável `series_subset_values`.

Chame a função `q9.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q9.hint()` onde n é o número da dica.
"""

# q9.hint()

series_subset_values = series[(series > 500) & (series < 700)]
print(series_subset_values)

q9.check()

"""## 10. Imprima a raiz quadrada de todos os valores da Série
Armazene-os na variável `series_sqrt_values`.

**Atenção**: Mantenha o tipo da série como `float64`. Os valores inválidos devem ser `NaN`.

Chame a função `q10.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q10.hint()` onde n é o número da dica.
"""

# q10.hint()

series_sqrt_values = pow(series,1/2)
print(series_sqrt_values)

q10.check()

"""## 11. Faça sua própria ~5ª~ série!

Agora é sua vez de brincar com as séries. E bem não é *exatamente* a 5ª série, mas é quase!

### 11.a.
Crie uma série (`pd.Series`) que possui os dados das notas de **todas** as turmas de 5ª série de **todas as disciplinas** de uma escola fictícia. Dê um nome pra essa escola e explique quantas disciplinas essas turmas cursam e quantos alunos possuem em cada sala.

Armazene a sua série na variável `grades`.

Chame a função `q11.a.check()` no fim da célula para verificar a resposta.
Você pode pedir dica com `q11.a.hint()`.

#### Resposta: A escola Core possui 5 turmas e 5 matérias ao todo, sendo elas: Matemática, Português, Ciências, Geografia e História. Existem 4 alunos em cada sala.
"""

# q11.a.hint()

notas = random.sample(range(0,100),100)
grades = pd.Series(notas)

materia1 = grades[0:21]
materia2 = grades[21:41]
materia3 = grades[41:61]
materia4 = grades[61:81]
materia5 = grades[81:101]

turma1 = [materia1[0:6],materia2[0:6],materia3[0:6],materia4[0:6],materia5[0:6]]
turma2 = [materia1[6:11],materia2[6:11],materia3[6:11],materia4[6:11],materia5[6:11]]
turma3 = [materia1[11:16],materia2[11:16],materia3[11:16],materia4[11:16],materia5[11:16]]
turma4 = [materia1[16:21],materia2[16:21],materia3[16:21],materia4[16:21],materia5[16:21]]
turma5 = [materia1[21:26],materia2[21:26],materia3[21:26],materia4[21:26],materia5[21:26]]

print("Notas dos alunos matriculados na escola Core")
print(grades)

print("Notas obtidas em Matemática")
print(materia1)
print("Notas obtidas em Portugês")
print(materia2)
print("Notas obtidas em Ciências")
print(materia3)
print("Notas obtidas em Geografia")
print(materia4)
print("Notas obtidas em História")
print(materia5)

print("Notas da turma 1")
print(turma1)
print("Notas da turma 2")
print(turma2)
print("Notas da turma 3")
print(turma3)
print("Notas da turma 4")
print(turma4)
print("Notas da turma 5")
print(turma5)

q11.a.check()

"""### 11.b.
Agora, usando a série `grades` que você criou, extraia 5 informações que podem ser úteis em uma reunião de pais, análise pedagócica, avaliações, etc.

Esta questão não possui `check`.
Mas você pode pedir dica com `q11.b.hint()`.
"""

# q11.b.hint()
print("Notas obtidas em Matemática maiores que 60")
aprovado = materia1[materia1 > 60]
print(aprovado)

print("Quantidade de alunos aprovados em Geografia")
geo = (materia4[materia4 >= 60]).size
print(geo)

print("Notas obtidas em História menores que 60")
hist = materia5[materia5 < 60]
print(hist)

print("Notas pares em Português")
pt = materia2[materia2 % 2 == 0]
print(pt)

print("Notas impares em Ciências")
ciencia = materia3[materia3 % 2 != 0 ]
print(ciencia)

"""### 11.c.
Faça uma breve análise sobre a utilidade e limitações de uma série `pandas`. Também inclua uma opinião pessoal curta se gostou ou não dessa estrutura.

Esta questão não possui `check`.
Mas você pode pedir dica com `q11.c.hint()`.
"""

# q11.c.hint()

"""#### Resposta: A utilização de séries para os desafios propostos na questão 11 torna-se difícil e inviável para certas implementações. Ela pode ser utilizada quando trata-se apenas de uma informação, como uma lista de notas de uma turma em uma única matéria. Entretanto, quando há a necessidade de representar diversos dados, o entendimento da série se torna trabalhoso, uma alternativa pra isso é a utilização de Dataframes."""