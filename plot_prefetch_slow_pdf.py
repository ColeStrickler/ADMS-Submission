import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("data/fig8_rocket_prefetch_reformat.csv")
df2 = pd.read_csv("data/fig8_rocket_prefetch_slow_2_reformat.csv")
df4 = pd.read_csv("data/fig8_rocket_prefetch_slow_4_reformat.csv")
df6 = pd.read_csv("data/fig8_rocket_prefetch_slow_6_reformat.csv")
df7 = pd.read_csv("data/fig8_rocket_prefetch_slow_7_reformat.csv")
df8 = pd.read_csv("data/fig8_rocket_prefetch_slow_8_reformat.csv")
df9 = pd.read_csv("data/fig8_rocket_prefetch_slow_9_reformat.csv")
df10 = pd.read_csv("data/fig8_rocket_prefetch_slow_10_reformat.csv")
df11 = pd.read_csv("data/fig8_rocket_prefetch_slow_11_reformat.csv")

# Strip column names to remove any extra spaces
df.columns = df.columns.str.strip()
df2.columns = df2.columns.str.strip()
df4.columns = df4.columns.str.strip()
df6.columns = df6.columns.str.strip()
df7.columns = df7.columns.str.strip()
df8.columns = df8.columns.str.strip()
df9.columns = df9.columns.str.strip()
df10.columns = df10.columns.str.strip()
df11.columns = df11.columns.str.strip()
# Convert 'RME Enabled' to string (ensure it's not boolean)
#df["RME Enabled"] = df["RME Enabled"].astype(str)

# Create a new grouping column that combines 'DB Organization' and 'RME Enabled'
#df["DB+RME"] = df["DB Organization"] + " (RME: " + df["RME Enabled"] + ")"

# Step 1: Get the value for "row RME: false"
#Step 1: Get the value for "row" in DB Organization, "False" in RME Enabled, and a specific Num Columns value


for i in range(1,12):
    reference_value = df[(df["DB Organization"] == "rme") &\
                        (df["Num Columns"] == i)]["Time(Cycles)"].iloc[0]
    print(reference_value)
    # Step 2: Normalize the "Time(Cycles)" column by dividing by the reference value
    #df["Normalized Time(Cycles)"] = df["Time(Cycles)"] / reference_value
    # Step 2: Normalize the "Time(Cycles)" column only for the rows that don't match the reference
    df.loc[(df["Num Columns"] == i) & 
           (df["DB Organization"] == "rme"), "Normalized Time(Cycles)"] = \
        df.loc[(df["Num Columns"] == i) & 
               (df["DB Organization"] == "rme"), "Time(Cycles)"] / reference_value

    df2.loc[(df2["Num Columns"] == i) & 
           (df2["DB Organization"] == "rme"), "Normalized Time(Cycles)"] = \
        df2.loc[(df2["Num Columns"] == i) & 
               (df2["DB Organization"] == "rme"), "Time(Cycles)"] / reference_value

    df4.loc[(df4["Num Columns"] == i) & 
           (df4["DB Organization"] == "rme"), "Normalized Time(Cycles)"] = \
        df4.loc[(df4["Num Columns"] == i) & 
               (df4["DB Organization"] == "rme"), "Time(Cycles)"] / reference_value
    
    df6.loc[(df6["Num Columns"] == i) & 
           (df6["DB Organization"] == "rme"), "Normalized Time(Cycles)"] = \
        df6.loc[(df6["Num Columns"] == i) & 
               (df6["DB Organization"] == "rme"), "Time(Cycles)"] / reference_value

    df7.loc[(df7["Num Columns"] == i) & 
           (df7["DB Organization"] == "rme"), "Normalized Time(Cycles)"] = \
        df7.loc[(df7["Num Columns"] == i) & 
               (df7["DB Organization"] == "rme"), "Time(Cycles)"] / reference_value
    
    df8.loc[(df8["Num Columns"] == i) & 
           (df8["DB Organization"] == "rme"), "Normalized Time(Cycles)"] = \
        df8.loc[(df8["Num Columns"] == i) & 
               (df8["DB Organization"] == "rme"), "Time(Cycles)"] / reference_value
    
    df9.loc[(df9["Num Columns"] == i) & 
           (df9["DB Organization"] == "rme"), "Normalized Time(Cycles)"] = \
        df9.loc[(df9["Num Columns"] == i) & 
               (df9["DB Organization"] == "rme"), "Time(Cycles)"] / reference_value

    df10.loc[(df10["Num Columns"] == i) & 
           (df10["DB Organization"] == "rme"), "Normalized Time(Cycles)"] = \
        df10.loc[(df10["Num Columns"] == i) & 
               (df10["DB Organization"] == "rme"), "Time(Cycles)"] / reference_value


    df11.loc[(df11["Num Columns"] == i) & 
           (df11["DB Organization"] == "rme"), "Normalized Time(Cycles)"] = \
        df11.loc[(df11["Num Columns"] == i) & 
               (df11["DB Organization"] == "rme"), "Time(Cycles)"] / reference_value


# Step 3: Filter out rows where DB+RME is "row RME: false" (we don't want to plot this)
df_filtered =   df[df["DB Organization"] == "rme"]
df2_filtered =  df2[df2["DB Organization"] == "rme"]
df4_filtered =  df4[df4["DB Organization"] == "rme"]
df6_filtered =  df6[df6["DB Organization"] == "rme"]
df7_filtered =  df7[df7["DB Organization"] == "rme"]
df8_filtered =  df8[df8["DB Organization"] == "rme"]
df9_filtered =  df9[df9["DB Organization"] == "rme"]
df10_filtered = df10[df10["DB Organization"] == "rme"]
df11_filtered =  df11[df11["DB Organization"] == "rme"]


df_filtered["Clock"] = "1000 MHz"
df2_filtered["Clock"] = "500 MHz"
df4_filtered["Clock"] = "250 MHz"
df6_filtered["Clock"] = "167 MHz"
df7_filtered["Clock"] = "142 MHz"
df8_filtered["Clock"] = "125 MHz"
df9_filtered["Clock"] = "111 MHz"
df10_filtered["Clock"] = "100 MHz"
df11_filtered["Clock"] = "91 MHz"

combined_df = pd.concat([
    df_filtered,
    df2_filtered,
    df4_filtered,
    df6_filtered,
    df7_filtered,
    df8_filtered,
    df9_filtered,
    df10_filtered,
    #df11_filtered,
], ignore_index=True)

print(combined_df)


# BW styles
palette = ["gray", "white", "lightgray", "gray", "white",  "lightgray", "gray", "black"]
edge =    ["black", "black", "black",    "black", "black",  "black", "black", "black"]
hatches = ["", "xx", "/", "xx", "/", "", "/", ""] # hatch per hue
sns.set(style="ticks", context="paper")

# Plot
fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
barplot = sns.barplot(
    x="Num Columns",
    y="Normalized Time(Cycles)",
    hue="Clock",
    data=combined_df,
    palette=palette,
    ax=ax,
    edgecolor="black"
)

# Set hatching per hue group
# Each hue gets len(x) bars, grouped together
num_column_sizes = df_filtered["Column Size"].nunique()
for i, bar_container in enumerate(barplot.containers):
    for bar in bar_container:
        bar.set_facecolor(palette[i])
        bar.set_edgecolor(edge[i])
        bar.set_hatch(hatches[i])


handles, labels = ax.get_legend_handles_labels()
for i, (patch, hatch) in enumerate(zip(handles, hatches)):
    bar.set_facecolor(palette[i])
    bar.set_edgecolor(edge[i])
    patch.set_hatch(hatches[i])

# Add horizontal line at y=1.0
plt.axhline(y=1.0, color="black", linestyle="-", linewidth=2)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylim((0.0, 2.5))
# Format axes and legend
ax.set_xlabel("# Projected Columns", fontsize=22, weight="bold")
ax.set_ylabel("Normalized Exec. Time", fontsize=22, weight="bold")
ax.tick_params(axis='both', which='major', labelsize=22)
ax.legend(
    fontsize=16,
    title_fontsize=24,
    frameon=False,
    loc="upper center",              # place it at the top center
    bbox_to_anchor=(0.5, 1.00),      # shift it above the plot
    ncol=4,                           # number of columns for compact display
    borderaxespad=0,
)

plt.tight_layout()
out_file = "image/plot_prefetch_slow_crop.pdf"
plt.savefig(out_file)
plt.close()
#os.system(f"pdfcrop {out_file} {out_file}")
