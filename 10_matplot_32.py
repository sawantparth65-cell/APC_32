'''#line plot
import matplotlib.pyplot as plt 
plt.plot([1,2,3],[4,5,6])
plt.show()

#line plot
import matplotlib.pyplot as plt 
plt.plot([1,2,3],[4,5,6],color="red")
plt.xlim(1,5)
plt.ylim(1,6)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#Bar chart
import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
marks = [85, 90, 75]

plt.bar(subjects, marks, color="skyblue")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

#Scatter plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 12, 20, 25]

plt.scatter(x, y, color="red")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot")
plt.show()

#Pie chart
import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++"]
values = [50, 30, 20]

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)
plt.title("Programming Languages")
plt.show()

#Histogram
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 60, 65, 70, 70, 75, 80, 85, 90]

plt.hist(marks, bins=5, color="skyblue", edgecolor="black")

plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram of Student Marks")

plt.show()

#3D plot
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]
z = [3, 1, 4, 2, 6]

ax.plot(x, y, z, color="blue", marker="o")

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.set_title("3D Line Plot")

plt.show()

#Subplot
import matplotlib.pyplot as plt

# Create 4 subplots (2 rows, 2 columns)
plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Line Plot")

plt.subplot(2, 2, 2)
plt.bar(["A", "B", "C"], [10, 20, 15])
plt.title("Bar Chart")

plt.subplot(2, 2, 3)
plt.scatter([1, 2, 3], [4, 5, 6])
plt.title("Scatter Plot")

plt.subplot(2, 2, 4)
plt.hist([10, 20, 20, 30, 30, 30, 40], bins=4)
plt.title("Histogram")

plt.tight_layout()
plt.show()'''