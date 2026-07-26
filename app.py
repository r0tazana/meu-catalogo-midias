from funcoes import inicializar_csv, adicionar_itens, listar_midas, buscar_midias

if __name__ == "__main__":
   
    inicializar_csv()


    print("=====================================")
    print("    INICIANDO SISTEMA DE CATÁLOGO    ")
    print("=====================================")

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Cadastrar Nova Mídia")
    print("2 - Listar Todas as Mídias")
    print("3 - Buscar Mídia no Catalogo")
    print("4 - Sair Do Sistema")

    opcao = input("\nEscolha Uma Opição: ").strip()

    if opcao == '1':
#Chamada da função que criamos de captura de dados 
        adicionar_itens()
    elif opcao == '2':
#Chamada da função de impressão
        listar_midas()
    elif opcao == '3':
#Busca dados por meio de Titulo e Tipo
        buscar_midias()
    elif opcao == '4':
        print("\n * Saindo do Sistema...! Até Logo!")
        break # encerra o loop

    else:
        print("\nOpção Invalida! Digite um Numero de 1 a 4.")