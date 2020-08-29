class ListDivideException(Exception):
    pass


def listDivide(numbers, divide=2):
    divamt = 0
    try:
        for num in numbers:
            divamt += 1 if not num % divide else 0
    except:
        raise ListDivideException()
    print(divamt)
    return divamt


def testListDivide():
    listDivide([1, 2, 3, 4, 5])
    listDivide([2, 4, 6, 8, 10])
    listDivide([30, 54, 63, 98, 100], divide=10)
    listDivide([])
    listDivide([1, 2, 3, 4, 5], 1)


testListDivide()
