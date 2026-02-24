import numpy as np
# Creazione di una matrice quadrata
'''A = np.array([[1, 2], [3, 4]])
# Calcolo dell'inversa della matrice
A_inv = np.linalg.inv(A)
print("Inversa di A:\n", A_inv)
# Creazione di un vettore
v = np.array([3, 4])
# Calcolo della norma del vettore
norm_v = np.linalg.norm(v)
print("Norma di v:", norm_v)  # Output: 5.0
#Questa funzione viene utilizzata per risolvere
#  un sistema lineare di equazioni della forma Ax=BAx = BAx=B, 
# dove AAA è una matrice quadrata e BBB è un vettore o una matrice.
# Creazione della matrice A e del vettore B
A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])
# Risoluzione del sistema di equazioni Ax = B
x = np.linalg.solve(A, B)
print("Soluzione x:", x)'''  # Output: [2. 3.]

#Questa funzione calcola la Trasformata di Fourier Discreta (DFT) di un array.
#  La DFT è uno strumento potente per analizzare le frequenze dei segnali.
# Creazione di un segnale
t = np.linspace(0, 1, 400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)
# Calcolo della Trasformata di Fourier
fft_sig = np.fft.fft(sig)
# Frequenze associate
freqs = np.fft.fftfreq(len(fft_sig))
print("Trasformata di Fourier:", fft_sig)
print("Frequenze associate:", freqs)