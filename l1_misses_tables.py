import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
#dfboom = pd.read_csv("data/fig8_boom_reformat.csv")
#dfboom_pref = pd.read_csv("data/fig8_boom_prefetch_reformat.csv")
df = pd.read_csv("data/fig8_rocket_reformat.csv")
#dfrocket_pref = pd.read_csv("data/fig8_rocket_prefetch_reformat.csv")

# Strip column names to remove any extra spaces
#dfboom.columns = dfboom.columns.str.strip()
#dfboom_pref.columns = dfboom_pref.columns.str.strip()
df.columns = df.columns.str.strip()
#dfrocket_pref.columns = dfrocket_pref.columns.str.strip()

df_rme = df[df['DB Organization'] == 'rme']
df_col = df[df['DB Organization'] == 'col']
df_row = df[df['DB Organization'] == 'row']

# Extract LLC accesses
rme_llc = df_rme['llc-access'].reset_index(drop=True)
col_llc = df_col['llc-access'].reset_index(drop=True)
row_llc = df_row['llc-access'].reset_index(drop=True)

col_count = [col for col in range(1,12)]
row_labels = ['RME', 'Col', 'Row']
table_data = [rme_llc, col_llc, row_llc]




# Create a matplotlib table
fig, ax = plt.subplots()
ax.axis('off')  # hide axes

table = ax.table(
    cellText=table_data,
    rowLabels=row_labels,
    colLabels=col_count,
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.title('LLC Accesses per Study for Each DB Organization')
plt.show()