largest=lambda value1,value2,value3: value1 if value1>value2 and value1>value3 else value2 if value2>value3 else value3
        

    
def main():
    no1=int(input("Enter 1 no"))
    no2=int(input("Enter 1 no"))
    no3=int(input("Enter 1 no"))
    ret=largest(no1,no2,no3)
    print("Largest value is ",ret)

if __name__=="__main__":
    main()
