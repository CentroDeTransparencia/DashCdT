import dash
from dash import html,dcc
import plotly.graph_objs as go
import pandas as pd

dash.register_page(__name__)


#Grafica Ruido día habil 1
prueba2 = pd.read_excel("Ruido_Python.xlsx")
prueba2=pd.ExcelFile("Ruido_Python.xlsx")
prueba2.parse("Sector A")

import plotly.express as px

df = prueba2.parse("Sector A")
figRuido1 = px.scatter(df, x="Dia 1 habil", y="Riesgo", animation_frame="Hora", animation_group="Nombre",
           size="Dia 1 habil", color="Nombre", hover_name="Nombre",title="Ruido, mediciones día 1 habil Kale",
           log_x=True, size_max=70, range_x=[45,105], range_y=[40,80])

figRuido1["layout"].pop("updatemenus") # optional, drop animation buttons

#Grafica Ruido día habil 2
prueba2 = pd.read_excel("Ruido_Python.xlsx")
prueba2=pd.ExcelFile("Ruido_Python.xlsx")
prueba2.parse("Sector A")

import plotly.express as px

df = prueba2.parse("Sector A")
figRuido2 = px.scatter(df, x="Día 2 habil", y="Riesgo", animation_frame="Hora", animation_group="Nombre",
           size="Día 2 habil", color="Nombre", hover_name="Nombre",title="Ruido, mediciones día 2 habil Kale",
           log_x=True, size_max=70, range_x=[45,105], range_y=[40,80])

figRuido2["layout"].pop("updatemenus") # optional, drop animation buttons

#Grafica Ruido día no hablil
prueba2 = pd.read_excel("Ruido_Python.xlsx")
prueba2=pd.ExcelFile("Ruido_Python.xlsx")
prueba2.parse("Sector A")

import plotly.express as px

df = prueba2.parse("Sector A")
figRuido3 = px.scatter(df, x="Día no habil", y="Riesgo", animation_frame="Hora", animation_group="Nombre",
           size="Día no habil", color="Nombre", hover_name="Nombre",title="Ruido, mediciones día no habil Kale",
           log_x=True, size_max=70, range_x=[45,105], range_y=[40,80])

figRuido3["layout"].pop("updatemenus") # optional, drop animation buttons

#Grafica 
#Olores ofensivos Amoniaco
prueba = pd.read_excel("Acumulados_python.xlsx")
figAmon= go.Figure()
figAmon.add_trace(go.Line(y=prueba["Maximo"]))
figAmon.add_trace(go.Bar(x=prueba["Febrero-Mayo"],y=prueba["Mediciones"]))

#Grafica 
#Olores ofensivos Sulfuro de hidrogeno

Sulfuro = pd.read_excel("Sulfuro.xlsx")
figsulf= go.Figure()
figsulf.add_trace(go.Line(y=Sulfuro["Maximo"]))
figsulf.add_trace(go.Bar(x=Sulfuro["Febrero-Mayo"],y=Sulfuro["Mediciones"]))

#interfaz grafica
layout= html.Div([html.H1("Curaduria Aire y Clima"),
 html.Div(dcc.Graph(figure=figRuido1)),
 html.Div(dcc.Graph(figure=figRuido2)),
 html.Div( dcc.Graph(figure=figRuido3)),
 html.Div(dcc.Graph(figure=figAmon)),
 html.Div(dcc.Graph(figure=figsulf))]) 



