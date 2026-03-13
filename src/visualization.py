import plotly.express as px
import matplotlib.pyplot as plt


def plot_with_plotly(data, x_column, y_column):
    # Create a scatter plot using Plotly
    fig = px.scatter(data, x=x_column, y=y_column, title='Scatter Plot with Plotly')
    fig.show()


def plot_with_matplotlib(data, x_column, y_column):
    # Create a scatter plot using Matplotlib
    plt.scatter(data[x_column], data[y_column])
    plt.title('Scatter Plot with Matplotlib')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()
