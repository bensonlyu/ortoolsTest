# Extracted from https://developers.google.com/optimization/mip/integer_opt_cp
#
# Assembled and modified by Beichen Lyu, unbenson.lyu@gmail.com, on 03/10/2018
#
# This program is used to test the ortools package with a constraint optimization problem as a MIP solver.
#
# Portions of this page are reproduced from work created and shared by Google and used according
# to terms described in the Creative Commons 3.0 Attribution License.


from __future__ import print_function
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import solver_parameters_pb2

def main():
  # Instantiate a CP solver.
  parameters = pywrapcp.Solver.DefaultSolverParameters()
  solver = pywrapcp.Solver("simple_CP", parameters)

  # x and y are integer non-negative variables.
  x = solver.IntVar(0, 17, 'x')
  y = solver.IntVar(0, 17, 'y')

  # Ensure that the coefficients in the constraints are integer to increase processing speed.
  solver.Add(2*x + 14*y <= 35)
  solver.Add(2*x <= 7)
  obj_expr = solver.IntVar(0, 1000, "obj_expr")
  solver.Add(obj_expr == x + 10*y)
  objective = solver.Maximize(obj_expr, 1)
  decision_builder = solver.Phase([x, y],
                                  solver.CHOOSE_FIRST_UNBOUND,
                                  solver.ASSIGN_MIN_VALUE)

  # Create a solution collector.
  collector = solver.LastSolutionCollector()
  # Add the decision variables.
  collector.Add(x)
  collector.Add(y)
  # Add the objective.
  collector.AddObjective(obj_expr)
  solver.Solve(decision_builder, [objective, collector])
  if collector.SolutionCount() > 0:
    best_solution = collector.SolutionCount() - 1
    print("Objective value:", collector.ObjectiveValue(best_solution))
    print()
    print('x= ', collector.Value(best_solution, x))
    print('y= ', collector.Value(best_solution, y))

if __name__ == '__main__':
  main()
