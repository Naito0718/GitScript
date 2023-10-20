"""
二分法

"""

#二分法
def bisection_method(f, a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        raise ValueError("区間 [a, b] で f(a) と f(b) の符号が異なる必要があります。")

    for i in range(max_iterations):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < tolerance:
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return c


def f(x):   #関数の定義
    return x ** 2 - 4

# 区間 [1, 3] で解を求める
a = 1
b = 3
solution = bisection_method(f, a, b)

print("解:", solution)
