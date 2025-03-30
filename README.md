
# Sistema de Gerenciamento Comercial para Sorveterias

Este projeto é um sistema de linha de comando desenvolvido em Python, com o objetivo de simplificar e otimizar a gestão comercial de sorveterias. Utilizando SQLAlchemy para manipulação de banco de dados SQLite, o sistema oferece uma interface intuitiva para o gerenciamento de sorveterias, sabores, clientes e pedidos.

## Sumário

-   [Funcionalidades](#funcionalidades)
-   [Requisitos](#requisitos)
-   [Instalação](#instalação)
-   [Uso](#uso)
-   [Exemplos](#exemplos-de-cadastros-e-listagens)
-   [Estruturas](#estruturas)
-   [Banco de Dados](#banco-de-dados)
-   [Conclusão](#conclusão)
-   [Notas](#notas)
-   [Contribuição](#contribuição)

## Funcionalidades

Nosso sistema oferece as seguintes funcionalidades principais:

-   **Cadastro de Sorveterias:** Permite adicionar e gerenciar informações de diferentes sorveterias (nome, endereço e telefone).
-   **Cadastro de Sabores:** Permite registrar novos sabores de sorvete, associando-os a sorveterias específicas (nome, descrição, preço).
-   **Cadastro de Clientes:** Permite criar registros detalhados de clientes (nome, idade e telefone).
-   **Realização de Pedidos:** Permite que clientes façam pedidos, selecionando sabores e calculando automaticamente o total.
-   **Listagem de Pedidos:** Exibe uma lista de todos os pedidos realizados, com detalhes do cliente, sabores e total.
-   **Listagem de Sorveterias e Clientes:** Exibe listas detalhadas de todas as sorveterias, seus determinados sabores e clientes cadastrados.
-   **Exclusão de Sorveterias e Clientes:** Permite a exclusão de registros de sorveterias e clientes.

## Requisitos

-   Python **3.11**+
-   Bibliotecas Python:
    -   **SQLAlchemy** (ORM para banco de dados com SQLite embutido)
    -   **mypy** (Verificador estático de tipos)
    -   **os** (nativa do Python)
    -   **sys** (nativa do Python)
    -   **datetime** (nativa do Python)
    -   **time** (nativa do Python)

## Instalação

1.  Clone o repositório em sua máquina local:

    ```bash
    git clone https://github.com/gustavor0d/poo_project.git
    ```

2.  Entre no repositório:
   
    ```bash
    cd poo_project
    ```

3.  Crie um ambiente virtual (venv):

    ```bash
    python -m venv venv
    ```

4.  Ative o ambiente virtual:

    -   Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    -   Linux ou macOS:

        ```bash
        source ./venv/bin/activate
        ```

5.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

6.  Execute o arquivo principal para iniciar a aplicação:

    ```bash
    python.exe main.py
    ```

## Uso

### Menu Principal

Ao executar o programa, o menu principal é exibido com opções numéricas para cada funcionalidade:

```
Menu:
1. Cadastrar Sorveteria
2. Cadastrar Sabor
3. Cadastrar Cliente
4. Realizar Pedido
5. Listar Pedidos
6. Listar Sorveterias
7. Listar Clientes
0. Sair
```

Insira o número correspondente à funcionalidade desejada. O sistema guiará você através dos processos de cadastro, listagem e exclusão de dados.

## Exemplos de Cadastros e Listagens

### Exemplo de Cadastro de Sorveterias

1. Selecione a opção `1` do menu para cadastrar uma sorveteria.  
2. Siga as instruções na tela para inserir o **nome**, **endereço** e **telefone** da sorveteria.  
3. Caso não haja erros, o sistema confirmará o cadastro e retornará ao menu principal, atribuindo um **Identificador Único** à sorveteria.  

### Exemplo de Cadastro de Sabores

1. Selecione a opção `2` do menu para cadastrar um sabor em uma sorveteria.  
2. Informe o **Identificador Único** da sorveteria à qual deseja adicionar o sabor.  
3. Siga as instruções na tela para inserir o **nome do sabor**, **descrição** e **preço**.  
4. Caso não haja erros, o sistema confirmará o cadastro e retornará ao menu principal.  

### Exemplo de Listagem de Sorveterias e Sabores

1. Selecione a opção `6` do menu para listar as sorveterias.  
2. A lista de sorveterias cadastradas será exibida, contendo seus respectivos **nomes**, **endereços**, **telefones** e a **quantidade de sabores cadastrados**.  
3. Nesta tela, um **menu secundário** será apresentado, permitindo:  
   - **Listar os sabores** cadastrados de uma determinada sorveteria.  
   - **Deletar uma sorveteria**.  
   - **Voltar ao menu principal**.  
4. Ao selecionar a opção `1` para listar os sabores, o sistema solicitará que insira o **Identificador Único** da sorveteria. Em seguida, exibirá uma lista com os sabores cadastrados, incluindo suas **descrições** e **preços**.  

## Estruturas 

###  Estrutura do Sistema

O sistema é estruturado em torno das seguintes entidades principais:

-   `Sorveteria`: Gerencia as informações das sorveterias cadastradas (nome, endereço, telefone).
-   `Sabor`: Registra os diferentes sabores de sorvetes disponíveis (nome, descrição, preço, sorveteria).
-   `Cliente`: Mantém os registros dos clientes que realizam pedidos (nome, idade, telefone).
-   `Pedido`: Gerencia os pedidos feitos pelos clientes (cliente, sabores, valor total, data do pedido).

###  Estrutura de Arquivos

```
poo_project/
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── cliente.py
│   ├── pedido.py
│   ├── sabor.py
│   └── sorveteria.py
├── services/
│   ├── __init__.py
│   ├── cliente_service.py
│   ├── pedido_service.py
│   ├── sabor_service.py
│   └── sorveteria_service.py 
├── utils/
│   ├── __init__.py
│   └── helpers.py
├── .gitignore
├── main.py
│── README.md
│── requirements.txt
```

## Banco de Dados

O sistema utiliza SQLite, um banco de dados leve e eficiente, adequado para armazenar as informações de sorveterias, sabores, clientes, pedidos e funcionários de forma organizada e segura.

## Conclusão

O Sistema de Gerenciamento Comercial para Sorveterias foi desenvolvido para facilitar a administração de sorveterias, tornando os processos mais simples e organizados. Ele proporciona um gerenciamento completo e eficiente, garantindo um atendimento de qualidade aos clientes.

## Notas

  - O banco de dados _(**sorveteria.db**)_ é criado automaticamente após a primeira execução
  - O sistema possui opção de cancelamento em todas as operações
  - Validações de entrada são implementadas para evitar erros

## Contribuição

Se você deseja contribuir com melhorias para o projeto, siga estas etapas:

1.  Faça um fork do repositório.
2.  Crie uma nova branch para sua modificação.
3.  Envie um pull request com suas alterações.

Sugestões para novas funcionalidades e aprimoramento do código são sempre bem-vindas!

Com esses recursos, o programa proporciona uma base sólida para a otimização e o aprimoramento da eficiência operacional das sorveterias, garantindo uma gestão mais eficaz e estratégica dos recursos disponíveis.
-

>> Desenvolvido por: Gustavo Oliveira

>> GitHub: https://github.com/gustavor0d/poo_project
