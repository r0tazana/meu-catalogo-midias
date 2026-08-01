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

#função que ficar responsavel por imprimir e deixar visivel ao usuario os dados que ele inseriu no sistema de forma organizada

def listar_midas():

    try:
     with open('catalogo.csv', mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        #Variavel que criamos para servir como um  escaner as midias catalogadas no arquivo

        midias = list(leitor)
        #Conversão da variavel leitor a um array

        if not midias:
            print("\n====Nenhuma Mídia Cadastrada ainda!====")

            return

        
        print("\n---CATALOGO DE MÍDIAS---")
        for midia in midias:
            print("------------------------------------------------------------------------------------------")
            print(f"• Título: {midia['titulo']} | Categoria: {midia['tipo']} | Status: {midia['status']}")
            print("------------------------------------------------------------------------------------------")
    except FileNotFoundError:
            print("\n Arquivo de catálogo não encontrado.\n Tente Cadatra uma Mídia Primeiro!!")


#função de busca pra capturar midas catalogadas no banco de dados csv por meio de nome ou categoria
# Função de busca para capturar mídias catalogadas no banco de dados CSV por meio de nome ou categoria
def buscar_midias():
    try:
        with open('catalogo.csv', mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            midias = list(leitor)

            # Verificação de antigos cadastros
            if not midias:
                print("\n=== Nenhuma Mídia Cadastrada Para Usarmos a Opção de Busca! ===")
                return

            print("\n--- Busca de Mídias ---")
            print("1 - Buscar Por Título da Obra")
            print("2 - Buscar Por Categoria")
            opcao = input("Escolha o Critério de Busca: ").strip()

            # Validação de escolha inserida pelo usuário
            if opcao not in ('1', '2'):
                print("\nOpção Inválida! Escolha entre 1 ou 2.")
                return

            # Variável responsável por armazenar a obra a ser buscada no nosso banco de dados
            termo = input("\nPesquisar Mídia: ").strip().lower()

            # "Sacola" onde serão armazenados nossos itens que passem na verificação no loop
            encontrados = []

            # Busca e armazenamento de itens na lista 
            for midia in midias:
                if opcao == '1' and termo in midia['titulo'].lower():
                    encontrados.append(midia)
                elif opcao == '2' and termo in midia['tipo'].lower():
                    encontrados.append(midia)

            # Exibição de resultado
            if encontrados:
                print(f"\n==== {len(encontrados)} Mídia(s) Encontrada(s) ====")
                print("==========================================================================================") 
                for item in encontrados:
                    print(f"* Obra: {item['titulo']} | Categoria: {item['tipo']} | Status: {item['status']}")     
                print("==========================================================================================\n")

            else:
                print("\nNenhuma Mídia encontrada com esse Termo!")

    except FileNotFoundError:
        print("\nArquivo de Catálogo Não Encontrado. Cadastre uma Mídia Primeiro!")

#Função responsavel por sobescrever os dados ja existentes em nosso banco para correção de erros ou promoção de status, utilizando menu simples
def atualizar_midia():
    try:
        with open('catalogo.csv', mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            midias = list(leitor)

            if not midias:
                print("\n ===Nenhuma Mídia Cadastrada Para Utilizarmos a Atualização!===")
                return
            
        print("\n---Atualização de Obras---")
        titulo_busca = input("\n===Informe o Nome da Obra que Deseja Realizar Alterações=== ").strip().lower()
        encotrado = False

        # Percorre a lista para procurar a mídia
        for midia in midias:
            if midia['titulo'].lower() == titulo_busca:
                encotrado = True
                print(f"\n===*Obra {midia['titulo']} | Categoria: {midia['tipo']} | Status Atual: {midia['status']} | Ano: {midia['ano']} | Nota: {midia['nota']} | URL: {midia['url_imagem']}===")

                print('\n---Informe Qual Campo Deseja Atualizar---')
                print("1 - titulo:")
                print("2 - tipo:")
                print("3 - genero:")
                print("4 - ano:")
                print("5 - status:")
                print("6 - nota:")
                print("7 - comentario:")
                print("8 - url_imagem:")

                opcao = input("\n===Campo Desejado=== ").strip()

                if opcao == '1':
                    midia['titulo'] = input("Digite um Novo Titulo: ").strip()
                elif opcao == '2':
                    midia['tipo'] = input("Digite uma Nova Categoria: ").strip()
                elif opcao == '3':
                    midia['genero'] = input("Digite um Novo Genero: ").strip()
                elif opcao == '4':
                    midia['ano'] = input("Digite um Novo Ano: ").strip()
                elif opcao == '5':
                    midia['status'] = input("Digite um Novo Status: ").strip()
                elif opcao == '6':
                    midia['nota'] = input("Digite uma Nova Nota: ").strip()
                elif opcao == '7':
                    midia['comentario'] = input("Digite um Novo Comentario: ").strip()
                elif opcao == '8':
                    midia['url_imagem'] = input("Insira uma Nova Imagem: ").strip()
                else:
                    print("\n Valor inserido Invalido. Por Favor Escolha uma Opiçao dentre as que estão no Menu!")
                    return

                print("\n ===Mídia Atualizada Com Sucesso na Memoria!===")
                break # Para a busca pois já achou e alterou

        # Verificação FORA do loop for
        if not encotrado:
            print(f"\n Nenhuma Mídia com o título '{titulo_busca}' foi encontrada!")
            return

        # Sobrescrevendo o arquivo CSV com os dados novos
        with open('catalogo.csv', mode='w', newline='', encoding='utf-8') as arquivo:
            colunas = ['id', 'titulo', 'tipo', 'genero', 'ano', 'status', 'nota', 'comentario', 'url_imagem']
            escritor = csv.DictWriter(arquivo, fieldnames=colunas)

            escritor.writeheader()
            escritor.writerows(midias)  

    except FileNotFoundError:
        print("\nArquivo de catálogo não encontrado!")
                
#função final com onjetivo de excluir completamente uma mídia do catalogo
def remover_midia():
    try:
        with open('catalogo.csv', mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            midias = list(leitor) 

            if not midias:
                print("\n ===Nenhuma Mídia Cadastrada Para Removermos!=== ")
                return

        print("\n ===REMOÇÃO DE OBRA===")
        opcao_remo = input("\n---Qual Obra Voce Deseja Remover do Catalogo ?--- ").strip().lower()
        encontrado = False

        for midia in midias:
            if midia['titulo'].lower() == opcao_remo:
                encontrado = True

                # Camada de segurança para confirmação (UX)
                confirmacao = input(f"\n===Certeza que deseja remover '{midia['titulo']}' do catálogo? (s/n)=== ").strip().lower()

                if confirmacao == 's':
                    midias.remove(midia)
                    print(f"\n === {midia['titulo']} acaba de ser removido(a) de seu Catálogo!===")
                else:
                    print("\n ===Operação encerrada!===")
                    return
                break # Para o loop após encontrar e processar

        # Verificação FORA do loop
        if not encontrado:
            print(f"\n Obra '{opcao_remo}' Não Foi Encontrada No Catálogo De Mídias.")
            return

        # Sobrescreve os dados no CSV sem a mídia removida
        with open('catalogo.csv', mode='w', newline='', encoding='utf-8') as arquivo:
            colunas = ['id', 'titulo', 'tipo', 'genero', 'ano', 'status', 'nota', 'comentario', 'url_imagem']
            escritor = csv.DictWriter(arquivo, fieldnames=colunas)

            escritor.writeheader()  # Escreve o cabeçalho
            escritor.writerows(midias)

    except FileNotFoundError:
        print("\nArquivo de catálogo não encontrado!")


