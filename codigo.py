import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

df = pd.DataFrame({"Categoria": ["A", "B", "C", "D"], "Valor": [120, 340, 230, 410]})
fig = px.bar(df, x="Categoria", y="Valor")

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Dashboard de Análise"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
