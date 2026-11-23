# 👕 Sistema de Estoque e Carrinho em Python

Projeto de estudo desenvolvido em Python: um sistema no terminal para gerenciar estoque e carrinho de compras de uma loja de roupas, com categorias, validação de quantidades e cálculo de valores.

## 📋 Funcionalidades

- Permite navegar entre categorias (camisetas e calças) exibindo preço e quantidade disponível
- Valida a quantidade desejada considerando o que já está no carrinho
- Acumula quantidades e valores ao adicionar a mesma peça mais de uma vez
- Desconta do estoque apenas na finalização da compra
- Permite visualizar o carrinho, limpar ou voltar ao menu
- Normaliza entradas com "ç" na digitação e exibe os nomes formatados na tela

## 🧠 Conceitos praticados

- Dicionários aninhados (`estoque` e `carrinho`)
- Modularização em funções (`validar_quantidade`, `calcular`, `adicionar_carrinho`, `mostrar_carrinho`, `finalizar_compra` e `formatar_exibicao`)
- Estruturas condicionais: `if`, `elif`, `else`
- Laços de repetição `while` e `for` com controle de fluxo (`break`, `continue`)
- Tratamento de erros com `try` e `except ValueError`
- Manipulação de texto com `.strip()`, `.lower()`, `.replace()` e formatação com `f-strings` (`:.2f`)

## ▶️ Como executar

1. Instale o Python 3
2. Baixe o arquivo `sistema_estoque.py`
3. No terminal, execute:

```bash
python sistema_estoque.py
