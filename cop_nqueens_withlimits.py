# Extracted from https://developers.google.com/optimization/cp/cp_tasks
#
# Assembled and modified by Beichen Lyu, unbenson.lyu@gmail.com, on 03/10/2018
#
# This program is used to test the ortools package with a constraint optimization problem named N-queens.
# Two functions  - solution collector (with data analysis) and (time/solution #) limit - are added.
#
# Sample commands from the windows command prompt are "python cop_queens.py" (default boardsize 8*8)
# OR "python cop_queens.py 4" (boardsize mannually set as 4*4)
#
# Portions of this page are reproduced from work created and shared by Google and used according
# to terms described in the Creative Commons 3.0 Attribution License.

from __future__ import print_function
import sys
from ortools.constraint_solver import pywrapcp

def main(board_size):
  # Creates the solver.
  solver = pywrapcp.Solver("n-queens")
  # Creates the variables.
  queens = [solver.IntVar(0, board_size - 1, "x%i" % i) for i in range(board_size)]
  # Creates the constraints.

  # All rows must be different.
  solver.Add(solver.AllDifferent(queens))

  # No two queens can be on the same diagonal.
  solver.Add(solver.AllDifferent([queens[i] + i for i in range(board_size)]))
  solver.Add(solver.AllDifferent([queens[i] - i for i in range(board_size)]))
  db = solver.Phase(queens,
                    solver.CHOOSE_FIRST_UNBOUND,
                    solver.ASSIGN_MIN_VALUE)
  # Add variables to the solution collector.
  solution = solver.Assignment()
  solution.Add(queens)
  collector = solver.AllSolutionCollector()
  collector.Add(queens)

  # Set a time limit of 15 s.
  time_limit_ms = solver.TimeLimit(15000)
  if solver.Solve(db, [time_limit_ms, collector]):
    print("Solutions found in 15 seconds: ", collector.SolutionCount())

    # To implement the limit on solution # of 100, replace the three lines above with the code below.
##  solutions_limit = solver.SolutionsLimit(100)
##  if solver.Solve(db, [solutions_limit, collector]):
##    print("Solutions found: ", collector.SolutionCount(), "\n")
    
    solution_count = collector.SolutionCount()
    # Create the solution distribution array, whose ith entry will be the number of solutions
    # that have a queen in the first entry of row i.
    sol_dist = []

    for i in range(board_size):
      sol_dist.append(0)

    for sol in range(solution_count):
      for i in range(board_size):
        if collector.Value(sol, queens[0]) == i:
          # The solution has a queen in the first entry of row i, so increment sol_
          sol_dist[i] += 1
    print("Row    Number of solutions with a queen in the row's first entry\n")

    for i in range(len(sol_dist)):
      print(str(i), "    ", str(sol_dist[i]))
  else:
    print("No solution found.")

# By default, solve the 8x8 problem.
board_size = 8

if __name__ == "__main__":
  if len(sys.argv) > 1:
    board_size = int(sys.argv[1])
  main(board_size)
