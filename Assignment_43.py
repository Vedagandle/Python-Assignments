import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier



def assign(datapath):
    border="-"*50

#Load dataset from csv
    print(border)
    print("Step 1: Load dataset from csv")
    print(border)
    df=pd.read_csv(datapath)

    print("Some entries from dataset")
    print(df.head(5))
    print(border)

#Clean the dataset
    print(border)
    print("Step 2: Clean the dataset")
    print(border)

    df.dropna(inplace=True)

    print("Shape of dataset: ",df.shape)
    print("Total records of rows: ",df.shape[0])
    print("Total records of columns: ",df.shape[1])

    print(border)
#Enocidng
    df["Wether"] = df["Wether"].replace({
        "Sunny": 1,
        "Overcast": 2,
        "Rainy": 3
    })

    df["Temperature"] = df["Temperature"].replace({
        "Hot": 1,
        "Mild": 2,
        "Cool": 3
    })

    df["Play"] = df["Play"].map({
    "No": 0,
    "Yes": 1
})

    df.dropna(inplace=True)

    df["Play"] = df["Play"].astype(int)

#decide dependent and independent variables
    print(border)
    print("Step 3: Seperate independent and dependent variables")
    print(border)

    x=df.drop(columns=["Play"])
    y=df["Play"]

    print("Shape of x is: ",x.shape)
    print("Shape of y is: ",y.shape)

    print("Columns is list are: ",x.columns.to_list())
    print(border)

#Split Dataset for training and testing
    print(border)
    print("Step 4: Split dataset for training and testing")
    print(border)

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#Hyper Parameter Tuning
    accuracy_scores=[]  #will store values of k
    k_values=range(1,21)

    for k in k_values:
        model=KNeighborsClassifier(n_neighbors=3)
        model=model.fit(x_train,y_train)
        y_pred=model.predict(x_test)
        accuracy=accuracy_score(y_test,y_pred)
        accuracy_scores.append(accuracy)

    print("Accuracy Reprot")
    for no in accuracy_scores:
        print(no)

    print(border)

def main():
    assign("MarvellousInfosystems_PlayPredictor.csv")

if __name__=="__main__":
    main()



