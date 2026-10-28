import numpy as np

def reshape_rows(values, width):
    arr = np.asarray(values, dtype = float)
    if len(arr) % width != 0:
        return []
    return arr.reshape((len(arr) // width), width).tolist()

def block(matrix, rows, columns):
    arr = np.asarray(matrix, dtype = float)
    return arr[np.ix_(rows, columns)].tolist()

def column_means(matrix):
    if matrix == []:
        return []
    arr = np.asarray(matrix, dtype  = float)
    means = np.mean(arr, axis = 0)
    return np.round(means, 6).tolist()

def column_range(matrix, column):
    if matrix == []:
        return 0.0
    arr = np.asarray(matrix, dtype = float)
    p = arr[:, column]
    res = np.max(p) - np.min(p)
    return float(np.round(res, 6))




if __name__ == "__main__":
    values = [12, 14.5, 11, 13, 15.5, 10.5]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rows = [0, 2]
    columns = [1, 2]
    print(reshape_rows(values, 3))
    print(block(matrix, rows, columns))
    print(column_means(matrix))
    print(column_range([[1, 2], [5, 7]], 1))