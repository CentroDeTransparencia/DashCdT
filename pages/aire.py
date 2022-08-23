import dash
from dash import html,dcc
import plotly.graph_objs as go
import pandas as pd

dash.register_page(__name__)

prueba = pd.read_excel("Acumulados_python.xlsx")

#Grafica 
#Olores ofensivos 2
fig1= go.Figure()
fig1.add_trace(go.Line(y=prueba["Maximo"]))
fig1.add_trace(go.Bar(x=prueba["Febrero-Mayo"],y=prueba["Mediciones"]))



#interfaz grafica
layout= html.Div([html.H1("Curaduria Aire y Clima"), dcc.Graph(figure=fig1)]) 

