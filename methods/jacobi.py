
def jacobi(A, B, tolerance=1e-6, max_iterations=100):
    n = len(B)

    if len(A) != n or any(len(row) != n for row in A):
        raise ValueError("A must be a square matrix matching B.")

    if any(abs(A[i][i]) < 1e-12 for i in range(n)):
        raise ValueError("Jacobi requires non-zero diagonal elements.")

    X = [0.0] * n

    for iteration in range(max_iterations):
        X_new = [0.0] * n

        for i in range(n):
            total = 0.0

            for j in range(n):
                if i != j:
                    total += A[i][j] * X[j]

            X_new[i] = (B[i] - total) / A[i][i]

        error = max(
            abs(X_new[i] - X[i])
            for i in range(n)
        )

        X = X_new

        if error < tolerance:
            return X, iteration + 1

    raise ValueError(
        f"Jacobi did not converge within {max_iterations} iterations."
    )
