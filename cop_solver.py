# Extracted from https://developers.google.com/optimization/cp/cp_solver
#
# Assembled and modified by Beichen Lyu, unbenson.lyu@gmail.com, on 03/10/2018
#
# This program is used to test the ortools package with a simple constraint optimization problem.
#
# Portions of this page are reproduced from work created and shared by Google and used according
# to terms described in the Creative Commons 3.0 Attribution License.

from __future__ import print_function
import sys
from ortools.constraint_solver import pywrapcp

def main(comb):
  # Creates the solver.
  solver = pywrapcp.Solver("simple_example")
  # Creates the variables.
  num_vals = 3
  x = solver.IntVar(0, num_vals - 1, "x")
  y = solver.IntVar(0, num_vals - 1, "y")
  z = solver.IntVar(0, num_vals - 1, "z")

  # Create the constraints.
  label = ''     # Label for displaying results.

  if comb is 'A_and_B':
    # Combine constraints by "and."
    solver.Add(x != y)
    solver.Add(y != z)
    label = 'Solutions for which x != y and y != z:'

  elif comb is 'A_or_B':
    # Combine constraints by "or."
    solver.Add(solver.Max(x != y, y !=z ) == 1)
    label = 'Solutions for which x != y or y != z:'
  # Create the decision builder.
  db = solver.Phase([x, y, z], solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
  solver.Solve(db)
  print(label)
  print()
  count = 0

  while solver.NextSolution():
    count += 1
    print("Solution" , count, '\n')
    print("x = ", x.Value())
    print("y = ", y.Value())
    print("z = ", z.Value())
    print()
  print("Number of solutions: ", count)

  # Boolean combinations for two statments:
  # A: x != y
  # B: y != z
boolean_combs = ['A_and_B', 'A_or_B']

if __name__ == "__main__":
  for comb in boolean_combs:
    main(comb)
