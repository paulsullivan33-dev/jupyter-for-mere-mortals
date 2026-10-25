"""Build the lab notebook (unexecuted) with nbformat."""
import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {"display_name": "Python 3 (ipykernel)",
                   "language": "python", "name": "python3"},
    "language_info": {"name": "python"},
}

nb.cells = [
    nbf.v4.new_markdown_cell(
        "# Millbrook weather, June 2026\n"
        "\n"
        "A month of daily readings from a weather diary: each day's\n"
        "high and low in degrees Celsius, and the rain in millimetres.\n"
        "This notebook loads the diary from `weather.csv`, works out\n"
        "the shape of the month, and draws it."
    ),
    nbf.v4.new_code_cell(
        'import pandas as pd\n'
        'import matplotlib.pyplot as plt\n'
        '\n'
        'df = pd.read_csv("weather.csv", parse_dates=["date"])\n'
        'df.head()'
    ),
    nbf.v4.new_markdown_cell(
        "## The shape of the month\n"
        "\n"
        "Five numbers tell most of the story: how many days, the\n"
        "hottest one, the average high, and how the rain fell."
    ),
    nbf.v4.new_code_cell(
        'hottest = df.loc[df["high_c"].idxmax()]\n'
        'print(f"Days of readings: {len(df)}")\n'
        'print(f"Hottest day: {hottest[\'date\'].date()} at '
        '{hottest[\'high_c\']} C")\n'
        'print(f"Mean high: {df[\'high_c\'].mean():.1f} C")\n'
        'print(f"Total rain: {df[\'rain_mm\'].sum():.1f} mm")\n'
        'print(f"Rainy days (1 mm or more): {(df[\'rain_mm\'] >= 1).sum()}")'
    ),
    nbf.v4.new_markdown_cell(
        "## The month in one picture\n"
        "\n"
        "Highs and lows, day by day. The gap between the two lines\n"
        "is the day's swing; the hot spell in the third week and the\n"
        "wet break after it are both easy to see."
    ),
    nbf.v4.new_code_cell(
        'fig, ax = plt.subplots(figsize=(8, 3))\n'
        'ax.plot(df["date"], df["high_c"], marker="o", label="High")\n'
        'ax.plot(df["date"], df["low_c"], marker="o", label="Low")\n'
        'ax.set_ylabel("Degrees C")\n'
        'ax.legend()\n'
        'fig'
    ),
    nbf.v4.new_markdown_cell(
        "## Week by week\n"
        "\n"
        "The same month in four rough weeks (the last one is nine\n"
        "days; diaries are not tidy), averaged."
    ),
    nbf.v4.new_code_cell(
        'df["week"] = (df["date"].dt.day - 1) // 7 + 1\n'
        'weekly = df.groupby("week")[["high_c", "low_c", "rain_mm"]].mean()\n'
        'print(weekly.round(1).to_string())'
    ),
]

nbf.write(nb, "weather-lab.ipynb")
print("wrote weather-lab.ipynb with", len(nb.cells), "cells")
