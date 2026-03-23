# Exercício 1 — Claude-Autofix-Action

## Introdução

Este exercício tem o objetivo de testar o projeto Claude Autofix Action, disponível em [https://github.com/enriconunes/claude-autofix-action](https://github.com/enriconunes/claude-autofix-action). É importante manter a estrutura de ficheiros original e descrita no README do projeto; assim como proceder às configurações necessárias dentro repositório que forem utilizar. São as seguintes:

---

- **Criar um repositório publico** (com este código)

- **Configurar algumas definições:**  
  `Settings → Actions → General → Workflow permissions`
  - Selecionar **"Read and write permissions"**
  - Marcar **"Allow GitHub Actions to create and approve pull requests"**
  - Clicar **Save**

- **Adicionar chave de API Anthropic:**  
  `Settings → Secrets and variables → Actions → New repository secret`

  | Name | Value |
  |------|-------|
  | `ANTHROPIC_API_KEY` | A tua chave de console.anthropic.com |

---

## Exercício 1 — Testar a ferramenta

O primeiro exercício serve para testar o funcionamento da ferramenta com um exemplo simples. Um função divisão no ficheiro `dividir.py` e alguns testes em `test_dividir.py`. Este exemplo tem um teste que falhará propositadamente, uma vez que a função de divisão não está a tratar possíveis divisões por 0.
O objetivo é verificar o funcionamento da ferramenta: ao fazer um Pull Request, o teste falhará e o agente claude entrará em ação, fazendo um comentário e propondo uma correção do código numa nova branch.
