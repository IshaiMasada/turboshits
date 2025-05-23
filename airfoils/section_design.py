import sys
import numpy
import matplotlib.pyplot as plotlib

# Change the list of target searches
sys.path.append('/home/imasada/code/turboshits/classes/')

# Import the Position Vector class
from Point import Point
from BSpline import BSpline
from BezierCurve import BezierCurve

# Example Usage
# Sample inputs
control_points = [Point(0,0,0), Point(2,2,0), Point(5,4,0), Point(7,4,0)]
degree = 3

num_points = 100
spline = BSpline(control_points, degree, num_points)

# Generate spline points
spline_points = spline.get_positions()

# Plot the curve
spline.plot_points()
