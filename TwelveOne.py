def vowel(value):
    
        if value in "aeiou":
            print("It is a vowel")
        else:
            print("It is a constant")
        
        return value


def main():
    number=input("Enter your character")
    ret=vowel(number)

if __name__=="__main__":
    main()
