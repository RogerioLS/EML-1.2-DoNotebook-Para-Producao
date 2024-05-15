<div align = center>

# Predição de churn

![CI](https://github.com/RogerioLS/EML-1.2-DoNotebook-Para-Producao/actions/workflows/ci_cd.yml/badge.svg)

[Docs CI/CD](sources/docs/CI_CD.md)

</div>

---

Para desenvolver essa tarefa vamos reutilizar o notebook de predição de churn, de uma entrega que foi feita entre o periodo de Data de Abertura: **26/08/2023**  Data de Entrega: **03/09/2023**

A ideia de exercício era conciderar as seguintes 

**Orientações:**

- Os alunos receberão uma base de dados com informações de abandono de clientes em uma empresa provedora de internet. A base contém informações de interações dos clientes com a empresa e se houve ou não abandono. Ao final, o modelo escolhido deve ser utilizado para prever se o cliente abandonará ou não a empresa de acordo com suas características;

- Os alunos têm total liberdade para escolher quais modelos consideram mais coerentes para a resolução do problema, bem como a criação de novas covariáveis de acordo com as informações disponíveis e a avaliação dos modelos;

- É importante deixar claro quais covariáveis estão sendo utilizadas, se houve criação de novas covariáveis e qual foi o processo adotado, além de clareza de quais foram os modelos escolhidos para serem testados e qual foi o critério de comparação de modelos;

> [!WARNING]
> Todos passos acima você encontrar no própio notebook!!

---

Seguindo para nossa entrega vamos transforma esse notebook em um produto final, que seguirar o seguinte pipeline.

> [!IMPORTANT]  
> Antes de seguirmos é super importante que você tenha instalado na sua máquina.
>
> - Docker
> - Anaconda
> - Ubunto
>
> Caso esteja utilizando uma máquina Windows uma opção bem valida é instalar o WSL2.

- Construir uma imagen com Docker;
- Rodar nossa aplicação com flask;
- Testar aplicação;
- Encerrando nossa aplicação;

---
### Construindo imagen com Docker
Para construção da nossa imagem com Docker vamos utilizar uma especie de arquivo que funciona como orquestrado chamado **Makefile**, no seu terminal de o comando:

```bash
make
```

Ele vai garantir que sua imagem seja construida com o comando:

```
docker build
```

Após isso você terá a seguinte visão no seu terminal.

<img align="center" src="https://github.com/RogerioLS/EML-1.2-DoNotebook-Para-Producao/blob/main/sources/images/image_build.png">

### Rodar nossa aplicação com flask
Para rodar nossa aplicação vamos utilizar o seguinte comando:
```bash
make run doci
```
**run** garante que podemos rodar nosso aplicativo, e o **doci** lista as imagens e container para nós, por de baixo dos panos estamos rodando esse comando aqui do docker:
```bash
docker run -d -p 5000:5000 --rm --name modelo-churn-container modelo:churn
docker images
docker ps
```
Após isso você terá a seguinte visão no seu terminal.

<img align="center" src="https://github.com/RogerioLS/EML-1.2-DoNotebook-Para-Producao/blob/main/sources/images/image_run.png">

Prontinho, se todos os passos acima deram certo agora podemos testar nossa apricação.

### Testando aplicação
Para testar nossa aplicação vamos utilizar o comando:
```bash
make test
```
Esse comando garante que estamos passando nossos dados para o nosso modelo e gerando uma saida do tipo **1** para churn e **0** para não churn, no teste foi passado dez requisiços para nossa aplicação.

### Encerrando nossa aplicação
É super importante após realizar todos os teste encerrarmos nosso container e images, para isso vamos utilizar os seguintes comandos:
```bash
make doccs
make docip
make doci
```
O **doccs** garante que vamos dar um stop no nosso contaneir, **docip** remover todas as imagens que não estão em uso de uma vez, e o, **doci** é para vermos se não temos de fato mais nenhuma imagem e container.

<img align="center" src="https://github.com/RogerioLS/EML-1.2-DoNotebook-Para-Producao/blob/main/sources/images/image_encerrar.png">
