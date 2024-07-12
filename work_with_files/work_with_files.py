"""

r -> read,
w -> write,
a -> append,
x -> create

t -> text mode
b -> binary mode

"""


# file = open('work_with_files/data.txt')

# print(file.read())

# file.close()


# MUTLEQ YADDA SAXLA -> FAYLLARI ACDIQDAN SONRA MUTLEQ SEKILDE BAGLAMAQ LAZIMDI


# file = open('work_with_files/data2.txt', 'w')

# file.write('Python')
# file.seek(3) # Kursorun yerini deyisir
# file.write(' oyrenirem')
# print(file.tell()) # Kursorun yerini gosterir

# file.close()



file = open('work_with_files/data2.txt', 'r+')

file.write('\nPython')
print(file.read())


