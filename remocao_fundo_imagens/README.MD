# Remoção Automática de Fundo de Imagens

Este projeto usa a biblioteca `gradio` e o modelo de segmentação de imagens `briaai/RMBG-1.4` para remover automaticamente o fundo de imagens. A aplicação gera uma nova imagem no formato PNG com o fundo transparente.

## Como funciona

1. **Envie uma imagem**: O usuário faz upload de uma imagem no formato de sua escolha.
2. **Remoção do fundo**: A aplicação usa um modelo de segmentação de imagem para identificar e remover o fundo.
3. **Resultado final**: A imagem processada é retornada no formato PNG, com o fundo removido.

## Tecnologias Utilizadas

- [Gradio](https://gradio.app/): Para criar a interface gráfica de fácil utilização.
- [Transformers](https://huggingface.co/transformers/): Biblioteca usada para o modelo de segmentação de imagens.
- [Pillow](https://python-pillow.org/): Para manipulação de imagens no Python.
- Modelo de segmentação: `briaai/RMBG-1.4` hospedado no Hugging Face.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
