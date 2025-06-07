import numpy as np

def analyze_array(arr):
    arr = np.array(arr)
    print("Max:", np.max(arr))
    print("Min:", np.min(arr))
    print("Col Wise Min:", np.min(arr, axis=0))
    print("Col Wise Max:", np.max(arr, axis=0))
    print("Row Wise Min:", np.min(arr, axis=1))
    print("Row Wise Max:", np.max(arr, axis=1))

matrix = [
    [0, 1, 2, 3],
    [3, 4, 5, 5],
    [6, 7, 8, 8],
    [9, 0, 1, 9]
]
analyze_array(matrix)
