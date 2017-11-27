import moduloEntero
import moduloRango


def checkNumerosValidos(sudoku):

    # precondiciones

    return moduloEntero.sonNumerosEnteros(sudoku) and moduloRango.numerosEnRango(sudoku)