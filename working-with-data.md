# Working with Data

The canonical notebook job, and this
guide's running example: a file of
data on the disk, and questions to
ask it. The data is `weather.csv` —
thirty rows of invented daily weather
readings for June 2026: a date, a high
and a low in degrees Celsius, and the
day's rain in millimetres. The tool
for asking is **pandas**, the Python
library for tables; Jupyter itself is
table-agnostic, and everything in
this chapter is pandas wearing a
notebook, which is how most real
notebook work looks.

## Loading

```python
import pandas as pd

df = pd.read_csv("weather.csv", parse_dates=["date"])
df.head()
```

`read_csv` returns a **DataFrame** —
a table with named columns and one
row per reading. Two habits are built
into these three lines. The data file
is named *relative to the notebook*,
so the pair travels together; and
`parse_dates` turns the date column
into real dates at load time, because
every question worth asking a diary
involves time, and text that looks
like a date answers none of them.

The cell ends with the bare name of
nothing but `df.head()` — a call whose
value is the table's first five rows.
In a notebook, the value of a cell's
last expression is its result, and
the notebook displays it. For a
DataFrame, the display is a rendered
table (chapter 7 takes that apart).
In a plain Python program the same
line would compute five rows and
throw them away in silence: notebooks
reward ending cells with the thing
you want to *see*.

## Asking questions

The lab notebook's second code cell
asks five small questions and prints
the answers:

```python
hottest = df.loc[df["high_c"].idxmax()]
print(f"Days of readings: {len(df)}")
print(f"Hottest day: {hottest['date'].date()} at {hottest['high_c']} C")
print(f"Mean high: {df['high_c'].mean():.1f} C")
print(f"Total rain: {df['rain_mm'].sum():.1f} mm")
print(f"Rainy days (1 mm or more): {(df['rain_mm'] >= 1).sum()}")
```

```
Days of readings: 30
Hottest day: 2026-06-21 at 33 C
Mean high: 27.3 C
Total rain: 39.4 mm
Rainy days (1 mm or more): 7
```

These are the answers the lab later
checked against an independent
recount straight from the CSV
(transcript t01) — they matched, and
the checking is part of the method,
not a garnish: a notebook computes
cheerfully and says nothing about
whether it computed the right thing.

Reading the questions themselves:
`df["high_c"]` is one column;
`.mean()`, `.sum()` are column
answers; `(df["rain_mm"] >= 1)` is a
column of true/false answers whose
`.sum()` counts the trues; and
`.idxmax()` finds *where* the largest
high lives so `.loc[...]` can fetch
its whole row — the difference
between knowing the hottest *value*
and knowing the hottest *day*.

## Grouping

The last cell groups the month into
rough weeks and averages each:

```python
df["week"] = (df["date"].dt.day - 1) // 7 + 1
weekly = df.groupby("week")[["high_c", "low_c", "rain_mm"]].mean()
print(weekly.round(1).to_string())
```

```
      high_c  low_c  rain_mm
week
1       25.0   14.3     1.7
2       28.0   16.4     0.8
3       28.3   16.6     0.0
4       28.0   17.1     3.1
5       27.0   16.5     0.2
```

`groupby` is the spreadsheet's pivot
table as a line of code: split the
rows by a key, compute per group.
Note the first line *adds a column*
to `df` — a mutation of state the
kernel now holds. Run this cell twice
and nothing changes (the week of a
day is the week of a day); run a
variant that divides a column by ten
in place, twice, and your data is a
hundredth of itself with no error
anywhere. Notebooks make such
mutations easy and invisible, which
is chapter 8's territory; the defence
is the same there as here: cells that
can be re-run safely, and a
restart-and-run-all before you
believe the answers.
