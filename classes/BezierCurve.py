'''
Bezier Curve class for curve design
'''
from Point import Point
import math
import matplotlib.pyplot as plt

class BezierCurve():
    def __init__(self, control_points, ps_ss=None):
        self.control_points = control_points
        self.positions = []
        self.ps_ss = ps_ss
        self.degree = len(self.control_points) - 1


    def get_positions(self, parameters):
        '''
        Returns positions based on the parameters given
        '''
        # Returns the bernstein polynomial coefficient
        def basis_polynomial(parameter, iterator):
            binomial_coefficient = math.factorial(self.degree) / (math.factorial(iterator) * math.factorial(self.degree - iterator))

            return binomial_coefficient * (parameter**iterator) * ((1 - parameter)**(self.degree - iterator))

        # Clear any existing positions
        self.positions.clear()

        # Iterate Through Each Parameter Step
        for t in parameters:
            position = Point(0, 0)

            # Apply the effects of each control point to the parameter
            for idx, point in enumerate(self.control_points):
                position += point.scalar_mul(basis_polynomial(t, self.degree, idx))

            # Store the position
            self.positions.append(position)

        return self.positions


    def plot_points(self):
        '''
        Plots the positions on the curve
        '''
        if len(self.positions) == 0:
            print("No positions have been generated. Parameter(s) must be provided")
            return

        x_positions = [point.x_coord for point in self.positions]
        y_positions = [point.y_coord for point in self.positions]
        plt.scatter(x_positions, y_positions, 'o')
        plt.plot(x_positions, y_positions)
