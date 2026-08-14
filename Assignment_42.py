import math
import numpy 


border="-"*50

def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt((P1['x'] - P2['x'])**2 + (P1['y'] - P2['y'])**2)
    return Ans
def assKNNclassifier(no1,no2):

    data=[
        {"studyhours":2, "attendance":60, "Result":"fail"},
        {"studyhours":5, "attendance":80, "Result":"pass"},
        {"studyhours":6, "attendance":85, "Result":"pass"},
        {"studyhours":1, "attendance":50, "Result":"fail"}
    ]

    print(border)
    print("Assignment KNN")
    print(border)

    for i in data:
        print(i)

    print(border)

    # Calculating distance
    for i in data:
        i["distance"]=MarvellousEucDistance(
            {"x":no1, "y":no2},                         #this will have input data from user no1=4, no2=70
            {"x":i["studyhours"], "y":i["attendance"]}  #this will have data from dataset x:2, y:60
            
        )

    print(border)
    #sorted in ascending order

    sorted_data=sorted(data, key=lambda x :x["distance"])  #sorted is function, lambda x means it will take one full dict/one full record in x and will give distance present in that dict
    print("The sored data is :")
    for i in sorted_data:
        print(i)

    #decide value of k

    k=3
    nearest=sorted_data[:k]  #:k means slicing, sorted_data madhe javalche 3

    print(border)
    print("The nearest 3 numbers are: ")
    print(border)

    for d in nearest:
        print(d)

    print(border)

#voting
    votes={}

    for d in nearest:   #neartes madhe je javalche 3 alet
        result=d["Result"]         #d will have one full record of dict
        votes[result]=votes.get(result,0)+1 # for 1 iteration it is pass so it will check if this is already there in empty set or not, if dosent exist it will give 0 initially and will add 1 so that pass is added to votes now

    print(border)
    print("Voting result : ")
    print(border)

    for d in votes:
        print("Result :", d, "Number of votes :", votes[d])

    print(border)

    imax=0
    Name=""

    for d in votes:
        if(votes[d]>imax):
            imax=votes[d]
            Name=d

    print("The final prediction is",Name)


def main():
    sh=int(input("Enter study hours"))
    ap=int(input("Enter attendance percentage"))
    
    assKNNclassifier(sh,ap)
    

if __name__=="__main__":
    main()