import matplotlib.pyplot as plt
from timeit import default_timer as timer
import sys

sys.setrecursionlimit(5000)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 2080, 2100, 4096]
times = []

for n in n_values:
    start = timer()
    factorial(n)
    end = timer()
    times.append(end - start)

plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', color='b', label='Tiempo de ejecución')
plt.xscale('log')
plt.xlabel('Tamaño de entrada n')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de factorial recursivo')
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()
