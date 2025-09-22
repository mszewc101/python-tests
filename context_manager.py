# CREATE
import os
import json
import xml

file_name = 'new_file1.txt'
with open(file_name, 'w') as f:
    f.write("New line\n")
    f.write("New line 1\n")
    f.write("New line 2\n")

# READ
with open(file_name, 'r') as f:
    lines = f.readlines()

print(lines[1])
lines[1] = "New Value\n"

# UPDATE
with open(file_name, 'a') as f:
    f.writelines(lines)

file_name1 = 'new_file2.txt'
with open(file_name1, 'a+') as f:
    f.write("Tworze plik, i dodaje do niego zawartosc gdy jeszcze nie istnieje")

os.remove(file_name)
os.remove(file_name1)

with open('example_file.json', 'r') as j:
    data = json.load(j)

print(f'Name {data['name']}')
