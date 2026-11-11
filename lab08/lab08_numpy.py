import numpy as np
hours = np.arange(0, 22, 3)
line = np.arange(0, 1, 5)
zeros = np.zeros(6, dtype = int)
unknown_table = np.full((2, 3), -1)
identity = np.identity(3)
print(f"Часы:{hours}")
print(f"Форма:{hours.shape}")
print(f"Размер:{hours.ndim}")
print(f"Количесвто элементов:{hours.size}")
print(f"Тип эл-ов массива:{hours.dtype}")

print(f"Третий элемент = {hours[2]}")
print(f"Последний элемент = {hours[-1]}")
print(f"лементы с индексами 2-5 = {hours[2:6]}")
print(f"Каждый второй элемент = {hours[::2]}")
print(f"Массив в обратном порядке = {hours[::-1]}")

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(f"Форма, число измерений и число элементов:{temperatures.shape,temperatures.ndim, temperatures.size})")
print(f"Значение из второй строки и третьего столбца:{temperatures[1, 2]}")
print(f"Первая строка:{temperatures[0]}")
print(f"Последний столбец:{temperatures[:, -1]}")
print(f"Первые две строки без первого столбца:{temperatures[:2, 1:]}")
print(f"Центральный фрагмент:{temperatures[:2, 1:3]}")


