#== Alphabet ==#
MORSE_ALPHABET = {
    'A':'.-', 'B':'-...', 'C':'-.-.',
    'D':'-..', 'E':'.', 'F':'..-.',
    'G':'--.', 'H':'....', 'I':'..',
    'J':'.---', 'K':'-.-', 'L':'.-..',
    'M':'--', 'N':'-.', 'O':'---',
    'P':'.--.', 'Q':'--.-', 'R':'.-.',
    'S':'...', 'T':'-', 'U':'..-',
    'V':'...-', 'W':'.--', 'X':'-..-',
    'Y':'-.--', 'Z':'--..', '1':'.----',
    '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...',
    '8':'---..', '9':'----.', '0':'-----',
}


#== Latin to Morse ==#

# Adil Yusublu -> .- -.. .. .-.. 
# latin_text = input('Zəhmət olmasa, mətn daxil edin: ').upper() # Adil Yusublu
# morse_text = ''

# for letter in latin_text:
#     morse_symbol = MORSE_ALPHABET.get(letter) # None
#     if morse_symbol is not None:
#         # morse_text = morse_text + morse_symbol + ' ' # morse_text += morse_symbol   (i = 1, i += 1)
#         morse_text += morse_symbol + ' '
#     elif letter == ' ':
#         morse_text += letter

# print(morse_text)



#== Morse to Latin ==#

# morse_text = input('Zəhmət olmasa, Morse əlifbası ilə mətn daxil edin: ')
# latin_text = ''

# morse_alphabet_values = list(MORSE_ALPHABET.values())
# morse_alphabet_keys = list(MORSE_ALPHABET.keys())
# splitted_morse_text = morse_text.split(' ')

# print('morse_alphabet_values: ', morse_alphabet_values)
# print('---------------------------------')
# print('morse_alphabet_keys: ', morse_alphabet_keys)
# print('---------------------------------')
# print('splitted_morse_text: ', splitted_morse_text)

# counter = 0
# while counter < len(splitted_morse_text):
#     morse_symbol = splitted_morse_text[counter]
#     if morse_symbol in morse_alphabet_values:
#         index = morse_alphabet_values.index(morse_symbol)
#         latin_text += morse_alphabet_keys[index]
#     elif morse_symbol == '':
#         latin_text += ' '
#     counter += 1

# print(latin_text)


#== Factorial ==#

# number = abs(int(input('Faktorialı hesablanacaq rəqəm daxil edin: '))) # 3
# result = 1

# for num in range(1, number + 1):
#     result *= num

# print(result)


#== Sum of numbers ==#
# 123
# number = abs(int(input('Rəqəm daxil edin: '))) # -123
# str_number = str(number) # '123'
# result = 0

# for i in str_number:
#     result += int(i)

# print(-result)


#== Reverse of numbers ==#

# number = abs(int(input('Rəqəm daxil edin: ')))
# str_number = str(number)
# print(str_number[::-1])


#== Simple numbers ==#

# number = int(input('Rəqəm daxil edin: ')) # 10
# simple_number_list = []

# for i in range(1, number + 1):
#     counter = 0

#     for j in range(1, i + 1):
#         if i % j == 0:
#             counter += 1

#     if counter == 2:
#         simple_number_list.append(i)

# print(simple_number_list)


#== Method 1: ƏBOB, ƏKOB ==#

# num1 = int(input('1-ci rəqəmi daxil edin: '))
# copied_num1 = num1 # 18
# num1_dividers = []

# num2 = int(input('2-ci rəqəmi daxil edin: '))
# copied_num2 = num2 
# num2_dividers = [] # 12

# divisor = 2
# while divisor <= copied_num1:
#     if copied_num1 % divisor == 0:
#         num1_dividers.append(divisor)
#         copied_num1 = copied_num1 / divisor # 3
#         continue
#     divisor += 1


# divisor = 2
# while divisor <= copied_num2:
#     if copied_num2 % divisor == 0:
#         num2_dividers.append(divisor)
#         copied_num2 = copied_num2 / divisor
#         continue
#     divisor += 1

# common_numbers = list(set(num1_dividers) & set(num2_dividers))
# ebob = 1
# for i in common_numbers:
#     divider_count1 = num1_dividers.count(i)
#     divider_count2 = num2_dividers.count(i)

#     if divider_count1 <= divider_count2:
#         ebob *= i ** divider_count1
#     else:
#         ebob *= i ** divider_count2

# ekob = int(num1 * num2 / ebob)
# print(ebob)
# print(ekob)


#== Method 2: ƏBOB, ƏKOB (Evklid alqoritmi) ==#

# num1 = int(input('1-ci rəqəmi daxil edin: '))
# num2 = int(input('2-ci rəqəmi daxil edin: '))

# big_num = max(num1, num2)  # 75
# small_num = min(num1, num2) # 50

# while big_num != 0:
#     remainder = big_num % small_num # 0
#     if remainder == 0:
#         ebob = small_num
#         break

#     big_num = small_num # 50
#     small_num = remainder # 25

# ekob = int(num1 * num2 / ebob)
# print(ekob)
# print(ebob)
