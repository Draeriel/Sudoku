def sonNumerosEnteros(sudoku):

    for fila in sudoku:

        for numero in fila:

            if not isinstance(numero, int):
                print(f"Alguno de los valores de {sudoku} no es un número entero.")
                return False

    return True
