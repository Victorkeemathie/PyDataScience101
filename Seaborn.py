# Seaborn
# Seaborn is a popular Python library for data visualization that is built on top of matplotlib
# It creates a a high-level interface for creating attractive and informative statistical graphs

# Examples:

# 1. Scatter Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('dark_background')

# Generate example data
tips = sns.load_dataset("tips")

# Create scatter plot
sns.scatterplot(data=tips, x="total_bill", y="tip", color='green', marker='s')

# Display the plot
plt.show()

# 2. Line Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('seaborn-whitegrid')

# Generate example data
flights = sns.load_dataset("flights")

# Create line plot
sns.lineplot(data=flights, x="year", y="passengers", color='blue', linestyle='--')

# Display the plot
plt.show()


# 3. Bar Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('ggplot')

# Generate example data
titanic = sns.load_dataset("titanic")

# Create bar plot
sns.barplot(data=titanic, x="class", y="fare", color='purple', hatch='//')

# Display the plot
plt.show()

# 4. Histogram
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('seaborn')

# Generate example data
iris = sns.load_dataset("iris")

# Create histogram
sns.histplot(data=iris, x="sepal_length", color='orange', edgecolor='black')

# Display the plot
plt.show()


# 5. Box Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('fivethirtyeight')

# Generate example data
tips = sns.load_dataset("tips")

# Create box plot
sns.boxplot(data=tips, x="day", y="total_bill", color='red', linewidth=2)

# Display the plot
plt.show()


# 6. Heatmap

import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('bmh')

# Generate example data
flights = sns.load_dataset("flights")

# Pivot the data to create the desired format for the heatmap
flights = flights.pivot(index="month", columns="year", values="passengers")

# Create heatmap
sns.heatmap(data=flights, annot=True, cmap="YlGnBu", linewidths=0.5)

# Display the plot
plt.show()

# 7. Scatter Plot with Regression Line

import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('dark_background')

# Generate example data
tips = sns.load_dataset("tips")

# Create scatter plot with regression line
sns.lmplot(data=tips, x="total_bill", y="tip", line_kws={'color': 'purple', 'linestyle': '--'}, scatter_kws={'color': 'orange', 'marker': 's'})

# Display the plot
plt.show()


# 8. Violin Plot
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('seaborn')

# Generate example data
tips = sns.load_dataset("tips")

# Create violin plot
sns.violinplot(data=tips, x="day", y="total_bill", palette="husl", linewidth=1)

# Display theplot
plt.show()


# 9. Pair Plot

import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('ggplot')

# Generate example data
iris = sns.load_dataset("iris")

# Create pair plot
sns.pairplot(data=iris, hue="species", palette="Set2", markers=["o", "s", "D"])

# Display the plot
plt.show()


# 10. Facet Grid
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('seaborn-whitegrid')

# Generate example data
tips = sns.load_dataset("tips")

# Create facet grid
g = sns.FacetGrid(data=tips, col="time", row="smoker")
g.map(sns.scatterplot, "total_bill", "tip")

# Display the plot
plt.show()

# 11. Swarm Plot
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('classic')

# Generate example data
titanic = sns.load_dataset("titanic")

# Create swarm plot
sns.swarmplot(data=titanic, x="class", y="age", hue="survived", palette=["red", "blue"], marker='D')

# Display the plot
plt.show()


# 12.  Joint Distribution Plot
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
plt.style.use('seaborn-white')

# Generate example data
iris = sns.load_dataset("iris")

# Create joint distribution plot
sns.jointplot(data=iris, x="sepal_length", y="sepal_width", kind="kde", fill=True, cmap="coolwarm", shade_lowest=False)

# Display the plot
plt.show()


# 13. 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy as sp

# Load the flights dataset from Seaborn library
database1 = sns.load_dataset("flights")

# Print the loaded dataset
print(database1)

# Create a categorical plot using Seaborn's catplot
sns.catplot(x="month", y='passengers', data=database1, kind='box')

# Display the plot
plt.show()


# 14
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy as sp

# Load the tips dataset from Seaborn library
database1 = sns.load_dataset('tips')

# Print the loaded dataset
print(database1)

# Create a joint plot using Seaborn's jointplot
sns.jointplot(x='tip', y='total_bill', data=database1)

# Display the plot
plt.show()

# 15





