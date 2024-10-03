# FAQ E-commerce AxoTecnologia

Este projeto utiliza a biblioteca `gradio` e o modelo de `question-answering` (`bert-base-cased-squad-v1.1-portuguese`) da Hugging Face para responder automaticamente às perguntas frequentes (FAQ) relacionadas a uma loja de e-commerce.

## Como Funciona

1. **Selecione uma pergunta**: O usuário escolhe uma das perguntas frequentes listadas no dropdown.
2. **Resposta automatizada**: O modelo de linguagem responde à pergunta com base no contexto fornecido.
3. **Tecnologia usada**: O modelo `pierreguillou/bert-base-cased-squad-v1.1-portuguese` é usado para responder em português de forma precisa.

## Tecnologias Utilizadas

- [Gradio](https://gradio.app/): Para a criação da interface gráfica interativa.
- [Transformers](https://huggingface.co/transformers/): Biblioteca utilizada para carregar o modelo de `question-answering`.
- Modelo de linguagem: `pierreguillou/bert-base-cased-squad-v1.1-portuguese`.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
