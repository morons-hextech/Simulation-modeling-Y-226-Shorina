import numpy as np

def multiply(A,B):
    if A.shape[1] != B.shape[0]:
        print("Несовместимые размеры матриц")
        return 0
    result = np.dot(A, B)
    return result

A=np.random.randint(0, 10, size=(3, 4))
B=np.random.randint(0, 10, size=(4, 2))
print("Матрица A:")
print(A)
print("\nМатрица B:")
print(B)
print("\nРезультат A × B:")
print(multiply(A,B))
