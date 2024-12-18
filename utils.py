import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Função para gerar PDF com rótulos
def gerar_pdf(pedido, quantidade, numero_item, itens_disponiveis):
    if numero_item not in itens_disponiveis:
        raise ValueError("Número de item inválido.")

    nome_item = itens_disponiveis[numero_item]["nome"]
    quantidade_padrao = itens_disponiveis[numero_item]["quantidade"]

    pdf_filename = f"pedido_{pedido}_item_{numero_item}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    c.setFont("Helvetica", 9)
    x_position = 50
    y_position = 750
    colunas = 3
    contador_colunas = 0

    for i in range(quantidade):
        if y_position < 100:
            c.showPage()
            y_position = 750
            x_position = 50
            contador_colunas = 0
            c.setFont("Helvetica", 9)

        c.drawString(x_position, y_position, "GRAFICA - EXEMPLO")
        c.drawString(x_position, y_position - 12, "CLIENTE - EXEMPLO")
        c.drawString(x_position, y_position - 24, f"PEDIDO - {pedido}")
        c.drawString(x_position, y_position - 36, f"ITEM - {numero_item}")
        text_object = c.beginText(x_position, y_position - 48)
        text_object.setFont("Helvetica", 9)
        text_object.textLines(nome_item)
        c.drawText(text_object)
        c.drawString(x_position, y_position - 60 - 12 * nome_item.count("\n"), f"QTD. - {quantidade_padrao}")

        x_position += 180
        contador_colunas += 1

        if contador_colunas == colunas:
            x_position = 50
            y_position -= 100
            contador_colunas = 0

    c.save()
    return pdf_filename

# Função para exibir itens disponíveis
def exibir_itens(itens_disponiveis):
    print("Itens disponíveis:")
    for numero, dados in itens_disponiveis.items():
        print(f"{numero} - {dados['nome']} ({dados['quantidade']})")

# Função para limpar o terminal de forma cross-platform
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")