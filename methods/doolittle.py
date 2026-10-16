
def doolittle(A, B):
    n = len(A)

    # Create L and U matrices
    L = [[0.0 for _ in range(n)] for _ in range(n)]
    U = [[0.0 for _ in range(n)] for _ in range(n)]

    # Diagonal elements of L = 1
    for i in range(n):
        L[i][i] = 1.0

    # LU Decomposition
    for i in range(n):

        # Calculate U
        for k in range(i, n):
            total = 0.0
            for j in range(i):
                total += L[i][j] * U[j][k]

            U[i][k] = A[i][k] - total

        # Calculate L
        for k in range(i + 1, n):
            total = 0.0
            for j in range(i):
                total += L[k][j] * U[j][i]

            if abs(U[i][i]) < 1e-12:
                raise ValueError(
                    "Zero pivot: Doolittle needs pivoting for this system."
                )

            L[k][i] = (A[k][i] - total) / U[i][i]

    # Forward substitution: L Y = B
    Y = [0.0 for _ in range(n)]

    for i in range(n):
        total = 0.0
        for j in range(i):
            total += L[i][j] * Y[j]

        Y[i] = B[i] - total

    # Backward substitution: U X = Y
    X = [0.0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        total = 0.0
        for j in range(i + 1, n):
            total += U[i][j] * X[j]

        if abs(U[i][i]) < 1e-12:
            raise ValueError(
                "Zero pivot: cannot solve this system directly."
            )

        X[i] = (Y[i] - total) / U[i][i]

    return X
A = [
    [2, 1],
    [4, 3]
]

B = [5, 11]

solution = doolittle(A, B)

print("Solution:", solution)