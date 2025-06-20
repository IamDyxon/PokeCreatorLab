import os

# Obtiene la ruta de la carpeta donde está el script
carpeta = os.getcwd()

# Recorre los archivos en esa carpeta
for nombre_archivo in os.listdir(carpeta):
    if os.path.isfile(nombre_archivo):
        nombre, extension = os.path.splitext(nombre_archivo)
        # Evitar renombrar archivos que ya tienen _shiny
        if not nombre.endswith("_shiny"):
            nuevo_nombre = f"{nombre}_shiny{extension}"
            os.rename(nombre_archivo, nuevo_nombre)
            print(f"Renombrado: {nombre_archivo} -> {nuevo_nombre}")

print("Renombrado completo.")
