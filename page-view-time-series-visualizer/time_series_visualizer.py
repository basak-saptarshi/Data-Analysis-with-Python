import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset and use the date column as the index
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    parse_dates=["date"],
    index_col="date"
)

# Remove the top and bottom 2.5% of page views
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    """Draw a line plot of daily page views."""

    fig, ax = plt.subplots(figsize=(15, 5))

    ax.plot(df.index, df["value"], color="red", linewidth=1)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    """Draw a bar plot of average monthly page views grouped by year."""

    df_bar = df.copy()

    df_bar["Year"] = df_bar.index.year
    df_bar["Month"] = df_bar.index.strftime("%B")

    month_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    df_bar["Month"] = pd.Categorical(
        df_bar["Month"],
        categories=month_order,
        ordered=True
    )

    df_bar = (
        df_bar
        .groupby(["Year", "Month"])["value"]
        .mean()
        .unstack()
    )

    fig = df_bar.plot(
        kind="bar",
        figsize=(12, 8)
    ).figure

    ax = fig.axes[0]

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")

    fig.tight_layout()
    fig.savefig("bar_plot.png")

    return fig


def draw_box_plot():
    """Draw year-wise and month-wise box plots."""

    df_box = df.copy()
    df_box.reset_index(inplace=True)

    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")

    month_order = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    fig, axes = plt.subplots(1, 2, figsize=(18, 7))

    # Year-wise trend
    sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        ax=axes[0]
    )

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise seasonality
    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        order=month_order,
        ax=axes[1]
    )

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.tight_layout()
    fig.savefig("box_plot.png")

    return fig

if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()

    print("All plots have been generated successfully!")
