import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Sample data for population by country
data = {
    'Country': ['USA', 'China', 'India', 'Brazil', 'Russia'],
    'Population': [331, 1441, 1380, 212, 146],
}

# Create Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in data['Country']],
        value='USA'  # Default selected value
    ),
    dcc.Graph(id='population-bar-chart')
])

# Define callback to update the chart based on dropdown selection
@app.callback(
    Output('population-bar-chart', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_chart(selected_country):
    # Filter data for the selected country
    filtered_data = data[data['Country'] == selected_country]
    
    # Create bar chart using Plotly Express
    fig = px.bar(filtered_data, x='Country', y='Population', title=f'Population of {selected_country}')
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
