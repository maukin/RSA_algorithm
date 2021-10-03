import random
from math import gcd as bltin_gcd

def coprime(a, b):
    return bltin_gcd(a, b) == 1


def prime_number():
    # n = int(input("Введите верхнюю границу диапазона: "))  # ввод границы
    n = 31
    arr = []
    for i in range(n + 1):  # заполнение массива числами от 0 до n
        arr.append(i)
    # print(arr)

    arr[1] = 0  # число 1 не является простым

    i = 2
    while i ** 2 <= n:  # проверка всех элементов массива от 2 до последнего
        if arr[i] != 0:  # если элемент массива не равен 0
            j = i * 2  # следующее число, кратное i
            while j <= n:  # проверка всех элементов от j до n
                arr[j] = 0  # обнуление элемента
                j += i  # следующее число, кратное i
        i += 1  # переход к следующему числу

    arr = set(arr)  # преобразование массива в set (set удаляет все повторяющеся элементы)
    arr.remove(0)  # удаление значения 0 из сета
    print(arr)
    arr = list(arr)
    index = random.randint(0, len(arr)-1)
    num1 = arr[index]
    print("num 1 =", num1)
    arr.remove(num1)
    index = random.randint(0, len(arr) - 1)
    num2 = arr[index]
    print("num2 =", num2)
    arr.remove(num2)
    arr = set(arr)
    print(arr)
    return arr, num1, num2

arr1, p, q = prime_number()
arr1 = list(arr1)
print("p =", p)
print("q =", q)
m = p * q
print("m =", m)
f = (p - 1) * (q - 1)
print("f =", f)

e = random.choice(arr1)
print("e =", e)

flag = 1
while flag:
    if not(1 < e < f) or not coprime(e, p) or not coprime(e, p):
        print("change e")
        arr1.remove(e)
        e = random.choice(arr1)
        print("e_new =", e)
    else:
        flag = 0

for d in range(3, f, 2):
        if d * e % f == 1:
            break
print("d =", d)

n = int(input("Число: "))

cr = (n ** e) % m
print("cr =", cr)

decr = (cr ** d) % m

print("decr =", decr)
