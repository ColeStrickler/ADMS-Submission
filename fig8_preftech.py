import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("data/fig8_prefetch.csv")

# Strip column names to remove any extra spaces
df.columns = df.columns.str.strip()

# Convert 'RME Enabled' to string (ensure it's not boolean)
df["RME Enabled"] = df["RME Enabled"].astype(str)

# Create a new grouping column that combines 'DB Organization' and 'RME Enabled'
df["DB+RME"] = df["DB Organization"] + " (RME: " + df["RME Enabled"] + ")"

# Step 1: Get the value for "row RME: false"
#Step 1: Get the value for "row" in DB Organization, "False" in RME Enabled, and a specific Num Columns value


for i in range(1,12):
    reference_value = df[(df["DB Organization"] == "row") &
                        (df["RME Enabled"] == "False") &
                        (df["Num Columns"] == i)]["Time(Cycles)"].iloc[0]
    print(reference_value)
    # Step 2: Normalize the "Time(Cycles)" column by dividing by the reference value
    #df["Normalized Time(Cycles)"] = df["Time(Cycles)"] / reference_value
    # Step 2: Normalize the "Time(Cycles)" column only for the rows that don't match the reference
    df.loc[(df["Num Columns"] == i) & 
           (df["DB+RME"] != "row (RME: False)"), "Normalized Time(Cycles)"] = \
        df.loc[(df["Num Columns"] == i) & 
               (df["DB+RME"] != "row (RME: False)"), "Time(Cycles)"] / reference_value


# Step 3: Filter out rows where DB+RME is "row RME: false" (we don't want to plot this)
df_filtered = df[df["DB+RME"] != "row (RME: False)"]

# Step 4: Plot the normalized data
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Create the grouped bar chart with normalized values
sns.barplot(x="Num Columns", y="Normalized Time(Cycles)", hue="DB+RME", data=df_filtered)

# Add a horizontal black line at y=1.0 for row store normalization reference
plt.axhline(y=1.0, color="black", linestyle="-", linewidth=2, label="Row Store (RME: FALSE)")

# Labels and title
plt.ylim((0.0, 2.5))
plt.xlabel("# Enabled Columns")
plt.ylabel("Normalized Exec. Time (Cycles)")
plt.title("Fig 8 With Prefetchers")
plt.legend(title="DB Organization + RME")

# Show the plot
# Show the plot
plt.savefig("fig8_prefetch.png")
