#biblioteca de sorteio aleatorio de dicas 
import random

#siga add dicas para manter o pique na programação
nova_dica = input("Digite uma nova dica para seu forum motivacional!!!")

#criamos o arquivo que será recebido a nova dica pro arquivo txt, aceitando caracteres especiais
with open("dicas.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(nova_dica + "\n")
#O "a" faz com que arescente ao final do arquivo a nova variavel sem apagar oq esta nele posteriormente
    print("===========================")
    print("Dica salva com sucesso no dicas.txt!!!")


#aqui estamos acessando o arquivo na função de leitura dos itens da lista com o "r"
with open("dicas.txt", "r", encoding="utf-8") as arquivo:
    #o readlines garante que cada item pulando linha no arquivo txt se torne um item
    todas_as_dicas = arquivo.readlines()
    #criamos a variavel que receberam uma linha sorteada do arquivo que criamos abrimos e acessamos com leitura 
    dica_sorteada = random.choice(todas_as_dicas)


print("========================================")
print(dica_sorteada.strip())
print("=============================================")