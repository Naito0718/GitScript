def runge_kutta_1st_order(f, x0, y0, h, n):
    """
    1次のルンゲクッタ法により常微分方程式を数値的に解く関数

    :param f: 常微分方程式の右辺の関数 (dy/dx = f(x, y))
    :param x0: 初期x
    :param y0: 初期y
    :param h: 刻み幅
    :param n: ステップ数
    :return: 近似的な解のリスト [x0, x1, ..., xn], [y0, y1, ..., yn]
    """
    x_values = [x0]
    y_values = [y0]
    
    for i in range(n):
        x = x_values[-1]
        y = y_values[-1]
        
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)
        
        y_next = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        x_next = x + h
        
        x_values.append(x_next)
        y_values.append(y_next)
    
    return x_values, y_values

# 常微分方程式の右辺の関数 (dy/dx = x)
def f(x, y):
    return x

# 初期条件
x0 = 0
y0 = 0

# 刻み幅とステップ数
h = 0.1
n = 10

# ルンゲクッタ法で解く
x_values, y_values = runge_kutta_1st_order(f, x0, y0, h, n)

# 結果を表示
for x, y in zip(x_values, y_values):
    print(f"x: {x}, y: {y}")
