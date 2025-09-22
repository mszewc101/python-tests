#### Ćwiczenie nr 5:
# Zmodyfikuj program ponizej tak aby kwota, ilosc rat oraz oprocentowanie były przechowywane
# słowniku, a następnie te wartosci wykorzystywane w obliczeniach

# Zdefiniowanie zmiennych
dane = {
    'kwota' : 10000,
    'okres' : 3,
    'oprocentowanie': 8
}

# Zestaw ze slownika ubrac w zmienne
kwota = dane['kwota']

# Obliczenia 
kwota_koncowa = kwota * (1 + dane['oprocentowanie'] / 100) ** dane['okres'] - dane['kwota']

# Wynik
print(f'Zysk wynosi {kwota_koncowa:.2f}')
