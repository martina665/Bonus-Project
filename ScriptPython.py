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

#PLOT 7: after master exp
plot6= dataset["after_master_exp"].value_counts().plot(kind='bar', title='Post graduation expectations\n', color=["red", "blue"])


#PLOT 8: master selection 
plot8= dataset["master_selection"].value_counts().plot(kind='bar', title='Master choice\n', color=["green", "blue", "black", "pink", "yellow", "orange", "red", "grey"])


#PLOT 9: study organization 
plot9= dataset["study_organization"].value_counts().plot(kind='bar', title='Study organization\n', color=["green", "blue", "black"]) 


#PLOT 10: live with famility
plot10= dataset.groupby('live_with_family')['live_with_family'].count().plot.pie(autopct='%.2f',figsize=(6,6))


#PLOT 11: private life management 
plot11= dataset["privatelife_management"].value_counts().plot(kind='bar', title='Can you manage your private life while studying?\n', color=["pink", "yellow"])


#PLOT 12: sport frequency 
plot12= dataset["sport_freq"].value_counts().plot(kind='bar', title='Hours of sport per week\n', color=["purple", "green", "yellow", "blue", "pink"])


#PLOT 13: erasmus experience 
plot13= dataset["erasmus_experience"].value_counts().plot(kind='bar', title='Erasmus experience\n', color=["purple", "green"])


#PLOT 14: university bachelor 
plot14= dataset.groupby('university_bachelor')['university_bachelor'].count().plot.pie(autopct='%.2f',figsize=(6,6))

# MIXED PLOTS 

#PLOT 15: programming level pre/after vs mean grades 
# ordinare i valori in maniera ASCENDENTE
dataset.sort_values(by=['mean_grades'], inplace = True)
dataset.sort_values(by=['mean_grades'], ascending = True, inplace = True)
dataset.sort_values(by=['mean_grades'], ascending = 1, inplace = True)

#programming level pre vs mean grades
df= dataset[['mean_grades', 'programminglevel_pre']]
df.plot(kind='scatter', x='programminglevel_pre', y='mean_grades', alpha=0.7)
plt.tight_layout()
plt.show

#programminglevel after vs mean grades 
df= dataset[['mean_grades', 'programminglevel_after']]
df.plot(kind='scatter', x='programminglevel_after', y='mean_grades', alpha=0.7)
plt.tight_layout()
plt.show


#PLOT 16: proramming level pre/after vs bachelor field 
# programming level (pre and after) of the students who have took a bachelor in Economics
Ec1=dataset[dataset.bachelor_field=='E']
Ec1["programminglevel_pre"].value_counts().plot(kind='bar', title='Programming level Economics students pre\n', color=["yellow", "orange", "blue", "red"])
Ec1["programminglevel_after"].value_counts().plot(kind='bar', title='Programming level Economics students after\n', color=["yellow", "orange", "blue", "red", "purple"])

# programming level (pre and after) of the students who have took a bachelor in Economics and Management

Ec2=dataset[dataset.bachelor_field=='M']
Ec2["programminglevel_pre"].value_counts().plot(kind='bar', title='Programming level Economics and Management students pre\n', color=["green", "blue", "orange", "yellow"])
Ec2["programminglevel_after"].value_counts().plot(kind='bar', title='Programming level after Economics and Management students after\n', color=["green", "blue", "orange", "yellow"])


# programming level (pre and after) of the students who have took a bachelor in Management and Computer Science
Ec3=dataset[dataset.bachelor_field=='S']
Ec3["programminglevel_pre"].value_counts().plot(kind='bar', title='Programming level Management and Computer Science students pre\n', color=["orange", "pink"])
Ec3["programminglevel_after"].value_counts().plot(kind='bar', title='Programming level Management and Computer Science students after\n', color=["orange"])


# programming level (pre and after) of the students who have took a bachelor in Economics and Business 
Ec4=dataset[dataset.bachelor_field=='B']
Ec4["programminglevel_pre"].value_counts().plot(kind='bar', title='Programming level Economics and Business students pre\n', color=["purple", "blue"])
Ec4["programminglevel_after"].value_counts().plot(kind='bar', title='Programming level Economics and Business students after\n', color=["purple", "blue"])


# programming level (pre and after) of the students who have took a bachelor in Political Science 
Ec5=dataset[dataset.bachelor_field=='P']
Ec5["programminglevel_pre"].value_counts().plot(kind='bar', title='Programming level Political Science students pre\n', color=["pink", "blue", "green"])
Ec5["programminglevel_after"].value_counts().plot(kind='bar', title='Programming level Political Science students after\n', color=["pink", "blue", "green", "yellow"])


# programming level (pre and after) of the students who took a bachelor in Communication 
Ec6=dataset[dataset.bachelor_field=='C']
Ec6["programminglevel_pre"].value_counts().plot(kind='bar', title='Programming level Communication students pre\n', color=["blue"])
Ec6["programminglevel_after"].value_counts().plot(kind='bar', title='Programming level Communication students after\n', color=["blue"])


# programming level (pre and after) of the students who took a bachelor in Business Administration
Ec7=dataset[dataset.bachelor_field=='A']
Ec7["programminglevel_pre"].value_counts().plot(kind='bar', title='Programming level Business Administration students pre\n', color=["orange"])
Ec7["programminglevel_after"].value_counts().plot(kind='bar', title='Programming level Business Administration students after\n', color=["orange"])


# PLOT 17: mean grades vs hours study
plt.hist(dataset['mean_grades'],alpha=0.5);
plt.hist(dataset.hours_study,alpha=0.5);
plt.legend(['mean_grades','hours_study']);