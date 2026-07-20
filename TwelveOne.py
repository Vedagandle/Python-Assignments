def vowel(value):
    
        for i in value:
             if i=="aeiou":
                  print("Vowel")
             else:
                  print("constant")



def main():
    number=input("Enter your character")
    ret=vowel(number)

if __name__=="__main__":
    main()
