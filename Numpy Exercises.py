#All code was developed in Intellji

#NumPy Exercises 
#Now that we've learned about NumPy let's test your knowledge. 
#We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

#1)Import NumPy as np
import numpy as np

#2)Create an array of 10 zeros 
zerosArray = np.zeros(10)
print(zerosArray)

#3)Create an array of 10 ones
OnesArray = np.ones(10)
print(OnesArray)


#4)Create an array of 10 fives
FivesArray = np.array([5,5,5,5,5,5,5,5,5,5], float)
print(FivesArray)


#5)Create an array of the integers from 10 to 50
ArrayFromOneToFifty = np.arange(10,51)
print(ArrayFromOneToFifty)


#6)Create an array of all the even integers from 10 to 50
ArrayFromOneToFiftyEven = np.arange(10,51,2)
print(ArrayFromOneToFiftyEven)


#7)Create a 3x3 matrix with values ranging from 0 to 8
ArrayZeroToEight = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(ArrayZeroToEight)


#8)Create a 3x3 identity matrix
identity = np.eye(3,3)
print(identity)


#9)Use NumPy to generate a random number between 0 and 1
print(np.random.rand(1))


#10)Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print(np.random.randn(25))



#11)Create the following matrix:
# array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
       # [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
       # [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
       # [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
       # [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
       # [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
       # [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
       # [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
       # [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
       # [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]])
workingList = [i for i in range(1,101)]
arr = np.array(workingList)/100
print(arr.reshape(10,10))



#12)Create an array of 20 linearly spaced points between 0 and 1:
# array([ 0.        ,  0.05263158,  0.10526316,  0.15789474,  0.21052632,
        # 0.26315789,  0.31578947,  0.36842105,  0.42105263,  0.47368421,
        # 0.52631579,  0.57894737,  0.63157895,  0.68421053,  0.73684211,
        # 0.78947368,  0.84210526,  0.89473684,  0.94736842,  1.        ])
print(np.linspace(0,1,20))




#Numpy Indexing and Selection
#13)
#Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
mat = np.arange(1,26).reshape(5,5)
mat
array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])

#14)
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
array([[12, 13, 14, 15],
       [17, 18, 19, 20],
       [22, 23, 24, 25]])

newArray = mat[2: , 1: ]
print(newArray)


#15)
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
20
newArray = mat[3,4]
print(newArray)




#16)
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
array([[ 2],
       [ 7],
       [12]])
newArray = mat[ :3, 1:2]
print(newArray)	   



#17)
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
array([21, 22, 23, 24, 25])
newArray = mat[4]
print(newArray)



#18)
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
array([[16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])
	   
newArray = mat[3:5]
print(newArray)



#Now do the following

#19)Get the sum of all the values in mat
newArray = mat.sum()
print(newArray)


#20)Get the standard deviation of the values in mat
newArray = mat.std()
print(newArray)


#21)Get the sum of all the columns in mat
newArray1 = mat[ : , 0:1].sum()
newArray2 = mat[ : , 1:2].sum()
newArray3 = mat[ : , 2:3].sum()
newArray4 = mat[ : , 3:4].sum()
newArray5 = mat[ : , 4:5].sum()
print(np.array([newArray1, newArray2, newArray3, newArray4, newArray5]))
