import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

x = 0
y = 0
app = dash.Dash(__name__, suppress_callback_exceptions=True)


sidebar_style = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "8rem",
    "height": "200vh",
    "padding": "1rem 1rem",
    "background-color": "#000e2d",
}

content_style = {
    "color": "#fff",
    "padding": "2rem 1rem",
    "padding-left": "42.5%",
}

output_style = {
    "position": "absolute",
    "padding-left": "42%",
    "top": "45%",
    "color": "#fd6a02",
}

nav = html.Div(
    [
        html.Img(src="assets/cool.png"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
                html.Hr(),
                dbc.NavItem(dbc.NavLink("Input", href="/input", active="exact")),
                html.Hr(),
                dbc.NavItem(dbc.NavLink("Output", href="/output", active="exact")),
                html.Hr()
            ],
            pills=True,
            fill=True
        ),
    ],
    style=sidebar_style,
)

home = html.Div(
    [
        html.P("This very cool web app does some very cool stuff bro")
    ], style=content_style
)

input_page = html.Div(
    [
         dcc.Input(id='input', placeholder="Enter a number between (and including) 0 - 1000",
                      type='number', min=0, max=1000, step=1,
                      debounce=True, required=True,),
    ], style=content_style
)
@app.callback(
     Output("store", "data"),
     Input("input", "value"),
            )

def update_value(val):
    if val == None:
        raise dash.exceptions.PreventUpdate
    else:
        val += 5
        return val
output_page = html.Div(
    [
    html.A(id="output-text", children="",style=output_style),
    ]
)
@app.callback(
    Output("output-text", "children"),
    State("store", "data"),
    Input("url", "pathname")
    )

def update_text(val, path):

    return "the all-important value driving our business decisions is " + str(val)


content = html.Div(id="page-content", children=[],)

app.layout = html.Div([

        dcc.Location(id="url"),
        html.H1("Very Cool Web App"),
        nav,
        content,
        dcc.Store(id='store', data=0, storage_type='session',)

])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)



def render_content(pathname):

    if pathname == "/":
        return [
            home
        ]

    elif pathname == "/input":
        return [
            input_page,
            ]


    elif pathname == "/output":
        return [
            output_page
        ]



if __name__ == '__main__':
    app.run_server(debug=True)
