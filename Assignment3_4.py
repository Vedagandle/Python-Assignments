def frequency(value, search):   #value=list, search=no to be saerched
    count = 0

    for i in value:
        if i == search:
            count = count + 1

    return count


def main():
    data = []

    no = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(no):
        n = int(input())
        data.append(n)

    search = int(input("Enter element to search: "))

    ret = frequency(data, search)

    print("Frequency is:", ret)


if __name__ == "__main__":
    main()