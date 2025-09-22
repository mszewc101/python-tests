#### Ćwiczenie nr 2:
# Zmodyfikuj program ponizej tak aby kwota, ilosc rat oraz oprocentowanie bylo 
# wprowadzane przez uzytkownika 

# Zdefiniowanie zmiennych
kwota = float(input("Podaj kwotę: "))
ilosc_lat = int(input("Podaj ilość lat: "))
oprocentowanie = float(input("Podaj oprocentowanie: "))

# Obliczenia
kwota_koncowa = kwota * (1 + oprocentowanie / 100) ** ilosc_lat - kwota

# Wynik
print(f'Zysk wynosi {kwota_koncowa:.2f}')
