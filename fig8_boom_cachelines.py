import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("data/fig8_boom_reformat.csv")

# Strip column names to remove any extra spaces
df.columns = df.columns.str.strip()

# Step 1: Normalize 'Cache Lines Missed' for each column size relative to 'row' organization
for i in range(1,12):  # column sizes
    reference_value_miss = df[(df["DB Organization"] == "row") & 
                        (df["Num Columns"] == i)]["llc-out"].iloc[0]
    reference_value_access = df[(df["DB Organization"] == "row") & 
                        (df["Num Columns"] == i)]["llc-access"].iloc[0]

    print(f"Reference Cache Lines Missed for Column Size {i}: {reference_value_miss}")
    
    # Normalize 'Cache Lines Missed' for non-row organizations
    df.loc[(df["Num Columns"] == i) & 
           (df["DB Organization"] != "row"), "Cache Lines Miss(Normalized)"] = \
        df.loc[(df["Num Columns"] == i) & 
               (df["DB Organization"] != "row"), "llc-out"] / reference_value_miss

    # Normalize 'Cache Lines Missed' for non-row organizations
    df.loc[(df["Num Columns"] == i) & 
           (df["DB Organization"] != "row"), "Cache Lines Access(Normalized)"] = \
        df.loc[(df["Num Columns"] == i) & 
               (df["DB Organization"] != "row"), "llc-access"] / reference_value_access

        

# Step 2: Filter out rows where DB Organization is 'row' (not plotted)
df_filtered = df[df["DB Organization"] != "row"]
print(df_filtered)

# Step 3: Plot the normalized cache lines missed
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Create the grouped bar chart for normalized cache lines missed
sns.barplot(x="Num Columns", y="Cache Lines Miss(Normalized)", hue="DB Organization", data=df_filtered)

# Add a horizontal black line at y=1.0 for row store normalization reference
plt.axhline(y=1.0, color="black", linestyle="-", linewidth=2, label="Row")

# Labels and title
plt.ylim((0.0, 2.5))
plt.xlabel("Num Columns")
plt.ylabel("Normalized Cache Lines Missed")
plt.title("Fig 8 Boom - Normalized Cache Lines Missed")
plt.legend(title="DB Organization")

# Save the plot
plt.savefig("image/fig8_boom_cache_lines_missed.png")
plt.close()



# Step 4: Plot cache lines accessed (non-normalized, assuming you want raw values)
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Create the grouped bar chart for cache lines accessed
sns.barplot(x="Num Columns", y="Cache Lines Access(Normalized)", hue="DB Organization", data=df_filtered)
# Add a horizontal black line at y=1.0 for row store normalization reference
plt.axhline(y=1.0, color="black", linestyle="-", linewidth=2, label="Row")
plt.ylim((0.0, 4.5))
# Labels and title
plt.xlabel("Num Columns")
plt.ylabel("Cache Lines Accessed")
plt.title("Fig 8 Boom - Cache Lines Accessed")
plt.legend(title="DB Organization")

# Save the plot
plt.savefig("image/fig8_boom_cache_lines_accessed.png")
plt.close()