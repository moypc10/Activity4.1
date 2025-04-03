import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from fitter import Fitter

# Datos observados
rangos = ['403-422', '423-442', '443-462', '463-482', '503-522', '523-542',
          '543-562', '563-582', '583-602', '603-622', '623-642', '643-662',
          '663-682', '683-702']
frecuencias = [2, 3, 1, 2, 2, 2, 4, 1, 1, 2, 1, 1, 1, 2]

# Convertir rangos a valores numéricos (usaremos el punto medio de cada rango)
puntos_medios = []
for rango in rangos:
    inicio, fin = map(int, rango.split('-'))
    puntos_medios.append((inicio + fin) / 2)

# Expandir los datos según las frecuencias (para ajustar distribuciones)
datos_expandidos = []
for punto, frecuencia in zip(puntos_medios, frecuencias):
    datos_expandidos.extend([punto] * frecuencia)

# 4. Crear histograma de frecuencias
plt.figure(figsize=(12, 6))
plt.bar(rangos, frecuencias, color='steelblue', edgecolor='black')
plt.plot(rangos, frecuencias, color='orangered', marker='o', linestyle='-', linewidth=2)
plt.xticks(rotation=45)
plt.title('Histograma de Frecuencias')
plt.xlabel('Rangos')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()

# 5. Aplicar herramienta de ajuste de distribución (Fitter)
print("Ajustando distribuciones...")
distribuciones_comunes = ['gamma', 'lognorm', 'norm', 'poisson', 'exponweib', 'weibull_max', 'weibull_min']
fitter = Fitter(datos_expandidos, distributions=distribuciones_comunes)
fitter.fit()
fitter.summary()

# Obtener la mejor distribución
mejor_distribucion = fitter.get_best(method='sumsquare_error')
print(f"Mejor distribución según suma de errores cuadráticos: {mejor_distribucion}")
