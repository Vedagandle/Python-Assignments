def pattern(no):
    for i in range(no):              #i=rows
        for j in range(no):           #j=columns
            print(j+1,end=" ")
            
        print()




def main():
    value=int(input("Enter your no"))
    ret=pattern(value)

if __name__=="__main__":
    main()