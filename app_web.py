#trazemos nossas duas bibliotecas novas pro nosso projeto, o stramlit para estruturação de pagweb
import streamlit as st
import csv
#criação de aba da web onde ficara o titulo app
st.set_page_config(page_title="Catálogo", page_icon="🎬")

st.title("🎬: Catálogo de Obras")
st.write("visão do nosso catálogo direto no 'catalogo.csv'!")

#leitura e varetura do arquivo csv ja criado dierto para a tela

try:
    with open('catalogo.csv', mode='r', encoding='utf-8', newline='') as arquivo:
        leitor = list(csv.DictReader(arquivo))
#verificaçao se haver obras cadastradas ou não no nosso arquivo csv
        if leitor:
            st.dataframe(leitor)

        else:
            st.info("===Nenhuma Mídia Cadastrada ainda!===")
except FileNotFoundError:
    st.error("===Arquivo catalogo.csv Não Encotrado!===")