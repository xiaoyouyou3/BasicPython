from math import sin, pi
# --example--
# print(sin(0))
# >>> 0
# -----------
#積分範囲
a = 0
b = 0.5*pi
#分割数
n = 100
#各区間の幅
h = (b - a) / n

#計算
answer = 0
for i in range(1, n+1):
    answer += (h/2)*(sin(a+(i-1)*h) + sin(a+i*h))

print(answer)