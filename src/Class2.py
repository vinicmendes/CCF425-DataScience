# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12MN9JXeAOW7NSCYjz2XzYhWKvxNY3L9d

> Introdução à Ciência dos Dados \
> Ciência da Computação – UFV/Florestal


* **Nome:** Vinícius de Oliveira Mendes
* **Matrícula:**  3881

# Aula Prática 02
##  Estatística Descritiva

**Objetivo:** Avaliar dados numéricos com base em cálculos estatísticos \
**Pré-requisitos:** Linguagem de programação Python, estatística básica \
**Meta:** Ao final da prática, o aluno será capaz de utilizar ferramentas de análise de dados para calcular indicadores estatísticos e comparar valores.

----
"""

### NÃO REMOVA ESSA CÉLULA! ####
!pip install learntools_dados_ufv

!wget https://raw.githubusercontent.com/gfviegas/CCF425-resources/master/p2/series.csv
!wget https://raw.githubusercontent.com/gfviegas/CCF425-resources/master/p2/altura_homens.csv
!wget https://raw.githubusercontent.com/gfviegas/CCF425-resources/master/p2/altura_mulheres.csv

#### Não altere essa célula!!! ####
import pandas as pd
from scipy import stats

from learntools_dados_ufv.core import binder; binder.bind(globals())
from learntools_dados_ufv.ccf425.pratica_2 import *

"""# Roteiro

## Leitura dos dados
Veja os dados do arquivo `series.csv`. 

Use a opção `squeeze=True` para obter uma Série do arquivo e não um DataFrame (comportamento default).
"""

series = pd.read_csv('./series.csv', index_col=False, header=None, squeeze=True)
series

"""## Explore os dados com base em estatísticas descritivas"""

# Mínimo
print('O valor mínimo é: {}'.format(series.min()))

# Máximo
print('O valor máximo é: {}'.format(series.max()))

# Média
print('O valor da média é: {:.2f}'.format(series.mean()))

# Desvio Padrão
print('O valor do desvio padrão é: {:.2f}'.format(series.std()))

# Moda
print('A moda é: {}'.format(series.mode()))

"""## Calcule os percentis"""

# Percentil 25 (1º quartil)
print('Percentil 25: {:.2f}'.format(series.quantile(.25)))

# Percentil 50 (2º quartil ou mediana)
print('Percentil 50: {:.2f}'.format(series.quantile(.50)))

# Percentil 75 (3º quartil)
print('Percentil 75: {:.2f}'.format(series.quantile(.75)))

# Percentil 95
print('Percentil 95: {:.2f}'.format(series.quantile(.95)))

"""## Calcule a tablea de frequências"""

series.value_counts()

"""# Exercícios

## 1. Leia os arquivos `altura_homens.csv` e `altura_mulheres.csv`
Esses arquivos contém as alturas (em cm) de 1000 homens e 1000 mulheres, respectivamente. \
Leia os arquivos e salve-os em uma variável contendo uma série Pandas com os dados respectivos.

Armazene-os nas variáveis `men_height_series` e `women_height_series` respectivamente. 

Chame a função `q1.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q1.hint()`
"""

# q1.hint()

men_height_series = pd.read_csv('./altura_homens.csv', index_col=False, header=None, squeeze=True)
women_height_series = pd.read_csv('./altura_mulheres.csv', index_col=False, header=None, squeeze=True)

print('Dados dos homens:')
display(men_height_series)

print('Dados das mulheres:')
display(women_height_series)

q1.check()

"""## 2. Recupere a altura mínima e máxima dos homens e das mulheres dessas amostras.
Armazene a altura mínima e máxixma dos homens nas variáveis `men_min_height` e `men_max_height`, respectivamente. \
Armazene a altura mínima e máxixma das mulheres nas variáveis `women_min_height` e `women_max_height`, respectivamente. 

Chame a função `q2.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q2.hint()`
"""

# q2.hint()

men_min_height = men_height_series.min()
men_max_height = men_height_series.max()
women_min_height = women_height_series.min()
women_max_height = women_height_series.max()

print('A altura mínima dos homens é: {:.2f}'.format(men_min_height))
print('A altura máxima dos homens é: {:.2f}'.format(men_max_height))

print('A altura mínima das mulheres é: {:.2f}'.format(women_min_height))
print('A altura máxima das mulheres é: {:.2f}'.format(women_max_height))

q2.check()

"""## 3. Recupere a média de altura dos homens e das mulheres.
Armazene-as nas variáveis `men_mean_height` e `women_mean_height`, respectivamente.

Chame a função `q3.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q3.hint()`
"""

# q3.hint()

men_mean_height = men_height_series.mean()
women_mean_height =women_height_series.mean()

print('A altura média dos homens é: {:.2f}'.format(men_mean_height))
print('A altura média das mulheres é: {:.2f}'.format(women_mean_height))

q3.check()

"""## 4. Recupere a mediana de altura dos homens e das mulheres
Armazene-as nas variáveis `men_median_height` e `women_median_height`, respectivamente.

Chame a função `q4.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q4.hint()`
"""

# q4.hint()

men_median_height = men_height_series.median()
women_median_height = women_height_series.median()

print('O valor da mediana da altura dos homens é: {:.2f}'.format(men_median_height))
print('O valor da mediana da altura das mulheres é: {:.2f}'.format(women_median_height))

q4.check()

"""## 5. Recupere o desvio padrão da altura dos homens e das mulheres
Armazene-os nas variáveis `men_std_height` e `women_std_height`, respectivamente.

Chame a função `q5.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q5.hint()`
"""

# q5.hint()

men_std_height = men_height_series.std()
women_std_height =women_height_series.std()

print('O valor do desvio padrão da altura dos homens é: {:.2f}'.format(men_std_height))
print('O valor do desvio padrão da altura das mulheres é: {:.2f}'.format(women_std_height))

q5.check()

"""## 6. Recupere o percentual de homens com altura menor que 160cm
Armazene-o na variável `men_shorter_160cm_perc`.

Chame a função `q6.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q6.hint(n)` onde n é o número da dica.
"""

q6.hint()
q6.hint(2)
q6.hint(3)

men_shorter_160cm_perc = men_height_series[men_height_series < 160].count()/1000 * 100

print(men_shorter_160cm_perc)

q6.check()

"""## 7. Recupere o percentual de mulheres com altura maior que 180cm
Armazene-o na variável `women_taller_180cm_perc`.

Chame a função `q7.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q7.hint(n)` onde n é o número da dica.
"""

# q7.hint()

women_taller_180cm_perc = women_height_series[women_height_series > 180].count()/1000 * 100
print(women_taller_180cm_perc)

q7.check()

"""## 8. Um homem com altura 185cm está em qual percentil?
Armazene a resposta na variável `men_185cm_percentile`.

Chame a função `q8.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q8.hint(n)` onde n é o número da dica.
"""

# q8.hint()
from scipy import stats
men_185cm_percentile = stats.percentileofscore(men_height_series, 185)
print(men_185cm_percentile)

q8.check()

"""## 9. Uma mulher com altura 150cm está em qual percentil?
Armazene a resposta na variável `women_150cm_percentile`.

Chame a função `q9.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q9.hint(n)` onde n é o número da dica.
"""

# q9.hint()

women_150cm_percentile = stats.percentileofscore(women_height_series, 150)
print(women_150cm_percentile)

q9.check()

"""## 10. Quais as três alturas de homens que são as mais frequentes? Quantos homens possuem, no total, essas alturas?
Armazene a resposta das perguntas nas variáveis `men_top3_height` e `men_in_top3_height` respectivamente.

Chame a função `q10.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q10.hint(n)` onde n é o número da dica.
"""

# q10.hint()

men_top3_height = men_height_series.value_counts().head(3)
men_in_top3_height = int(men_top3_height.sum())

print('As alturas mais frequentes dos homens são: ', men_top3_height)
print('A quantidade de homens que possuem essas alturas são: ',men_in_top3_height)

q10.check()

"""## 11. Uma mulher com altura 185cm está distante quantos desvios padrões da média das mulheres? E uma de 145cm?
Armazene as respostas das perguntas nas variáveis `women_185cm_std_distance` e `women_145cm_std_distance` respectivamente.

Chame a função `q11.check()` no fim da célula para verificar a resposta.
Você pode pedir dicas com `q11.hint(n)` onde n é o número da dica.
"""

# q11.hint()
zscore = lambda x, mean, std: (x-mean)/std
women_185cm_std_distance = zscore(185,women_height_series.mean(),women_height_series.std())
women_145cm_std_distance = zscore(145,women_height_series.mean(),women_height_series.std()) * -1

print('A quantidade de desvios padrões distante da média de uma mulher de 185cm é: ',women_185cm_std_distance)
print('A quantidade de desvios padrões distante da média de uma mulher de 145cm é: ',women_145cm_std_distance)

q11.check()

"""## 12.
É possível afirmar com determinado grau de confiança que uma pessoa com altura 150cm é um homem ou uma mulher?
- E uma pessoa com altura 190cm?
- E uma pessoa com altura 165cm?


Esta questão não possui `check`.
Mas você pode pedir dica com `q12.hint()`.

### Resposta:

(escreva aqui sobre seu problema 12.)
"""

# q12.hint()

print("Analisando os dados a seguir, pode-se observar que é mais provável uma mulher possuir 150 cm do que um homem.")
print("Média da altura das mulheres: ",women_mean_height)
print("Desvio padrão da altura das mulheres: ",women_std_height)

print("Média da altura dos homens: ",men_mean_height)
print("Desvio padrão da altura dos homens: ",men_std_height)

print("Já uma pessoa com 190cm, é mais provável que ela seja homem.")
print("Por outro lado, não há resultado com certo grau de confiança.")

"""## 13. As alturas dos homens e mulheres seguem uma distribuição Normal?
Justifique a sua resposta com evidências.

Esta questão não possui `check`.
Mas você pode pedir dica com `q13.hint()`.

### Resposta:

O teste de normalidade que escolhi define testa a hipotese nula dos dados extraidos. Dessa forma, como o P-Valor obtido abaixo foi superior a 0.05, a hipótese nula é aceitavel e assim os dados das mulheres seguem a distribuição normal.
"""

# q13.hint()

women_height_series.plot(kind= "hist")
shapiro_wilk = stats.shapiro(women_height_series)
print("Teste de normalidade(P-value) = ", shapiro_wilk[1])

"""Da mesma forma, podemos provar que as alturas dos homens seguem uma distribuíção normal, como provado abaixo:"""

men_height_series.plot(kind="hist")
shapiro_wilk = stats.shapiro(men_height_series)
print("P-valor = ", shapiro_wilk[1])

"""## 14. Para que serve a função “describe()” de uma Series?
Justifique a sua resposta com evidências.

Esta questão não possui `check`.
Mas você pode pedir dica com `q14.hint()`.

### Resposta:

Essa função é responsável por gerar estatísticas descritivas da série.
"""

# q14.hint()
women_height_series.describe()

"""## 15. Para que serve a função "unique()” de uma Series?
Justifique a sua resposta com evidências.

Esta questão não possui `check`.
Mas você pode pedir dica com `q15.hint()`.

### Resposta:

Essa Função é responsável por identificar e retornar os valores únicos de uma séire, ou seja, os valores que não se repetem. A forma com que eles são exibidos é baseada na ordem de aparição.
"""

# q15.hint()

men_height_series.unique()