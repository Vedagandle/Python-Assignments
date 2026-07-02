def palindrome(value):
    pali = ""

    for no in value:
        pali = no + pali

    if value == pali:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

    return pali


def main():
    number = input("Enter your number: ")
    palindrome(number)


if __name__ == "__main__":
    main() 