import matplotlib.pyplot as plt
import numpy as np

ages = [22,55,36,67,89,34,56,76,14,15,28]
bins = [0,10,20,30,40,50,60,70,80,90,100]
#bins are the ranges of values that are grouped together to create bars.
#plt.hist is the same as plt.plot for histograms
plt.hist(ages,bins,histtype = "bar", rwidth = 0.8)
plt.xlabel("Age Interval")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
#scatter plot
x = [1,2,3,4,5,6,7,8,9]
y = [0,1,0,1,0,1,0,1,0]

plt.scatter(x,y,label="Scatter Plot", color = "red", marker = "o", s=50)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.legend()
plt.show()

#pie chart
activities = ["Sleeping", "Eating", "Working", "Netlfix", "Workout & Friends"]
hours = [6,1,12,2,3]

colour = ['c','m', "r", "y", "g"]
plt.pie(hours,labels=activities,colors=colour,startangle=90,shadow= True)
plt.title("Day Pie Chart")
plt.show()

#stack plot

days = [1,2,3,4,5]
eating = [2,3,4,3,2]
sleeping = [5,6,7,8,4]
working = [4,5,6,7,8]
playing = [2,3,4,5,1]

plt.plot([], [], color = "m", label = "Eating", linewidth = 5)
plt.plot([], [], color = "b", label = "Sleeping", linewidth = 5)
plt.plot([],[], color = "g", label = "Working", linewidth = 5)
plt.plot([],[],color = "y", label = "Playing", linewidth = 5)
plt.stackplot(days,eating,sleeping,working,playing,colors = ["m", "b", "g", "y"])
plt.xlabel = ("x")
plt.ylabel("y")
plt.title("Stack Plot")
plt.legend()
plt.show()

#subplot
def f(t):
  return np.exp(-t)*np.cos(2*np.pi*t)
t1 = np.arange(0, 5, 0.1)
plt.figure()
plt.subplot(221)
plt.plot(t1, f(t1), 'bo')
t2 = np.arange(0, 5, 0.02)
plt.subplot(224)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.show()


