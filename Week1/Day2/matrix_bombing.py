# Main Solution
from pprint import pprint
import copy

def matrix_bombing_plan(matrix):

    copy_matrix = copy.deepcopy(matrix)
    bomb_dict = {}
    sum_matrix = 0

    for row_position in range(0, len(matrix)):
        for col_position in range(0, len(matrix[0])):

            if row_position > 0 and row_position < len(matrix) - 1:
                rows = (0, -1, 1)
            elif row_position > 0:
                rows = (0, -1)
            else:
                rows = (0, 1)
            if col_position > 0 and col_position < len(matrix) - 1:
                cols = (0, -1, 1)
            elif col_position > 0:
                cols = (0, -1)
            else:
                cols = (0, 1)
            for row in rows:
                for col in cols:
                    if row == col == 0:
                        copy_matrix[row_position][col_position] = copy_matrix[row_position][col_position]
                        continue
                    copy_matrix[row_position+row][col_position+col] -= copy_matrix[row_position][col_position]
                    if copy_matrix[row_position+row][col_position+col] < 0:
                        copy_matrix[row_position+row][col_position+col] = 0
            for rows_ in copy_matrix:
                for cols_ in rows_:
                    sum_matrix += cols_
            bomb_dict[(row_position, col_position)] = sum_matrix
            sum_matrix = 0
            copy_matrix = copy.deepcopy(matrix)

    return (pprint(bomb_dict))


def main():
     matrix = [[1,2,3],[4,5,6],[7,8,9]]
     print(matrix_bombing_plan(matrix))


if __name__ == "__main__":
    main()

"""
# Another solution: Избираме си каква да е големината на бомбата и я поставяме на определено място в матрицата

def matrix_bombing_plan(matrix, bomb, row_position, col_position):

    sum_matrix = 0
    bomb_dict = {}

    if row_position > 0 and row_position < len(matrix) - 1:
        rows = (0, -1, 1)
    elif row_position > 0:
        rows = (0, -1)
    else:
        rows = (0, 1)
    if col_position > 0 and col_position < len(matrix) - 1:
        cols = (0, -1, 1)
    elif col_position > 0:
        cols = (0, -1)
    else:
        cols = (0, 1)
    for row in rows:
        for col in cols:
            if row == col == 0:
                matrix[row_position][col_position] = bomb
                continue
            matrix[row_position+row][col_position+col] -= bomb
            if matrix[row_position+row][col_position+col] < 0:
                matrix[row_position+row][col_position+col] = 0
    for rows_ in matrix:
        for cols_ in rows_:
            sum_matrix += cols_
    bomb_dict[(row_position, col_position)] = sum_matrix

    return bomb_dict, matrix

def main():
     matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
     bomb = int(input("Please enter the bomb: "))
     row_position = int(input("Please enter the row_postition: "))
     col_position = int(input("Please enter the col_position: "))
     print(matrix_bombing_plan(matrix, bomb, row_position, col_position))

if __name__ == "__main__":
    main()
"""
