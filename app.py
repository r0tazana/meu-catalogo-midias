from funcoes import inicializar_csv, adicionar_itens, listar_midas

if __name__ == "__main__":
    print("=== INICIANDO SISTEMA DE CATÁLOGO ===")
    inicializar_csv()

    #Chamada da função que criamos de captura de dados 
    adicionar_itens()

    #Chamada da função de impressão
    listar_midas()