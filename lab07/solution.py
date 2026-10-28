import numpy as np

def reshape_rows(values, width):
    arr = np.asarray(values, dtype = float)
    if len(arr) % width != 0:
        return []
    return arr.reshape((len(arr) // width), width).tolist()

def block(matrix, rows, columns):
    arr = np.asarray(matrix, dtype = float)
    return arr[np.ix_(rows, columns)].tolist()



if __name__ == "__main__":
    values = [12, 14.5, 11, 13, 15.5, 10.5]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rows = [0, 2]
    columns = [1, 2]
    print(reshape_rows(values, 3))
    print(block(matrix, rows, columns))