import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("data/fig7_cachelines.csv")
print(df)
# Strip column names to remove any extra spaces
df.columns = df.columns.str.strip()


# Step 2: Normalize the "Time(Cycles)" column by dividing by the reference value
for i in [1, 2, 4, 8, 16]: # column size
    reference_value = df[(df["Store"] == "row") &\
                        (df["Column Size"] == i)]["# Cache Lines"].iloc[0]
    print(reference_value)
    # Step 2: Normalize the "Time(Cycles)" column by dividing by the reference value
    #df["Normalized Time(Cycles)"] = df["Time(Cycles)"] / reference_value
    # Step 2: Normalize the "Time(Cycles)" column only for the rows that don't match the reference
    df.loc[(df["Column Size"] == i), 
           "# Cache Lines"] = \
        df.loc[(df["Column Size"] == i),
                "# Cache Lines"] / reference_value

# Step 3: Filter out rows where DB+RME is "row RME: false" (we don't want to plot this)
# Step 4: Plot the normalized data
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

# Create the grouped bar chart with normalized values
sns.barplot(x="Column Size", y="# Cache Lines", hue="Store", data=df)



# Labels and title
plt.ylim((0.0, 1.5))
plt.xlabel("Column Size (bytes)")
plt.ylabel("Normalized # Cache lines accessed")
plt.title("Fig 7 Cache lines accessed")
plt.legend(title="Organization")

# Show the plot
plt.show()

