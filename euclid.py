a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
aa = int(a)
bb = int(b)

while  bb != 0:
    r = aa % bb
    aa = bb
    bb = r   
    
print(f"{a}と{b}の最大公約数は{aa}です")