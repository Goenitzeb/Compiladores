import subprocess

def ejecutar_analizador(archivo):
    # Leer el archivo como texto en lugar de binario
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Ejecutar el analizador léxico
    proceso = subprocess.run(["analizador.exe"], input=contenido, capture_output=True, text=True)

    # Diccionario para contar los tokens
    conteo = {
        "KEYWORD": 0, "IDENTIFIER": 0, "NUMBER": 0,
        "OPERATOR": 0, "DELIMITER": 0, "COMMENT": 0, "STRING": 0, "UNKNOWN": 0
    }

    # Procesar la salida del analizador
    for linea in proceso.stdout.splitlines():
        partes = linea.split()
        if partes:
            tipo_token = partes[0]
            if tipo_token in conteo:
                conteo[tipo_token] += 1

    # Mostrar resultados
    print("\n📊 Resultado del análisis léxico:")
    for tipo, cantidad in conteo.items():
        print(f"{tipo}: {cantidad}")

# Nombre del archivo de entrada (código fuente a analizar)
archivo_prueba = "prueba.txt"

# Ejecutar el analizador léxico y contar los tokens
ejecutar_analizador(archivo_prueba)