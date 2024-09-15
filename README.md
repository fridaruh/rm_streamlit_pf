# Análisis Financiero de Empresas Dashboard

## Descripción
Este dashboard interactivo proporciona un análisis financiero detallado de múltiples empresas. Permite a los usuarios cargar datos financieros en formato CSV y visualizar diversos ratios financieros y métricas de rendimiento a través de gráficos interactivos.

## Características
- Carga de datos financieros vía archivo CSV
- Filtros interactivos por industria, país y tamaño de empresa
- Visualizaciones de ratios financieros clave:
  - Ratio de Liquidez Corriente
  - Ratio Deuda a Patrimonio
  - Cobertura de Gastos Financieros
- Gráfico de dispersión de Rentabilidad vs Riesgo
- Integración opcional con ChatGPT para análisis adicional

## Cómo usar
1. Ejecute la aplicación Streamlit
2. Cargue su archivo CSV con los datos financieros de las empresas
3. Use los filtros en la barra lateral para seleccionar industria, país y tamaño de empresa
4. Explore los gráficos interactivos para analizar los ratios financieros
5. (Opcional) Utilice la función de ChatGPT para hacer preguntas sobre los datos

## Requisitos
- Python 3.7+
- Streamlit
- Pandas
- Plotly
- OpenAI (para la integración con ChatGPT)

## Instalación
1. Clone este repositorio
2. Instale las dependencias:

pip install -r requirements.txt

3. Ejecute la aplicación:


## Estructura de datos requerida
El archivo CSV debe contener las siguientes columnas:
- Company_ID
- Industry
- Country
- Company_Size
- Total_Revenue
- Short_Term_Debt
- Long_Term_Debt
- Current_Assets
- Current_Liabilities
- Equity
- Financial_Expenses

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios mayores antes de crear un pull request.

## Licencia
[MIT License](https://opensource.org/licenses/MIT)