import numpy as np

if __name__ == "__main__":
    matriz_a = np.array([[1, 2],
                        [4, 5]])
    matriz_b = np.array([[3, 6],
                        [7, 8]])

    print("Matriz A:")
    print(matriz_a)
    print("Matriz B:")
    print(matriz_b)
    print("Transpuesta de A")
    print(matriz_a.transpose())
    print("Matriz inversa de A:")
    print(np.linalg.inv(matriz_a))
    print("Determinante de B")
    print(np.linalg.det(matriz_b))

    print("Suma entre matrices")
    print(matriz_a + matriz_b)
    print("Resta entre matrices")
    print(matriz_a - matriz_b)
    print("A * 2:")
    print(matriz_a * 2)
    print("B / 2:")
    print(matriz_b / 2)

    vector1 = np.array([1, 2, 3])
    vector2 = np.array([6, 5, 4])
    print(f"vector1 -> {vector1}")
    print(f"vector2 -> {vector2}")
    print("Poducto escalar:")
    print(np.dot(vector1, vector2))
    print("Producto cruz:")
    print(np.cross(vector1,vector2))
    print("Producto posición a posición:")
    print(vector1 * vector2)

    # Resolver un sistema de equiaciones lineales
    # del tipo Ax = B, por ejemplo:
    #       3x + 2y = 12
    #       x + y/3 = 3

    # Se genera una matriz con los coeficientes
    # que acompañan a las incógnitas:
    lst_incognitas = np.array( [[3,  2],
                                [1, 1/3]])
    # Se genera un vector con los valores después
    # del igual
    lst_constantes = np.array([12, 3])

    # Black Magic, el resultado es un vector que contiene los valores
    # ordenados de cada incognita: índice 0 -> x, índice 1 -> y
    lst_resultado = np.linalg.solve(lst_incognitas, lst_constantes)
    print("Sistema de ecuaciones:\n3x + 2y = 12\nx + y/3 = 3")
    print("Solución:")
    print(f"x= {lst_resultado[0]}, y={lst_resultado[1]}")
