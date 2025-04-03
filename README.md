# Actividad 4.1: Procesos de la vida real como distribuciones de probabilidad

## Proceso diario de interés: Minutos diarios de uso de celular

### Recolección de datos
Recopilé el tiempo de uso diario de mi celular durante el último mes y lo transformé en rangos.

![image](https://github.com/user-attachments/assets/ad38e81d-5436-44f0-a4dc-0a6cc37e08a0)
![image](https://github.com/user-attachments/assets/87339c01-971c-40c2-a2ee-beaa30c911c0)


### Histograma
Creé un histograma con los datos recolectados:

![image](https://github.com/user-attachments/assets/37efac12-1465-482e-bebf-da8a61323a85)

### ¿El histograma se parece a alguna distribución de probabilidad que conoces?
Con tan pocos datos (25 observaciones) y un patrón algo "irregular", no se aprecia una forma claramente asociada a alguna de las distribuciones más típicas (normal, Poisson, exponencial, etc.). A simple vista:
- **No parece normal**: no hay un pico central claro ni simetría marcada.
- **No parece exponencial**: la mayoría de los valores no están concentrados cerca de un extremo.
- **No luce como Poisson**: para datos discretos contables típicos de Poisson, esperaríamos un solo pico y una cola a la derecha más larga.
- Presenta varios picos (multimodal), especialmente en los rangos 423-442 y 543-562.
- Se asemeja parcialmente a una distribución gamma o log-normal, ya que tiene un sesgo hacia la derecha, pero con múltiples modas.



### Ajuste de distribuciones con Python
Utilizamos la librería `Fitter` para ajustar distribuciones comunes a los datos:

```python
# Aplicar herramienta de ajuste de distribución (Fitter)
print("Ajustando distribuciones...")
distribuciones_comunes = ['gamma', 'lognorm', 'norm', 'poisson', 'exponweib', 'weibull_max', 'weibull_min']
fitter = Fitter(datos_expandidos, distributions=distribuciones_comunes)
fitter.fit()
fitter.summary()

# Obtener la mejor distribución
mejor_distribucion = fitter.get_best(method='sumsquare_error')
print(f"Mejor distribución según suma de errores cuadráticos: {mejor_distribucion}")
```

Dandonos la siguiente salida:
```Python Shell
Ajustando distribuciones...
2025-04-03 08:44:21.174 | INFO     | fitter.fitter:_fit_single_distribution:333 - Fitted norm distribution with error=0.010134)
2025-04-03 08:44:21.177 | WARNING  | fitter.fitter:_fit_single_distribution:337 - SKIPPED poisson distribution (taking more than 30 seconds)
2025-04-03 08:44:21.179 | INFO     | fitter.fitter:_fit_single_distribution:333 - Fitted lognorm distribution with error=0.010255)
2025-04-03 08:44:21.208 | INFO     | fitter.fitter:_fit_single_distribution:333 - Fitted weibull_max distribution with error=0.010765)
2025-04-03 08:44:21.212 | INFO     | fitter.fitter:_fit_single_distribution:333 - Fitted gamma distribution with error=0.010134)
2025-04-03 08:44:21.283 | INFO     | fitter.fitter:_fit_single_distribution:333 - Fitted weibull_min distribution with error=0.010126)
2025-04-03 08:44:21.340 | INFO     | fitter.fitter:_fit_single_distribution:333 - Fitted exponweib distribution with error=0.010924)
Mejor distribución según suma de errores cuadráticos: {'weibull_min': {'c': 1.6955507667807075, 'loc': 394.51208430764405, 'scale': 164.70168117505904}}
```

### Resultados
La mejor distribución según la suma de errores cuadráticos fue `weibull_min`, con los siguientes parámetros:
- **Forma (c)**: 1.695
- **Ubicación (loc)**: 394.51
- **Escala (scale)**: 164.70

### Reflexiones sobre los parámetros y usos del modelo

#### Parámetros más apropiados que describen la distribución seleccionada
Los tres parámetros mencionados arriba son los que mejor describen tu distribución:
- El parámetro **c** (forma) de 1.695 indica que la tasa de fallo aumenta con el tiempo, ya que es mayor que 1. Esto sugiere que los valores tienden a concentrarse hacia la parte central-derecha de la distribución.
- El parámetro **loc** (394.51) representa el punto de inicio o desplazamiento de la distribución.
- El parámetro **scale** (164.70) define la dispersión o amplitud de la distribución.


#### ¿Cómo podrías utilizar el modelo creado?
- **Predicción de uso diario**: Puedo utilizar este modelo Weibull para predecir la probabilidad de que en un día determinado use mi celular por una cantidad específica de minutos. Por ejemplo, podría calcular la probabilidad de que use mi celular más de 500 minutos en un día.
- **Establecimiento de límites saludables**: Basándote en la distribución, podría identificar qué constituye un uso "normal" versus "excesivo", ayudándome a establecer límites saludables de uso del celular.
- **Planificación de tiempo**: Si estoy intentando reducir el tiempo de pantalla, el modelo puede ayudarme a establecer objetivos realistas basados en mis patrones de uso actuales.
- **Detección de cambios en hábitos**: Cualquier desviación significativa del modelo podría indicar un cambio en mis hábitos de uso (como períodos de mayor estrés, cambios en mi rutina diaria, o el efecto de intentar reducir conscientemente el uso).

#### ¿Puedes usar distribuciones de probabilidad para identificar similitudes entre varios procesos?
Sí, definitivamente puedo usar distribuciones de probabilidad para identificar similitudes entre varios procesos, especialmente cuando se trata del uso diario del celular. Por ejemplo:
- **Comparación de patrones de uso entre diferentes aplicaciones:** Podría modelar el tiempo que paso en diferentes aplicaciones (redes sociales, mensajería, juegos) con distribuciones de - probabilidad. Si dos aplicaciones muestran distribuciones similares (mismo tipo y parámetros parecidos), esto sugiere que las utilizo de manera similar.
- **Comparación de mi uso con el de otras personas:** Podría comparar mi distribución Weibull de uso del celular con la de amigos o familiares para ver quién usa más el teléfono o si tienen patrones similares.
- **Comparación de periodos de tiempo:** Puedo ajustar distribuciones para diferentes periodos (semanas laborales vs. fines de semana, o diferentes meses) y usar métricas estadísticas para determinar si mi comportamiento es consistente o cambia significativamente.
- **Identificación de cambios en hábitos:** Si de repente mi uso deja de seguir la distribución Weibull que has identificado, esto podría indicar un cambio en mis hábitos o rutina diaria.

### Conclusion
La distribución Weibull con los parámetros específicos obtenidos (forma: 1.696, ubicación: 394.51, escala: 164.70) sugiere que mi uso del celular tiene cierta consistencia pero también variabilidad predecible, lo que hace que sea un buen candidato para este tipo de modelado predictivo de comportamiento personal.
El parámetro de forma mayor que 1 indica que la probabilidad de uso aumenta hasta cierto punto y luego disminuye, lo cual es coherente con patrones típicos de uso de dispositivos móviles.
