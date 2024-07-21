import pandas as pd

# Series, DataFrame


# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# dt = pd.DataFrame(mydataset)

# print(dt)


# a = ('Python', 'Java', 'C#')

# myvar = pd.Series(a, index = ["x", "y", "z"])

# print(myvar)
# print(myvar['x'])


# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)

# print(myvar)



# myvar = pd.Series(calories, index = ["day1", "day2"])

# print(myvar)



# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar)


# pd.read_csv()
datas = pd.read_excel('file_example_XLSX_5000.xlsx')

# for k, v in datas.items():
#     print(k)
#     print(v)
# print(datas.loc[3882])


country = 'United States'
datas['Country']
n = datas[datas['Age'] >= 50]

print(type(n))



datas_csv = pd.read_csv('grades.csv')
print(type(datas_csv))
# for i in range(len(datas)):
#     print(datas.loc[i])
