from solver import Solver_ampl
from solver import Solver_mz

#Solveur AMPL
solver = Solver_ampl('tp2_new_inst1.dat')
solver.solve_ampl()

solver = Solver_ampl('tp2_new_inst2.dat')
solver.solve_ampl()

solver = Solver_ampl('tp2_new_inst3.dat')
solver.solve_ampl()

#Solveur Minizinc
solvermz = Solver_mz('inst1.dzn.txt')
solvermz.solve_mz()

solvermz = Solver_mz('inst2.dzn.txt')
solvermz.solve_mz()

solvermz = Solver_mz('inst3.dzn.txt')
solvermz.solve_mz()