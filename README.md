# Gerador de PDFs para Rótulos

Este projeto é uma aplicação em Python para gerar PDFs com rótulos personalizados, organizada de forma modular e eficiente. Os nomes utilizados nos exemplos foram alterados para preservar a privacidade das empresas.

## Estrutura do Projeto

O projeto é dividido em três arquivos principais:

### 1. `main.py`
Este arquivo contém o fluxo principal da aplicação. Ele:
- Solicita informações do usuário (número do pedido, quantidade de rótulos, etc.).
- Exibe os itens disponíveis para seleção.
- Chama as funções para geração do PDF.

### 2. `utils.py`
Este arquivo contém funções utilitárias importantes, como:
- `gerar_pdf(pedido, quantidade, numero_item, itens_disponiveis)` - Gera o PDF de rótulos com base nas informações fornecidas.
- `exibir_itens(itens_disponiveis)` - Exibe a lista de itens disponíveis para o usuário.
- `limpar_tela()` - Limpa o terminal, funcionando tanto em sistemas Windows quanto Linux/MacOS.

### 3. `config.py`
Este arquivo centraliza as configurações e dados estáticos do projeto, incluindo:
- O dicionário `itens_disponiveis`, que armazena os itens disponíveis com seus respectivos nomes e quantidades padrão.

## Requisitos

### Dependências do Projeto
Certifique-se de instalar as dependências necessárias. Elas estão listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Lista de Dependências
- `reportlab` - Biblioteca para criação de arquivos PDF.

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/loesnardo/GerarPdfRotulos.git
   cd GerarPdfRotulos
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o programa principal:
   ```bash
   python main.py
   ```

4. Siga as instruções exibidas no terminal para:
   - Inserir o número do pedido.
   - Selecionar a quantidade de rótulos.
   - Escolher um item da lista disponível.
   - Gerar o PDF correspondente.

---

### Estrutura de Arquivos

```
/
├── config.py          # Configurações e itens disponíveis
├── main.py            # Fluxo principal da aplicação
├── utils.py           # Funções utilitárias
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto
```
