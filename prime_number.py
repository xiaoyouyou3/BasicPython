a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO
prime_numbers = [a,b]
for number in prime_numbers:
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
    
    if is_prime:
        print(f"{number}は素数です")
    else:
        print(f"{number}は素数ではありません")