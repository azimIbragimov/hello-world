import matplotlib.pyplot as plt
import numpy as np
import json

"""
This file scans information from database 'City of Seattle Staff Demographics'
from https://catalog.data.gov/dataset/city-of-seattle-staff-demographics.
This file analyzes City of Seattle emploeyees' race and gender.
"""

# Open the file
with open('information.json') as f:
  data = json.load(f)

# Put all the information about race and gender into seperate lists
race = []
gender = []
for item in data['data']:
    print(item[8], item[9])
    race.append(item[8])
    gender.append(item[9])

# Counts how many people of any race there are
print("")
print("Race")
print("-----------------------------------------------------")
print("White: " + str(race.count("White")))
print("Asian: " + str(race.count("Asian")))
print("Hispanic or Latino: " + str(race.count("Hispanic or Latino")))
print("Black of African American: " + str(race.count("Black or African American")))
print("Nat Hawaiian/Oth Pac Islander: " + str(race.count("Nat Hawaiian/Oth Pac Islander")))
print("American Indian/Alaska Native: " + str(race.count("American Indian/Alaska Native")))
print("Two or More Races: " + str(race.count("Two or More Races")))
print("Not Specified: " + str(race.count("Not Specified")))


# Counts how many people of any gender there are
print("")
print("Gender")
print("-----------------------------------------------------")
print("Male: " + str(gender.count("M")))
print("Female: " + str(gender.count("F")))


"""Visualizing the racial data"""
np.random.seed(19680801)
plt.rcdefaults()
fig, ax = plt.subplots()

# List of races
races = ('White', 'Asian', 'Hispanic or Latino', 'Black or African American',
'Nat Hawaiian/Oth Pac Islander', 'American Indian/Alaska Native',
"Two or More Races", "Not Specified")
y_pos = np.arange(len(races))  # Output: Numpy array [0,1,2,3,4]

# A Numpy array with information about racial demograics
emploeyees = np.array([race.count("White"),
race.count("Asian"),
race.count("Hispanic or Latino"),
race.count("Black or African American"),
race.count("Nat Hawaiian/Oth Pac Islander"),
race.count("American Indian/Alaska Native"),
race.count("Two or More Races"),
race.count("Not Specified")])

# Creating a graphical statistics
ax.barh(y_pos, emploeyees, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(races)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Number of emploeyees')
ax.set_title('City of Seattle Staff Racial Demographics')
plt.show()


"""Visualizing the gender data"""
np.random.seed(19680801)
plt.rcdefaults()
fig, ax = plt.subplots()

# list of genders
gender_names = ("Male", "Female")
y_pos = np.arange(len(gender_names))

# Creates a Numoy array with gender information
emploeyees = np.array([gender.count("M"), gender.count("F")])

# Creates a graphical statistics
ax.barh(y_pos, emploeyees, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(gender_names)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Number of emploeyees')
ax.set_title('City of Seattle Staff Gender Demographics')
plt.show()
