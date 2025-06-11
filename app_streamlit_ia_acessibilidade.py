
import streamlit as st
import openai

st.set_page_config(page_title="Agente IA - Acessibilidade NBR 9050", layout="centered")

# Inicializa o cliente da OpenAI (V1)
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🧠 Agente IA - Avaliação de Acessibilidade (NBR 9050)")

st.markdown("Preencha os dados do projeto para verificar a conformidade com a norma de acessibilidade.")

porta = st.number_input("🔲 Largura da porta (m)", min_value=0.0, max_value=2.0, step=0.01)
rampa = st.number_input("📐 Inclinação da rampa (%)", min_value=0.0, max_value=20.0, step=0.1)
barras = st.selectbox("🧱 Possui barras de apoio?", ["Sim", "Não"])
espaco_sanitario = st.text_input("🚽 Dimensões do sanitário (ex: 1.20x1.20)")
botoeiras = st.number_input("🔘 Altura da botoeira (m)", min_value=0.0, max_value=2.5, step=0.01)

if st.button("🔍 Avaliar Projeto"):
    prompt = f"""
Você é um engenheiro especialista na NBR 9050.
Avalie os seguintes dados de um projeto de arquitetura e indique se estão conformes com a norma:

- Largura da porta: {porta} m
- Inclinação da rampa: {rampa}%
- Barras de apoio: {barras}
- Espaço do sanitário: {espaco_sanitario}
- Altura da botoeira: {botoeiras} m

Responda com justificativas técnicas e recomendações.
    """

    with st.spinner("Consultando a NBR 9050 com IA..."):
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        resposta = response.choices[0].message.content
        st.success("✅ Avaliação concluída!")
        st.markdown("### 📋 Resultado da Análise:")
        st.markdown(resposta)
