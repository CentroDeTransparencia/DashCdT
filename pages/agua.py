import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc, callback
from dash.dependencies import Output,Input, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

#Cargue de datos de las estaciones metereológicas del IDEAM
df_est = pd.read_csv('CNE_IDEAM.csv', sep=";", decimal=',', encoding='latin-1')
df_hid = pd.read_csv('HIDROMETEO.csv', sep=";", decimal='.', encoding='latin-1')

#Estilos utilizados

tabs_styles = {
    'flex-direction': 'row',
    'height':'40px',
    'textAlign': 'center',
    'margin-left':'20px',
    'margin-right':'20px'
}
tab_style = {
    'border': '#094958',
    'borderBottom': '3px solid #1F2132',
    'padding': '10px',
    'backgroundColor': '#094958',
    'height':'40px',
    'textAlign': 'center'
}

tab_selected_style = {
    'border': '#094958',
    'borderBottom': '3px solid #1F2132',
    'boxShadow': 'inset 0px -1px 0px 0px lightgrey',
    'padding': '8px',
    'backgroundColor': '#fcf9eb',
    'height':'40px',
    'textAlign': 'center'
}

#Creación de la figuras utilizadas
## Ubicación de estaciones con Open Street Maps de fondo
fig1 = px.scatter_mapbox (df_est, 
                          lon= df_est['longitud'], 
                          lat= df_est['latitud'], 
                          zoom=8, 
                          height=400, 
                          hover_data=["nombre", "CATEGORIA"],
                          )
fig1.update_layout(mapbox_style="open-street-map")
fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

##Gráfica de temperatura
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df_hid['Fecha'], 
                         y=df_hid['Valor'],
                         fill=None,
                         mode='lines'))

#Configuración de las pestañas a visualizar
## Pestaña de variables hidrometereológicas
v_hidrometereo = html.Div([    
        html.Div([
        html.Div([
            #html.H5("Ubicación de estaciones IDEAM"),
            html.Div([html.H5("Ubicación de estaciones IDEAM", className="map column"),
                    dbc.Button("¿CÓMO FUNCIONA?", outline=True, color="info",id="bu_vhidro",className="me-2 control column",n_clicks=0)],className="row flex-display"),
                    #html.P("Los PPII se desarrollan en el municipio de Puerto Wilches, departamento de Santandar; la selección de un PPII en particular en el mapa presentado a continuación permite actualizar y observar su información de pozo."),
                    dbc.Modal(
                                    [
                                        dbc.ModalHeader(dbc.ModalTitle("Explicación")),
                                        dbc.ModalBody(
                                            html.P("Los PPII se desarrollan en el municipio de Puerto Wilches, departamento de Santandar; la selección de un PPII en particular en el mapa presentado a continuación permite actualizar y observar su información de pozo.")),
                                    ],
                                    id="mu_vhidro",
                                    size="md",
                                    is_open=False,
                                ),
            dcc.Graph(figure=fig1, id='Ubicacion1'),
            ],className="one-half column pretty-container",
                style={'height':'100rem','padding':'3rem',"margin-left": "10px","margin-right": "5px"}
                ),
            html.Div([
            #html.H5("Ubicación de estaciones IDEAM"),
            html.Div([html.H5("Temperatura de estaciones IDEAM", className="map column"),
                    dbc.Button("¿CÓMO FUNCIONA?", outline=True, color="info",id="t1_vhidro",className="me-2 control column",n_clicks=0)],className="row flex-display"),
                    #html.P("Los PPII se desarrollan en el municipio de Puerto Wilches, departamento de Santandar; la selección de un PPII en particular en el mapa presentado a continuación permite actualizar y observar su información de pozo."),
            dcc.Graph(figure=fig2, id='Temperatura'),
            ],className="one-half column pretty-container",
                style={'height':'100rem','padding':'3rem',"margin-left": "10px","margin-right": "5px"}
                )]
                ,className="row flex-display"
                #,style={"display": "flex", "flex-direction": "column"}
                )
])

##Pestaña de agua superficial
c_asuper = html.Div(id='body_asuper', 
                    className='app-body', 
                    children=[html.Div([html.Div(id='ali_asuper', 
                                                    className='control-tabs', 
                                                    children=[dcc.Tabs(id='Tabs_asuper', 
                                                                    value='info_asuper',
                                                                    children=[dcc.Tab(label='Información',
                                                                                        value='info_asuper',
                                                                                        children=html.Div(className='control-tab', 
                                                                                        children=[html.H4(className='what-is',
                                                                                                        children='Aquí va una explicación'),
                                                                                                html.P("___________________")]),
                                                                                        style=tab_style,
                                                                                        selected_style=tab_selected_style),
                                                                                dcc.Tab(label='Gráfico interactivo',
                                                                                        value='filt_asuper',
                                                                                        children=html.Div(className='control-tab', 
                                                                                                        children=[html.Div([html.H3('General', 
                                                                                                                                        className='alignment-settings-section'),
                                                                                                                            html.Div(className='app-controls-block',
                                                                                                                                        children=[html.Div(className='app-controls-name',
                                                                                                                                                        children="Colorscale"),
                                                                                                                                                dcc.Dropdown(id='alignment-colorscale-dropdown',
                                                                                                                                                            className='app-controls-block-dropdown',
                                                                                                                                                            value='clustal2'),
                                                                                                                                                html.Div(className='app-controls-desc',
                                                                                                                                                        children='Choose the color theme of the viewer.')])]),
                                                                                                                    html.Hr()]),
                                                                                        style=tab_style,
                                                                                        selected_style=tab_selected_style)], 
                                                                                        className = 'tabs_width')])])],
                    style={"overflow": "scroll","width": "45rem",'height':'50rem'})

g_asuper =  html.Div([
            html.Div([html.H5("", style={"height":"1rem"}),
                    html.H5("Puntos de monitoreo de agua superficial", className="map column"),
                    dbc.Button("¿CÓMO FUNCIONA?", outline=True, color="info",id="bu_asuper",className="me-2 control column",n_clicks=0)],className="row flex-display",style={"margin-right":"20px","margin-bottom":"5px"}),
                    dbc.Modal([ dbc.ModalHeader(dbc.ModalTitle("Explicación")),
                                dbc.ModalBody(
                                html.P("Los PPII se desarrollan en el municipio de Puerto Wilches, departamento de Santandar; la selección de un PPII en particular en el mapa presentado a continuación permite actualizar y observar su información de pozo.")),
                                    ],
                                    id="mu_asuper",
                                    size="md",
                                    is_open=False),
            dcc.Graph(figure=fig1,style={"margin-left":"20px","margin-right":"20px"})])

a_super = html.Div([
    dbc.Row([dbc.Col(c_asuper, width=4,style={"margin-left":"20px"}),
             dbc.Col(g_asuper,style={"margin-left":"20px","margin-right":"20px"})], 
             justify="start"),              
])

##Pestaña de agua subterránea
a_subte = html.Div(id='body_asubte', className='app-body', children=[
        html.Div([
            html.Div(id='ali_asubte', className='control-tabs', children=[
                dcc.Tabs(
                    id='Tabs_asubte', value='info_asuper',
                    children=[
                        dcc.Tab(
                            label='Información',
                            value='info_asubte',
                            children=html.Div(className='control-tab', children=[
                                html.H4(
                                    className='what-is',
                                    children='What is Alignment Viewer?'
                                ),
                                html.P(
                                    """
                                    The 
                                    """
                                ),
                            ]),
                        style=tab_style,
                        selected_style=tab_selected_style
                        ),
                        dcc.Tab(
                            label='Gráfico interactivo',
                            value='filt_asuper',
                            children=html.Div(className='control-tab', children=[
                                html.Div([
                                    html.H3('General', className='alignment-settings-section'),
                                    html.Div(
                                        className='app-controls-block',
                                        children=[
                                            html.Div(className='app-controls-name',
                                                     children="Colorscale"),
                                            dcc.Dropdown(
                                                id='alignment-colorscale-dropdown_subte',
                                                className='app-controls-block-dropdown',
                                                value='clustal2',
                                            ),
                                            html.Div(
                                                className='app-controls-desc',
                                                children='Choose the color theme of the viewer.'
                                            )
                                        ],
                                    ),
                                ]),
                                html.Hr()
                            ]),
                        style=tab_style,
                        selected_style=tab_selected_style
                        ),
                    ], className = 'tabs_width'),
            ]),
        ]),
    ],
    style={"overflow": "scroll","width": "45rem",'height':'50rem'})

##Pestaña de indicadores de Planes de Manejo Ambiental
pma = html.Div([    
        html.Div([html.H5("No actualizado")])
        ]
        ,style={'height':'10rem','padding':'3rem',"margin-left": "10px","margin-right": "5px",'textAlign': 'center'})

#### Dash

dash.register_page(__name__)

layout = html.Div([
    
 html.Div([
            dcc.Tabs(id = "tabs_principal", value = 'V_hidrom', children = [
                dcc.Tab(v_hidrometereo,
                        label = 'HIDROMETEREOLOGÍA',
                        value = 'V_hidrom',
                        className = 'font_size',
                        style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(a_super,
                        label = 'AGUA SUPERFICIAL',
                        value = 'a_super',
                        className = 'font_size',
                        style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(a_subte,
                        label = 'AGUA SUBTERRÁNEA',
                        value = 'a_subte',
                        className = 'font_size',
                        style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(pma,
                        label = 'PLANES DE MANEJO AMBIENTAL',
                        value = 'pma',
                        className = 'font_size',
                        style=tab_style, selected_style=tab_selected_style),
            ], style=tabs_styles),
        ]),

        ])


def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open

callback(
    Output("mu_vhidro", "is_open"),
    Input("bu_vhidro", "n_clicks"),
    State("mu_vhidro", "is_open"),
    )(toggle_modal)

callback(
    Output("mu_asuper", "is_open"),
    Input("bu_asuper", "n_clicks"),
    State("mu_asuper", "is_open"),
    )(toggle_modal)

callback(
    Output("Temperatura", "figure"),
    Input("Ubicacion1", "clickData")
    )

def click(clickData):
    if not clickData:

        raise dash.exceptions.PreventUpdate
    print(clickData)
    nombre_estacion=clickData['points'][0]['customdata'][0].split('[')[1][:-1]
    print(nombre_estacion)

    fig2= go.Figure()
    fig2.add_trace(go.Scatter(x=df_hid['Fecha'], 
                              y=df_hid['Estación'],
                              fill=None,
                              mode='lines'))
    return fig2
