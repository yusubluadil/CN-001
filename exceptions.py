# try, except, else and finally

# try:
#     print(5 / 0)
# except:
#     print('0-a bölmək olmaz!')

# try:
#     print(a)
#     print(5 / 0)
# except (ZeroDivisionError, NameError):
#     print('0-a bölmək olmaz və ya daxil edilən dəyişən adı təyin olunmayıb!')

# try:
#     print(a)
#     print(5 / 0)
# except ZeroDivisionError:
#     print('0-a bölmək olmaz!')
# except NameError:
#     print('Daxil edilən dəyişən adı təyin olunmayıb!')



# my_dict = {'name': 'CodeNext'}
# try:
#     my_dict['name']
# except KeyError:
#     print('Daxil edilən key dict-də mövcud deyil!')
# else:
#     print('Hər şey qaydasındadır!')


lst = [1, 2, 3, 4]

# try:
#     print(5 / 0)
# except IndexError:
#     print('Daxil edilən index list-də mövcud deyil!')
# else:
#     print('Bu blok hər zaman icra olunacaq!')


# str1 = 'Python'

# try:
#     str1[0] = 'R'
# except TypeError:
#     print('Stringlər dəyişməzdir!')
# else:
#     print('Hər şey yolundadır!')
# finally:
#     print('Hər zaman çağrılacaq!')



# try:
#     num1 = int(input('Number daxil edin: '))
#     print(f'Entered a number {num1}')
# except ValueError:
#     print('Int daxil edin!')


# num1 = int(input('Number daxil edin: '))

# try:
#     num1 = int(input('Number daxil edin: '))
#     num2 = int(input('Number daxil edin: '))
#     print(f'Entered a number {num1}')
# except (ValueError, TypeError) as e:
#     print(e)


# try:
#     print(5 / 0)
# except Exception as e:
#     print(e)


# raise
# annotation

# def divide(a: float=0.0, b: float=0.0) -> float:
#     if b == 0:
#         raise ZeroDivisionError('0-a bolmek olmaz!')
#     return a / b


# divide(10, 0)
