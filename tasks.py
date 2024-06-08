my_tpl = (1, 2, 3, 4)

index = int(input("İndeks-i daxil edin: "))
value = input("Datanı daxil edin: ")

lst = list(my_tpl)

lst[index] = value

print(tuple(lst))
