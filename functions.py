def sum_two_numbers(a, b):
    '''
    Docstring - dokumentacja
    Funkcja przyjmuje dwie liczby i zwraca ich sume
    :param a: liczba
    :param b: liczba
    '''
    return a + b

def main():
    help(sum_two_numbers)
    input("Press any key")

    # Wywolanie
    result = sum_two_numbers(2, 3)
    print(f"Wynik dzialania funkcji {result}")

    result1 = sum_two_numbers('Test', 'Test')
    print(f"Wynik dzialania funkcji {result1}")

    x = float(input("Podaj liczbe "))
    y = float(input("Podaj liczbe "))

    result2 = sum_two_numbers(x, y)
    print(f"Wynik dzialania funkcji {result2}")

    result3 = sum_two_numbers(float(10), 3)
    print(f"Wynik dzialania funkcji {result3}")

if __name__ == "__main__":
    main()
