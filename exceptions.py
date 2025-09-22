a = 10
b = 10

try:
    result = a / b
except ZeroDivisionError as e:
    print(f'Nie mozesz dzielic przez zero ponieważ: {e}')
except TypeError as e:
    print(f'nie mozesz dzielic przez litery ponieważ: {e}')
except Exception as e:
    print(f'Niestety kod nie działa bo: {e}')
else:
    print("Ten kod wywoła sie tylko gdy nie ma wyjatku")
finally:
    print("Wszystko jest ok")


oprocentowanie = 10
if oprocentowanie >= 9:
    raise Exception("Oprocentowanie jest zbyt wysokie")

# try:
#     result = a + '10'
# except TypeError as e:
#     print(f'Nie da rady dodawac roznych typow danych: {e}')

# result = a + '10'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# lista = [1, 2, 3, 4]
# print(lista[10])
# IndexError: list index out of range