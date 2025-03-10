import math
import random


# 1. Sukurkite Funkciją kuri priima du int tipo kintamuosius. Juos susumuoja ir atspausdina.

def suma(x,y):
    z = x + y
    return z
print(suma(1,2))

# 2. Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina float tipo reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.

def PISq(pisq: float):
    return 9.8596
print(PISq(0))

def PISq():
    return round(math.pi ** 2, 4)

print(PISq())

def PISq():
    return round(math.pi * math.pi, 4)

print(PISq())

# 3. Sukurkite Funkciją kuri priima du int tipo kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.

def sandauga(x,y):
    z = x * y
    return z
print(sandauga(2,3))

# 4. Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
def print_list(arr):
    row = ""
    for i, num in enumerate(arr):
        row += f"{num} "
    print(row)
arr = [random.randint(1, 100) for _ in range(10)]
print_list(arr)

# 5. Sukurkite Funkciją kuri priima du int tipo kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int skaičių ir jį gražintų.

def find_min_max(skaiciai):
    min_sk = min(skaiciai)
    max_sk = max(skaiciai)
    return min_sk, max_sk
skaiciai = [random.randint(1,100) for i in range(10)]
min_sk, max_sk = find_min_max(skaiciai)
print(f"Min: {min_sk}', Max: {max_sk}")
print(skaiciai)

# 6. Sukurkite Funkciją kuri sugeneruotų random int skaičių masyvą ir jį gražintų. Funkcija priima tris int tipo kintamuosius, min, max ir length reikšmėms nustatyti.
def find_min_max_len(skaiciai):
    min_sk = min(skaiciai)
    max_sk = max(skaiciai)
    len_sk = len(skaiciai)
    return min_sk, max_sk, len_sk
skaiciai = [random.randint(1,100) for i in range(10)]
min_sk, max_sk, len_sk = find_min_max_len(skaiciai)
print(f"Min: {min_sk}', Max: {max_sk}, Length: {len_sk}")
print(skaiciai)

# 7. Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.
def sum_min_max_len(skaiciai):
    min_sk = min(skaiciai)
    max_sk = max(skaiciai)
    len_sk = len(skaiciai)
    return min_sk + max_sk + len_sk
result = sum_min_max_len(skaiciai)
print(f"Sum Min, Max, Length: {result}")
print(f"Skaiciai: {skaiciai}")

# 8. Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį (double).
def avg_min_max_len(skaiciai):
    min_sk = min(skaiciai)
    max_sk = max(skaiciai)
    len_sk = len(skaiciai)
    return (min_sk + max_sk + len_sk) / 3
result = round(avg_min_max_len(skaiciai), 2)
print(f"Avg Min, Max, Length: {result}")
print(f"Skaiciai: {skaiciai}")

# 9. Sukurkite Funkciją kuri priimtų du int skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis. Pirmas int - išoriniam ciklui, antras vidiniam.
def staciakampis():
    ilgis = random.randint(1,10)
    plotis = random.randint(1,10)
    for i in range(ilgis):
        krastine = ''
        for n in range(plotis):
            krastine += '*'
        print(krastine)
staciakampis()

# 10. Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų. Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)
def count_LS(sakinys, char=None):
    raides = 0
    tarpai = 0
    for char in sakinys:
        if char != ' ':
            raides += 1
        elif char == ' ':
            tarpai += 1
    return raides, tarpai
sakinys = "Šiandien labai graži diena"
raides, tarpai = count_LS(sakinys)
print(f"Raides: {raides}, Tarpai: {tarpai}")

# 11. Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.

def synikas(sakinys):
    return sakinys[::-1]
sakinys = "Šiandien labai graži diena"
apsuktas = synikas(sakinys)
print(apsuktas)

# 1. Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir gale. PVZ (---labas---)

def add_symbols(tekstas, simboliai="---"):
    return f"{simboliai}{tekstas}{simboliai}"
default = add_symbols("Šiandien labai graži diena", '---')
print(default)

# 2. Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu. Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75]. (apačioje yra funkcija, ją nusikopijuokite ir paleiskite, ji sugeneruos stringą, su kuriuo dirbsite)
def generateRndStr(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text
rnd_str = generateRndStr(10)
print(rnd_str)

def stulpeliu(rnd_str):
    for char in rnd_str:
        print(f"{char}")
stulpeliu(rnd_str)

def stulpeliu(rnd_str):
    length = len(rnd_str)
    i = 0
    while i < length:
        if '0' <= rnd_str[i] <= '9':
            num_str = "["
            while i < length and '0' <= rnd_str[i] <= '9':
                num_str += rnd_str[i]
                i += 1
            num_str += "]"
            print(num_str)
        else:
            print(f" {rnd_str[i]}")
            i += 1
stulpeliu(rnd_str)

# 3. Parašykite funkciją, kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių jos argumentas
# dalijasi be liekanos(išskyrus vienetą ir patį save).Pvz padavus 10 turi grąžinti 2, o padavus 20 gražintų3.
def count_divide(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    print(f"{n} dalinasi {count} kartus be lienakos")

count_divide(random.randint(1,100))

# 4. Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77. Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka, panaudodami trečio uždavinio funkciją.

# masyvas = [random.randint(33,77) for i in range (100)]
# print(masyvas)

def count_divide(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    return count

masyvas = [random.randint(33,77) for i in range (100)]
def dalikliai(x):
    return count_divide(x)

sorted_masyvas = sorted(masyvas, key=dalikliai, reverse=True)

sorted_with_counts = [(num, dalikliai(num)) for num in sorted_masyvas]

print(sorted_with_counts)


# 5. Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 333 iki 777. Naudodami 3 uždavinio funkciją iš masyvo suskaičiuokite kiek yra pirminių skaičių.
def count_divide(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    return count

masyvas2 = [random.randint(333, 777) for _ in range(100)]
pirminiai = [num for num in masyvas2 if count_divide(num) == 0]
print(f"pirminiai: {pirminiai}")
prime_count = len(pirminiai)
print(prime_count)

#8. Sugeneruokite masyvą iš trijų elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 33. Jeigu tarp trijų paskutinių elementų yra nors vienas ne pirminis skaičius, prie masyvo pridėkite dar vieną elementą- atsitiktinį skaičių nuo 1 iki 33. Vėl patikrinkite pradinę sąlygą ir jeigu reikia pridėkite dar vieną elementą. Kartokite, kol sąlyga nereikalaus pridėti elemento.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate_prime_array():
    array = [random.randint(1, 33) for _ in range(3)]

    while not all(is_prime(num) for num in array[-3:]):
        array.append(random.randint(1, 33))

    return array

prime_array = generate_prime_array()
print(prime_array)
# 9. Sugeneruokite masyvą iš 10 elementų, kurie yra masyvai iš 10 elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 100. Jeigu tokio didelio masyvo (ne atskirai mažesnių) pirminių skaičių vidurkis mažesnis už 70, suraskite masyve mažiausią skaičių (nebūtinai pirminį) ir prie jo pridėkite 3. Vėl paskaičiuokite masyvo pirminių skaičių vidurkį ir jeigu mažesnis nei 70 viską kartokite.

# def generate():
#     return [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
#
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def find_primes(arr):
#     return [num for row in arr for num in row if is_prime(num)]
#
# def average_primes(primes):
#     return sum(primes) / len(primes) if primes else 0
#
# def find_and_increment_min(arr):
#     min_value = min(min(row) for row in arr)
#     for i in range(10):
#         for j in range(10):
#             if arr[i][j] == min_value:
#                 arr[i][j] += 3
#                 return
#
# while True:
#     array = generate()
#     prime_numbers = find_primes(array)
#     avg_prime = average_primes(prime_numbers)
#
#
#     print("\nPrime Numbers Found:", prime_numbers)
#     print("\nAverage of Prime Numbers:", avg_prime)
#
#     if avg_prime >= 70:
#         break
#
#     print("\nAverage is lower than 70, increasing the smallest number and retrying...\n")
#     find_and_increment_min(array)

# 6. Sugeneruokite atsitiktinio (nuo 10 iki 20) ilgio masyvą,
# kurio visi, išskyrus paskutinį, elementai yra atsitiktiniai skaičiai nuo 0 iki 10,
# o paskutinis masyvas, kuris generuojamas pagal tokią pat salygą kaip ir pirmasis masyvas.
# Viską pakartokite atsitiktinį nuo 10 iki 30  kiekį kartų. Paskutinio masyvo paskutinis elementas yra lygus 0;
# 7. Suskaičiuokite šešto uždavinio elementų, kurie nėra masyvai, sumą. Skaičiuoti reikia visuose masyvuose ir submasyvuose.
def generate():
    arr1 = [random.randint(0,10) for i in range(random.randint(10,20)-1)]
    arr2 = [random.randint(0,10) for i in range(random.randint(10,20)-1)]
    arr1.append(arr2)
    return arr1
print()