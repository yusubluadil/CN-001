# JSON

import json

# laods, load

# with open('json_module/data.json') as file:
#     print(type(json.load(file)))
#     file.seek(0)

#     print(json.load(file))


# a: str = [1,2 ]  # Istifade etme!
# print(a)



# my_data = '{"name": "Elçin", "surname": "Bayramlı", "age": 21}'
# new_data = json.loads(my_data)

# print(new_data)
# print(type(new_data))



# dump, dumps

# data = {'name': 'Elçin', 'surname': 'Bayramlı', 'age': 21}

# json_data = json.dumps(data, ensure_ascii=False) # -> str

# print(type(json_data))


# with open('json_module/data.json', 'w+') as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)
#     json.dump(data, file, ensure_ascii=False, indent=4)




data = {'name': 'İzzət', 'surname': 'Ağayev', 'age': 21}

with open('json_module/data.json', encoding='UTF-8') as file: # Butun melumatlar
    datas = json.load(file)

print(datas)


with open('json_module/data.json', 'w', encoding='UTF-8') as file: # Yeni melumatin elave olunmasi
    datas.append(data)
    json.dump(datas, file, ensure_ascii=False, indent=4)


with open('json_module/data.json', encoding='UTF-8') as file: # Update olunmus melumatlara catmaq
    datas = json.load(file)

print(datas)






"""

Generate strong password

q daxil olunana kimi proqram icra olunsun
1 -> 12 simvoldan ibaret password (Boyuk ve kicik herfler, reqemler, Simvollar)
2 -> Emeliyyat siyahisi (elave faylda json) ---> sorgunu gonderdiyi zaman, password

"""


