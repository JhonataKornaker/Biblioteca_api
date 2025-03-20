# Relatório de Teste de Software - Biblioteca Api

Este relatório apresenta os testes realizados no software Biblioteca Api, com o objetivo de garantir a qualidade, estabilidade e conformidade com os requisitos estabelecidos. Os testes foram conduzidos utilizando a ferramenta pytest e abrangeram diferentes níveis, incluindo testes unitários, de integração, de regressão, de sistema e de aceitação.

Durante o processo, foram avaliados aspectos como funcionalidade, desempenho e possíveis falhas, assegurando que o software atenda às expectativas dos usuários e aos critérios técnicos definidos.

## 1. *Testes Unitário*

#### **Objetivo** :

Garantir que cada unidade do sistema (função/método) esteja funcionando de acordo com o esperado de maneira isolada.

#### **Metodologia** :

- `test_cadastrar_usuario`: Verifica se um usuário é cadastrado com sucesso; Verifica se o sistema impede o cadastro de uma matrícula duplicada.
- `test_login`: Verifica a autenticação de login com sucesso; Verifica a autentica de login com senha invalida; Verifica a autenticação com usuario inexistente
- `test_cadastrar_livro`: Verifica se um livro é cadastrado corretamente no sistema.
- `test_emprestar_livro`: Verifica se um livro pode ser emprestado corretamente e se o sistema impede o empréstimo de um livro já emprestado.
- `test_devolver_livro`: Verifica se um livro pode ser devolvido corretamente e se o sistema impede a devolução de um livro já disponível.
- `test_consultar_livro`: Verifica se um livro pode ser consultado corretamente e se o sistema lida com a consulta de um livro inexistente.
- `test_alterar_livro`: Verifica se as informações de um livro podem ser alteradas corretamente e se o sistema lida com a alteração de um livro inexistente.
- `test_excluir_livro`: Verifica se um livro pode ser excluído corretamente e se o sistema lida com a exclusão de um livro inexistente.

## 2. *Testes de Regressão*

#### **Objetivo** :

Verificar se as mudanças no código não quebraram funcionalidades existentes e se o sistema continua funcionando como antes após novas alterações.

#### **Metodologia** :

- Repetição de testes antigos para validar se mudanças recentes não afetaram negativamente as funcionalidades.
- As funções cadastrar_livro, alterar_livro e emprestar_livro foram testadas para garantir que não houve impacto nas funcionalidades anteriores.

## 3. *Testes de Integração*

#### **Objetivo** :

Verificar se os componentes do sistema interagem corretamente entre si, como por exemplo, o cadastro e login, ou o relacionamento entre livros e usuários.

#### **Metodologia** :

- Testes realizados com a interação entre as funcionalidades de cadastro e login, assim como a relação com usuários e livros.

## 4. *Testes de Sistema*

#### **Objetivo** :

Verificar o comportamento do sistema como um todo, simulando interações reais entre os diferentes componentes do sistema, incluindo simulação de erros.

#### **Metodologia** :

- Validamos o fluxo completo de interação entre o sistema de livros e os usuários.

## 5. *Testes de Aceitação*

#### **Objetivo** :

O teste de aceitação verifica se todas as funcionalidades principais do sistema funcionam corretamente de ponta a ponta. Isso significa que ele testa o fluxo completo de um usuário utilizando o sistema, desde o cadastro até a exclusão de um livro. Diferente do teste de sistema, não enfatiza falhas técnicas, mas sim a experiência do usuário.

#### **Metodologia** :

- Testes realizados simulando a utilização do sistema por um usuário.
- Verificações do cadastro, consulta e exclusão de livros foram feitas.

## 6. *Testes de Desempenho*

#### **Objetivo** :

Os testes de desempenho foram realizados para medir a eficiência das operações no sistema de gerenciamento de livros da biblioteca. Os testes avaliaram o tempo necessário para cadastrar, emprestar, devolver e consultar livros em um banco de dados em memória, utilizando um conjunto de 5.000 registros.

#### **Metodologia e Resultados** :

| Testes | Tempo Médio (&#181;s) |
|:--------:|:-----------------------:|
|`test_desempenho_devolver_livros` | 1,063.6 |
| `test_desempenho_emprestar_livros` | 1,082.8 |
| `test_desempenho_consultar_livros` | 1,068.9 |
| `test_desempenho_cadastrar_livros` | 2,109.1 |

**Melhor Desempenho** : A devolução de livros foi a operação mais rápida, com um tempo médio de 1.063,6 µs e 940 operações por segundo.

**Emprestar vs. Consultar** : A consulta teve um tempo médio levemente menor do que o empréstimo, indicando que ambas as operações têm desempenho semelhante.

**Pior desempenho** : O cadastro de livros teve o maior tempo médio (2.109,1 µs) e a menor taxa de operações por segundo (474 ops/s).
O alto desvio padrão (329,4 µs) sugere que essa operação pode ser mais variável, talvez por manipulação de estruturas de dados internas.


## Como Executar os Testes

```bash
git clone https://github.com/JhonataKornaker/Biblioteca_api.git
cd biblioteca_api
pip install -r requirements.txt
```

Para realizar os testes de modo separado usa-se o comando abaixo para realizar cada um dos testes:

```
pytest tests/test_unitario.py -v
pytest tests/test_integracao.py -v
pytest tests/test_regressao.py -v
pytest tests/test_sistema.py -v
pytest tests/test_aceitacao.py -v
pytest tests/test_desempenho.py -v
```

Ou para testar todos de uma vez:

```
pytest -v
```