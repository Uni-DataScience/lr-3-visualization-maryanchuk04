import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def plot_1d(data):
    """
    Creates a 1D line plot for a sequence of values.

    Parameters:
    data (array-like): A sequence of numerical values.
    """
    plt.figure()
    plt.plot(data)
    plt.title('1D Line Plot')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

def plot_2d(x, y):
    """
    Creates a 2D scatter plot to show the relationship between two variables.

    Parameters:
    x (array-like): X-axis data.
    y (array-like): Y-axis data.
    """
    plt.figure()
    plt.scatter(x, y)
    plt.title('2D Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

def plot_3d(x, y, z):
    """
    Creates a 3D scatter plot to represent three-dimensional data points.

    Parameters:
    x (array-like): X-axis data.
    y (array-like): Y-axis data.
    z (array-like): Z-axis data.
    """
    from mpl_toolkits.mplot3d import Axes3D  # Import inside the function
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.set_title('3D Scatter Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.show()
# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
