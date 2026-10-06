import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add overweight column
df["overweight"] = (
    df["weight"] / ((df["height"] / 100) ** 2) > 25
).astype(int)

# Normalize cholesterol and glucose
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


def draw_cat_plot():
    """Generate and save the categorical plot."""

    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=[
            "active",
            "alco",
            "cholesterol",
            "gluc",
            "overweight",
            "smoke",
        ],
    )

    df_cat = (
        df_cat.value_counts(["cardio", "variable", "value"])
        .reset_index(name="total")
    )

    cat_plot = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
        order=[
            "active",
            "alco",
            "cholesterol",
            "gluc",
            "overweight",
            "smoke",
        ],
    )

    fig = cat_plot.fig
    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    """Generate and save the correlation heat map."""

    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 10))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax,
    )

    fig.savefig("heatmap.png")
    return fig


if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()
    print("Plots generated successfully!")
  
