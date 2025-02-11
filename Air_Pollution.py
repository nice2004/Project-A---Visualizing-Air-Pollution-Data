import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Plotly graphs aren't just static images. Users can hover over data points to see details,
# zoom in and out, pan around, and even interact with elements in the graph to explore the data


# Exploring my data & Preparing my data for usage *********************************************************
df = pd.read_csv('San_Franscisco_Dataset.csv')
print(df.head())
print(df['Daily Max 8-hour CO Concentration'])

has_missing_values1 = df['Daily Max 8-hour CO Concentration'].isnull().any()
has_missing_values2 = df['Daily AQI Value'].isnull().any()
has_missing_values3 = df['Local Site Name'].isnull().any()
has_missing_values4 = df['Date'].isnull().any()
print(has_missing_values1)
print(has_missing_values1)
print(has_missing_values1)
print(has_missing_values1)

# changing the date column to date time
df['Date'] = pd.to_datetime(df['Date'])

# App Layout **************************************************************************
# this goes to styles.css and tells it what to do!
stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=stylesheets)

# dcc provides a wide range of components like dropdowns,
# sliders, input boxes, graphs, date pickers, and more, allowing users to interact with your app
app.layout = html.Div([
    dcc.Dropdown(id='site-dropdown',
                 options=[{'label': site, 'value': site} for site in df['Local Site Name'].unique()],
                 multi=True,
                 value=df['Local Site Name'].unique()[0]  # default to one site
                 ), dcc.Graph(id='Air Index Graph in Northern California Due to Carbon Monoxide')
])


# Callbacks ***************************************************************************

# callbacks are used to make the dashboard interactive.
# They allow you to define how the dashboard should respond
# to user interactions like clicking a button, selecting a value from a dropdown,
# or dragging a slider.

@app.callback(Output('Air Index Graph in Northern California Due to Carbon Monoxide', 'figure'),
              Input('site-dropdown', 'value'))
# is in is always used for sites only, so created a list for local sites
def update_graph(selected_site):
    if isinstance(selected_site, str):
        selected_site = [selected_site]
    # filter the dataframe to include only the selected sites
    filtered_df = df[df['Local Site Name'].isin(selected_site)]
    fig = px.bar(filtered_df, x='Date',
                 y='Daily AQI Value', color='Local Site Name', title=f'Air Quality Index for {selected_site} over Time',
                 labels={'Date': "Date", 'Daily AQI Value': 'AQI Value'})
    fig.update_layout(
        title={
            'text': f'Air Quality Index for {selected_site} over Time in Northern California',
            'y': 0.9,  # vertical position
            'x': 0.5,  # Center the Title
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'size': 25,
                'family': 'Arial, sans-serif',
                'color': 'black',
                'weight': 'bold'

            }
        }
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
