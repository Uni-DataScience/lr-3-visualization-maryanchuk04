import numpy as np
import pandas as pd
import plotly.express as px

def create_interactive_plotly(df):
    """
    Creates an interactive scatter plot using Plotly.

    Parameters:
    df (DataFrame): A DataFrame containing 'x' and 'y' columns.

    Returns:
    fig: A Plotly Figure object representing the interactive scatter plot.
    """
    fig = px.scatter(
        df,
        x='x',
        y='y',
        title='Interactive Scatter Plot of X vs Y',
        labels={'x': 'X-axis Label', 'y': 'Y-axis Label'},
    )

    fig.update_layout(
        title={'x': 0.5},
        legend_title_text='Legend',
    )

    fig.show()

    return fig

# Example data
df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})
create_interactive_plotly(df)
