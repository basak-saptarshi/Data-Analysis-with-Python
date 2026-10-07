import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    """
    Read the sea level dataset, create a scatter plot with two
    lines of best fit, save the figure, and return the figure object.
    """

    # Read the dataset
    df = pd.read_csv("epa-sea-level.csv")

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Scatter plot of the original data
    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"],
        s=10,
        color="#89CBE1",
        alpha=0.5,
        marker="o",
        label="Observed Data"
    )

    # --------------------------------------------------
    # First line of best fit (1880–2050)
    # --------------------------------------------------
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    x = pd.Series(range(1880, 2051))

    ax.plot(
        x,
        slope * x + intercept,
        color="green",
        linewidth=2,
        label="Best Fit (1880–2050)"
    )

    # --------------------------------------------------
    # Second line of best fit (2000–2050)
    # --------------------------------------------------
    df_recent = df[df["Year"] >= 2000]

    slope, intercept, r_value, p_value, std_err = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    x_recent = pd.Series(range(2000, 2051))

    ax.plot(
        x_recent,
        slope * x_recent + intercept,
        color="red",
        linewidth=2,
        label="Best Fit (2000–2050)"
    )

    # Add title and labels
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    # Display legend and grid
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.3)

    # Adjust layout
    fig.tight_layout()

    # Save the figure
    fig.savefig("sea_level_plot.png", dpi=300)

    # Return the figure object
    return fig


if __name__ == "__main__":
    fig = draw_plot()
    plt.show()

