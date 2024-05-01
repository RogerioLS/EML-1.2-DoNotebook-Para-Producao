
## Integração Contínua (CI) com GitHub Actions

Este repositório contém um fluxo de trabalho do GitHub Actions para Integração Contínua (CI) que automatiza o processo de teste e implantação. O fluxo de trabalho de CI é definido no arquivo .github/workflows/ci.yml.

### Descrição do Fluxo de Trabalho
O fluxo de trabalho CI é acionado pelos seguintes eventos:

* Envio para o ramo main
* Solicitação de pull request para o ramo main
* Tarefa agendada cron às 12:00 a cada 15º dia do mês

O fluxo de trabalho consiste nos seguintes jobs:

1. build-and-run
- Executado em: Ubuntu latest
- Passos:
    1. Verificação do repositório
    2. Instalação do Python e pip
    3. Instalação das dependências do projeto (numpy e requests)
    4. Instalação do Docker Engine
    5. Instalação do Make
    6. Construção da imagem Docker usando o comando make
    7. Execução do contêiner Docker usando o comando make run
    8. Aguardo do contêiner Docker estar pronto enviando requisições HTTP para http://localhost:5000/ (tentativas de até 3 vezes)
    9. Verificação da acessibilidade da porta na porta 5000
    10. Execução dos testes usando o comando make test
    11. Limpeza dos contêineres Docker usando o comando make doccs (sempre executado)
    12. Limpeza das imagens Docker usando o comando make docip (sempre executado)
    13. Execução da imagem Docker usando o comando make doci (sempre executado)

Observações:

Este fluxo de trabalho garante que o código seja testado e implantado automaticamente para cada alteração no ramo main ou em qualquer solicitação de pull request aberta contra ele. Além disso, é executado periodicamente em um cronograma para manter a saúde do projeto.

Os comandos make simplificam a configuração e execução de várias tarefas relacionadas à construção, execução e teste do projeto.
Certifique-se de que o contêiner Docker esteja configurado para expor a porta 5000 e que a aplicação dentro do contêiner esteja ouvindo nesta porta.