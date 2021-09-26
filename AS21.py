import matplotlib.pyplot as plt
import numpy as np

# Set up two lists for data later drawn from text file
density_parish = []
density_rat = []

# Open text file, scan its data and makes it into a 2D list
f = open("death_parishes.txt")
for row in f:
    parsed_row = str.split(row,",")
    rowlist = []
    for value in parsed_row:
        rowlist.append(float(value))
    density_parish.append(rowlist)

# Open text file, scan its data and makes it into a 2D list
f = open("death_rats.txt")
for row in f:
    parsed_row = str.split(row,",")
    rowlist1 = []
    for value in parsed_row:
        rowlist1.append(float(value))
    density_rat.append(rowlist1)

# Create two arrays for the two 2D lists
array_parish = np.array(density_parish)
array_rat = np.array(density_rat)

# Calculate average death based on data from two arrays and given coefficients
death_average = (0.8 * array_rat) * (1.3 * array_parish)

# Sum all the average deaths 
death_total=np.sum(death_average, dtype=np.float64) 
"""float64 is used to obtain a higher precision for the output,
especially data in the array contains many floating numbers. """

print ("Based on existing small scale studies to gauge \
the effect of average population density and average rats caught on death,\
the estimated total death in the 1665 Black Death outbreak is:", death_total)

# Create a matrix for the average death 2D list and save it as a txt file
death=np.matrix(death_average)
file = open("death.txt", "w")
for row in death_average:
    np.savetxt(file,death_average,fmt='%d')
file.close

# Show the map on population density, save it as png and gives it a title 
plt.imshow(density_parish)
plt.savefig("density_parish.png")
plt.title("Relationship between average population density and average deaths")
plt.show()

# Show the map on rats caught, save it as png and gives it a title 
plt.imshow(density_rat)
plt.savefig("density_rat.png")
plt.title("Relationship between average rats caught and average deaths")
plt.show()

# Show the map on deaths, save it as png and gives it a title 
plt.imshow(death_average)
plt.savefig("death_average.png")
plt.title("Final estimation of average deaths")
plt.show()

# Create command line for user inputs
coefficient_parish = float(input ("Enter the coefficient indicating the relationship between average population density and average deaths: "))
coefficient_rat = float(input ("Enter the coefficient indicating the relationship between average rats caught and average deaths: "))
"""The input() returns str, hence conversion to float numbers is required for later calculation"""

# Create an equation to calculate average death based upon user inputs
death_average_users = (coefficient_parish * array_parish) * (coefficient_rat * array_rat)
death_total_users=np.sum (death_average_users, dtype=np.float64)
print ("The total death is estimated to be", death_total_users,end='.')
  