'''
Create a BSpline curve 
Uses the Cox-de Boor recursion formula to determine the basis coefficients

NOTE: This program currently assumes a uniform knot vector. Different types of knot vectors must be accounted for
'''
from Point import Point
import matplotlib.pyplot as plotlib
import numpy

class BSpline():
    def __init__(self, control_points, degree, num_points):
        self.control_points = control_points
        self.degree = degree
        self.positions = []

        # Uniform knot vector 
        num_knots = degree + len(self.control_points) + 1
        self.knots = numpy.linspace(0, num_knots, num=num_knots)

        # Parameter values
        min_parameter = self.knots[0]
        max_parameter = self.knots[-1]
        self.parameters = numpy.linspace(min_parameter, max_parameter, num_points)

    def get_positions(self):
        def basis_function(parameter, degree, i):
            # Check for curve simplicity
            if degree == 0:
                if self.knots[i] <= parameter < self.knots[i + 1]:
                    return 1
                return 0

            # First Term
            if self.knots[i + degree] == self.knots[i]:
                term1 = 0
            else:
                term1 = ((parameter - self.knots[i]) / (self.knots[i + degree] - self.knots[i])) * basis_function(parameter, degree - 1, i)
            
            # Second Term
            if self.knots[i + degree + 1] == self.knots[i + 1]:
                term2 = 0
            else:
                term2 = ((self.knots[i + degree + 1] - parameter) / (self.knots[i + degree + 1] - self.knots[i + 1])) * basis_function(parameter, degree - 1, i + 1)

            return term1 + term2
        
        for parameter in self.parameters:
            point = Point(0,0,0)
            for i in range(len(self.control_points)):
                basis_coefficient = basis_function(parameter, self.degree, i)
                point += self.control_points[i].scalar_mul(basis_coefficient)
            self.positions.append(point)

        return self.positions

    def plot_points(self):
        '''
        Plots the spline points.
        '''
        if len(self.positions) == 0:
            print("No positions have been generated. Parameter(s) must be provided")
            return

        # Retrieve the x-components and y-components of the spline points and control points
        spline_x = [point.x_coord for point in self.positions]
        spline_y = [point.y_coord for point in self.positions]
        control_x = [point.x_coord for point in self.control_points]
        control_y = [point.y_coord for point in self.control_points]

        # Plot all points
        plotlib.scatter(spline_x, spline_y, label = "Resultant BSpline Curve")
        plotlib.plot(spline_x, spline_y, label = "Resultant BSpline Curve")
        plotlib.scatter(control_x, control_y)
        plotlib.show()