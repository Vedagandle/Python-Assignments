import pandas as pd
import matplotlib.pyplot as plt

border="_"*30
###############################################
#Load dataset
###############################################
print(border)
print("Load the data set")
print(border)

datapath="c:\\Users\\vedag\\OneDrive\\Desktop\\Marvellous Python\\Machine_learning\\student_performance_ml.csv"

df=pd.read_csv(datapath)

print("Dataset loaded successfully")

print(border)
print("Data Analysis")
print(border)

###############################################
#Data Analysis
###############################################
print(border)
print("Data Analysis")
print(border)

print("First 5 records:",df.head(5))
print("Last 5 records:",df.tail(5))
print("Dataset shape:",df.shape)
print("List of column names: ",list(df.columns))
print("Data type of each columns: ",df.dtypes[df.columns]) #data types of column names

print("No of students :",df.shape[0])  #no of rows

print("No of students passed are :",df["FinalResult"].value_counts()[1])

print("No of students failed are :",df["FinalResult"].value_counts()[0])

print("Average study hours: ",df["StudyHours"].mean())
print("Average attendance: ",df["Attendance"].mean())
print("Maximum previous score: ",df["PreviousScore"].max())
print("Minimum sleep hours: ",df["SleepHours"].min())

print(border)
print("Data Analysis")
print(border)

###############################################
#Data Visualization
###############################################
print(border)
print("Data Visualization")
print(border)

#histogram
plt.figure(figsize=(7,5))
plt.hist(df["StudyHours"])
    
plt.title("Histogram for study hours")

plt.xlabel("Study Hours")
plt.ylabel("No of students")

plt.grid()
plt.show()

###############################################
#Data Visualization (Scatter plot)
###############################################
print(border)
print("Data Visualization Scatter Plot")
print(border)

plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp=df[df["FinalResult"]==sp]
    plt.scatter(temp["StudyHours"],temp["PreviousScore"],label=sp)

plt.title("Student Performance Case Study")

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.legend()
plt.grid()
plt.show()






