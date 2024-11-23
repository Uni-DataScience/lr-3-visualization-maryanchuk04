import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.

    Returns:
    Figure: Matplotlib Figure object containing the plot.
    """
    count = collections.Counter(data)
    categories = list(count.keys())
    counts = list(count.values())

    fig, ax = plt.subplots()
    ax.bar(categories, counts)

    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title('Category Distribution')

    return fig


data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
