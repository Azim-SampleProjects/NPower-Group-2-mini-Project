# Import pandas for data handling
import pandas as pd

# Import Dash tools for dashboard layout and callbacks
from dash import Dash, html, dcc, Input, Output

# Import Plotly Express for charts
import plotly.express as px

# Import webbrowser and time so the dashboard opens automatically
import webbrowser
import time


# ------------------------------------------------------------
# 1. LOAD THE CLEANED DATASET
# ------------------------------------------------------------

# Read the cleaned CSV file
df = pd.read_csv("Online_Retail_clean2.csv")

# Convert InvoiceDate to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create Total_Sales column if it does not already exist
df['Total_Sales'] = df['Quantity'] * df['UnitPrice']

# Create date/time columns if they do not already exist
df['InvoiceYear'] = df['InvoiceDate'].dt.year
df['InvoiceMonth'] = df['InvoiceDate'].dt.month
df['InvoiceDayName'] = df['InvoiceDate'].dt.day_name()
df['InvoiceHour'] = df['InvoiceDate'].dt.hour
df['YearMonth'] = df['InvoiceDate'].dt.to_period('M').astype(str)

# Create time of day function
def get_time_of_day(hour):
    # Morning: 5 AM to before 12 PM
    if 5 <= hour < 12:
        return "Morning"

    # Afternoon: 12 PM to before 5 PM
    elif 12 <= hour < 17:
        return "Afternoon"

    # Evening: 5 PM to before 9 PM
    elif 17 <= hour < 21:
        return "Evening"

    # Night: anything else
    else:
        return "Night"

# Apply the time of day function to InvoiceHour
df['Invoice_Time_of_Day'] = df['InvoiceHour'].apply(get_time_of_day)


# ------------------------------------------------------------
# 2. CREATE DROPDOWN OPTIONS
# ------------------------------------------------------------

# Create country dropdown options
country_options = [{'label': 'All Countries', 'value': 'All'}]

# Add each country to the dropdown
country_options += [
    {'label': country, 'value': country}
    for country in sorted(df['Country'].dropna().unique())
]

# Create month dropdown options
month_options = [{'label': 'All Months', 'value': 'All'}]

# Add each month to the dropdown
month_options += [
    {'label': month, 'value': month}
    for month in sorted(df['YearMonth'].dropna().unique())
]

# Create time of day dropdown options
time_options = [{'label': 'All Times of Day', 'value': 'All'}]

# Add each time of day to the dropdown
time_options += [
    {'label': time_day, 'value': time_day}
    for time_day in sorted(df['Invoice_Time_of_Day'].dropna().unique())
]


# ------------------------------------------------------------
# 3. START DASH APP
# ------------------------------------------------------------

# Create the Dash app
app = Dash(__name__)

# Add title to browser tab
app.title = "E-Commerce Sales Dashboard"


# ------------------------------------------------------------
# 4. DASHBOARD LAYOUT
# ------------------------------------------------------------

app.layout = html.Div(

    # Main dashboard style
    style={
        'backgroundColor': '#f4f6f8',
        'fontFamily': 'Arial',
        'padding': '20px'
    },

    children=[

        # Dashboard title
        html.H1(
            "Group 2: E-Commerce Sales Dashboard",
            style={
                'textAlign': 'center',
                'color': '#1f2c56',
                'marginBottom': '5px'
            }
        ),

        # Dashboard subtitle
        html.P(
            "Interactive dashboard based on the cleaned Online Retail dataset",
            style={
                'textAlign': 'center',
                'color': '#555555',
                'fontSize': '16px'
            }
        ),

        # ----------------------------------------------------
        # DROPDOWNS
        # ----------------------------------------------------

        html.Div(

            style={
                'display': 'flex',
                'gap': '20px',
                'marginTop': '25px',
                'marginBottom': '25px'
            },

            children=[

                # Country dropdown container
                html.Div(
                    style={'width': '33%'},

                    children=[
                        html.Label("Select Country:", style={'fontWeight': 'bold'}),
                        dcc.Dropdown(
                            id='country_dropdown',
                            options=country_options,
                            value='All',
                            clearable=False
                        )
                    ]
                ),

                # Month dropdown container
                html.Div(
                    style={'width': '33%'},

                    children=[
                        html.Label("Select Month:", style={'fontWeight': 'bold'}),
                        dcc.Dropdown(
                            id='month_dropdown',
                            options=month_options,
                            value='All',
                            clearable=False
                        )
                    ]
                ),

                # Time of day dropdown container
                html.Div(
                    style={'width': '33%'},

                    children=[
                        html.Label("Select Time of Day:", style={'fontWeight': 'bold'}),
                        dcc.Dropdown(
                            id='time_dropdown',
                            options=time_options,
                            value='All',
                            clearable=False
                        )
                    ]
                )
            ]
        ),

        # ----------------------------------------------------
        # KPI CARDS
        # ----------------------------------------------------

        html.Div(

            id='kpi_cards',

            style={
                'display': 'flex',
                'gap': '20px',
                'marginBottom': '25px'
            }
        ),

        # ----------------------------------------------------
        # FIRST ROW OF CHARTS
        # ----------------------------------------------------

        html.Div(

            style={
                'display': 'flex',
                'gap': '20px',
                'marginBottom': '20px'
            },

            children=[

                # Top countries chart
                html.Div(
                    style={
                        'width': '50%',
                        'backgroundColor': 'white',
                        'padding': '10px',
                        'borderRadius': '10px',
                        'boxShadow': '0px 2px 5px rgba(0,0,0,0.1)'
                    },

                    children=[
                        dcc.Graph(id='country_sales_chart')
                    ]
                ),

                # Monthly sales chart
                html.Div(
                    style={
                        'width': '50%',
                        'backgroundColor': 'white',
                        'padding': '10px',
                        'borderRadius': '10px',
                        'boxShadow': '0px 2px 5px rgba(0,0,0,0.1)'
                    },

                    children=[
                        dcc.Graph(id='monthly_sales_chart')
                    ]
                )
            ]
        ),

        # ----------------------------------------------------
        # SECOND ROW OF CHARTS
        # ----------------------------------------------------

        html.Div(

            style={
                'display': 'flex',
                'gap': '20px'
            },

            children=[

                # Top products chart
                html.Div(
                    style={
                        'width': '50%',
                        'backgroundColor': 'white',
                        'padding': '10px',
                        'borderRadius': '10px',
                        'boxShadow': '0px 2px 5px rgba(0,0,0,0.1)'
                    },

                    children=[
                        dcc.Graph(id='product_sales_chart')
                    ]
                ),

                # Sales vs returns chart
                html.Div(
                    style={
                        'width': '50%',
                        'backgroundColor': 'white',
                        'padding': '10px',
                        'borderRadius': '10px',
                        'boxShadow': '0px 2px 5px rgba(0,0,0,0.1)'
                    },

                    children=[
                        dcc.Graph(id='sales_returns_chart')
                    ]
                )
            ]
        )
    ]
)


# ------------------------------------------------------------
# 5. CALLBACK TO UPDATE DASHBOARD
# ------------------------------------------------------------

@app.callback(
    Output('kpi_cards', 'children'),
    Output('country_sales_chart', 'figure'),
    Output('monthly_sales_chart', 'figure'),
    Output('product_sales_chart', 'figure'),
    Output('sales_returns_chart', 'figure'),
    Input('country_dropdown', 'value'),
    Input('month_dropdown', 'value'),
    Input('time_dropdown', 'value')
)

def update_dashboard(selected_country, selected_month, selected_time):

    # Make a copy of the full dataframe
    filtered_df = df.copy()

    # Filter by country if a country is selected
    if selected_country != 'All':
        filtered_df = filtered_df[filtered_df['Country'] == selected_country]

    # Filter by month if a month is selected
    if selected_month != 'All':
        filtered_df = filtered_df[filtered_df['YearMonth'] == selected_month]

    # Filter by time of day if selected
    if selected_time != 'All':
        filtered_df = filtered_df[filtered_df['Invoice_Time_of_Day'] == selected_time]


    # --------------------------------------------------------
    # KPI CALCULATIONS
    # --------------------------------------------------------

    # Calculate positive sales only
    total_sales = filtered_df[filtered_df['Total_Sales'] > 0]['Total_Sales'].sum()

    # Count unique invoices
    total_invoices = filtered_df['InvoiceNo'].nunique()

    # Count known customers only
    total_customers = filtered_df[
        filtered_df['CustomerID_Label'] != 'Unknown Customer'
    ]['CustomerID_Label'].nunique()

    # Count cancelled orders
    total_cancelled = filtered_df['Cancelled_Order_Flag'].sum()


    # Create reusable KPI card function
    def create_kpi_card(title, value):

        return html.Div(

            style={
                'width': '25%',
                'backgroundColor': 'white',
                'padding': '20px',
                'borderRadius': '10px',
                'textAlign': 'center',
                'boxShadow': '0px 2px 5px rgba(0,0,0,0.1)'
            },

            children=[
                html.H4(title, style={'color': '#555555'}),
                html.H2(value, style={'color': '#1f2c56'})
            ]
        )


    # Create KPI cards
    kpi_cards = [

        create_kpi_card(
            "Total Sales",
            f"${total_sales:,.2f}"
        ),

        create_kpi_card(
            "Total Invoices",
            f"{total_invoices:,}"
        ),

        create_kpi_card(
            "Known Customers",
            f"{total_customers:,}"
        ),

        create_kpi_card(
            "Returns / Cancellations",
            f"{total_cancelled:,}"
        )
    ]


    # --------------------------------------------------------
    # CHART 1: TOP 10 COUNTRIES BY TOTAL SALES
    # --------------------------------------------------------

    # Group total sales by country
    country_sales = (
        filtered_df[filtered_df['Total_Sales'] > 0]
        .groupby('Country', as_index=False)['Total_Sales']
        .sum()
        .sort_values('Total_Sales', ascending=False)
        .head(10)
    )

    # Create horizontal bar chart
    country_fig = px.bar(
        country_sales,
        x='Total_Sales',
        y='Country',
        orientation='h',
        title='Top 10 Countries by Total Sales',
        text='Total_Sales'
    )

    # Make the largest country appear at the top
    country_fig.update_layout(yaxis={'categoryorder': 'total ascending'})

    # Format labels
    country_fig.update_traces(texttemplate='%{text:,.2f}', textposition='outside')


    # --------------------------------------------------------
    # CHART 2: MONTHLY SALES TREND
    # --------------------------------------------------------

    # Group total sales by month
    monthly_sales = (
        filtered_df[filtered_df['Total_Sales'] > 0]
        .groupby('YearMonth', as_index=False)['Total_Sales']
        .sum()
        .sort_values('YearMonth')
    )

    # Create line chart
    monthly_fig = px.line(
        monthly_sales,
        x='YearMonth',
        y='Total_Sales',
        markers=True,
        title='Monthly Sales Trend'
    )


    # --------------------------------------------------------
    # CHART 3: TOP 10 PRODUCTS BY QUANTITY SOLD
    # --------------------------------------------------------

    # Use only positive quantity rows for sold products
    product_sales = (
        filtered_df[filtered_df['Quantity'] > 0]
        .groupby('Description', as_index=False)['Quantity']
        .sum()
        .sort_values('Quantity', ascending=False)
        .head(10)
    )

    # Create horizontal bar chart
    product_fig = px.bar(
        product_sales,
        x='Quantity',
        y='Description',
        orientation='h',
        title='Top 10 Products by Quantity Sold',
        text='Quantity'
    )

    # Make largest product appear at the top
    product_fig.update_layout(yaxis={'categoryorder': 'total ascending'})

    # Format labels
    product_fig.update_traces(texttemplate='%{text:,.0f}', textposition='outside')


    # --------------------------------------------------------
    # CHART 4: SALES VS RETURNS/CANCELLATIONS
    # --------------------------------------------------------

    # Calculate total positive sales
    sales_value = filtered_df[filtered_df['Total_Sales'] > 0]['Total_Sales'].sum()

    # Calculate absolute value of negative sales
    returns_value = abs(filtered_df[filtered_df['Total_Sales'] < 0]['Total_Sales'].sum())

    # Create dataframe for chart
    sales_returns_df = pd.DataFrame({
        'Transaction_Type': ['Sales', 'Returns/Cancellations'],
        'Amount': [sales_value, returns_value]
    })

    # Create pie chart
    sales_returns_fig = px.pie(
        sales_returns_df,
        names='Transaction_Type',
        values='Amount',
        title='Sales vs Returns/Cancellations Impact',
        hole=0.35
    )


    # --------------------------------------------------------
    # RETURN UPDATED DASHBOARD OBJECTS
    # --------------------------------------------------------

    return kpi_cards, country_fig, monthly_fig, product_fig, sales_returns_fig


# ------------------------------------------------------------
# 6. RUN THE DASHBOARD
# ------------------------------------------------------------

if __name__ == '__main__':

    # Small pause before opening browser
    time.sleep(1.0)

    # Open the dashboard automatically
    webbrowser.open_new("http://127.0.0.1:8050/")

    # Run the Dash app
    app.run(debug=True, port=8050)