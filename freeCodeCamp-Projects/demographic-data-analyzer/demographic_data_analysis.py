import pandas as pd


def demographic_data_analysis(data_file):
    """
    Analyze the Adult Census Income dataset using pandas.

    This program calculates:
    - Race distribution
    - Average age of men
    - Percentage of people with Bachelor's degrees
    - Percentage of high-income earners based on education level
    - Minimum work hours per week
    - Percentage of high-income earners among minimum-hour workers
    - Country with the highest percentage of high-income earners
    - Most common high-income occupation in India
    """

    # ==========================================================
    # Load Dataset
    # ==========================================================
    df = pd.read_csv(data_file)

    # ==========================================================
    # Race Distribution
    # ==========================================================
    race_count = df["race"].value_counts()

    # ==========================================================
    # Average Age of Men
    # ==========================================================
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(), 1
    )

    # ==========================================================
    # Percentage of Bachelor's Degree Holders
    # ==========================================================
    percentage_bachelors = round(
        (df[df["education"] == "Bachelors"].shape[0] / df.shape[0]) * 100,
        1
    )

    # ==========================================================
    # Higher vs Lower Education Income Analysis
    # ==========================================================
    higher_education = df[
        df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    ]

    lower_education = df[
        ~df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    ]

    higher_education_rich = round(
        (higher_education["salary"] == ">50K").mean() * 100,
        1
    )

    lower_education_rich = round(
        (lower_education["salary"] == ">50K").mean() * 100,
        1
    )

    # ==========================================================
    # Minimum Working Hours
    # ==========================================================
    min_work_hours = df["hours-per-week"].min()

    num_min_workers = df[
        df["hours-per-week"] == min_work_hours
    ].shape[0]

    rich_percentage = round(
        (
            df[
                (df["hours-per-week"] == min_work_hours)
                & (df["salary"] == ">50K")
            ].shape[0]
            / num_min_workers
        ) * 100,
        1
    )

    # ==========================================================
    # Country with Highest Percentage of High Earners
    # ==========================================================
    country_earnings = (
        df.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    highest_earning_country = country_earnings.idxmax()

    highest_earning_country_percentage = round(
        country_earnings.max(),
        1
    )

    # ==========================================================
    # Most Popular High-Income Occupation in India
    # ==========================================================
    top_IN_occupation = (
        df[
            (df["native-country"] == "India")
            & (df["salary"] == ">50K")
        ]["occupation"]
        .value_counts()
        .idxmax()
    )

    # ==========================================================
    # Display Results
    # ==========================================================
    print("=" * 60)
    print("        ADULT CENSUS INCOME DATA ANALYSIS")
    print("=" * 60)

    print("\nRace Distribution:")
    print(race_count)

    print(f"\nAverage age of men: {average_age_men} years")

    print(f"\nPercentage of people with Bachelor's degree: {percentage_bachelors}%")

    print(
        f"\nPercentage of higher education people earning >50K: "
        f"{higher_education_rich}%"
    )

    print(
        f"Percentage of lower education people earning >50K: "
        f"{lower_education_rich}%"
    )

    print(f"\nMinimum working hours per week: {min_work_hours} hours")

    print(
        f"Percentage of >50K earners among minimum-hour workers: "
        f"{rich_percentage}%"
    )

    print(
        f"\nCountry with highest percentage of >50K earners: "
        f"{highest_earning_country}"
    )

    print(
        f"Highest earning percentage: "
        f"{highest_earning_country_percentage}%"
    )

    print(
        f"\nMost common high-income occupation in India: "
        f"{top_IN_occupation}"
    )

    print("=" * 60)

    # Return results 
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }


if __name__ == "__main__":
    demographic_data_analysis("adult.data.csv")
