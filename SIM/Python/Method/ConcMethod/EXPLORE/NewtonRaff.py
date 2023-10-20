"""
ニュートンラフソン法

"""

"""
#ニュートン法（導関数が既知の場合）
def newton_raphson(f, f_prime, initial_guess, tolerance=1e-6, max_iterations=100):
    x = initial_guess
    for i in range(max_iterations):
        fx = f(x)
        if abs(fx) < tolerance:
            break
        fpx = f_prime(x)
        if fpx == 0:
            break
        x = x - fx / fpx
    return x

def f(x):   #関数の定義
    return x ** 2 - 4

def f_prime(x):
    return 2 * x

initial_guess = 2   #初期推測値
solution = newton_raphson(f, f_prime, initial_guess)

print("解:", solution)

"""

#ニュートン法（導関数が未知の場合）
import numpy as np

def newton_raphson(f, initial_guess, tolerance=1e-6, max_iterations=100, alpha=0.2, beta=0.8):
    dx=3.e-1    #微小量
    x = initial_guess
    for i in range(max_iterations): #100回
        fx = f(x)
        if abs(fx) < tolerance:
            break
        dfx=(f(x+dx)-f(x))/dx
        if dfx == 0:    #失敗！推測値を変えてやり直し
            break

        # バックトラッキングによるステップサイズの調整
        t = 1.0
        while abs(f(x + t * dx)) >= (1 - alpha * t) * abs(fx):
            t *= beta

        x = x - t * fx / dfx

    return x

def f(x):   #関数の定義
    return x ** 2 - 4

def f_prime(x):
    return 2 * x

initial_guess = 2   #初期推測値
solution = newton_raphson(f, initial_guess)

print("解:", solution)