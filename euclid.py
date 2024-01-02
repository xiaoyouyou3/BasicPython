# TODO
def euclid(a,b):
    a = int(a)
    b = int(b)
    while  b != 0:
        r = a % b
        a = b
        b = r   
    return a

a = input("a の値を入力: ")
b = input("b の値を入力: ")

result = euclid(a,b)
print(f"最大公約数は{result}です")

import random

def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
max_try = 100000

for _ in range(max_try):
    aa = random.randint(1, 10000)
    bb = random.randint(1, 10000)
    if prime_number(aa) and prime_number(bb):
        count += 1
answer = count / max_try
print(f"素数になる確率：{answer}")