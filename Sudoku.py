
def validar(sud, num, f, c):
    # Verifica que el numero no se repita en la fila
    for j in range(9):
        if sud[f][j] == num:
            return False

    # Verifica que el numero no se repita en la columna
    for i in range(9):
        if sud[i][c] == num:
            return False

    # Verifica que el numero no se repita en el bloque 3x3
    inicio_f = (f // 3) * 3
    inicio_c = (c // 3) * 3

    for i in range(inicio_f, inicio_f + 3):
        for j in range(inicio_c, inicio_c + 3):
            if sud[i][j] == num:
                return False

    return True


def fi_co_disponible(sud):
    # Busca una casilla vacia
    for f in range(9):
        for c in range(9):
            if sud[f][c] == 0:
                return f, c

    # Si no hay casillas vacias, devuelve -1
    return -1, -1


def imprimir(sud):
    # Muestra el tablero de Sudoku
    for f in range(9):
        if f % 3 == 0 and f != 0:
            print("------+-------+------")

        for c in range(9):
            if c % 3 == 0 and c != 0:
                print("|", end=" ")

            print(sud[f][c] if sud[f][c] != 0 else ".", end=" ")

        print()


def sudoku(sud):
    # Busca una casilla disponible
    f, c = fi_co_disponible(sud)

    # Si no hay casillas vacias, el Sudoku esta resuelto
    if f == -1:
        return True

    # Prueba los numeros del 1 al 9
    for num in range(1, 10):
        if validar(sud, num, f, c):
            # Coloca el numero temporalmente
            sud[f][c] = num

            # Comprueba si puede resolver el resto del Sudoku
            if sudoku(sud):
                return True

            # Si no funciona, retrocede
            sud[f][c] = 0

    return False


# Tablero inicial: 0 representa una casilla vacia
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku inicial:")
imprimir(tablero)

if sudoku(tablero):
    print("\nSudoku resuelto:")
    imprimir(tablero)
else:
    print("\nNo se encontro una solucion.")
