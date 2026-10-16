
def gaussian_elimination(A, B):
    n = len(A)

    # Create the augmented matrix
    M = [
        [float(A[i][j]) for j in range(n)] + [float(B[i])]
        for i in range(n)
    ]

    # Forward elimination
    for i in range(n):
        # Check for zero pivot and swap rows if needed
        pivot_row = max(range(i, n), key=lambda r: abs(M[r][i]))

        if abs(M[pivot_row][i]) < 1e-12:
            raise ValueError("The system has no unique solution.")

        M[i], M[pivot_row] = M[pivot_row], M[i]

        # Eliminate entries below the pivot
        for k in range(i + 1, n):
            factor = M[k][i] / M[i][i]

            for j in range(i, n + 1):
                M[k][j] -= factor * M[i][j]

    # Back substitution
    X = [0.0] * n

    for i in range(n - 1, -1, -1):
        total = 0.0

        for j in range(i + 1, n):
            total += M[i][j] * X[j]

        X[i] = (M[i][n] - total) / M[i][i]

    return X


# Test the method
A = [
    [2, 1],
    [4, 3]
]

B = [5, 11]

solution = gaussian_elimination(A, B)

for i, value in enumerate(solution):
    print(f"x{i + 1} = {value:.6f}")
