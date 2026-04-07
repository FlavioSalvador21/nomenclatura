import streamlit as st
import re

def limpar_nome(nome_original):
    # 1. Remove a extensão (ex: .mp4)
    nome = re.sub(r'\.[^.]+$', '', nome_original)
    
    # 2. Remove os blocos específicos ignorando maiúsculas/minúsculas
    # O padrão r'_(NA|VID|POLI)_' remove o termo entre underscores
    termos_para_deletar = [r'_NA_', r'_VID_', r'_POLI_', r'_V\d+_', r'\s-\s']
    
    for padrao in termos_para_deletar:
        nome = re.sub(padrao, '_', nome, flags=re.IGNORECASE)
    
    # 3. Substitui todos os underscores por espaços
    nome = nome.replace('_', ' ')
    
    # 4. Limpeza final de espaços duplos
    nome = re.sub(r'\s+', ' ', nome).strip()
    
    return nome

# --- Interface Streamlit ---
st.title("✂️ Formatador Pro")

entrada = st.text_input("Cole o nome do arquivo:", value="W2Y26_FTO_NA_SLOWENGLISHAITUTOR_V5_VID_POLI_BR_V - apa sem hook.mp4")

if entrada:
    resultado = limpar_nome(entrada)
    st.subheader("Nome Limpo:")
    st.code(resultado, language=None)
