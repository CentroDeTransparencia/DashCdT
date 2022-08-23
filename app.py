from dash import Dash, html, dcc, Input, Output,State
import dash
import dash_bootstrap_components as dbc 
from dash_bootstrap_components._components.Container import Container
from flask import Flask


server = Flask(__name__)
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])



navbar = dbc.NavbarSimple(
    
     children=[      
         dbc.NavItem(dbc.NavLink("Agua", href="/agua",)),
         dbc.NavItem(dbc.NavLink("Aire y Clima", href="/aire",)),
         dbc.NavItem(dbc.NavLink("Ecosistemas", href="/ecosistemas",)),
         dbc.NavItem(dbc.NavLink("Hidrocarburos", href="/hidrocarburos",)),
         dbc.NavItem(dbc.NavLink("Salud", href="/salud",)),
         dbc.NavItem(dbc.NavLink("Sismicidad", href="/sismicidad",)),
         dbc.NavItem(dbc.NavLink("Socioeconnómico", href="/socioeconomico",)),
     ],
     color="#002c35",
     dark=True,
     brand="Centro de Transparencia",
 )
# navbar_items = [
#     dbc.NavItem(dbc.NavLink("Agua", href="/agua",)), 
#    dbc.NavItem(dbc.NavLink("Aire y Clima", href="/aire",)),
#     dbc.NavItem(dbc.NavLink("Ecosistemas", href="/ecosistemas",)) ,
#     dbc.NavItem(dbc.NavLink("Hidrocarburos", href="/hidrocarburos",)),
#     dbc.NavItem(dbc.NavLink("Salud", href="/salud",)),
#     dbc.NavItem(dbc.NavLink("Sismicidad", href="/sismicidad",)), 
#     dbc.NavItem(dbc.NavLink("Socioeconnómico", href="/socioeconomico",)),
# ]
# navbar = dbc.Navbar(
#     dbc.Container(
#         [
#             html.A(
#                 # Use row and col to control vertical alignment of logo / brand
#                 dbc.Row(
#                     [
#                         dbc.Col(html.Img(src="/assets/positivo_recortado.png", height="30px")),
                        
#                     ],
#                     align="center",
#                     className="g-0",
#                 ),
#                 href="/",
#                 style={"textDecoration": "none"},
#             ),
#             dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
#             dbc.Collapse(
#                 navbar_items,
#                 id="navbar-collapse",
#                 is_open=False,
#                 navbar=True,
#             ),
#         ]
#     ),
#     color="dark",
#     dark=True,
# )


# # add callback for toggling the collapse on small screens
# @app.callback(
#     Output("navbar-collapse", "is_open"),
#     [Input("navbar-toggler", "n_clicks")],
#     [State("navbar-collapse", "is_open")],
# )
# def toggle_navbar_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

app.layout = html.Div([
	html.Div(navbar),
    # html.Div(
    #     [
    #         html.Div(
    #             # dcc.Link(
    #             #     f"{page['name']} - {page['path']}", href=page["relative_path"]
    #             # )
    #         )
    #         for page in dash.page_registry.values()
    #     ]
    # ),

	dash.page_container,
	html.Div(
            html.Img(

                            src= ("assets/Institucional_3Logos_letrasblancas.png"),

                            id="logos-image",

                            style={

                                "height": "auto",

                                "max-width": "600px",
                                "margin-top": "25px",

                                "margin-bottom": "25px",

                            }),id="footer"

    )
])

if __name__ == '__main__':
	app.run_server(debug=True)