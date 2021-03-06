# Referred to https://developers.google.com/optimization/introduction/using
#
# Assembled and modified by Beichen Lyu, unbenson.lyu@gmail.com, on 03/10/2018
#
# This program is used to test the ortools package with a simple linear optimization problem.
#
# Portions of this page are reproduced from work created and shared by Google and used according
# to terms described in the Creative Commons 3.0 Attribution License.

from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
  # Step 4
  # Instantiate a Glop solver, naming it LinearExample.
  solver = pywraplp.Solver('LinearExample',
                           pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

  # Step 1
  # Create the two variables and let them take on any value.
  x = solver.NumVar(-solver.infinity(), solver.infinity(), 'x')
  y = solver.NumVar(-solver.infinity(), solver.infinity(), 'y')

  # Step 2
  # Constraint 1: x + 2y <= 14.
  constraint1 = solver.Constraint(-solver.infinity(), 14)
  constraint1.SetCoefficient(x, 1)
  constraint1.SetCoefficient(y, 2)

  # Constraint 2: 3x - y >= 0.
  constraint2 = solver.Constraint(0, solver.infinity())
  constraint2.SetCoefficient(x, 3)
  constraint2.SetCoefficient(y, -1)

  # Constraint 3: 0.5x - y <= 2.
  constraint3 = solver.Constraint(-solver.infinity(), 2)
  constraint3.SetCoefficient(x, 0.5)
  constraint3.SetCoefficient(y, -1)
 
  # Step 3
  # Objective function: 3x + 4y.
  objective = solver.Objective()
  objective.SetCoefficient(x, 3)
  objective.SetCoefficient(y, 4)
  objective.SetMaximization()

  # Step 5
  # Solve the system.
  solver.Solve()
  opt_solution = 3 * x.solution_value() + 4 * y.solution_value()
  print('Number of variables =', solver.NumVariables())
  print('Number of constraints =', solver.NumConstraints())
  # The objective value of the solution.
  print('Optimal objective value =', opt_solution)
  print()
  # The value of each variable in the solution.
  print('x = ', x.solution_value())
  print('y = ', y.solution_value())
  
if __name__ == '__main__':
  main()
