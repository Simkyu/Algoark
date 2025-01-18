def init_matrix(rows, columns):
    matrix = [[(i * columns) + j + 1 for j in (range(columns))] for i in range(rows)]
    return matrix

def rotate(matrix, query):
    y1, x1, y2, x2 = query
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    
    unapplied_value = matrix[y1][x1] 
    next_value = None
    min_value = matrix[y1][x1]
    for x in range(x1, x2):
        next_value = matrix[y1][x + 1]
        matrix[y1][x + 1] = unapplied_value
        unapplied_value = next_value

        min_value = min(min_value, matrix[y1][x + 1])

    for y in range(y1, y2):
        next_value = matrix[y + 1][x2]
        matrix[y + 1][x2] = unapplied_value
        unapplied_value = next_value

        min_value = min(min_value, matrix[y + 1][x2])

    for x in range(x2, x1, -1):
        next_value = matrix[y2][x - 1]
        matrix[y2][x - 1] = unapplied_value
        unapplied_value = next_value

        min_value = min(min_value, matrix[y2][x - 1])

    for y in range(y2, y1, -1):
        next_value = matrix[y - 1][x1]
        matrix[y - 1][x1] = unapplied_value
        unapplied_value = next_value

        min_value = min(min_value, matrix[y - 1][x1])
        
    return matrix, min_value


def solution(rows, columns, queries):
    answer = []
    matrix = init_matrix(rows, columns)
    for query in queries:
        matrix, min_value = rotate(matrix, query)
        answer.append(min_value)
    
    return answer