# For this capstone project we will be analyzing some 911 call data from Kaggle. The data contains the following fields:
#
# lat : String variable, Latitude
# lng: String variable, Longitude
# desc: String variable, Description of the Emergency Call
# zip: String variable, Zipcode
# title: String variable, Title
# timeStamp: String variable, YYYY-MM-DD HH:MM:SS
# twp: String variable, Township
# addr: String variable, Address
# e: String variable, Dummy variable (always 1)

#1)** Import numpy and pandas **
import numpy as np
import pandas as pd

#2)** Import visualization libraries and set %matplotlib inline. **
import matplotlib.pyplot as plt
import seaborn as sns

#3** Read in the csv file as a dataframe called df **
df = pd.read_csv('911.csv')

#4** Check the info() of the df **
print(df.info())
print('\n')

#5** Check the head of df **
print(df.head())
print('\n')


#Basic Questions
#6** What are the top 5 zipcodes for 911 calls? **
print(df['zip'].value_counts().head(5))
print('\n')

#7** What are the top 5 townships (twp) for 911 calls? **
print(df['twp'].value_counts().head(5))
print('\n')

#8** Take a look at the 'title' column, how many unique title codes are there? **
print(df['title'].nunique())
print('\n')


# Creating new features
#
# ** In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic.
# Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.**
#
# *For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS. *
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


#9** What is the most common Reason for a 911 call based off of this new column? **
print(df['Reason'].value_counts()  )
print('\n')

#10** Now use seaborn to create a countplot of 911 calls by Reason. **
sns.countplot(x = 'Reason', data= df)


#11** Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column? **
print(type(df['timeStamp'].iloc[0]))
print('\n')

#12** You should have seen that these timestamps are still strings. Use pd.to_datetime to convert the column from strings to DateTime objects. **
df['timeStamp'] = pd.to_datetime(df['timeStamp'])


#13 Use .apply() to create 3 new columns called Hour, Month, and Day of Week.
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


#14 ** Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week: **
# dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)


# 15** Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column. **
sns.countplot(x = 'Day of Week', data= df, hue='Reason')


#16 Now do the same for Month:
sns.countplot(x = 'Month', data= df, hue='Reason')


#17** Now create a groupby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation.
# Use the head() method on this returned DataFrame. **
byMonth = df.groupby('Month').count()
print(byMonth.head())
print('\n')

#18** Now create a simple plot off of the dataframe indicating the count of calls per month. **
byMonth['desc'].plot()


#19 ** Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you may need to reset the index to a column. **
sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())

# 20** Now let's move on to creating heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the
# Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an unstack method.
# Reference the solutions if you get stuck on this!**
dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
print(dayHour.head())
print('\n')

#21 ** Now create a HeatMap using this new DataFrame. **
sns.heatmap(dayHour, cmap='rocket')

#22 ** Now create a clustermap using this DataFrame. **
sns.clustermap(dayHour,cmap='viridis')

#23 ** Now repeat these same plots and operations, for a DataFrame that shows the Month as the column. **
dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
print(dayMonth.head())
sns.heatmap(dayMonth,cmap='viridis')
sns.clustermap(dayMonth,cmap='viridis')
print('\n')

#show all of the plots
plt.show()