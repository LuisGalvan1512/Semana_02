import matplotlib.pyplot as plt
import numpy as np

def towersOfHanoi(nro_disks, _from=1, _to=3, _tmp=2):
    if nro_disks == 1:
        print(f"Mover el disco {nro_disks}, desde la torre {_from} a la torre {_to}")
        return
    
    towersOfHanoi(nro_disks - 1, _from=_from, _to=_tmp, _tmp=_to)
    print(f"Mover el disco {nro_disks}, desde la torre {_from} a la torre {_to}")
    towersOfHanoi(nro_disks - 1, _from=_tmp, _to=_to, _tmp=_from)

if __name__ == "__main__":
    nro_disks = 3  
    towersOfHanoi(nro_disks)

    discos = np.arange(1, 15)
    movimientos = [2**n - 1 for n in discos]
    
    plt.figure(figsize=(8, 5))
    plt.plot(discos, movimientos, marker='o', linestyle='-', color='b', label='Movimientos necesarios')
    plt.xlabel('Número de discos')
    plt.ylabel('Movimientos')
    plt.title('Número de movimientos en la Torre de Hanoi')
    plt.grid(True)
    plt.legend()
    plt.show()
