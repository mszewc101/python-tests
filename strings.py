kurs = 'Codebrainers'
typ_kursu = 'Tester'

grupa = kurs + " " + typ_kursu
print(grupa)

print(f"{kurs} {typ_kursu}")
print('-' * 120)

# wyswietlanie apostrofow i cudzyslowiow
print("Test'Test'")
print('Test"Test"')

print('Test\'Test')
print('Test"Test')

# Znak specjalny \n
print('PierwszLinia\nDrugaLinia\nTrzeciaLinia\nCzwartaLinia\nPiataLinia')

print('PierwszaLinia\n' \
      'DrugaLinia\n' \
      'TrzeciaLinia\n' \
      'Czwarta\n' \
      'Piata\n')

print("""Test
      TEst
      Test""")

# Znak specjalny \t
print("Columna1\t\tColumna2\t\tColumna3\t\tColumna4\n"
      "1\t\t2\t\t3\t\t4")

# \a

# Wyswietlanie sciezki do katalogu
print('Informacje znajduja sie w katalogu C:\nowy katalog\testy')
print(r'Informacje znajduja sie w katalogu C:\nowy katalog\testy')
print('Copyright -> \u00A9')
print(r"Znaczek copyright jest ukryt pod tym kodem \u00A9")
print('\t \2')              # 
print(r'<html><body><h1>Test</h1></body></html>') 

4