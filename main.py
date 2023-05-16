from solver import Solver_ampl
from solver import Solver_mz


solver = Solver_ampl('tp2_new_inst1.dat')
solver.solve_ampl()

solvermz = Solver_mz('inst1.dzn')
solvermz.solve_mz()