# estou importando bibliotecas que vão ser necessarias para a confecção do sistma do catalogo sendo ela  uma biblioteca nativa do prthon para sistemas operacionais e uma para salvar os arquivos que iram estuturas os dados no csv
import os
import csv

ARQUIVO_CSV = "catalogo.csv"

def inicializar_csv():
    # Criação de arquivo csv com suas colunas caso ele não exista
    if not os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            # "struct" de dados necessarios para o catalogo 
            escritor.writerow(['id', 'titulo', 'tipo', 'genero', 'ano', 'status', 'nota', 'comentario', 'url_imagem'])
        print("Arquivo criado com sucesso!!")
    else:
        print("Banco de dados carregado com sucesso.")


#função de capitura de dados do nosso catalogo de obras 

def adicionar_itens():
    print("====CADASTRO DE NOVA OBRA====")

    titulo = input("Infome a Obra: \n")
    tipo = input("Categoria: \n")
    genero = input("Gênero:")

    #Validação simples pra garantir integridade de numero inteiro cedido pelo usuario
    try: 
        ano = int(input("Ano de Lançamento:\n"))
    except ValueError:
        print("Ano invalido! Salvação padrão ativada para 0. \n")
        ano = 0


    status = input("Status: \n")

    # segunda validação para segunda inserção de valor floatante 
    try:
        nota = float(input("Nota: \n"))
    except ValueError:
        print("Nota inserida invalida! Definida com 0.0 . \n")
        nota = 0.0

    comentario = input("Comentario: \n")
    url_imagem = input("Link da imagem (Opcional) \n")
    
    #biblioteca gerenciadora de ids aleatorios para indentificador unico necessario(por hora usaremos o gerenciador aleatorio baseado no tempo ) 

    import time
    item_id = int(time.time()) # Gera um id baseado no segundo atual 

    # Salvação de dados inseridos pelo usuario no nosso arquivo csv com o modolo "a" ( append)
    with open(ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([item_id, titulo, tipo, genero, ano, status, nota, comentario, url_imagem])

    print(f"\n '{titulo}' foi adicionado ao catálogo com sucesso!")

