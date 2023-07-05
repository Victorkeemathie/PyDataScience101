# Matplotlib is a widely used plotting library in Python that provides a comprehensive set of tools for creating various types of plots and visualizations. 

# 1. Line Plot
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

