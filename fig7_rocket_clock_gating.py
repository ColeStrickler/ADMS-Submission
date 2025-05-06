import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("data/fig7_rocket_slow_reformat.csv")
df2 = pd.read_csv("data/fig7_rocket_reformat.csv")
# Strip column names to remove any extra spaces
df.columns = df.columns.str.strip()
df2.columns = df2.columns.str.strip()
# Convert 'RME Enabled' to string (ensure it's not boolean)
#df["RME Enabled"] = df["RME Enabled"].astype(str)

# Create a new grouping column that combines 'DB Organization' and 'RME Enabled'
#df["DB+RME"] = df["DB Organization"] + " (RME: " + df["RME Enabled"] + ")"

# Step 1: Get the value for "row RME: false"
#reference_value = df[(df["DB+RME"] == "row (RME: False)")]["Time(Cycles)"].iloc[0]

# Step 2: Normalize the "Time(Cycles)" column by dividing by the reference value
for i in [1, 2, 4, 8, 16]: # column sizes
    reference_value = df2[(df2["DB Organization"] == "rme") &\
                        (df2["Column Size"] == i)]["Time(Cycles)"].iloc[0]
    print(reference_value)
    # Step 2: Normalize the "Time(Cycles)" column by dividing by the reference value
    #df["Normalized Time(Cycles)"] = df["Time(Cycles)"] / reference_value
    # Step 2: Normalize the "Time(Cycles)" column only for the rows that don't match the reference
    df.loc[(df["Column Size"] == i) & 
           (df["DB Organization"] == "rme"), "Normalized Time(Cycles)"] = \
        df.loc[(df["Column Size"] == i) & 
               (df["DB Organization"] == "rme"), "Time(Cycles)"] / reference_value

# Step 3: Filter out rows where DB+RME is "row RME: false" (we don't want to plot this)
df_filtered = df[df["DB Organization"] != "row"]
df_filtered = df[df["DB Organization"] != "col"]

# Step 4: Plot the normalized data
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Create the grouped bar chart with normalized values
sns.barplot(x="Column Size", y="Normalized Time(Cycles)", hue="DB Organization", data=df_filtered)

# Add a horizontal black line at y=1.0 for row store normalization reference
plt.axhline(y=1.0, color="black", linestyle="-", linewidth=2)

# Labels and title
plt.ylim((0.0, 2.0))
plt.xlabel("Column Size (bytes)")
plt.ylabel("Slowdown")
plt.title("Fig 7 Rocket Clock Gating")
#plt.legend(title="DB Organization")

# Show the plot
plt.savefig("image/fig7_rocket_clock_gating.png")
