import numpy as np

def reshape_rows(values, width):
    a = np.asarray(values, dtype = float)
    if len(a) % width != 0:
        return []
    return a.reshape((len(a) // width), width).tolist()

if __name__ == "__main__":
    values = [12, 14.5, 11, 13, 15.5, 10.5]
    print(reshape_rows(values, width))