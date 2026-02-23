import numpy as np
#dim

# Creiamo tre array con dimensioni diverse
d1 = np.array([1, 2, 3])                 # Una linea (vettore)
d2 = np.array([[1, 2], [3, 4]])          # Un piano (matrice)
d3 = np.array([[[1], [2]], [[3], [4]]])  # Un volume (cubo)

# Stampiamo il numero di dimensioni
print(d1.ndim)  # Output: 1
print(d2.ndim)  # Output: 2
print(d3.ndim)  # Output: 3

#copy

originale = np.array([1, 2, 3])

# Creiamo una copia vera e propria
clonato = originale.copy()

# Se modifichiamo il clone, l'originale non cambia
clonato[0] = 99

print("Originale:", originale) # Rimane [1, 2, 3]
print("Clonato:", clonato)     # Diventa [99, 2, 3]

#flatten
matrice = np.array([[1, 2], [3, 4]])

# Appiattimento
vettore_piatto = matrice.flatten()

print("Originale (2D):\n", matrice)
print("Appiattito (1D):", vettore_piatto) 
# Output: [1 2 3 4]

#ravel
matrice = np.array([[10, 20], [30, 40]])

# Creiamo una vista appiattita
vista = matrice.ravel()

# Modificando la vista, cambia anche la matrice originale!
vista[0] = 99

print("Vista (1D):", vista)        # [99 20 30 40]
print("Originale (2D):\n", matrice) # [[99, 20], [30, 40]]