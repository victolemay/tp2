import unittest
import os
import numpy as np
from solver import Solver
#from amplpy import AMPL

#add_to_path = (r'/Applications/ampl_macos643')
#ampl = AMPL() 

class TestSolver(unittest.TestCase):

    def test_solve_ampl(self):
        solver = Solver('tp2_new_inst1.dat')
        solver.solve_ampl()

        # Vérifier que la solution obtenue est entière
        solution = solver.get_solution()
        self.assertTrue(np.allclose(solution, np.round(solution)))

        # Vérifier que la solution est optimale
        self.assertAlmostEqual(solver.get_objective(), 10510.0, places=1)

        # Vérifier que le nombre de bus utilisés est inférieur ou égal à Maxbus
        self.assertLessEqual(np.sum(solution), solver.get_max_bus())

if __name__ == '__main__':
    unittest.main()