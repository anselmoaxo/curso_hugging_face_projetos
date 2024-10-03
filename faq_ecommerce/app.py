from transformers import pipeline
import gradio as gr

model_name = 'pierreguillou/bert-base-cased-squad-v1.1-portuguese'
model_QA = pipeline("question-answering", model=model_name)

contextos = {
    "Como posso criar uma conta em seu site?": "Você pode criar uma conta clicando no botão 'Criar Conta' na página inicial. Insira seu e-mail e crie uma senha para começar a aproveitar nossas ofertas.",
    "Quais métodos de pagamento vocês aceitam?": "Aceitamos cartões de crédito, débito, PayPal e transferências bancárias. Consulte nosso site para ver a lista completa de métodos de pagamento.",
    "Vocês oferecem frete grátis?": "Sim, oferecemos frete grátis para pedidos acima de R$300. Para pedidos abaixo desse valor, uma taxa de envio será aplicada.",
    "Como posso rastrear meu pedido?": "Após o envio do seu pedido, você receberá um e-mail com um link de rastreamento. Utilize esse link para acompanhar a entrega do seu produto.",
    "Qual é a política de devolução?": "Você pode devolver produtos dentro de 30 dias após o recebimento, desde que estejam em sua embalagem original e sem sinais de uso. Alguns produtos podem não ser elegíveis para devolução, como itens em promoção.",
    "O que devo fazer se receber um produto danificado?": "Se o seu produto chegar danificado, entre em contato conosco em até 48 horas após a entrega para iniciar o processo de devolução ou troca.",
    "Vocês oferecem garantia nos produtos?": "Sim, todos os produtos têm garantia de fábrica. O prazo de garantia varia de acordo com o fabricante e pode ser consultado na descrição do produto.",
    "Como posso saber se um produto é compatível com meu dispositivo?": "Verifique a descrição do produto para informações de compatibilidade. Se tiver dúvidas, entre em contato com nosso suporte ao cliente.",
    "Vocês têm assistência técnica para os produtos?": "Oferecemos suporte técnico para produtos adquiridos em nossa loja. Você pode entrar em contato com nossa equipe para obter ajuda.",
    "Como posso aplicar um código de desconto?": "Durante o checkout, haverá um campo para inserir seu código de desconto. Certifique-se de que o código é válido e que atende aos requisitos.",
    "Os produtos têm data de validade?": "Produtos eletrônicos geralmente não têm data de validade, mas recomendamos seguir as instruções de armazenamento e uso do fabricante para garantir a durabilidade.",
    "Como posso alterar ou cancelar meu pedido?": "Você pode alterar ou cancelar seu pedido dentro de 24 horas após a realização. Entre em contato com nosso atendimento ao cliente para assistência.",
    "Vocês enviam para todo o Brasil?": "Sim, enviamos para todo o Brasil. Os prazos de entrega variam conforme a localidade.",
    "O que devo fazer se esquecer minha senha?": "Se você esquecer sua senha, clique em 'Esqueceu a Senha?' na página de login e siga as instruções para redefini-la.",
    "Vocês têm um programa de fidelidade?": "Sim, temos um programa de fidelidade que permite acumular pontos em suas compras, que podem ser trocados por descontos e produtos exclusivos.",
    "Como posso me inscrever na newsletter?": "Você pode se inscrever na nossa newsletter no rodapé do nosso site. Assim, você receberá atualizações sobre novos produtos e promoções.",
    "Qual é a política de sustentabilidade da empresa?": "Estamos comprometidos em práticas sustentáveis, como o uso de embalagens recicláveis e doação de equipamentos eletrônicos para reciclagem.",
    "Posso devolver um produto se não gostei?": "Sim, você pode devolver produtos em até 30 dias, desde que estejam em sua condição original. O frete de devolução será de responsabilidade do cliente.",
    "Quais são as opções de embalagem para presente?": "Oferecemos opções de embalagem para presente durante o checkout. Basta selecionar essa opção e escolher o tipo de embalagem desejada.",
    "Como posso saber mais sobre os produtos?": "Visite as páginas de descrição dos produtos para informações detalhadas sobre especificações, características e análises.",
    "Vocês têm um blog ou recursos de tecnologia?": "Sim, temos um blog onde compartilhamos análises, dicas de uso e novidades sobre produtos tecnológicos. Confira nossas postagens para mais informações!",
    "Como posso entrar em contato com o atendimento ao cliente?": "Você pode entrar em contato conosco através do nosso formulário de contato, e-mail ou chat ao vivo disponível no site.",
    "O que devo fazer se o produto estiver fora de estoque?": "Se um produto estiver fora de estoque, você pode se inscrever para receber uma notificação por e-mail quando ele estiver disponível novamente.",
    "Como funciona a entrega expressa?": "A entrega expressa é uma opção que permite que você receba seu pedido mais rapidamente, geralmente em 1 a 2 dias úteis, dependendo da sua localização.",
    "Posso comprar produtos em quantidade?": "Sim, você pode comprar produtos em quantidade. Entre em contato conosco para informações sobre preços e disponibilidade.",
    "Vocês aceitam cartões-presente?": "Sim, aceitamos cartões-presente em nossa loja online. Você pode usar o código do cartão durante o checkout.",
    "Qual é a política de segurança do site?": "Nosso site utiliza tecnologia de criptografia SSL para garantir que suas informações pessoais e de pagamento estejam seguras.",
    "Como posso deixar uma avaliação de um produto?": "Você pode deixar uma avaliação na página do produto após fazer login na sua conta. A sua opinião é muito importante para nós!",
    "O que são produtos de edição limitada?": "Produtos de edição limitada são itens que estão disponíveis por um tempo restrito ou em quantidades limitadas. Fique atento às nossas novidades!",
    "Quais são as melhores práticas para armazenar produtos eletrônicos?": "Recomendamos armazenar produtos eletrônicos em local fresco e seco, longe da luz solar direta e umidade.",
    "Como funciona o programa de influenciadores?": "Nosso programa de influenciadores permite que você colabore conosco, promovendo nossos produtos e recebendo recompensas. Entre em contato para mais informações.",
    "O que é a garantia de satisfação?": "Oferecemos uma garantia de satisfação, que permite que você experimente nossos produtos e, se não estiver satisfeito, poderá devolvê-los dentro do prazo estipulado.",
}

def respondendo_faq(pergunta):
  contexto = contextos[pergunta]
  resultado = model_QA(question=pergunta, context=contexto)
  return resultado['answer']

app = gr.Interface(fn=respondendo_faq,
                  inputs= gr.Dropdown(choices=list(contextos.keys()),label='Selecione sua Duvida sobre Inteligencia Artificial'),
                  outputs="text",
                   title= 'FAQ E-commerce AxoTecnologia',
                   description="<div style='text-align: center;'><b>Selecione um Pergunta em Nosso FAQ AxoTecnologia .</b><br><br>Desenvolvido por Anselmo Xavier.</div>",
)

if __name__ == '__main__':
    app.launch(share=True)