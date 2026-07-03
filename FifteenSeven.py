st=lambda no:no if len(no)>5 else ""
     
    
def main():
   data=["veda","raj","prithviraj"]
   print("Your input data is ",data)

   filteredData=list(filter(st,data))
   print("Your data is",filteredData)

if __name__=="__main__":
   main()