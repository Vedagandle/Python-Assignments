import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

border="-"*50

data={
    'Name':["Amit","Sagar","Pooja"],
    'Math':[85,90,78],
    'Science':[92,88,90],
    'English':[75,85,82]
}

df=pd.DataFrame(data)

print("Normalizing Math using min-max scaling")

scalar=MinMaxScaler()

df['Math']=scalar.fit_transform(      # .fit will find min and max values , transform converts each value to between 0 to 1
    df[['Math']]                      #2 bracket so that it will git dataframe back, scalar expects data in 2d
)

print(df)
print(border)

print("Adding new column as total :")
df["Total"]=df['Math']+df['Science']+df['English']   #added new column as total
print(df)

print(border)

print("Create a gender column and perform one hot encoding")
df["Gender"]=["Male","Male","Female"]
print(df)

print(border)

print("Group students by gender and calculate avg marks")

avg_marks=df.groupby("Gender")[['Math','Science','English']].mean()
print(avg_marks)

print(border)

df=pd.get_dummies(df, columns=["Gender"], dtype=int)    #get dummies will perform one hot encoding
print(df)

print(border)

print("Plotting pie chart for marks of sagar")
student=df[df["Name"]=="Sagar"].iloc[0]     #iloc[0] means stores sagar complete row in student , 0 = row

marks=[student['Math'],student['Science'],student['English']]
subject=['Math','Science','English']
plt.pie(
    marks,
    labels=subject,                 #labels should always ne x 
    autopct="%1.1f%%"               #it will give in percentage

)

plt.title("Marks of Sagar")
plt.legend()
plt.show()

print(border)

print("Add new column status  where students with total >= 250 are pass else fail")

df["Status"]=df["Total"].map(lambda x:"Pass" if x >=250 else "Fail")  #We use .map() because we want to perform the same operation on every value in the Total column, one by one.
print(df)

print(border)

print("Count how many students passed")

count = 0

for status in df["Status"]:
    if status == "Pass":
        count = count + 1

print("Number of students passed:", count)

print(border)

print("Exporting final data frame to csv")

df.to_csv("Students_final.csv", index=False)  #prevents Pandas from adding the row numbers (0, 1, 2...) as an extra column.

print("Exported successfully")

print(border)

print("Plot a histogram of maths marks")
plt.hist(
    df["Math"],
    bins=5,
    edgecolor="black",
    alpha=0.8,
    rwidth=0.9,
    label="Marks"

)

plt.title("Maths marks")
plt.xlabel="Marks"
plt.ylabel="Subject"
plt.legend()
plt.grid(True)
plt.show()

print(border)

print("Rename math column to mathematics")

df=df.rename(columns={'Math': 'Mathematics'})

print(df)

print(border)

print("Plot a boxplot for english marks to check distribution and outliers")

plt.boxplot(
    df["English"],
)

plt.title("English Marks")
plt.xlabel="Englis"
plt.ylabel="Marks"
plt.legend
plt.grid(True)
plt.show()
