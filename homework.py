import matplotlib.pyplot as plt

genders = ['Males', 'Females']
Number = [10, 15] 
plt.bar(genders, Number, color=['blue', 'pink'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Number of Males and Females in a Room')
plt.show()
