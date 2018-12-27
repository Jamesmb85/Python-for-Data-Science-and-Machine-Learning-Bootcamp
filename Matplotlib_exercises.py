#Exercises
#Follow the instructions to recreate the plots using this data:

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y = x*2
z = x**2

#Exercise 1
#** Follow along with these steps: **
#
#** Create a figure object called fig using plt.figure() **
#** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
#** Plot (x,y) on that axes and set the labels and titles to match the plot below:**
fig = plt.figure()
ax = fig.add_axes([0,0,1,1]) #left,bottom, width, height
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')


# Exercise 2
# ** Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])
# ** Now plot (x,y) on both axes. And call your figure object to show it.**
ax1.plot(x,y, color = 'red')
ax2.plot(x,y, color = 'red')


# Exercise 3
# ** Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**
fig = plt.figure()
ax3 = fig.add_axes([0,0,1,1])
ax4 = fig.add_axes([0.2,0.5,.4,.4])
# ** Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:**
ax3.plot(x,z)
ax4.plot(x,y)
ax3.set_xlabel('x')
ax3.set_ylabel('Z')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_xlim([20,22])
ax4.set_ylim([30,50])
ax4.set_title("zoom")

# Exercise 4
# ** Use plt.subplots(nrows=1, ncols=2) to create the plot below.**
fig5,axes5 = plt.subplots(nrows = 1, ncols = 2, figsize = (12,2)) #a subplot with one row and two columns
# plt.subplots() returns a tuple containing two objects, the first object represents our figure, and the
# second one our axes, thus, assigning it to two variables allow us to individually call them.

#since axes5 is iterable, we can index it and change the graphs individually
axes5[0].plot(x,y, linestyle = '--', linewidth = 2)
axes5[1].plot(x,z, color = 'red', linewidth = 2)



#show all of the plots
plt.show()
