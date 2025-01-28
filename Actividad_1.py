def validar_instruccion(instruccion):
    # Verificar que la instrucción comience con "print("
    if not instruccion.strip().startswith("print("):
        return "Error: La instrucción debe comenzar con 'print('."

    # Verificar que termine con un paréntesis de cierre
    if not instruccion.strip().endswith(")"):
        return "Error: La instrucción debe terminar con un paréntesis de cierre ')'."

    # Extraer el contenido entre los paréntesis
    try:
        contenido = instruccion[instruccion.index("(") + 1 : instruccion.rindex(")")]
    except ValueError:
        return "Error: Los paréntesis están desbalanceados."

    # Verificar que las comillas estén balanceadas
    comillas_simples = contenido.count("'")
    comillas_dobles = contenido.count('"')
    if comillas_simples % 2 != 0 and comillas_dobles % 2 != 0:
        return "Error: Las comillas no están balanceadas."

    # Validar el texto dentro de las comillas
    if contenido.startswith("'") and contenido.endswith("'"):
        texto = contenido[1:-1]
    elif contenido.startswith('"') and contenido.endswith('"'):
        texto = contenido[1:-1]
    else:
        return "Error: El contenido dentro de los paréntesis debe ser una cadena válida con comillas simples o dobles."

    # Validar que el texto no contenga caracteres no válidos
    if not isinstance(texto, str):
        return "Error: El texto dentro de las comillas debe ser una cadena válida."

    return "La instrucción es válida."


# Ejemplo de uso
instruccion_usuario = input("Ingresa una instrucción en Python: ")
resultado = validar_instruccion(instruccion_usuario)
print(resultado)
