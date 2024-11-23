import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.

    Returns:
    Figure: Matplotlib Figure object containing the scatter plot.
    """
    sns.set(style="whitegrid")

    fig, ax = plt.subplots()

    sns.scatterplot(data=data, x='x', y='y', ax=ax)

    ax.set_xlabel('X Variable')
    ax.set_ylabel('Y Variable')
    ax.set_title('Scatter Plot of X vs Y')

    ax.grid(True)

    fig.tight_layout()

    return fig

# Example data
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})
create_scatter_plot(data)
