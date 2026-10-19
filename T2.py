def imprime(mat):
    for x in mat:
        print(x)
    print()
def valido(lab, res, f, c):
    if f >= len(lab):
        return False
    if f < 0:
        return False
    if c >= len(lab[0]):
        return False
    if c < 0:
        return False
    if res[f][c] == 1:
        return False
    if lab[f][c] == 0:
        return False
    return True
def laberB(lab, res, f, c, puntos):
    if f == 0 and c == 0:
        if valido(lab, res, f, c):
            if puntos >= 23:
                res[f][c] = 1
                print("Puntos: ", puntos)
                return True
            else:
                return False
        else:
            return False
    else:
        if valido(lab, res, f, c):
            res[f][c] = 1
            if lab[f][c] == 3:
                puntos = puntos + 3
            elif lab[f][c] == 4:
                puntos = puntos + 4
            if laberB(lab, res, f-1, c, puntos):
                return True
            elif laberB(lab, res, f, c+1, puntos):
                return True
            elif laberB(lab, res, f+1, c, puntos):
                return True
            elif laberB(lab, res, f, c-1, puntos):
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False
lab = [
    ["F", 1, 1, 3, 0, 1, 1, 1, 4],
    [3,   0, 0, 1, 0, 1, 0, 0, 1],
    [1,   1, 0, 1, 1, 1, 1, 0, 1],
    [0,   1, 0, 1, 0, 0, 1, 0, 1],
    [1,   1, 1, 1, 1, 1, 3, 1, 1],
    [3,   0, 1, 0, 0, 0, 1, 0, 1],
    [1,   1, 1, 1, 3, 1, 1, 1, 1],
    [1,   0, 0, 1, 0, 1, 0, 0, 4],
    ["I", 1, 3, 1, 0, 1, 1, 1, 1]
]
res = [[0 for _ in range(9)] for _ in range(9)]
print("LABERINTO ORIGINAL")
imprime(lab)
if laberB(lab, res, 8, 0, 0):
    print("Salimos!")
    print("CAMINO DE SALIDA")
    imprime(res)
else:
    print("Quedamos atrapados")
    print("NO SE ENCONTRO CAMINO")
    imprime(res)