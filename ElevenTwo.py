def count(value):
    cnt = 0

    while value > 0:
        cnt = cnt + 1
        value = value // 10

    return cnt


def main():
    no = int(input("Enter your number: "))

    ret = count(no)

    print("Count of digits is:", ret)


if __name__ == "__main__":
    main()