
def gauss_seidel(A, B, tolerance=1e-6, max_iterations=100):
    n = len(B)

    # 1. Validate matrix dimensions
    if len(A) != n or any(len(row) != n for row in A):
        raise ValueError("A must be a square matrix matching B.")

    # 2. Check diagonal elements
    for i in range(n):
        if abs(A[i][i]) < 1e-12:
            raise ValueError(
                "Gauss-Seidel requires non-zero diagonal elements."
            )

    # 3. Initial guess
    X = [0.0] * n

    # 4. Iterations
    for iteration in range(max_iterations):
        X_old = X.copy()

        for i in range(n):
            total = 0.0

            for j in range(n):
                if i != j:
                    total += A[i][j] * X[j]

            X[i] = (B[i] - total) / A[i][i]

        # 5. Calculate error
        error = max(
            abs(X[i] - X_old[i])
            for i in range(n)
        )

        # 6. Check convergence
        if error < tolerance:
            return X, iteration + 1

    # 7. Return approximation if not converged
    return X, max_iterations
