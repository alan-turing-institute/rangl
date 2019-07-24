#!/usr/bin/env python


# %%
import matp lotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


# %%

df = pd.read_csv("data.csv")
df["A.targetTime"] = pd.to_datetime(df["A.targetTime"])

time = df["A.targetTime"]
keep = df.columns.str.contains("A.\d")
data = df.loc[:, keep]


fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(time, data, alpha=0.1)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H"))

plt.ylabel("Demand [standardised]")
plt.xlabel("Lead time [h]")
plt.savefig("demand_A.png", dpi=300)
