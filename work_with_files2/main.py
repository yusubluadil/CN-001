# file = open('work_with_files2/data.txt', 'w')

# file.write('CodeNext')

# file.close()



# data = ['Mən', 'Python', 'öyrənirəm!']

# with open('work_with_files2/data.txt', 'w') as file:
#     # file.write('CodeNext')
#     file.writelines(data)


# file.write('Code')  # Xeta verecek


with open('work_with_files2/data.txt', 'a+', encoding='UTF-8') as file:
    # file.seek(26)
    print(file.readline())
    print(file.tell())

    print(file.readline())
    file.seek(0)

    print(file.readlines())
