import os
from threading import Timer
import webbrowser

import dash
from dash import html
from dash import dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.DatePickerRange(id='date-range')
    ]
)

def open_browser():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:1222/')

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run_server(debug=True, port=1222)
