
# SISTEMA DE GESTÃO COMERCIAL PARA SORVETERIAS

Desenvolvemos um sistema completo para facilitar a administração de sorveterias, que abrange desde o cadastro de sorveterias, sabores e clientes até a realização e gestão de pedidos.

Este projeto é uma aplicação de linha de comando para gerenciamento comercial de redes de sorveterias tendo um sistema completo e totalmente intuitivo. Ele abrange desde o cadastramento de sorverias, sabores e clientes até a realização e gestão de pedidos.
Utilizando Python e SQLAlchemy para manipulação de banco de dados para oferecer funcionalidades avançadas.

## Sumário
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Funcionalidades](#funcionalidades)
- [Descrição das Funcionalidades](#descrição-das-funcionalidades)
- [Uso](#uso)
- [Estrutura do Sistema](#estrutura-do-sistema)
- [Banco de dados](#banco-de-dados)
- [Conclusão](#conclusão)
- [Contribuição](#contribuição)

## Requisitos

- Python 3.11 ou superior
- Bibliotecas Python:
  - SQLAlchemy
  - os (nativa do Python)
  - sys (nativa do Python)

## Instalação

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/gustavor0d/poo_project.git
   cd poo_project
   ```
   
2. Criação de um Ambiente Virtual (venv)
   ```bash
   python -m venv venv
   ```
   
3. Ativação do Ambiente Virtual
  - Windows
    ```bash
    .\venv\Scripts\activate
    ```
  - Linux ou MacOS
    ```bash
    source ./venv/bin/activate
    ```
    
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute o arquivo principal para iniciar a aplicação:
   ```bash
   python.exe main.py
   ```

## Funcionalidades

Com uma interface intuitiva, nosso sistema permite:
-	**Cadastro de Sorveterias**: Adicionar e gerenciar informações de diferentes sorveterias.
-	**Cadastro de Sabores**: Registrar e associar novos sabores de sorvete a sorveterias específicas.
-	**Cadastro de Clientes**: Criar registros detalhados de clientes para um melhor atendimento.
-	**Realização de Pedidos**: Permitir que clientes escolham sabores e façam pedidos, com cálculo automático do total.
-	**Listagem de Informações**: Visualizar todos os pedidos, sorveterias e clientes cadastrados de maneira organizada.

## Descrição das Funcionalidades

1. **Cadastro de Sorveterias**
-	Processo: O usuário insere o nome, endereço e telefone da nova sorveteria. O sistema salva essas informações no banco de dados.
-	Benefício: Permite gerenciar múltiplas sorveterias de forma eficiente.

3. **Cadastro de Sabores**
-	Processo: O usuário insere o nome, descrição e preço de um novo sabor. Além disso, escolhe a sorveteria a que este sabor pertence.
-	Benefício: Facilita a adição de novos sabores e sua associação com sorveterias específicas.

5. **Cadastro de Clientes**
-	Processo: O usuário insere o nome, idade e telefone de um novo cliente.
-	Benefício: Cria um registro detalhado dos clientes para melhor gerenciamento e atendimento.

7. **Realização de Pedidos**
-	Processo: O usuário seleciona um cliente, escolhe os sabores e registra o pedido. O sistema calcula automaticamente o total do pedido.
-	Benefício: Simplifica o processo de venda e garante precisão no cálculo dos valores.

9. **Listagem de Pedidos**
-	Processo: O sistema exibe uma lista de todos os pedidos, mostrando o cliente, os sabores e o total.
-	Benefício: Facilita a visualização e o controle dos pedidos realizados.

11. **Listagem de Sorveterias e Clientes**
-	Processo: O sistema exibe listas detalhadas de todas as sorveterias e clientes cadastrados.
-	Benefício: Proporciona uma visão geral e rápida consulta das informações cadastradas.

## Uso

### Menu Principal
Quando o programa é executado, o menu principal é exibido com opções numéricas para cada funcionalidade:

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

O usuário deve inserir o número correspondente à funcionalidade desejada. Se uma entrada inválida for fornecida, uma mensagem de erro personalizada será exibida.

## Estrutura do Sistema

1. Sorveteria
  - Função: Gerencia as informações das sorveterias cadastradas.
  - Dados Armazenados: Nome, endereço e telefone.
  - Exemplo de Uso: Adicionar uma nova sorveteria ao sistema.

3. Sabor
  - Função: Registra os diferentes sabores de sorvete disponíveis.
  - Dados Armazenados: Nome, descrição, preço e a sorveteria a que pertence.
  - Exemplo de Uso: Adicionar um novo sabor como 'Chocolate Belga' com sua descrição e preço.

4. Cliente
  - Função: Mantém os registros dos clientes que realizam pedidos.
  - Dados Armazenados: Nome, idade e telefone.
  - Exemplo de Uso: Cadastrar um novo cliente no sistema.

5. Pedido
  - Função: Gerencia os pedidos feitos pelos clientes.
  - Dados Armazenados: Cliente que fez o pedido, sabores escolhidos e valor total.
  - Exemplo de Uso: Registrar um pedido feito por um cliente com vários sabores selecionados e calcular o total.

6. Funcionário
  - Função: Mantém os registros dos funcionários da sorveteria.
  - Dados Armazenados: Nome e cargo.
  - Exemplo de Uso: Adicionar um novo funcionário ao sistema.

## Banco de Dados
O sistema utiliza o banco de dados SQLite, que é leve e eficiente, adequado para armazenar todas as informações de sorveterias, sabores, clientes, pedidos e funcionários de forma organizada e segura.

## Conclusão
Este sistema de gestão foi criado para tornar a administração de sorveterias mais simples, eficiente e organizada. Com ele, é possível gerenciar todas as operações de forma integrada, garantindo um atendimento de qualidade aos clientes.

## Contribuição

Se deseja contribuir com melhorias para o projeto, por favor, faça um fork do repositório, crie uma nova branch para a sua modificação, e envie um pull request. Sugestões para novas funcionalidades ou aprimoramento da estrutura de código são sempre bem-vindas!
---
