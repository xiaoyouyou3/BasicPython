# TODO
def prime_number(number):
    is_prime = True
    
    #1以下は素数ではない
    if number <= 1:
        is_prime = False
    else:
        #割り切れたら素数ではない
        for num in range(2, int(number**0.5+1)):
            if number % num == 0:
                is_prime = False
                break
    
    return is_prime

while True:
    try:
        n = int(input("nの値を入力: "))
        if n < 0:
            raise ValueError("自然数を入力してください")
        break
    except ValueError as e:
        print("自然数を入力してください")

print(prime_number(n))