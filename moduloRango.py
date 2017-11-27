def numerosEnRango(sudoku):

    numerosValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:

        for numero in fila:

            if numero not in numerosValidos:
                print(f"alguno de los números de {sudoku} no está dentro del rango esperado.")
                return False

    return True