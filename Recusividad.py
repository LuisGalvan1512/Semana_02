import matplotlib.pyplot as plt
from timeit import default_timer as timer
import sys

    
sys.setrecursionlimit(5000)


def armonica(n):
    if n == 1:
        return 1
    else:
        return 1 / n + armonica(n - 1)


n_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 3000, 4000]
times = []
results = []

for n in n_values:
    start = timer()
    result = armonica(n)
    end = timer()
    results.append(result)
    times.append(end - start)

print(f"{'n':>6} | {'H(n)':>10} | {'Tiempo (s)':>12}")
print("-" * 32)
for n, h, t in zip(n_values, results, times):
    print(f"{n:>6} | {h:10.6f} | {t:12.6f}")

# Graficamos el resultado
plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', color='g', label='Tiempo de ejecución')
plt.xscale('log')
plt.xlabel('Tamaño de entrada n')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución de la serie armónica recursiva')
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()
