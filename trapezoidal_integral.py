from math import sin, pi
# --example--
# print(sin(0))
# >>> 0
# -----------
def function(f, a=0, b=1, n=100):
    h = (b - a) / n

    #計算
    answer = 0
    for i in range(1, n+1):
        answer += (h/2)*(f(a+(i-1)*h) + f(a+i*h))

    return answer

print(function(sin, 0, 0.5*pi, 50))