import gradio as gr
from transformers import pipeline
from PIL import Image

def remove_background(image):
  pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
  pillow_mask = pipe(image, return_mask = True) # outputs a pillow mask
  pillow_image = pipe(image) # applies mask on input and returns a pillow image
  return pillow_image


app = gr.Interface(
    fn=remove_background,
    inputs=gr.components.Image(type='pil'),
    outputs=gr.components.Image(type='pil', format='png'),
    title="Remoção Automática de Fundo de Imagens",
    description="<div style='text-align: center;'><b>Envie uma imagem e o fundo será removido automaticamente. A imagem final será gerada no formato PNG com o fundo transparente.</b><br><br>Desenvolvido por Anselmo Xavier.</div>",
)
if __name__ == "__main__":
    app.launch(share=True)