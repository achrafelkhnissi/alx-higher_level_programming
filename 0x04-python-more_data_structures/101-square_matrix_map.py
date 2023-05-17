#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [-4, -5, -6],
        [7, 8, 9]
    ]
    new_matrix = square_matrix_map(matrix)
    print(new_matrix)
    print(matrix)
    print("--")
    new_matrix = square_matrix_map()
    print(new_matrix)
    print(matrix)
    print("--")
    matrix = []
    new_matrix = square_matrix_map(matrix)
    print(new_matrix)
    print(matrix)
    print("--")
