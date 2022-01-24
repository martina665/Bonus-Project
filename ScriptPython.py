# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:32:32 2022

@author: marti
"""

#Hello
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sns


dataset = pd.read_csv("csvdataR.csv", sep=";", encoding='cp1252')
print(dataset.info())

del dataset['course_feedback']
del dataset['self_description']
del dataset['dasmastudent_features']

#DATA ANALYSIS
dataset.describe()
dataset.info()

#information about single variable
dataset['gender'].describe() 
#How many males and females
dataset.gender.value_counts()#14 males , 12 females

#top students
#first top ten students
topStudent=dataset.sort_values('mean_grades',ascending=False).head(10)
topStudent

#least ten students
bottomStudent=dataset.sort_values('mean_grades',ascending=True).head(5)
bottomStudent

#Statistical analysis
dataset.mean()
#mean age= 22.5
#sport freq= 1.6 hours per week
#mean programming level prior to the semester= 2.7
#mean programming level after the semester= 4.8
#mean hours studied per day=3.8

#Informations on male and female
gender_details = dataset.groupby('gender')[['mean_grades','exams_passed','hours_study','age']].mean()
gender_details.sort_values('hours_study',ascending=False)

# exams_passed  hours_study        age
#gender                                      
#Male        2.714286     3.500000  23.000000
#Female      3.000000     4.083333  21.833333

#Parental level of edu
mother_lvl_of_edu_details = dataset.groupby('mother_degree')[['mean_grades','exams_passed','hours_study','age']].mean()
mother_lvl_of_edu_details.sort_values('exams_passed',ascending=False)

#father level of educ
father_lvl_of_edu_details = dataset.groupby('father_degree')[['mean_grades','exams_passed','hours_study','age']].mean()
father_lvl_of_edu_details.sort_values('exams_passed',ascending=False)

#scholarship
scholarship_details = dataset.groupby('scholarship')[['mean_grades','exams_passed','hours_study','age']].mean()
scholarship_details.sort_values('exams_passed',ascending=False)



#DATA VISUALISATION
#PLOT 1 AGE
plot1= dataset.groupby('age')['age'].count().plot.pie(autopct='%.2f',figsize=(6,6))
 
#PLOT 2 GENDER
plot2= dataset["gender"].value_counts().plot(kind='bar', title='Gender\n', color=["blue", "pink"])
plot2b= dataset.groupby('gender')['gender'].count().plot.pie(autopct='%.2f',figsize=(6,6))

#PLOT 3 EXAMS PASSED
plot3= dataset["exams_passed"].value_counts().plot(kind='bar', title='exams_passed\n', color=["green", "orange"])
plot3b= dataset.groupby('exams_passed')['exams_passed'].count().plot.pie(autopct='%.2f',figsize=(6,6))

#PLOT4 SCHOLARSHIP
plot4= dataset.groupby('scholarship')['scholarship'].count().plot.pie(autopct='%.2f',figsize=(6,6))

#PLOT 5 DIFFICULT CURSE
plot5= dataset.groupby('difficult_course')['difficult_course'].count().plot.pie(title= 'Difficoult Course',autopct='%.2f',figsize=(6,6))    

#PLOT 6 STUDY PREFERENCE
plot6= dataset["study_preferences"].value_counts().plot(kind='bar', title='Study preferences\n', color=["green", "blue"])
