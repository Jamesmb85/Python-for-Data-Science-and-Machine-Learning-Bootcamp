# Ecommerce Purchases Exercise
#
# In this Exercise you will be given some Fake Data about some purchases done through Amazon!
# Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. Feel free to reference the solutions.
# Most of the tasks can be solved in different ways. For the most part, the questions get progressively harder.
#
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
#
# Also note that all of these questions can be answered with one line of code.
#


# ** Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. **
import pandas as pd
econ = pd.read_csv("Ecommerce Purchases")

#Check the head of the DataFrame.
print(econ.head())
print('\n')

# ** How many rows and columns are there? **
print(econ.info())
print('\n')

# ** What is the average Purchase Price? **
print(econ['Purchase Price'].mean())
print('\n')

# ** What were the highest and lowest purchase prices? **
print(econ['Purchase Price'].max())
print(econ['Purchase Price'].min())
print('\n')

# ** How many people have English 'en' as their Language of choice on the website? **
print( econ[ econ['Language'] == 'en' ].count() )
print('\n')

#** How many people have the job title of "Lawyer" ? **
print( econ[ econ['Job'] == 'Lawyer' ].count() )
print('\n')

#** How many people made the purchase during the AM and how many people made the purchase during PM ? **
print( econ[ econ['AM or PM'] == 'PM' ]['AM or PM'].value_counts()  )
print( econ[ econ['AM or PM'] == 'AM' ]['AM or PM'].value_counts()  )
print('\n')

# ** What are the 5 most common Job Titles? **
print( econ['Job'].value_counts().head(5) )
print('\n')

#** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **
print( econ[ econ['Lot'] == '90 WT' ]['Purchase Price'] )
print('\n')

#** What is the email of the person with the following Credit Card Number: 4926535242672853 **
print( econ[ econ['Credit Card'] == 4926535242672853 ]['Email'] )
print('\n')

#* How many people have American Express as their Credit Card Provider *and made a purchase above $95 ?**
print( econ[ (econ['CC Provider'] == 'American Express') &  (econ['Purchase Price'] > 95) ].count()  )
print('\n')



