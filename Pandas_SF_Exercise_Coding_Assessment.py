#SF Salaries Exercise
#Welcome to a quick exercise for you to practice your pandas skills! We will be using the SF Salaries Dataset from Kaggle!
#Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

#1) ** Import pandas as pd.**
import pandas as pd

#2)** Read Salaries.csv as a dataframe called sal.**
sal = pd.read_csv("Salaries.csv")

#3) ** Check the head of the DataFrame. **
print(sal.head())
print('\n')

#4) ** Use the .info() method to find out how many entries there are.**
print(sal.info())
print('\n')

#5) What is the average BasePay ?
print(sal['BasePay'].mean())
#or can use print(sal['BasePay'].describe())
print('\n')

#6) ** What is the highest amount of OvertimePay in the dataset ? **
print(sal['OvertimePay'].max())
#or can use print(sal['OvertimePay'].describe())
print('\n')

#7) ** What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **
print(sal[ (sal['EmployeeName'] == 'JOSEPH DRISCOLL') ]['JobTitle'] )
print('\n')

#8)** How much does JOSEPH DRISCOLL make (including benefits)? **
print(sal[ (sal['EmployeeName'] == 'JOSEPH DRISCOLL') ]['TotalPayBenefits'] )
print('\n')

#9)** What is the name of highest paid person (including benefits)?**
print( sal[ sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max() ]['EmployeeName'] )
print('\n')

#10) ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**
print( sal[ sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min() ]['EmployeeName'] )
print('\n')

#11)** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **
print( sal.groupby('Year').mean()['BasePay'] )
print('\n')

#12)** How many unique job titles are there? **
print( sal['JobTitle'].nunique() )
print('\n')

#13) ** What are the top 5 most common jobs? **
print( sal['JobTitle'].value_counts().head(5) )
print('\n')

#14) * How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **
print( sum( sal[ sal['Year'] == 2013]['JobTitle'].value_counts() == 1)  )
print('\n')
