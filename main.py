
import customtkinter as ctk
import sympy as sp

from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
)

from methods.doolittle import doolittle
from methods.gaussian_elimination import gaussian_elimination
from methods.thomas import thomas
from methods.jacobi import jacobi
from methods.gauss_seidel import gauss_seidel


# ==========================================
# 1. Colors and App Settings
# ==========================================

BG = "#F5F6F3"
CARD = "#FFFFFF"
GREEN = "#58765E"
GREEN_HOVER = "#46634C"
LIGHT_GREEN = "#E8EFE7"
TEXT = "#303A32"
MUTED = "#758078"
BORDER = "#E0E5DE"
ERROR_COLOR = "#B94A48"

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

transformations = standard_transformations + (
    implicit_multiplication_application,
)


# ==========================================
# 2. Main Window
# ==========================================

app = ctk.CTk()
app.title("Numerical Methods Calculator")
app.geometry("950x760")
app.minsize(780, 650)
app.configure(fg_color=BG)

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)


# ==========================================
# 3. Header
# ==========================================

header = ctk.CTkFrame(
    app,
    fg_color=CARD,
    corner_radius=0,
    border_width=1,
    border_color=BORDER,
)
header.grid(row=0, column=0, sticky="ew")
header.grid_columnconfigure(1, weight=1)

logo = ctk.CTkLabel(
    header,
    text="N",
    width=46,
    height=46,
    corner_radius=12,
    fg_color=LIGHT_GREEN,
    text_color=GREEN,
    font=("Arial", 24, "bold"),
)
logo.grid(row=0, column=0, padx=(25, 12), pady=18)

header_text = ctk.CTkFrame(
    header,
    fg_color="transparent",
)
header_text.grid(row=0, column=1, sticky="w", pady=15)

ctk.CTkLabel(
    header_text,
    text="Numerical Methods Calculator",
    font=("Arial", 23, "bold"),
    text_color=TEXT,
).pack(anchor="w")

ctk.CTkLabel(
    header_text,
    text="Solve linear systems with numerical methods",
    font=("Arial", 12),
    text_color=MUTED,
).pack(anchor="w", pady=(4, 0))


# ==========================================
# 4. Main Content
# ==========================================

content = ctk.CTkFrame(
    app,
    fg_color="transparent",
)
content.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=25,
    pady=22,
)

content.grid_columnconfigure(0, weight=1)
content.grid_rowconfigure(2, weight=3)
content.grid_rowconfigure(5, weight=2)


# ==========================================
# 5. Method Selection Card
# ==========================================

method_card = ctk.CTkFrame(
    content,
    fg_color=CARD,
    corner_radius=14,
    border_width=1,
    border_color=BORDER,
)
method_card.grid(row=0, column=0, sticky="ew", pady=(0, 16))
method_card.grid_columnconfigure(0, weight=1)

ctk.CTkLabel(
    method_card,
    text="Numerical Method",
    font=("Arial", 15, "bold"),
    text_color=TEXT,
).grid(row=0, column=0, sticky="w", padx=18, pady=(16, 5))

method_menu = ctk.CTkOptionMenu(
    method_card,
    values=[
        "Doolittle's Method",
        "Gaussian Elimination",
        "Thomas Algorithm",
        "Jacobi Method",
        "Gauss-Seidel Method",
    ],
    height=40,
    corner_radius=8,
    fg_color=GREEN,
    button_color=GREEN,
    button_hover_color=GREEN_HOVER,
    dropdown_fg_color=CARD,
    dropdown_text_color=TEXT,
    text_color="#FFFFFF",
    font=("Arial", 13),
    command=lambda choice: update_method_info(),
)
method_menu.grid(
    row=1,
    column=0,
    sticky="ew",
    padx=18,
    pady=(4, 12),
)
method_menu.set("Gaussian Elimination")


method_info = ctk.CTkLabel(
    method_card,
    text="General method for solving linear systems.",
    font=("Arial", 11),
    text_color=MUTED,
    wraplength=800,
    justify="left",
)
method_info.grid(
    row=2,
    column=0,
    sticky="w",
    padx=18,
    pady=(0, 14),
)


def update_method_info():
    descriptions = {
        "Doolittle's Method":
            "Factorizes the coefficient matrix into L and U.",
        "Gaussian Elimination":
            "Solves a linear system using elimination.",
        "Thomas Algorithm":
            "Designed for tridiagonal coefficient matrices.",
        "Jacobi Method":
            "An iterative method; convergence is not guaranteed.",
        "Gauss-Seidel Method":
            "An iterative method using updated values immediately.",
    }

    method_info.configure(
        text=descriptions.get(method_menu.get(), "")
    )


# ==========================================
# 6. Equations Input Card
# ==========================================

input_card = ctk.CTkFrame(
    content,
    fg_color=CARD,
    corner_radius=14,
    border_width=1,
    border_color=BORDER,
)
input_card.grid(row=2, column=0, sticky="nsew", pady=(0, 16))
input_card.grid_columnconfigure(0, weight=1)
input_card.grid_rowconfigure(1, weight=1)

ctk.CTkLabel(
    input_card,
    text="Enter Equations",
    font=("Arial", 16, "bold"),
    text_color=TEXT,
).grid(row=0, column=0, sticky="w", padx=18, pady=(16, 4))

ctk.CTkLabel(
    input_card,
    text="Write one equation per line, using = between both sides.",
    font=("Arial", 11),
    text_color=MUTED,
).grid(row=0, column=0, sticky="w", padx=18, pady=(43, 10))

equations_box = ctk.CTkTextbox(
    input_card,
    height=150,
    corner_radius=9,
    border_width=1,
    border_color=BORDER,
    fg_color="#FBFCFA",
    text_color=TEXT,
    font=("Consolas", 15),
    wrap="none",
)
equations_box.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=18,
    pady=(0, 16),
)

equations_box.insert(
    "1.0",
    "2*x + y - z = 8\n"
    "-3*x - y + 2*z = -11\n"
    "-2*x + y + 2*z = -3",
)


# ==========================================
# 7. Action Buttons
# ==========================================

button_frame = ctk.CTkFrame(
    content,
    fg_color="transparent",
)
button_frame.grid(
    row=3,
    column=0,
    sticky="ew",
    pady=(0, 16),
)
button_frame.grid_columnconfigure((0, 1), weight=1)

solve_button = ctk.CTkButton(
    button_frame,
    text="Solve Equations",
    height=43,
    corner_radius=9,
    fg_color=GREEN,
    hover_color=GREEN_HOVER,
    text_color="#FFFFFF",
    font=("Arial", 14, "bold"),
    command=lambda: solve(),
)
solve_button.grid(row=0, column=0, sticky="ew", padx=(0, 7))

clear_button = ctk.CTkButton(
    button_frame,
    text="Clear",
    height=43,
    corner_radius=9,
    fg_color=LIGHT_GREEN,
    hover_color="#D8E4D7",
    text_color=GREEN,
    font=("Arial", 14, "bold"),
    command=lambda: clear(),
)
clear_button.grid(row=0, column=1, sticky="ew", padx=(7, 0))


# ==========================================
# 8. Results Card
# ==========================================

result_card = ctk.CTkFrame(
    content,
    fg_color=CARD,
    corner_radius=14,
    border_width=1,
    border_color=BORDER,
)
result_card.grid(row=5, column=0, sticky="nsew")
result_card.grid_columnconfigure(0, weight=1)
result_card.grid_rowconfigure(1, weight=1)

ctk.CTkLabel(
    result_card,
    text="Results",
    font=("Arial", 16, "bold"),
    text_color=TEXT,
).grid(row=0, column=0, sticky="w", padx=18, pady=(15, 8))

result_box = ctk.CTkTextbox(
    result_card,
    height=115,
    corner_radius=9,
    border_width=1,
    border_color=BORDER,
    fg_color="#FBFCFA",
    text_color=TEXT,
    font=("Consolas", 13),
    wrap="word",
)
result_box.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=18,
    pady=(0, 16),
)

result_box.insert(
    "1.0",
    "Your solution will appear here after you click Solve Equations."
)
result_box.configure(state="disabled")


def show_result(message, is_error=False):
    result_box.configure(state="normal")
    result_box.delete("1.0", "end")
    result_box.insert("1.0", message)
    result_box.configure(
        text_color=ERROR_COLOR if is_error else TEXT,
        state="disabled",
    )


# ==========================================
# 9. Equation Parser
# ==========================================

def equation_parser(line):
    if line.count("=") != 1:
        raise ValueError(f"Invalid equation: {line}")

    left, right = line.split("=")

    left_expr = parse_expr(
        left.strip(),
        transformations=transformations,
    )
    right_expr = parse_expr(
        right.strip(),
        transformations=transformations,
    )

    return sp.Eq(left_expr, right_expr, evaluate=False)


# ==========================================
# 10. Solve Function
# ==========================================

def solve():
    try:
        raw_equations = equations_box.get(
            "1.0", "end"
        ).strip()

        if not raw_equations:
            raise ValueError("Please enter the equations.")

        equations = [
            equation_parser(line.strip())
            for line in raw_equations.splitlines()
            if line.strip()
        ]

        if not equations:
            raise ValueError("No equations were entered.")

        variable_set = set()

        for equation in equations:
            variable_set.update(equation.free_symbols)

        variables = sorted(
            variable_set,
            key=lambda symbol: str(symbol),
        )

        if not variables:
            raise ValueError("No variables were found.")

        n = len(variables)

        if len(equations) != n:
            raise ValueError(
                f"Found {len(equations)} equations and {n} variables.\n"
                "Please enter an equal number of equations and variables."
            )

        A_matrix, B_matrix = sp.linear_eq_to_matrix(
            equations,
            variables,
        )

        if A_matrix.rows != A_matrix.cols:
            raise ValueError("The coefficient matrix must be square.")

        A = [
            [float(A_matrix[i, j]) for j in range(n)]
            for i in range(n)
        ]

        B = [
            float(B_matrix[i, 0])
            for i in range(n)
        ]

        method = method_menu.get()
        iterations = None

        if method == "Doolittle's Method":
            result = doolittle(A, B)

        elif method == "Gaussian Elimination":
            result = gaussian_elimination(A, B)

        elif method == "Thomas Algorithm":
            a = [0.0] * n
            b = [0.0] * n
            c = [0.0] * n

            for i in range(n):
                b[i] = A[i][i]

                if i > 0:
                    a[i] = A[i][i - 1]

                if i < n - 1:
                    c[i] = A[i][i + 1]

                for j in range(n):
                    if abs(i - j) > 1 and abs(A[i][j]) > 1e-12:
                        raise ValueError(
                            "Thomas Algorithm requires a tridiagonal matrix."
                        )

            result = thomas(a, b, c, B)

        elif method == "Jacobi Method":
            result, iterations = jacobi(A, B)

        elif method == "Gauss-Seidel Method":
            result, iterations = gauss_seidel(A, B)

        else:
            raise ValueError("Unknown numerical method.")

        if result is None or len(result) != n:
            raise ValueError("The method returned an invalid solution.")

        # Calculate residuals to check the returned approximation.
        residuals = [
            sum(A[i][j] * result[j] for j in range(n)) - B[i]
            for i in range(n)
        ]
        residual = max(abs(value) for value in residuals)

        lines = [
            f"Method: {method}",
            f"Equations: {len(equations)}",
            f"Variables: {n}",
            "",
            "Solution",
            "-" * 30,
        ]

        for variable, value in zip(variables, result):
            lines.append(f"{variable} = {value:.6f}")

        lines.extend([
            "",
            
        ])

        if iterations is not None:
            lines.append(f"Iterations: {iterations}")

            if iterations >= 100:
                lines.extend([
                    "",
                    "Warning: Check convergence before accepting this result."
                ])

        show_result("\n".join(lines))

    except Exception as error:
        show_result(f"Unable to solve:\n{error}", is_error=True)


# ==========================================
# 11. Clear Function
# ==========================================

def clear():
    equations_box.delete("1.0", "end")
    show_result(
        "Your solution will appear here after you click Solve Equations."
    )


# ==========================================
# 12. Run App
# ==========================================

app.mainloop()
