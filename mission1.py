testTab = []
intTab = []

def main():
    numberOfTest = int(input())
    recursive_test(numberOfTest)
    print(*testTab)


def recursive_test(numberOfTest):
    if numberOfTest == 0: return
    numberOfInt = int(input())
    intTab.clear()
    recursive_int(numberOfInt)
    sumOfSquares = sum(map(lambda x: x**2, filter(lambda x: x > 0, intTab)))
    testTab.append(sumOfSquares)
    recursive_test(numberOfTest - 1)

def recursive_int(numberOfInt):
    if numberOfInt == 0: return
    result = int(input())
    intTab.append(result)
    recursive_int(numberOfInt - 1)


if __name__ == "__main__":
    main()
