


import moduloCuadrado

import moduloValidos

import moduloFilas, moduloColumnas











def check_sudoku(sudoku):

    return moduloCuadrado.esCuadrado(sudoku) and moduloValidos.checkNumerosValidos(sudoku) and moduloFilas.checkFilas(sudoku) and moduloColumnas.checkColumnas(sudoku)


