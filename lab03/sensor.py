c = float(input("Введите порог температуры в градусах Цельсия"))
n = int(input("Введите n - количество записей"))
errors = 0
excess = 0
max_read = float('-inf')
reads = []
i = 1
for _ in range(n):
    read = input(f'Введите показание {i} в градусах Цельсия')
    i += 1
    if read == "error":
        errors += 1
        continue
    read = float(read)
    if read > c:
        excess += 1
    if read > max_read:
        max_read = read
    reads.append(read)
print(f'пришло записей: {n}')
print(f'среди них ошибок: {errors}')
print(f'количество превышений: {excess}')
print(f'Максимальное показание: {max_read:.1f}')
print(f'среднее показание: {sum(reads) / len(reads):.1f}')
