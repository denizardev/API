# Projeto CRUD de Alunos - Resumo e Progresso

Este documento serve como um resumo detalhado de todo o progresso realizado até o momento no desenvolvimento do projeto CRUD para gerenciamento de dados de alunos de uma escola. Ele inclui todas as etapas concluídas e as pendentes, fornecendo uma visão clara e estruturada do estado atual do projeto.

---

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Etapas Realizadas](#etapas-realizadas)
- [Tarefas Pendentes](#tarefas-pendentes)
- [Tabela de Progresso](#tabela-de-progresso)
- [Próximos Passos](#próximos-passos)

---

## Descrição do Projeto

O projeto consiste no desenvolvimento de uma aplicação CRUD (Create, Read, Update, Delete) para gerenciar informações de alunos de uma escola. A aplicação permite adicionar, visualizar, atualizar e deletar registros de alunos, facilitando o gerenciamento e organização dos dados educacionais.

Além disso, há o planejamento para desenvolver uma aplicação complementar destinada a gerenciar compras e metas pessoais, incorporando funcionalidades de checklist e links interativos para melhor organização e acompanhamento.

---

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Framework**: Flask
- **Banco de Dados**: MySQL
- **ORM**: mysql-connector-python
- **Ambientes de Desenvolvimento**:
  - **CMD (Prompt de Comando)**: Para operações gerais e configuração do ambiente.
  - **Ambiente Virtual (venv)**: Para gerenciamento de dependências e isolamento do ambiente de desenvolvimento.
- **Hospedagem**: Heroku (planejado)
- **Controle de Versão**: Git
- **Outros**:
  - **Gunicorn**: Servidor WSGI para deploy em produção.
  - **JetBrains Font**: Para estilização da interface da aplicação.

---

## Etapas Realizadas

1. ### Desenvolvimento do CRUD de Alunos
   - **Descrição**: Implementação das funcionalidades básicas de criação, leitura, atualização e deleção de registros de alunos.
   - **Detalhes**:
     - Configuração das rotas e views no Flask.
     - Integração com o banco de dados MySQL utilizando `mysql-connector-python`.
     - Criação de templates HTML para interação com o usuário.
   - **Ambiente**: Desenvolvido no **venv** para garantir o isolamento das dependências.

2. ### Geração do `requirements.txt`
   - **Descrição**: Criação do arquivo contendo todas as dependências do projeto.
   - **Comando Utilizado**:
     ```bash
     pip freeze > requirements.txt
     ```
   - **Ambiente**: Executado dentro do **venv**.

3. ### Acesso ao MySQL via CMD
   - **Descrição**: Configuração e teste de acesso ao banco de dados MySQL através do prompt de comando padrão.
   - **Comando Utilizado**:
     ```bash
     mysql -u your_username -p
     ```
   - **Ambiente**: Executado no **CMD normal**.

4. ### Configuração do Heroku CLI no CMD
   - **Descrição**: Instalação e configuração da interface de linha de comando do Heroku para gerenciamento de deploys e aplicações.
   - **Comandos Utilizados**:
     ```bash
     heroku login
     heroku create your-app-name
     ```
   - **Ambiente**: Executado no **CMD normal**.

5. ### Criação da Tabela de Progresso
   - **Descrição**: Elaboração de uma tabela para monitorar as tarefas concluídas e pendentes no projeto.
   - **Ferramenta**: Markdown (incluída neste documento).

---

## Tarefas Pendentes

1. ### Acesso ao MySQL no Ambiente Virtual (venv)
   - **Descrição**: Resolver problemas de acesso ao MySQL quando operando dentro do ambiente virtual.
   - **Possíveis Soluções**:
     - Verificar e configurar variáveis de ambiente corretamente dentro do venv.
     - Instalar quaisquer dependências ou drivers adicionais necessários no venv.

2. ### Configuração do Heroku CLI no venv
   - **Descrição**: Garantir que o Heroku CLI funcione corretamente dentro do ambiente virtual para facilitar o processo de deploy.
   - **Possíveis Soluções**:
     - Instalar o Heroku CLI dentro do venv ou ajustar o PATH para reconhecê-lo.

3. ### Melhoria da Página Inicial (Home)
   - **Descrição**: Refinar o design e a usabilidade da página inicial da aplicação.
   - **Requisitos**:
     - Centralização dos elementos na página.
     - Utilização da fonte **JetBrains** para melhor estética.
     - Implementação de um layout responsivo e intuitivo.

4. ### Deploy da Aplicação
   - **Descrição**: Implantar a aplicação em um serviço de hospedagem gratuito como o Heroku.
   - **Passos Necessários**:
     - Configurar o `Procfile` corretamente com Gunicorn.
     - Garantir que todas as configurações de ambiente estejam adequadas para produção.
     - Testar a aplicação após o deploy para assegurar funcionalidade completa.

5. ### Desenvolvimento da Aplicação de Compras/Metas
   - **Descrição**: Iniciar o desenvolvimento de uma nova aplicação para gerenciamento de compras e metas pessoais com funcionalidades de checklist.
   - **Requisitos**:
     - Interface simples e amigável.
     - Possibilidade de adicionar links clicáveis nos itens da lista.
     - Persistência de dados para manter o histórico de compras e metas.

---

## Tabela de Progresso

| **Tarefa**                                                                                             | **Status**    | **Observações**                                                                                                    |
|--------------------------------------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------|
| **Desenvolver um CRUD para armazenar dados dos alunos de uma escola**                                  | ✔️ **Concluído** | CRUD desenvolvido e testado com `mysql-connector-python` para conexão ao MySQL.                                   |
| **Gerar o arquivo `requirements.txt`**                                                                 | ✔️ **Concluído** | Arquivo gerado com todas as dependências necessárias.                                                              |
| **Acessar MySQL pelo CMD normal**                                                                      | ✔️ **Concluído** | Conseguiu acessar o MySQL pelo CMD normal.                                                                         |
| **Configurar Heroku CLI no CMD normal**                                                                | ✔️ **Concluído** | Heroku CLI configurado e funcional no CMD normal.                                                                  |
| **Criar tabela para visualizar o que foi feito e o que falta fazer no projeto CRUD**                   | ✔️ **Concluído** | Tabela criada para organizar as tarefas.                                                                           |
| **Acessar MySQL no ambiente virtual (venv)**                                                           | ❌ **Pendente** | Necessita resolver possíveis configurações incorretas do PATH ou dependências faltantes no venv.                   |
| **Configurar Heroku CLI no terminal do ambiente virtual (venv)**                                       | ❌ **Pendente** | Ajustar configurações para utilizar o Heroku CLI dentro do venv.                                                   |
| **Melhorar a página inicial (home) do projeto**                                                        | ❌ **Pendente** | Página inicial precisa ser mais bonita e centralizada, utilizando a fonte JetBrains e design responsivo.           |
| **Realizar o deploy da aplicação em um serviço de hospedagem gratuita (Heroku, Vercel, etc.)**         | ❌ **Pendente** | Preparar e executar o deploy da aplicação garantindo todas as configurações necessárias.                           |
| **Desenvolver aplicação para guardar compras/metas com checklist**                                     | ❌ **Pendente** | Iniciar o desenvolvimento da nova aplicação com funcionalidades especificadas.                                     |
| **Implementar opção de adicionar links nos nomes dos itens da lista na aplicação de compras/metas**    | ❌ **Pendente** | Incluir a funcionalidade de links clicáveis nos itens da lista para melhor usabilidade.                            |

---

## Próximos Passos

1. **Resolver Acesso ao MySQL no venv**
   - Revisar configurações de ambiente e dependências necessárias.
   - Testar conexão e realizar operações básicas dentro do venv.

2. **Configurar Heroku CLI no venv**
   - Instalar ou ajustar PATH para que o Heroku CLI seja reconhecido dentro do ambiente virtual.
   - Testar comandos básicos do Heroku para garantir funcionalidade.

3. **Melhorar Interface do Projeto CRUD**
   - Implementar melhorias de design na página inicial e demais páginas.
   - Assegurar responsividade e compatibilidade com diferentes dispositivos e navegadores.

4. **Executar Deploy no Heroku**
   - Configurar arquivos necessários (`Procfile`, variáveis de ambiente, etc.).
   - Realizar o deploy e executar testes completos para garantir o correto funcionamento em produção.

5. **Iniciar Desenvolvimento da Aplicação de Compras/Metas**
   - Planejar estrutura e funcionalidades principais da aplicação.
   - Configurar ambiente de desenvolvimento e iniciar implementação das features básicas.

---

## Contribuições

Sinta-se à vontade para contribuir com este projeto através de *pull requests* ou abrindo *issues* para relatar bugs e sugerir melhorias.

---

## Contato

Para quaisquer dúvidas ou sugestões, entre em contato:

- **Nome**: Denizard Oliveira
- **Email**: [denizard.oliveira@gmail.com](mailto:denizard.oliveira@gmail.com)

---

**Nota**: Este documento será atualizado regularmente à medida que novas tarefas forem concluídas ou surgirem novas necessidades.
