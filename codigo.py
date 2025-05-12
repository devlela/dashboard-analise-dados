# Importando bibliotecas necessárias
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Função para obter os dados
def get_data():
    """Retorna os dados em um DataFrame."""
    return pd.DataFrame({"Categoria": ["A", "B", "C", "D"], "Valor": [120, 340, 230, 410]})

# Função para criar o gráfico
def create_figure(data):
    """Gera o gráfico de barras com customizações."""
    return px.bar(
        data, 
        x="Categoria", 
        y="Valor", 
        title="Valores por Categoria",
        color="Categoria",  # Adiciona cores para cada categoria
        labels={"Valor": "Quantidade", "Categoria": "Tipo"},  # Renomeia os rótulos
        template="plotly_white"  # Aplica um tema ao gráfico
    )

# Obtendo os dados e criando o gráfico
df = get_data()
fig = create_figure(df)

# Inicializando a aplicação Dash
app = dash.Dash(__name__)

# Definindo o layout da aplicação com estilo
app.layout = html.Div([
    html.Div([
        html.H1("Dashboard de Análise", style={"textAlign": "center", "color": "#333"})
    ], style={"padding": "20px", "backgroundColor": "#f4f4f4"}),  # Estilo do cabeçalho
    html.Div([
        dcc.Graph(figure=fig)
    ], style={"padding": "20px"})  # Estilo do gráfico
])

# Configuração do servidor
if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=8050)
