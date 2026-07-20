def sumdigits(value):
    sum = 0
    for no in (value):
        sum = sum + int(no)

    return sum


def main():
    number = input("Enter your number: ")
    ret = sumdigits(number)
    print("Your addition is", ret)


if __name__ == "__main__":
    main()