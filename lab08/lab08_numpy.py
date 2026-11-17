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

matrix = np.arange(1, 26).reshape(5, 5)
print(f"Первые три строки = {matrix[:3]}")
print(f"Форма первых трех строк = {matrix[:3].shape}")
print(f"Последние две строки: \n{matrix[-2:]}")
print(f"Форма последних двух строк = {matrix[-2:].shape}")
print(f"Первые два столбца: \n{matrix[:, :2]}")
print(f"Форма первых двух столбцов = {matrix[:, :2].shape}")
print(f"Фрагмент строк 1-3 и столбцов 2-4: \n{matrix[1:4, 2:5]}")
print(f"Форма фрагмента строк 1-3 и столбцов 2-4: {matrix[1:4, 2:5].shape}")
print(f"Угловой блок 2х2 в правом нижнем углу: \n{matrix[-2:, -2:]}")
print(f"Форма углового блока = {matrix[-2:, -2:].shape}")

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
small.matrix[0,:] = -1
small.matrix[1:, 1:] = 9
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1






numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print(f"Форма numbers: {numbers.shape}")
print(f"Форма table: {table.shape}")
print(f"Форма transposed: {transposed.shape}")

