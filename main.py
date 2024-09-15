import pandas as pd
import plotly.express as px
import streamlit as st

# Título del Dashboard
st.title("Análisis Financiero de Empresas")

# Subir Archivo
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Cálculo de Ratios Financieros (si no están ya calculados)
    df['Total_Debt'] = df['Short_Term_Debt'] + df['Long_Term_Debt']
    df['Current_Ratio'] = df['Current_Assets'] / df['Current_Liabilities']
    df['Debt_to_Equity_Ratio'] = df['Total_Debt'] / df['Equity']
    df['Interest_Coverage_Ratio'] = df['Total_Revenue'] / df['Financial_Expenses']
    
       # Change multiselect to selectbox for industries
    industry = st.sidebar.selectbox(
        "Seleccione la Industria",
        options=["Todas"] + list(df["Industry"].unique()),
        index=0
    )
    
    # Change multiselect to selectbox for countries
    country = st.sidebar.selectbox(
        "Seleccione el País",
        options=["Todos"] + list(df["Country"].unique()),
        index=0
    )
    
    # Change multiselect to selectbox for company size
    company_size = st.sidebar.selectbox(
        "Seleccione el Tamaño de la Empresa",
        options=["Todos"] + list(df["Company_Size"].unique()),
        index=0
    )
    
    # Modify the query to handle the "Todos" option
    df_selection = df.query(
        "(Industry == @industry or @industry == 'Todas') and "
        "(Country == @country or @country == 'Todos') and "
        "(Company_Size == @company_size or @company_size == 'Todos')"
    ) 
    
    # Gráficos Interactivos
    st.header("Ratios Financieros")
    
    # Ratio de Liquidez
    st.subheader("Ratio de Liquidez Corriente")
    fig_current_ratio = px.bar(
        df_selection,
        x="Company_ID",
        y="Current_Ratio",
        color="Industry",
        barmode="group",
        title="Ratio de Liquidez por Empresa"
    )
    st.plotly_chart(fig_current_ratio)
    
    # Ratio Deuda a Patrimonio
    st.subheader("Ratio Deuda a Patrimonio")
    fig_debt_equity = px.bar(
        df_selection,
        x="Company_ID",
        y="Debt_to_Equity_Ratio",
        color="Industry",
        barmode="group",
        title="Ratio Deuda a Patrimonio por Empresa"
    )
    st.plotly_chart(fig_debt_equity)

    st.subheader("Rentabilidad vs Riesgo")
    fig_risk_return = px.scatter(
        df_selection,
        x="Debt_to_Equity_Ratio",
        y="Interest_Coverage_Ratio",  
        color="Industry",
        hover_name="Company_ID",
        title="Rentabilidad vs Riesgo por Empresa"
    )
    st.plotly_chart(fig_risk_return)
    
    # Cobertura de Gastos Financieros
    st.subheader("Cobertura de Gastos Financieros")
    fig_interest_coverage = px.bar(
        df_selection,
        x="Company_ID",
        y="Interest_Coverage_Ratio",
        color="Industry",
        barmode="group",
        title="Cobertura de Gastos Financieros por Empresa"
    )
    st.plotly_chart(fig_interest_coverage)
    
    # (Opcional) Integración con ChatGPT
    st.header("Consulta a ChatGPT (Opcional)")
    user_question = st.text_input("Haz una pregunta sobre los datos o los resultados del análisis:")
    
    if user_question:
        # Llamada a la API de OpenAI (asegúrate de tener la biblioteca openai instalada y tu clave API)
        import openai
        openai.api_key = 'TU_CLAVE_API'
    
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_question,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
    
        answer = response.choices[0].text.strip()
        st.write("**Respuesta de ChatGPT:**")
        st.write(answer)

else:
    st.warning("Por favor, sube un archivo CSV para comenzar el análisis.")