import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# Linear Regression Project
#
# Congratulations! You just got some contract work with an Ecommerce company based in New York City that sells clothing online but they also have in-store style
# and clothing advice sessions. Customers come in to the store, have sessions/meetings with a personal stylist, then they can go home
# and order either on a mobile app or website for the clothes they want.
#
# The company is trying to decide whether to focus their efforts on their mobile app experience or their website.
# They've hired you on contract to help them figure it out! Let's get started!
#
# Just follow the steps below to analyze the customer data (it's fake, don't worry I didn't give you real credit card numbers or emails).


#Get the Data
customers = pd.read_csv("Ecommerce Customers")

#Check the head of customers, and check out its info() and describe() methods.
print(customers.info())
print('\n')
print(customers.head())
print('\n')
print(customers.describe())

#Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns. Does the correlation make sense?
sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=customers)

#** Do the same but with the Time on App column instead. **
sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=customers)

#** Use jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.**
sns.jointplot(x='Time on App',y='Length of Membership',kind='hex',data=customers)

#Let's explore these types of relationships across the entire data set. Use pairplot to recreate the plot below.(Don't worry about the the colors
sns.pairplot(customers)

#Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?
#Length of Membership

#*Create a linear model plot (using seaborn's lmplot) of Yearly Amount Spent vs. Length of Membership. *
sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=customers)


# Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets.
# ** Set a variable X equal to the numerical features of the customers and a variable y equal to the "Yearly Amount Spent" column. **
from sklearn.model_selection import train_test_split
Y = customers['Yearly Amount Spent']
X = customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]

#** Use model_selection.train_test_split from sklearn to split the data into training and testing sets. Set test_size=0.3 and random_state=101**
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(X, Y, test_size=.30, random_state=101)

# Now its time to train our model on our training data!
# ** Import LinearRegression from sklearn.linear_model **
from sklearn.linear_model import LinearRegression

#Create an instance of a LinearRegression() model named LM.
LM = LinearRegression() #create an instance of the Linear Regression Model

#train/fit the model to the training data
LM.fit(X_TRAIN,Y_TRAIN)

#Print out the coefficients of the model
print(LM.coef_)

#** Use lm.predict() to predict off the X_test set of the data.**
predictions = LM.predict(X_TEST)
print('\n')
print(predictions)

#** Create a scatterplot of the real test values versus the predicted values. **
# plt.scatter(Y_TEST,predictions)
# plt.xlabel('Y Test')
# plt.ylabel('Predicted Y')


#** Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error. Refer to the lecture or to Wikipedia for the formulas**
from sklearn import metrics
print('\n')
print('MAE:', metrics.mean_absolute_error(Y_TEST, predictions))
print('MSE:', metrics.mean_squared_error(Y_TEST, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(Y_TEST, predictions)))


#Plot a histogram of the residuals and make sure it looks normally distributed. Use either seaborn distplot, or just plt.hist().
sns.distplot( (Y_TEST - predictions) , bins=50 )


# We still want to figure out the answer to the original question, do we focus our efforst on mobile app or website development?
# Or maybe that doesn't even really matter, and Membership Time is what is really important. Let's see if we can interpret the coefficients at all to get an idea.
# ** Recreate the dataframe below. **
coeffecients = pd.DataFrame(LM.coef_,X.columns)
coeffecients.columns = ['Coeffecient']
print(coeffecients)

# ** How can you interpret these coefficients? **
# Holding all other features fixed, a 1 unit increase in Avg. Session Length is associated with an increase of 25.98 total dollars spent.
# Holding all other features fixed, a 1 unit increase in Time on App is associated with an increase of 38.59 total dollars spent.
# Holding all other features fixed, a 1 unit increase in Time on Website is associated with an increase of 0.19 total dollars spent.
# Holding all other features fixed, a 1 unit increase in Length of Membership is associated with an increase of 61.27 total dollars spent.


#show graphs
plt.show()