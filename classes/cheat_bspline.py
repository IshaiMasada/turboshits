import numpy as np

def find_knot_span(u, degree, knots, n):
    """Find the knot span index for parameter u."""
    if u >= knots[n + 1]:  # Clamp to last span
        return n
    if u <= knots[degree]:  # Clamp to first span
        return degree
    for i in range(degree, n + 1):
        if knots[i] <= u < knots[i + 1]:
            return i
    raise ValueError("Parameter u is out of bounds.")

def de_boor(u, degree, knots, control_points):
    """Evaluate B-spline curve at parameter u using De Boor's algorithm."""
    n = len(control_points) - 1
    k = find_knot_span(u, degree, knots, n)

    d = [np.array(control_points[j]) for j in range(k - degree, k + 1)]

    for r in range(1, degree + 1):
        for j in range(degree, r - 1, -1):
            i = k - degree + j
            denom = knots[i + degree - r + 1] - knots[i]
            alpha = (u - knots[i]) / denom if denom != 0 else 0
            d[j] = (1.0 - alpha) * d[j - 1] + alpha * d[j]

    return d[degree]


degree = 3
control_points = [(0, 0), (1, 2), (3, 5), (6, 5), (7, 2), (8, 0)]
n = len(control_points) - 1

# Normalized, clamped uniform knot vector
knots = [0] * (degree + 1) + list(np.linspace(0, 1, n - degree + 1)) + [1] * (degree + 1)

# Evaluate B-spline at 100 points
curve = [de_boor(u, degree, knots, control_points) for u in np.linspace(0, 1, 100)]

# Optional plot
if __name__ == "__main__":
    import matplotlib.pyplot as plt

    x_vals, y_vals = zip(*curve)
    ctrl_x, ctrl_y = zip(*control_points)

    plt.plot(x_vals, y_vals, label="B-spline Curve")
    plt.plot(ctrl_x, ctrl_y, 'o--', label="Control Polygon")
    plt.legend()
    plt.axis('equal')
    plt.title("B-spline Curve (Robust De Boor)")
    plt.show()
