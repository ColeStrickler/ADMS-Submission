import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from matplotlib.ticker import AutoMinorLocator
# Load CSV and clean
df = pd.read_csv("data/fig8_rocket_reformat.csv")
df.columns = df.columns.str.strip()
df["Column Size"] = df["Column Size"].astype(str)

# Normalize execution time
df["Normalized Time(Cycles)"] = 0.0


for i in range(1,12):
    reference_value = df[(df["DB Organization"] == "row") &\
                        (df["Num Columns"] == i)]["Time(Cycles)"].iloc[0]
    print(reference_value)
    # Step 2: Normalize the "Time(Cycles)" column by dividing by the reference value
    #df["Normalized Time(Cycles)"] = df["Time(Cycles)"] / reference_value
    # Step 2: Normalize the "Time(Cycles)" column only for the rows that don't match the reference
    df.loc[(df["Num Columns"] == i) & 
           (df["DB Organization"] != "row"), "Normalized Time(Cycles)"] = \
        df.loc[(df["Num Columns"] == i) & 
               (df["DB Organization"] != "row"), "Time(Cycles)"] / reference_value


df_filtered = df[df["DB Organization"] != "row"]

# BW styles
palette = ["black", "gray"]
hatches = ["//", ""]  # hatch per hue

sns.set(style="ticks", context="paper")

# Plot
fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
barplot = sns.barplot(
    x="Num Columns",
    y="Normalized Time(Cycles)",
    hue="DB Organization",
    data=df_filtered,
    palette=palette,
    ax=ax,
    edgecolor="black"
)

# Set hatching per hue group
# Each hue gets len(x) bars, grouped together
num_column_sizes = df_filtered["Column Size"].nunique()
for i, bar_container in enumerate(barplot.containers):
    for bar in bar_container:
        bar.set_hatch(hatches[i])

# Add horizontal line at y=1.0
plt.axhline(y=1.0, color="black", linestyle="-", linewidth=2, label="row")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylim((0.0, 3.5))
# Format axes and legend
ax.set_xlabel("# Enabled Columns", fontsize=22, weight="bold")
ax.set_ylabel("Normalized Exec. Time (Cycles)", fontsize=22, weight="bold")
ax.tick_params(axis='both', which='major', labelsize=22)
ax.legend(title="DB Organization", fontsize=20, title_fontsize=20, frameon=False)

plt.tight_layout()
out_file = "image/fig8_rocket_crop.pdf"
plt.savefig(out_file)
plt.close()
#os.system(f"pdfcrop {out_file} {out_file}")
