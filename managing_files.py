# CREATE
import os

file_name = 'new_file.txt'
f = open(file_name, 'w')
print(f'Plik istnieje: {os.path.exists(file_name)}')
f.close()

# UPDATE
f = open(file_name, 'a')
f.write('Test\n')
f.write('Test1\n')
f.write('Test2\n')
f.write("Codebrainers\n")
f.write("Something\n")
f.writelines('Test3\n')
f.writelines('Test4\n')
f.close()

# READ
f = open(file_name, 'r')
# print(f.read())     # czytanie pliku w calosci
# print(f.readline())   # linija z góry, a potem kolejna, przy kolejnym wywołaniu funkcji
# print(f.readlines()[2]) # zwraca wszystkie linie z pliku w postaci listy!

for line in f.readlines():
    if 'Test' in line:
        print("Jest!")
    else:
        print("Nie ma!")

f.close()

# DELETE
os.remove(file_name)
print(f'Plik istnieje: {os.path.exists(file_name)}')
