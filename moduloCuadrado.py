def esCuadrado(sudoku):

    numeroFilas = len(sudoku)

    for fila in sudoku:

        if len(fila) != numeroFilas:
            print(f"{sudoku} no es cuadrado")
            return False


    return True