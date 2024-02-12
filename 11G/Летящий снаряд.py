import numpy as np
import matplotlib.pyplot as plt

# Параметры
rho = 1.2041 # плотность воздуха, кг/м^3
C = 0.47 # коэффициент аэродинамического сопротивления
rho_c = 7200 # плотность материала снаряда, кг/м^3
d = 0.1 # диаметр сечения снаряда, м
v0 = 1000 # начальная скорость, м/с
alpha = 45 # угол наклона ствола пушки, градусы

# Переводим угол в радианы
alpha = np.deg2rad(alpha)

# Вычисляем массу и площадь сечения снаряда
m = 4 / 3 * np.pi * (d / 2) ** 3 * rho_c # масса, кг
s = np.pi * (d / 2) ** 2 # площадь сечения, м^2
# Для k = 0
def f_0(t, y):
    dx = y[2]
    dy = y[3]
    dvx = 0
    dvy = -9.8
    return np.array([dx, dy, dvx, dvy])

# Для k = C * rho * s / (2 * m)
k = C * rho * s / (2 * m)
def f_k(t, y):
    dx = y[2]
    dy = y[3]
    v = np.sqrt(y[2]**2+y[3]**2)
    dvx = -k * v * y[2]
    dvy = -9.8 - k * v * y[3]
    return np.array([dx, dy, dvx, dvy])


def runge_kutta_4(f, a, b, y_0, h):
    n = int((b - a) / h)
    t_points = np.linspace(a, b, n + 1)
    y_points = np.zeros((n + 1, len(y_0)))
    y_points[0] = y_0

    for i in range(n):
        k1 = h * f(t_points[i], y_points[i])
        k2 = h * f(t_points[i] + h / 2, y_points[i] + k1 / 2)
        k3 = h * f(t_points[i] + h / 2, y_points[i] + k2 / 2)
        k4 = h * f(t_points[i] + h, y_points[i] + k3)
        y_points[i + 1] = y_points[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t_points, y_points
fig, ax = plt.subplots(2, 2, figsize=(15, 10))

# Начальные условия
y_0 = [0, 0, v0*np.cos(alpha), v0*np.sin(alpha)]

# Без сопротивления воздуха
t_points, y_points = runge_kutta_4(f_0, 0, 150, y_0, 5)
ax[0, 0].plot(t_points, y_points[:, 0], label="x1(t)")
ax[0, 0].plot(t_points, y_points[:, 1], label="x2(t)")
ax[0, 0].set_xlabel('t')
ax[0, 0].set_title('Без сопротивления воздуха')
ax[0, 0].legend()

ax[1, 0].plot(y_points[:, 0], y_points[:, 1], label="x2(x1)")
ax[1, 0].set_xlabel('x1')
ax[1, 0].legend()

# С сопротивлением воздуха
t_points, y_points = runge_kutta_4(f_k, 0, 150, y_0, 5)
ax[0, 1].plot(t_points, y_points[:, 0], label="x1(t)")
ax[0, 1].plot(t_points, y_points[:, 1], label="x2(t)")
ax[0, 1].set_xlabel('t')
ax[0, 1].set_title('С сопротивлением воздуха')
ax[0, 1].legend()

ax[1, 1].plot(y_points[:, 0], y_points[:, 1], label="x2(x1)")
ax[1, 1].set_xlabel('x1')
ax[1, 1].legend()

plt.tight_layout()
plt.show()
