import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("data/fig7_boom_reformat.csv")

# Strip column names to remove any extra spaces
df.columns = df.columns.str.strip()

# Convert 'RME Enabled' to string (ensure it's not boolean)
#df["RME Enabled"] = df["RME Enabled"].astype(str)

# Create a new grouping column that combines 'DB Organization' and 'RME Enabled'
#df["DB+RME"] = df["DB Organization"] + " (RME: " + df["RME Enabled"] + ")"

# Step 1: Get the value for "row RME: false"
#reference_value = df[(df["DB+RME"] == "row (RME: False)")]["Time(Cycles)"].iloc[0]

# Step 2: Normalize the "Time(Cycles)" column by dividing by the reference value
for i in [1, 2, 4, 8, 16]: # column sizes
    reference_value = df[(df["DB Organization"] == "row") &\
                        (df["Column Size"] == i)]["Time(Cycles)"].iloc[0]
    print(reference_value)
    # Step 2: Normalize the "Time(Cycles)" column by dividing by the reference value
    #df["Normalized Time(Cycles)"] = df["Time(Cycles)"] / reference_value
    # Step 2: Normalize the "Time(Cycles)" column only for the rows that don't match the reference
    df.loc[(df["Column Size"] == i) & 
           (df["DB Organization"] != "row"), "Normalized Time(Cycles)"] = \
        df.loc[(df["Column Size"] == i) & 
               (df["DB Organization"] != "row"), "Time(Cycles)"] / reference_value

# Step 3: Filter out rows where DB+RME is "row RME: false" (we don't want to plot this)
df_filtered = df[df["DB Organization"] != "row"]
# Use a black-and-white color palette with hatching for differentiation
bw_palette = ["#777777", "#000000"]  # dark gray, black
hatches = ["//", ""]  # hatching for different bar styles

# Step 4: Plot the normalized data
plt.figure(figsize=(12, 6), dpi=300)
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=2.0)  # Increase overall font scale

# Create the grouped bar chart with normalized values
sns.barplot(x="Column Size", y="Normalized Time(Cycles)", hue="DB Organization", data=df_filtered)
# Make tick labels bigger
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)


# Add a horizontal black line at y=1.0 for row store normalization reference
plt.axhline(y=1.0, color="black", linestyle="-", linewidth=2, label="row")

# Labels and title
plt.ylim((0.0, 2.0))
plt.xlabel("Column Size (bytes)", fontsize=18, fontweight="bold")
plt.ylabel("Normalized Exec. Time (Cycles)", fontsize=20, fontweight="bold")
#plt.title("Fig 7 Boom", fontsize=20, fontweight="bold")
plt.legend(title="DB Organization", fontsize=16, title_fontsize=16)

# Show the plot
plt.savefig("image/fig7_boom.png")
