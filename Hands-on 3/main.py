from parser import parser

while True:
    try:
        entrada = input("Entrada: ")
        if entrada.lower() == "salir":
            break
        resultado = parser.parse(entrada)
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Error: {e}")
