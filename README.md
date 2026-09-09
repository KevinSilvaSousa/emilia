# Emilia

## Visão

A Emilia é uma IA versátil, projetada para atuar como assistente pessoal e profissional, capaz de pesquisar informações, auxiliar em decisões empresariais, ensinar conteúdos e aprender com a interação do usuário.

## Objetivo

O objetivo da Emilia é auxiliar o usuário em decisões difíceis, fornecer conhecimento de forma eficiente e adaptar suas respostas de acordo com o contexto e as necessidades do usuário.

A Emilia deverá evoluir continuamente por meio de uma arquitetura que permita adicionar novas capacidades sem comprometer a organização e a manutenção do projeto.

## Funcionalidades planejadas

* Conversação com o usuário
* Pesquisa de informações
* Memória e histórico de conversas
* Auxílio em decisões empresariais
* Ensino e explicação de conteúdos
* Interação por texto
* Interação por voz
* Recuperação de informações através de RAG
* Integração com bancos de dados
* Utilização de diferentes modelos de IA
* Possibilidade de expansão para novas funcionalidades

## Arquitetura

A arquitetura da Emilia será desenvolvida de forma modular, separando responsabilidades e permitindo que cada componente do sistema evolua de maneira independente.

Tecnologias inicialmente planejadas:

* Python
* FastAPI
* PostgreSQL
* pgvector
* LLMs
* RAG
* HTML
* CSS
* JavaScript
* TypeScript
* Docker
* Git/GitHub
* Testes automatizados
* CI/CD

## Evolução do projeto

Este README deve ser atualizado sempre que houver uma mudança relevante no projeto, incluindo:

* Novas funcionalidades
* Mudanças de arquitetura
* Novas tecnologias
* Decisões importantes
* Alterações de escopo
* Componentes adicionados ou removidos

O README será utilizado como documentação viva da Emilia.


                  ┌──────────────┐
                  │    Usuário   │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │     API      │
                  └──────┬───────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Receber pergunta│
                └────────┬────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       ┌─────────────┐       ┌─────────────┐
       │   Memória   │       │     RAG     │
       │   / Banco   │       │  se preciso │
       └──────┬──────┘       └──────┬──────┘
              │                     │
              └──────────┬──────────┘
                         ▼
                  ┌──────────────┐
                  │     LLM      │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │    Resposta  │
                  └──────┬───────┘
                         │
                         ▼
                       Usuário




## Arquitetura inicial

### Fluxo

USUÁRIO
   ↓
FastAPI
   ↓
Orquestrador
   ↓
Classificador
   ↓
Decisão de rota
   ↓
┌───────────┬───────────┬──────────────────┐
│           │           │                  │
Memória     RAG      Pesquisa externa      │
│           │           │                  │
└───────────┴───────────┴──────────────────┘
                    ↓
                  LLM
                    ↓
                Resposta
                    ↓
                 Usuário


### Componentes
 
API: Vai ser responsável por receber as solicitações externas e encaminhá-las para o sistema.

Orquestrador: Vai decidir, a partir do resultado do classificador, quais componentes precisam ser acionados e em que ordem.

Classificador: Vai analisar a solicitação do usuário e identificar o tipo de informação ou recurso necessário.

LLM: Vai ser responsável por processar a pergunta juntamente com os contextos fornecidos e gerar a resposta em linguagem natural.


Memória: Vai ficar responsavel por usar as memorias antigas para responder as perguntas ou salvar

RAG: Vai ser responsável por recuperar informações relevantes de uma base de conhecimento previamente disponibilizada para a Emilia.


Pesquisa externa: Vai ser responsável por buscar informações em fontes externas quando a informação necessária não estiver disponível internamente ou precisar de dados atualizados.

Banco de dados: Ele vai ajudar na persistencia de dados
API: Ele serve pra

Regra 1:

Se a solicitação exigir conhecimento específico armazenado
na base de conhecimento da Emilia, utilizar RAG antes do LLM.

Caso contrário, utilizar o fluxo padrão do LLM.