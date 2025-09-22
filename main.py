# Biblioteki wbudowane
import os
import math as funkcje_matematyczne
from random import choice

# Biblioteki dodatkowe - zainstalowane dodatkowo
import pytest

# Biblioteki własne - własne moduły
import my_module
# from my_module import get_user_input, count_earnings

print(funkcje_matematyczne.sqrt(16))
os.system('hostname')
print(funkcje_matematyczne.gcd(35, 36))
print(choice(['osoba1', 'osoba2', 'osoba3', 'osoba4']))
result = my_module.get_user_input("Kwota")
print(result)