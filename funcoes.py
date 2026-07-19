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