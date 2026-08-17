import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

border="-"*50

data={
    'Name':["Amit","Sagar","Pooja"],
    'Math':[85,90,78],
    'Science':[92,88,90],
    'English':[75,85,82]
}

df=pd.DataFrame(data)

print("Shape of dataset is :")
print(df.shape)

print("Columns are: ")
print(df.columns)

print("Data types are")
print(df.dtypes)

print(border)

print("The descriptive statistics are of dataset are :")
print(df.describe)

print(border)

print("Adding new column as total :")
df["Total"]=df['Math']+df['Science']+df['English']   #added new column as total
print(df)

print(border)

print("Student more than 85 in science")
print(df[df["Science"]>85]["Name"])

print(border)

print("Replacing Pooja with puja in name column: ")
df["Name"]=df["Name"].replace("Pooja","Puja")
print(df)

print(border)

print("Sorting dataframe of total in descending order: ")
sorted_data=sorted(df["Total"],reverse=True) 
print(sorted_data)

print(border)

print("Bar plot of student names vs total marks")

plt.bar(
    df['Name'],
    df["Total"],
    width=0.6,
    edgecolor="black",
    linewidth=0.2,
    alpha=0.8,
    label="students"

)

plt.title("Students case study")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print(border)

plt.plot(
    ["Math", "Science", "English"],
    [
        df[df["Name"] == "Amit"]["Math"].iloc[0],           #iloc is used to acces rows or columns according to index, amit is at index 0
        df[df["Name"] == "Amit"]["Science"].iloc[0],
        df[df["Name"] == "Amit"]["English"].iloc[0]
    ],
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=7,
    label="Amit Marks"
)

plt.title("Marks of Amit")
plt.xlabel("Amit")
plt.ylabel("Marks")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print(border)

data2={
    'Name':["Amit","Sagar","Pooja"],
    'Math':[np.nan,90,78],
    'Science':[92,np.nan,90],
   
}

df1=pd.DataFrame(data2)

print("Replacing missing values by mean")
df1=df1.fillna(df1.mean(numeric_only=True))      #will replace only numeric values
print(df1)

print(border)

print("Drop english columns from original dataframe")
df.drop("English", axis=1, inplace=True)
print(df)