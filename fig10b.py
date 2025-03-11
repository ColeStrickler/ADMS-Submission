import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("data/fig10b.csv")

# Strip column names to remove any extra spaces
df.columns = df.columns.str.strip()

# Convert 'RME Enabled' to string (ensure it's not boolean)
df["RME Enabled"] = df["RME Enabled"].astype(str)
df["Row Size"] = df["Row Size"].astype(str)

# Create a new grouping column that combines 'DB Organization' and 'RME Enabled'
df["DB+RME"] = df["DB Organization"] + " (RME: " + df["RME Enabled"] + ")"

# Step 1: Get the value for "row RME: false"
reference_value = df[(df["DB+RME"] == "row (RME: False)")]["Time(Cycles)"].iloc[0]

# Step 2: Normalize the "Time(Cycles)" column by dividing by the reference value
for i in [16, 32, 64, 128, 256]: # row sizes
    reference_value = df[(df["DB Organization"] == "row") &
                        (df["RME Enabled"] == "False") &
                        (df["Row Size"] == f"{i}")]["Time(Cycles)"].iloc[0]
    print(reference_value)
    # Step 2: Normalize the "Time(Cycles)" column by dividing by the reference value
    #df["Normalized Time(Cycles)"] = df["Time(Cycles)"] / reference_value
    # Step 2: Normalize the "Time(Cycles)" column only for the rows that don't match the reference
    df.loc[(df["Row Size"] == f"{i}") & 
           (df["DB+RME"] != "row (RME: False)"), "Normalized Time(Cycles)"] = \
        df.loc[(df["Row Size"] == f"{i}") & 
               (df["DB+RME"] != "row (RME: False)"), "Time(Cycles)"] / reference_value

# Step 3: Filter out rows where DB+RME is "row RME: false" (we don't want to plot this)
df_filtered = df[df["DB+RME"] != "row (RME: False)"]

# Step 4: Plot the normalized data
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Create the grouped bar chart with normalized values
sns.barplot(x="Row Size", y="Normalized Time(Cycles)", hue="DB+RME", data=df_filtered)

# Add a horizontal black line at y=1.0 for row store normalization reference
plt.axhline(y=1.0, color="black", linestyle="-", linewidth=2, label="Row Store (RME: FALSE)")

# Labels and title
plt.ylim((0.0, 1.5))
plt.xlabel("Row Size (bytes)")
plt.ylabel("Normalized Exec. Time (Cycles)")
plt.title("Figure 10b")
plt.legend(title="DB Organization + RME")

# Show the plot
plt.savefig("fig10b.png", dpi=300, bbox_inches='tight')