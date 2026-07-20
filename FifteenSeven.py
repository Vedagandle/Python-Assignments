st=lambda no:no if len(no)>5 else ""
     
    
def main():


   print("Enter names:")
   Data = input().split(",")

   print("Your data is",Data)

   filteredData=list(filter(st,Data))
   print("Your data is",filteredData)

if __name__=="__main__":
   main()