# Electronics Toolkit · Python

Proyecto nuevo de aprendizaje creado en noviembre de 2026. Reúne seis cálculos educativos de electrónica y procesamiento básico de señales, sin dependencias externas.

## Requisitos

Python 3.10 o posterior. Ejecuta los comandos desde esta carpeta.

| Herramienta | Parámetros, en orden | Ejemplo | Resultado |
|---|---|---|---|
| Ley de Ohm | Voltaje (V), resistencia (Ω) | `python electronics.py ohm 5 1000` | 0.005 A |
| Amplificador inversor ideal | Rin (Ω), Rf (Ω) | `python electronics.py gain 1000 10000` | -10 |
| Divisor de voltaje | Vin (V), R1 (Ω), R2 (Ω) | `python electronics.py divider 5 1000 1000` | 2.5 V |
| Resistencias en paralelo | R1 (Ω), R2 (Ω) | `python electronics.py parallel 100 100` | 50 Ω |
| Constante de tiempo RC | R (Ω), C (F) | `python electronics.py rc 1000 0.000001` | 0.001 s |
| Mediana de tres lecturas | Tres lecturas positivas | `python electronics.py median 3 100 2` | 3 |

Los parámetros deben ser positivos y finitos. La mediana de este ejercicio se limita a lecturas positivas; no es un filtro general para señales con valores negativos.

## Pruebas

```powershell
python -m unittest -v
```

Se comprueban las seis operaciones y el rechazo de ceros, negativos, valores no finitos y cantidades de parámetros incorrectas. Las fórmulas usan componentes ideales; no modelan tolerancias ni saturación.
