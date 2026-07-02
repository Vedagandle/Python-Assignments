def perfect(value):
    sum = 0

    for i in range(1, value):
        if value % i == 0:
            sum = sum + i

    if sum == value:
        print("It is a perfect number")
    else:
        print("It is not a perfect number")


def main():
    number = int(input("Enter your number: "))
    perfect(number)

if __name__ == "__main__":
    main()