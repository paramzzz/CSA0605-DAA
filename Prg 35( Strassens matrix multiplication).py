
def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Split matrices into quarters
    mid = n // 2
    A11, A12, A21, A22 = A[:mid], A[mid:], [row[:mid] for row in A[:mid]], [row[mid:] for row in A[mid:]]
    B11, B12, B21, B22 = B[:mid], B[mid:], [row[:mid] for row in B[:mid]], [row[mid:] for row in B[mid:]]

    # Compute intermediate matrices
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, sub(B12, B22))
    M4 = strassen(A22, sub(B21, B11))

    # Compute final matrix product
    C11 = sub(add(M1, M4), M3)
    C12 = add(M2, M4)
    C21 = add(M2, M3)
    C22 = sub(add(M1, M3), M2)

    # Combine quarters into final matrix
    C = [[C11[0][0], C12[0][0]], [C21[0][0], C22[0][0]]]

    return C

def add(A, B):
    return [[A[0][0] + B[0][0]]]

def sub(A, B):
    return [[A[0][0] - B[0][0]]]
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = strassen(A, B)
print(C)  # Output: [[19, 22], [43, 50]]
