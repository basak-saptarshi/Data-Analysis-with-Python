# 📊 Page View Time Series Visualizer

A data visualization project built using **Python, Pandas, Matplotlib, and Seaborn** as part of the **FreeCodeCamp Data Analysis with Python Certification**.

This project analyzes daily page view data from the freeCodeCamp forum and visualizes trends using different types of charts.

---

## 📌 Project Overview

The dataset contains the number of daily page views on the freeCodeCamp forum between **May 9, 2016** and **December 3, 2019**.

The data is first cleaned by removing the top and bottom **2.5%** of page views to eliminate outliers. Three different visualizations are then created to analyze long-term trends and seasonal patterns.

---

## 📈 Visualizations

### 1. Line Plot
- Displays daily forum page views over time.
- Helps identify overall growth trends.

### 2. Bar Plot
- Shows average monthly page views grouped by year.
- Useful for comparing monthly traffic across different years.

### 3. Box Plots
- **Year-wise Box Plot:** Shows yearly trends and distribution.
- **Month-wise Box Plot:** Highlights seasonal variations throughout the year.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```text
page-view-time-series-visualizer/
│
├── fcc-forum-pageviews.csv
├── time_series_visualizer.py
├── line_plot.png
├── bar_plot.png
├── box_plot.png
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/page-view-time-series-visualizer.git
cd page-view-time-series-visualizer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python time_series_visualizer.py
```

The generated plots will be saved in the project directory as:

- `line_plot.png`
- `bar_plot.png`
- `box_plot.png`

---

## 📚 Dataset

- **Source:** freeCodeCamp
- **File:** `fcc-forum-pageviews.csv`

---

## 🎯 Learning Outcomes

This project demonstrates:

- Data cleaning using Pandas
- Time series analysis
- Data visualization with Matplotlib
- Statistical visualization using Seaborn
- Working with datetime objects
- Creating publication-quality plots

---

## 📄 License

This project was developed for educational purposes as part of the **FreeCodeCamp Data Analysis with Python** certification.
