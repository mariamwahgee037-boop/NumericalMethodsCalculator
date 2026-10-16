
def thomas(a, b, c, d):
    n = len(b)

    # Create copies to avoid changing original data
    c_star = [0.0] * n
    d_star = [0.0] * n
    x = [0.0] * n

    # Forward elimination
    if abs(b[0]) < 1e-12:
        raise ValueError("Zero pivot encountered.")

    c_star[0] = c[0] / b[0] if n > 1 else 0.0
    d_star[0] = d[0] / b[0]

    for i in range(1, n):
        denominator = b[i] - a[i] * c_star[i - 1]

        if abs(denominator) < 1e-12:
            raise ValueError("Zero pivot encountered.")

        if i < n - 1:
            c_star[i] = c[i] / denominator

        d_star[i] = (
            d[i] - a[i] * d_star[i - 1]
        ) / denominator

    # Back substitution
    x[n - 1] = d_star[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = d_star[i] - c_star[i] * x[i + 1]

    return x


# Example:
# 2x + y       = 5
# x + 3y + z   = 10
#     y + 2z   = 8

a = [0, 1, 1]  # Lower diagonal
b = [2, 3, 2]  # Main diagonal
c = [1, 1, 0]  # Upper diagonal
d = [5, 10, 8] # Right-hand side

solution = thomas(a, b, c, d)

for i, value in enumerate(solution):
    print(f"x{i + 1} = {value:.6f}")
