# Cultura Digital · Flask

Aplicación educativa que muestra siete progresiones desde una lista Python y las renderiza con una plantilla Jinja. Se separó el HTML que estaba pegado al final del archivo Python para recuperar una estructura ejecutable.

## Ejecutar

Python 3.10 o posterior. Desde esta carpeta:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python "proyectoo de cultura.py"
```

Abre http://localhost:5000. El servidor usa solo la interfaz local y el depurador está desactivado.

## Archivos

- `proyectoo de cultura.py`: datos y ruta principal.
- `templates/index.html`: plantilla HTML.
- `requirements.txt`: dependencia Flask.

## Estado

Sintaxis verificada. Prueba HTTP con Flask pendiente; las descripciones son contenido de ejemplo para completar en clase.
