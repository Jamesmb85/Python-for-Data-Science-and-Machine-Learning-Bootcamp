#Seaborn Exercises
#
#Time to practice your new seaborn skills! Try to recreate the plots below (don't worry about color schemes, just the plot itself.)
#
#If you want to see the plots, just download the seaborn and matplotlib libraries and run the code below. Comment out other plots so they don't overlap

# The Data
#
# We will be working with a famous titanic data set for these exercises.
# Later on in the Machine Learning section of the course, we will revisit this data, and use it to predict survival rates of passengers.
# For now, we'll just focus on the visualization of the data with seaborn:


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
print(titanic.head())
print('\n')

# Exercises
#
# ** Recreate the plots below using the titanic dataframe. There are very few hints since most of the plots can be done with just one or two lines of code
# and a hint would basically give away the solution. Keep careful attention to the x and y labels for hints.**

# sns.jointplot(x='fare', y='age', data=titanic)

# sns.distplot(titanic['fare'], kde=False, bins=30, color='red')

# sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')

# sns.swarmplot(x='class', y='age', data=titanic, palette='Set2')

# sns.countplot(x = 'sex', data= titanic)

# sns.heatmap(titanic.corr(), cmap='coolwarm')
# plt.title('titanic.corr()')

# g = sns.FacetGrid(data=titanic, col= 'sex')
# g.map(plt.hist,'age')


#need this code to show the plots
plt.show()