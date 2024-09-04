# Modelos Supervisionados de Machine Learning

**O que são?** São modelos preditivos, ou seja, que tentam prever o comportamento de observações de fora da amostra.

- A diferença de magnitude das variáveis não impacta nos resultados uma vez que modelos supervisionados não calculam distâncias. Portanto, a padronização não é necessária (compensada pelo beta).
- A normalização, entretanto, pode ser necessária (necessário avaliar).

## Modelos GLM (Modelos Lineares Generalizados)

Classe de modelos estatísticos que generalizam a regressão linear ao permitir diferentes distribuições para a variável resposta e diferentes funções de ligação.

\[ Y = f(X_1, X_2, X_3, ..., X_k) \]

| Modelo de Regressão                    | Característica da Variável Dependente            | Distribuição                          |
|----------------------------------------|--------------------------------------------------|---------------------------------------|
| **Linear**                             | Quantitativa                                     | Normal                                |
| **Com Transformação de Box-Cox**       | Quantitativa                                     | Normal Após a Transformação           |
| **Logística Binária**                  | Qualitativa com 2 Categorias (_Dummy_)           | Bernoulli                             |
| **Logística Multinomial**              | Qualitativa M (_M > 2_ Categorias)               | Binomial                              |
| **Poisson**                            | Quantitativa com Valores Inteiros e Não Negativos (_Dados de Contagem_) | Poisson        |
| **Binomial Negativo**                  | Quantitativa com Valores Inteiros e Não Negativos (_Dados de Contagem_) | Poisson-Gama   |

## Observação

Todas as imagens de lousas e os scripts presentes nesse repositório são de autoria dos professores. À mim cabem apenas algumas notas e pequenas alterações de código.
