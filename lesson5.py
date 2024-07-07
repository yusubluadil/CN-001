# def add(num1, num2):
#     print('salam')
#     return num1 + num2
#     # print('salam')

# print(add(1, 2))

# # print(type(...))

# def func():
#     ...

# print(func())


# print(add(2))



# def add2(num1=0, num2=0): return num1 + num2   # Bele yazma !!!!!!


def add2(num1=0, num2=0):
    return num1 + num2

# a = int(input('num1-i daxil et: '))
# b = int(input('num2-i daxil et: '))

# print(add2(a, b))



# *args -> arguments, **kwargs -> keywordarguments


def sum_numbers(*args):
    print(args)
    # return sum(args)

# print(sum_numbers)  # funksiyalari moterizesiz cagirdigimiz zaman yaddasda tutulan yeri gosterir!
# sum_numbers([1, 2, 3, 4, 5])

# def sum_numbers(*name):
#     # print(args)
#     return sum(name)


# print(sum_numbers(1, 2, 4, 5))
# print(sum_numbers())


def bolme(*, bolunen, bolen):
    return bolunen / bolen

# print(bolme(bolunen=10, bolen=2))

def vurma(**kwargs):
    print(kwargs)


# vurma(num1=2, num2=3)


# lambda funcs

kvadrat = lambda a, b: a ** b


# print(kvadrat(2, 3))



# recursive funcs

# a = 1
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))


# a = 0

# def func3():
#     global a
#     a += 1
#     print('salam')
#     print(a)
#     print(factorial(5))

# func3()



# function docstrings #


def divide(a: int=None, b: int=None) -> float | str:
    """ Bu funksiya bölmə əməliyyatını yerinə yetirir! """

    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a / b
        return b / a
    else:
        return 'Daxil edilən ədədlər integer olmalıdır'  # xeta mesaji


a = divide(5, 5)

print(a)


def say_hi(a, b, c, /):
    print(a)
    print(b)
    print(c)
    return 'Hello!'



say_hi('a', 'b', 'c')
