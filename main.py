from utils import gerar_pdf, exibir_itens, limpar_tela
from config import itens_disponiveis

def main():
    pedido = None
    while True:
        if not pedido:
            try:
                pedido = input("Digite o número do pedido: ")
                if not pedido.isdigit():
                    raise ValueError("O número do pedido deve ser um número.")
            except ValueError as e:
                print(e)
                continue

        try:
            quantidade = int(input("Digite a quantidade de rótulos: "))
        except ValueError:
            print("A quantidade deve ser um número inteiro.")
            continue

        exibir_itens(itens_disponiveis)
        while True:
            numero_item = input("Digite o número do item desejado: ")
            if numero_item in itens_disponiveis:
                break
            else:
                print("Número de item inválido. Tente novamente.")

        try:
            pdf_filename = gerar_pdf(pedido, quantidade, numero_item, itens_disponiveis)
            print(f"PDF gerado com sucesso: {pdf_filename}")
        except Exception as e:
            print(f"Erro ao gerar PDF: {e}")

        print("\nEscolha uma opção:")
        print("1 - Gerar novamente usando o mesmo número de pedido")
        print("2 - Reiniciar")
        print("3 - Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            continue
        elif opcao == "2":
            limpar_tela()
            pedido = None
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Reiniciando o processo.")
            limpar_tela()
            pedido = None

if __name__ == "__main__":
    main()