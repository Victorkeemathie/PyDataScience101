# Matplotlib is a widely used plotting library in Python that provides a comprehensive set of tools for creating various types of plots and visualizations. 

# 1. Line Plot

# Different parameters for a Lineplot

# plt.plot(x, y, color='red')
# plt.plot(x, y, linestyle='--')
# plt.plot(x, y, linewidth=2)
# plt.plot(x, y, marker='o')
# plt.plot(x, y, marker='o', markersize=5)
# plt.plot(x, y, label='data')
# plt.legend()
# plt.title('My Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.xlim(0, 10)
# plt.ylim(-5, 5)
# plt.grid(True)

import matplotlib.pyplot as plt
from matplotlib import style
#style.use('ggplot')
#style.use('bmh')
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 6, 8]
# Plot the values of x and y using a line plot
plt.plot(x, y)
# Add labels to the x-axis and y-axis
plt.xlabel('x')
plt.ylabel('y')
# Add a title to the plot
plt.title('Line Plot')
# Display the plot
plt.show()

# Example 2:
# Import the pyplot module from the matplotlib library
import matplotlib.pyplot as plt  
from matplotlib import style
#style.use('classic')
# Import the numpy library and assign it an alias "np"
import numpy as np  
# Create an array of 100 values evenly spaced between 0 and 2*pi
x = np.linspace(0, 2*np.pi, 100)  
# Calculate the sine of each value in the array
y = np.sin(x)  
# Plot the values of x and y using a line plot
plt.plot(x, y)  
# Set the label for the x-axis
plt.xlabel('x')  
# Set the label for the y-axis
plt.ylabel('y')  
# Set the title for the plot
plt.title('Line Plot') 
 # Display the plot 
plt.show() 

# 2. Scatter Plot
 # Import the pyplot module from the matplotlib library
import matplotlib.pyplot as plt 
from matplotlib import style
#style.use('dark_background')
# Import the numpy library and assign it an alias "np"
import numpy as np  
# Generate an array of 100 random numbers between 0 and 1 for the x-coordinates
x = np.random.rand(100)  
# Generate an array of 100 random numbers between 0 and 1 for the y-coordinates
y = np.random.rand(100)
# Generate an array of 100 random numbers between 0 and 1 for the colors  
colors = np.random.rand(100) 
# Generate an array of 100 random numbers between 0 and 1, and scale them by 1000 for the sizes 
sizes = 1000 * np.random.rand(100)  
 # Create a scatter plot using the x and y coordinates, with colors and sizes specified
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5) 
# Set the label for the x-axis
plt.xlabel('x')  
# Set the label for the y-axis
plt.ylabel('y')  
# Set the title for the plot
plt.title('Scatter Plot') 
 # Display the plot 
plt.show() 

# Example 2:
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
# Set the style to "seaborn"
#style.use('seaborn')
# Create a sample DataFrame
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 1, 6, 8],
    'color': ['red', 'blue', 'green', 'yellow', 'purple'],
    'size': [30, 50, 20, 40, 60]
}

df = pd.DataFrame(data)

# Create a scatter plot using the DataFrame columns
plt.scatter(df['x'], df['y'], c=df['color'], s=df['size'])

# Set labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot with Pandas DataFrame')

# Show the plot
plt.show()


# 3. Bar Plot
import matplotlib.pyplot as plt
# Define the categories for the x-axis
categories = ['A', 'B', 'C', 'D']  
# Define the corresponding values for the y-axis
values = [25, 50, 75, 100]  
# Create a bar plot using the categories and values
plt.bar(categories, values)  
# Set the label for the x-axis
plt.xlabel('Category')
# Set the label for the y-axis  
plt.ylabel('Value')
# Set the title for the plot  
plt.title('Bar Plot')
# Display the plot  
plt.show()  

# Example 2:
import pandas as pd
import matplotlib.pyplot as plt
# Create a dataframe
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [25, 50, 75, 100]}
df = pd.DataFrame(data)

# Create a bar plot using the dataframe
df.plot(x='Category', y='Value', kind='bar', color='red')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Plot')
plt.show()

# 4. Histogram
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # Generate an array of 1000 random numbers from a standard normal distribution

plt.hist(data, bins=30)  # Create a histogram using the data with 30 bins
plt.xlabel('Value')  # Set the label for the x-axis
plt.ylabel('Frequency')  # Set the label for the y-axis
plt.title('Histogram')  # Set the title for the plot
plt.show()  # Display the plot

# Example 2:
import pandas as pd
import matplotlib.pyplot as plt

# Create a pandas DataFrame with custom data
data = {'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]}
df = pd.DataFrame(data)

# Define custom bin sizes
bins = [20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create a histogram using the DataFrame and custom bin sizes
plt.hist(df['Age'], bins=bins)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()


# 5. Pie Chart
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataframe
data = {'Sizes': [30, 40, 20, 10],
        'Labels': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)

# Create a pie chart using the dataframe
df.plot.pie(y='Sizes', labels=df['Labels'], autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

# 6. Box Plot
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataframe
data = {'Value': pd.Series(np.random.randn(100))}
df = pd.DataFrame(data)

# Create a box plot using the dataframe
df.plot.box()
plt.ylabel('Value')
plt.title('Box Plot')
plt.show()

# In matplotlib.pyplot, there are various markers available that you can use to indicate individual data points in your plots. 
# Here are some commonly used markers:

# '.' - Point marker
# 'o' - Circle marker
# 'v' - Downward-pointing triangle marker
# '^' - Upward-pointing triangle marker
# '<' - Left-pointing triangle marker
# '>' - Right-pointing triangle marker
# 's' - Square marker
# 'p' - Pentagon marker
# '*' - Star marker
# '+' - Plus marker
# 'x' - Cross marker
# 'D' - Diamond marker
# 'd' - Thin diamond marker
# 'h' - Hexagon1 marker
# 'H' - Hexagon2 marker
# '|' - Vertical line marker
# '_' - Horizontal line marker

# In matplotlib.pyplot, there are various linestyles available that you can use to specify the style of lines in your plots. 
# Here are some commonly used linestyles:

# '-' - Solid line
# '--' - Dashed line
# '-.' - Dash-dot line
# ':' - Dotted line
# 'None' or ' ': No line (useful when you only want markers'


# In matplotlib.pyplot, you can specify different colors using color abbreviations or predefined color names. 
# Here are some commonly used color abbreviations
# 'b' - Blue
# 'g' - Green
# 'r' - Red
# 'c' - Cyan
# 'm' - Magenta
# 'y' - Yellow
# 'k' - Black
# 'w' - White
# 'navy' - Navy blue
# 'lime' - Lime green
# 'maroon' - Maroon
# 'teal' - Teal
# 'purple' - Purple
# 'gold' - Gold
# 'silver' - Silver

# Here's a list of 15 different styles that can be used with matplotlib using the style.use() function:
# 'bmh': Bayesian Methods for Hackers style
# 'ggplot': The style used by the popular R package ggplot2
# 'seaborn': The default style of the seaborn library
# 'fivethirtyeight': The visual style of the website FiveThirtyEight
# 'dark_background': A dark theme with dark background and light-colored lines and markers
# 'grayscale': A grayscale style with black lines and markers on a white background
# 'classic': The classic matplotlib style
# 'Solarize_Light2': A light-colored style similar to the Solarized theme
# 'fast': A minimalistic style optimized for fast rendering
# 'tableau-colorblind10': A style using Tableau's color palette for colorblindness
# 'seaborn-darkgrid': A dark grid-based style from seaborn
# 'seaborn-whitegrid': A white grid-based style from seaborn
# 'seaborn-ticks': A style with ticks from seaborn
# 'seaborn-poster': A style optimized for creating poster-sized plots with seaborn
# 'classic + bmh': A combination of the classic and Bayesian Methods for Hackers styles

# xlim: This parameter is used to set the limits of the x-axis. It takes a tuple (xmin, xmax)
# plt.xlim(0, 10)  # Set the x-axis limits from 0 to 10

# ylim is used to set the limits of the y-axis
# plt.ylim(-5, 5)  # Set the y-axis limits from -5 to 5

# xticks: This parameter is used to control the locations of the tick marks on the x-axis
# plt.xticks([0, 1, 2, 3, 4])  # Set tick marks at specific x-axis positions

# yticks controls the locations of the tick marks on the y-axis
# plt.yticks([-2, -1, 0, 1, 2])  # Set tick marks at specific y-axis positions
