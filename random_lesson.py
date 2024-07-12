import random


# # random, randint, uniform, choice, choices, shuffle 


# print(random.random()) # -> 0 ve 1 arasi random float eded

# print(random.randint(1, 999))

# print(random.uniform(1.1, 3.4))


# # a = 5
# # b = 5
# # c = 5

# # a = b = c = 5 

# lst = ['Alma', 'Armud', 'Heyva']

# print(random.choice(lst))

# print(random.choices(lst, k=2))

# random.shuffle(lst)

# print(lst)


# a = {'ls': 123}

# print(a['lre'])




#== 1, 2, 3, 4, 5, 6 ==#

1, 5

"""
* *
 *
* *
"""

z1 = """
#####
#   #
# * #
#   #
#####
"""

z2 = """
#####
#  *#
#   #
#*  #
#####
"""

z3 = """
#####
#  *#
# * #
#*  #
#####
"""

z4 = """
#####
#* *#
#   #
#* *#
#####
"""

z5 = """
#####
#* *#
# * #
#* *#
#####
"""

z6 = """
#####
#***#
#   #
#***#
#####
"""

dice = {'1': z1, '2': z2, '3': z3, '4': z4, '5': z5, '6': z6}

CASES = (1, 2, 3, 4, 5, 6)


def random_dice1() -> str:
    return dice.get(str(random.choice(CASES)))


def random_dice2() -> str:
    return dice.get(str(random.choice(CASES)))


print(random_dice1(), random_dice2())
