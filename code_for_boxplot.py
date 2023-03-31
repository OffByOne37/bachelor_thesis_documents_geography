import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('blah.csv')

# Group the data by algorithm
grouped = df.groupby('Algorithmus')

# Create a list of boxplot data for each column
data = []
for col in ['ACC', 'AUC', 'SE', 'SP', 'TSS', 'TS']:
    boxplot_data = []
    for name, group in grouped:
        boxplot_data.append(list(group[col].dropna()))
    data.append(boxplot_data)

# Set up the plot
fig, axes = plt.subplots(nrows=1, ncols=6, figsize=(24, 5))
fig.subplots_adjust(wspace=0.5) # Add some padding between subplots

# Add a boxplot to each axis
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
for i, ax in enumerate(axes.flatten()):
    box = ax.boxplot(data[i], patch_artist=True)
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
    # Add the letter label to the top left corner of each plot
    ax.set_title(chr(97+i) + ') ' + df.columns[i+1], loc='left')
    ax.set_xticklabels(grouped.groups.keys(), rotation=90)
    ax.set_ylabel(df.columns[i+1])
    
    # Set the y-axis limits for the last 5 boxplots to be the same
    if i > 0:
        ax.set_ylim(bottom=0.0, top=1.0)
        
    else:
        ax.set_ylim(bottom=70, top=100)

# Save the plot to a file
plt.savefig('boxplot.png')
