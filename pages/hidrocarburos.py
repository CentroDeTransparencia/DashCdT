import pandas as pd
import dash
from dash import html
from dash import dcc, callback
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from dash.dependencies import Output,Input

### Datos

prueba = pd.read_excel("Prueba_CdT.xlsx")

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=prueba["Dtp"], y=prueba["Z (TVD)"], mode="lines"))
fig1.update_yaxes(autorange="reversed")
fig1.update_layout(height=1600)

fig2 = px.histogram(prueba, x="Dtp",
                   marginal="box", # or violin, rug
                   hover_data=prueba.columns)

fig3 = px.scatter(prueba, x='Dts', y="Dtp", color="Z (TVD)")
fig3.update_coloraxes(col="Z (TVD")
#fig3.update_layout(width=500)

fig4 = go.Figure(go.Scattermapbox(
    lat=['7.3484'],
    lon=['-73.9030'],
    mode='markers',
    marker=go.scattermapbox.Marker(size=14),
    text=['Puerto Wilches']))
fig4.update_layout(
    hovermode='closest',
    mapbox_style="open-street-map", 
    mapbox=dict(bearing=0, center=go.layout.mapbox.Center(lat=7.3,lon=-73.9), pitch=0, zoom=10),
    #width=600,
    #height=500
    )

fig5 = make_subplots(rows=1, cols=3, )
fig5.add_trace(go.Scatter(x=prueba['Dtp'], y=prueba['Z (TVD)']), row=1, col=1)
fig5.add_trace(go.Scatter(x=prueba['Dts'], y=prueba['Z (TVD)']), row=1, col=2)
fig5.add_trace(go.Scatter(x=prueba['Dtp'], y=prueba['Z (TVD)']), row=1, col=3)

fig5.update_xaxes(title_text="Dtp", row=1, col=1)
fig5.update_xaxes(title_text="Dts", row=1, col=2)
fig5.update_xaxes(title_text="Dtp", row=1, col=3)

fig5.update_yaxes(title_text="Depth", row=1, col=1, autorange='reversed')
fig5.update_yaxes(title_text="Depth", row=1, col=2, autorange='reversed')
fig5.update_yaxes(title_text="Depth", row=1, col=3, autorange='reversed')

fig5.update_layout(height=1600)

#fig5.show()

#### Dash

dash.register_page(__name__)

layout = html.Div([
    html.Div([
        html.Div([
            html.H5("Ubicación de los PPII"),
            #html.P("Los PPII se desarrollan en el municipio de Puerto Wilches, departamento de Santandar; la selección de un PPII en particular en el mapa presentado a continuación permite actualizar y observar su información de pozo."),
            dcc.Graph(figure=fig4),
            html.H5("Correlaciones/Estadísticas"),
            html.P("   "),
            html.Div([dcc.Dropdown(style={'color':'black'},options=['Dtp','Dts'],id="eje_hist")]),
                dcc.Graph(figure=fig2,id='histograma'),
            html.Br(),
            html.Br(),
            html.Div([dcc.Dropdown(style={'color':'black'},options=['Dtp','Dts'],id="eje_y"),dcc.Dropdown(style={'color':'black'},options=['Dtp','Dts'],id="eje_x")]),
                dcc.Graph(figure=fig3,id='correlaciones')],className="one-half column pretty-container",
                style={'height':'100rem','overflow':'scroll','padding':'3rem',"margin-left": "10px","margin-right": "5px"}
                ),
        html.Div([
            html.H5("Registros de pozos"),
            html.P("   "),
            html.Div(
                #dcc.Dropdown(options=['Dtp','Dts'],id="filtros")),
                dcc.Graph(figure=fig5,id='registros'))],className="one-half column pretty-container",
                style={'height':'100rem','overflow':'scroll','padding':'3rem',"margin-left": "10px","margin-right": "5px"}
                )]
                ,className="row flex-display"
                #,style={"display": "flex", "flex-direction": "column"}
                ),
    ])



# @app.callback(Output('registros','figure'),[Input('filtros','value')])

# def update_figure (selected_value):
#     fig1 = go.Figure()
#     fig1.add_trace(go.Scatter(
#         x=prueba[selected_value],
#         y=prueba["Z (TVD)"],
#         mode="lines"
#         ))
#     fig1.update_yaxes(autorange="reversed")
#     fig1.update_layout(width=500,height=1200)
#     return fig1

@callback(Output('histograma','figure'),(Input('eje_hist','value')))

def update_figure (selected_value_hist):
    fig2 = px.histogram(prueba, x=selected_value_hist,
                   marginal="box", # or violin, rug
                   hover_data=prueba.columns)
    return fig2  

@callback(Output('correlaciones','figure'),(Input('eje_x','value')),(Input('eje_y','value')))

def update_figure (selected_value1,selected_value2):
    fig3 = px.scatter(prueba, x=selected_value1, y=selected_value2, color="Z (TVD)")
    fig3.update_coloraxes(col="Z (TVD")
    #fig3.update_layout(width=500)
    return fig3  


