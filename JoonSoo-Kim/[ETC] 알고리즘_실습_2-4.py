# 행렬 곱셈
def multiplyMatrix(firstMatrix: list, secondMatrix: list):
    # n x n 행렬의 resultMatrix 초기화
    number = 3
    resultMatrix = [ [0] * len(firstMatrix) for _ in range(len(firstMatrix))]
    resultMatrix = [[0] * number for _ in range(number)]
    print(resultMatrix)

    # firstIndex : i, secondIndex : k, thirdIndex : j
    # C[i][j] += A[i][k] * B[k][j]
    for firstIndex in range(len(firstMatrix)):
        for thirdIndex in range(len(secondMatrix[0])):
            for secondIndex in range(len(secondMatrix)):
                multiplyResult = firstMatrix[firstIndex][secondIndex] * secondMatrix[secondIndex][thirdIndex]
                resultMatrix[firstIndex][thirdIndex] += multiplyResult

    return resultMatrix


MatrixA = [[1, 2], [3, 4]]
MatrixB = [[4, 1], [1, 0]]

print(multiplyMatrix(MatrixA, MatrixB))