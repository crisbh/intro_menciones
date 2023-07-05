import numpy as np

def suma(a,n):
    suma = 0
    for i in range(n):
        for j in range(n):
            suma += a[i,j]
    return suma

n = 100
b = np.random.rand(n,n)

resultado = suma(b,n)
print(resultado)
