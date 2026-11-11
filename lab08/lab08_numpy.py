import numpy as np
hours = np.arange(0, 22, 3)
line = np.arange(0, 1, 5)
zeros = np.zeros(6, dtype = int)
unknown_table = np.full((2, 3), -1)
identity = np.identity(3)
print(f"Часы:{hours}")
print(f"Размер:{hours.ndim}")
print(f"Количесвто элементов:{hours.size}")
print(f"Тип эл-ов массива:{hours.dtype}")




