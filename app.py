import streamlit as st
import re

# Configuração da página para ser ampla e moderna
st.set_page_config(page_title="Analisador de Nomenclatura", layout="centered")

# Customização de CSS para cores e tamanhos
st.markdown(
    """
    <style>
    .erro { color: #d32f2f; font-weight: bold; background-color: #ffebee; padding: 5px; border-radius: 5px; }
    .reflexao { color: #004085; background-color: #e7f1ff; padding: 20px; border-radius: 10px; font-size: 24px; font-weight: bold; text-align: center; border: 2px solid #b8daff; }
    .stTable { font-size: 20px !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🔍 Analisador de Nomenclatura v9.0")

# Entrada de texto
entrada = st.text_input(
    "Cole aqui a nomenclatura completa:",
    placeholder="Ex: [S01]_[ALX]_[PFR]_[OFFER]_[V1]_[ADS]_[IDM]_[PT]_[H] - Nome do Video",
)

if entrada:
    mapas = {
        "COPY": {
            "CDS": "Cardoso",
            "ORN": "Ornelas",
            "FTO": "Foiato",
            "LET": "Letícia",
            "LEO": "Leonardo",
            "PFR": "Paiffer",
            "ALX": "Lucas Alexandre",
            "GIU": "Giulio",
            "PRI": "Priscila",
            "MLO": "Marcelo",
            "JAO": "João",
            "NA": "Não Aplicável",
        },
        "EDITOR": {
            "PFR": "Paiffer",
            "ALX": "Lucas Alexandre",
            "GIU": "Giulio",
            "PRI": "Priscila",
            "MLO": "Marcelo",
            "JAO": "João",
            "NA": "Não Aplicável",
        },
    }

    rotulos = [
        "SEMANA",
        "COPY",
        "VIDEO",
        "CONCEITO",
        "VERSÃO",
        "TIPO",
        "PRODUTO",
        "LANG",
        "FORMATO",
    ]

    partes = entrada.split(" - ", 1)
    tags_brutas = partes[0].replace("[", "").replace("]", "").split("_")
    descricao_valor = partes[1].strip() if len(partes) > 1 and partes[1].strip() else ""

    dados_finais = []

    # Processamento dos campos
    for i, rotulo in enumerate(rotulos):
        valor = tags_brutas[i].strip() if i < len(tags_brutas) else ""
        nome_exibicao = "EDITOR" if rotulo == "VIDEO" else rotulo

        # Traduções
        if rotulo == "COPY":
            valor = mapas["COPY"].get(valor.upper(), valor)
        elif rotulo == "VIDEO":
            valor = mapas["EDITOR"].get(valor.upper(), valor)

        # Validações
        if rotulo == "VERSÃO" and not re.match(r"^V\d+$", valor):
            valor = f"❌ ERRO: {valor} (Padrão Vx)"
        elif rotulo == "FORMATO" and valor.upper() not in ["H", "V"]:
            valor = f"❌ ERRO: {valor} (Use H ou V)"

        if not valor:
            valor = "⚠️ Não informado"
        dados_finais.append({"CAMPO": nome_exibicao, "CONTEÚDO": valor.upper()})

    # Adiciona Descrição
    desc_exibicao = (
        descricao_valor.upper() if descricao_valor else "❌ ERRO: DESCRIÇÃO AUSENTE!"
    )
    dados_finais.append({"CAMPO": "DESCRIÇÃO", "CONTEÚDO": desc_exibicao})

    # Exibe a Tabela
    st.table(dados_finais)

    # Mensagem Reflexiva
    st.markdown(
        '<div class="reflexao">💡 ESSA DESCRIÇÃO DESCREVE MESMO?</div>',
        unsafe_allow_html=True,
    )

    # Botão para copiar (O Streamlit já facilita a seleção de texto na tabela)
    st.info("Dica: Você pode selecionar e copiar os dados da tabela acima diretamente.")
