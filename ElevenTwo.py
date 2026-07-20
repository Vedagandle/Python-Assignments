def count(value):
    cnt = 0

    for no in str(value):
        cnt = cnt + 1

    return cnt


def main():
    print("Enter number:")
    value = int(input())

    ret = count(value)

    print("Number of digits are:", ret)


if __name__ == "__main__":
    main()