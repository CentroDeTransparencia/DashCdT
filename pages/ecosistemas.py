from pydoc import classname
import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([html.H1("Curaduria de Ecosistemas"), html.H2("En construcción"), html.P("probando cambios")],className="center"

                )
