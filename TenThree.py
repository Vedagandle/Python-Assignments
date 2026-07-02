def factorial(no):
    fact = 1

    for i in range(1, no + 1):
        fact = fact * i

    return fact


def main():
    print("Enter a number:")
    no = int(input())

    ret = factorial(no)

    print("Factorial is:", ret)


if __name__ == "__main__":
    main()