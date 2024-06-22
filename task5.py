# # Daxil edilen ededin hansi ededin faktoriali oldugunu tapan proqram yazin!

# number = int(input('Ədədi daxil edin: ')) # 24
# b = 2


# count = 1
# faktorial = 1
# flag = False
# while count <= number:
#     faktorial *= count
#     count += 1
#     if number == faktorial:
#         flag = True
#         print(count - 1)
#         break
# if not flag:
#     print('bu eded hec bir ededin faktoriali deyil!')
# # print(number)
# # print(b)

# # if number % b != 0:
# #     print('bu eded hec bir ededin faktoriali deyil!')
# # else:
# #     print(b)

# # BUG

# # while True:
# #     a = int(input('0 daxil et: '))
# #     if a == 0:
# #         break
# #     print('salam')


number = int(input('Ədədi daxil edin: ')) # 24
copynum= number
a = [1]
b = 2

while b <= number:
    # print(number,b)/
    if number % b == 0:
        a.append(b)
        number //= b
    else:
        break
    b += 1
# print(a[-1])
# print(copynum % a[-1])
if a[-1] == 1:
    print('bu eded hec bir ededin faktoriali deyil!')
else:
    print(a[-1])
