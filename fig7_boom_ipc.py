import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("data/fig7_boom_reformat.csv")

# Strip column names to remove any extra spaces
df.columns = df.columns.str.strip()

# Step 1: Normalize 'Cache Lines Missed' for each column size relative to 'row' organization
for i in [1, 2, 4, 8, 16]:  # column sizes
    reference_value_row = df[(df["DB Organization"] == "row") & 
                        (df["Column Size"] == i)]["Time(Cycles)"].iloc[0]
    reference_value_col = df[(df["DB Organization"] == "col") & 
                        (df["Column Size"] == i)]["Time(Cycles)"].iloc[0]
    reference_value_rme = df[(df["DB Organization"] == "rme") & 
                        (df["Column Size"] == i)]["Time(Cycles)"].iloc[0]


    #print(f"Reference Cache Lines Missed for Column Size {i}: {reference_valu}")
    
    # Normalize 'Cache Lines Missed' for non-row organizations
    df.loc[(df["Column Size"] == i) & (df["DB Organization"] == "row"), "IPC"] = \
        df.loc[(df["Column Size"] == i) & (df["DB Organization"] == "row"), "InstRet"] / reference_value_row
    df.loc[(df["Column Size"] == i)& (df["DB Organization"] == "col"), "IPC"] = \
        df.loc[(df["Column Size"] == i) & (df["DB Organization"] == "col"), "InstRet"] / reference_value_col
    df.loc[(df["Column Size"] == i) & (df["DB Organization"] == "rme"), "IPC"] = \
        df.loc[(df["Column Size"] == i) & (df["DB Organization"] == "rme"), "InstRet"] / reference_value_rme


# Step 2: Filter out rows where DB Organization is 'row' (not plotted)
#df_filtered = df[df["DB Organization"] != "row"]

# Step 3: Plot the normalized cache lines missed
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Create the grouped bar chart for normalized cache lines missed
sns.barplot(x="Column Size", y="IPC", hue="DB Organization", data=df)

# Add a horizontal black line at y=1.0 for row store normalization reference
#plt.axhline(y=1.0, color="black", linestyle="-", linewidth=2, label="Row")

# Labels and title
plt.ylim((0.0, 1.5))
plt.xlabel("Column Size (bytes)")
plt.ylabel("IPC")
plt.title("Fig 7 Boom - IPC")
plt.legend(title="DB Organization")

# Save the plot
plt.savefig("image/fig7_boom_ipc.png")
plt.close()



