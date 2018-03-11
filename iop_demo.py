# Extracted from https://developers.google.com/optimization/introduction/using and
# https://developers.google.com/optimization/mip/integer_opt
#
# Assembled and modified by Beichen Lyu, unbenson.lyu@gmail.com, on 03/10/2018
#
# This program is used to test the ortools package with a simple integer optimization problem.
# Note that there are only three revisions w.r.t. the lop_demo.py but their results may be far different.
#
# Portions of this page are reproduced from work created and shared by Google and used according
# to terms described in the Creative Commons 3.0 Attribution License.

##C:\Users\Beichen Lyu\Desktop\ML\or-tools_python_examples_v6.4.4495\ortools_examples>python iop_demo.py
##Number of variables = 2
##Number of constraints = 3
##Optimal objective value = 36
##
##x = 8
##y = 3
##
##C:\Users\Beichen Lyu\Desktop\ML\or-tools_python_examples_v6.4.4495\ortools_examples>python lop_demo.py
##Number of variables = 2
##Number of constraints = 3
##Optimal objective value = 37.0
##
##x =  9.0
##y =  2.5

from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
  # Step 4
  # Revision 1
  # Instantiate a mixed-integer solver, naming it SolveIntegerProblem.
  solver = pywraplp.Solver('SolveIntegerProblem',
                           pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

  # Step 1
  # Revision 2
  # x and y are integer non-negative variables.
  x = solver.IntVar(0.0, solver.infinity(), 'x')
  y = solver.IntVar(0.0, solver.infinity(), 'y')

  
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
  # Revision 3
  """Solve the problem and print the solution."""
  result_status = solver.Solve()
  # The problem has an optimal solution.
  assert result_status == pywraplp.Solver.OPTIMAL

  # The solution looks legit (when using solvers other than
  # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
  assert solver.VerifySolution(1e-7, True)

  print('Number of variables =', solver.NumVariables())
  print('Number of constraints =', solver.NumConstraints())

  # The objective value of the solution.
  print('Optimal objective value = %d' % solver.Objective().Value())
  print()
  # The value of each variable in the solution.
  variable_list = [x, y]

  for variable in variable_list:
    print('%s = %d' % (variable.name(), variable.solution_value()))

if __name__ == '__main__':
  main()
