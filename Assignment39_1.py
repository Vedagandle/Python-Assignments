from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay
import pandas as pd
import matplotlib.pyplot as plt

border="-"*80

def main():
#######################################################
#Step 1: Load Dataset
#######################################################
    print(border)
    print("Step 1: Load Dataset")
    print(border)

    df=pd.read_csv("student_performance_ml.csv")

    print("First 5 entries from dataset")
    print(df.head(5))
    print(border)

#########################################################
#Step 2: Data Analysis
#########################################################
    print(border)
    print("Step 2: Data Analysis")
    print(border)

    print("Shape of my data is ",df.shape)

##########################################################
#Step 3: Decide Dependent and Independent Variables
##########################################################
 
    print(border)
    print("Step 3: Decide Dependent and Independent Variables")
    print(border)

    x=df.drop(columns=['FinalResult'])
    y=df['FinalResult']

    print("Shape of x: ",x.shape)
    print("Shape of y: ",y.shape)

##################################################################
#Step 4: Split Data for training and testing
##################################################################

    print(border)
    print("Step 4: Split Data for training and testing")
    print(border)

    x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.5,random_state=42)
    
    model=DecisionTreeClassifier()

    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)

    accuracy=accuracy_score(y_test,y_pred)

    print("The accuracy is :",accuracy*100)

####################################################################
#Step 5: Data Visualization
####################################################################

    print(border)
    print("Step 5: Data Visualization")
    print(border)

    study_hours=[2,
    3,
    4,
    5,
    6,
    7,
    8,
    1,
    2.5,
    3.5,
    4.5,
    5.5,
    6.5,
    7.5,
    8.5,
    1.5,
    2.2,
    3.8,
    4.8,
    5.8,
    6.8,
    7.8,
    2.1,
    3.2,
    4.2,
    5.2,
    6.2,
    7.2,
    8.2,
    1.8]

    attendance=[65,
    70,
    75,
    80,
    85,
    90,
    92,
    60,
    68,
    72,
    78,
    82,
    88,
    93,
    95,
    62,
    67,
    74,
    79,
    83,
    89,
    94,
    66,
    71,
    76,
    81,
    87,
    91,
    96,
    63

        ]


    plt.scatter(
        study_hours,
        attendance,
        edgecolor="black",
        alpha=0.8,
        marker="o",
        s=100,
        label="Students",
        linewidth=1
    )

    plt.title("My Assignement Visualization")
    plt.xlabel("Stidy Hours")
    plt.ylabel("Attendance")

    plt.grid(True)
    plt.legend()
    plt.show()



if __name__=="__main__":
    main()
