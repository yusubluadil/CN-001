roman_to_int = {
    'I' : 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


roman_num = input('Rum rəqəmini daxil edin: ')
# XIII -> 13
# [10, 1, 1, 1]

# XX -> 20
# [10, 10]

# XIV -> 14
# [10, 1, 5]

values_list = []
for i in roman_num:
    int_num = roman_to_int.get(i)
    values_list.append(int_num)

counter = 0
result = 0
while counter < len(values_list) - 1:
    if values_list[counter] >= values_list[counter + 1]:
        result += values_list[counter]
    else:
        result -= values_list[counter]
    counter += 1
else:
    result += values_list[-1]


print(result)
