# zad. 1

print("Napisz cos: ")

napis = input()

a = napis.count("a")

print(f"Ilość liter a: {a}")

# zad. 2

print("Podaj trzy liczby całkowite: ")

a = int(input())
b = int(input())
c = int(input())
wyn = a ** b + c

f = open("wynik.txt", "w")

f.write(str(wyn))
f.close()

f = open("wynik.txt", "r")

print(f.readline())
f.close()

# zad. 3

print("Podaj a: ")
a = int(input())

print("Podaj b: ")
b = int(input())

print("Podaj c: ")
c = int(input())

if a == b and b == c:
    print("Wszystkie liczby są równe")

elif a == b and b > c:
    print("Liczby a i b są największe")

elif a == c and c > b:
    print("Liczby a i c są największe")

elif b == c and c > a:
    print("Liczby b i c są największe")

elif a > b:
    if a > c:
        print("Liczba a jest największa")
elif a > c:
    if a > b:
        print("Liczba a jest największa")

elif b > a:
    if b > c:
        print("Liczba b jest największa")
elif b > c:
    if b > a:
        print("Liczba b jest największa")

elif c > a:
    if c > b:
        print("Liczba c jest największa")
elif c > b:
    if c > a:
        print("Liczba c jest największa")

# zad. 4

lista = [4, 5, 2.5, 11, 7.3]

for n in lista:
    print(f"{n}^2 = {n ** 2}")

# zad. 5

i = 0
num = int
parz = []

print("Podawaj liczby: ")

while i < 10:
    num = int(input())
    i = i + 1
    if (num % 2) == 0:
        parz.append(num)

print("Koniec")

print(f"Lista liczb parzystych: {parz}")
