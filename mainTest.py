import unittest
from solver import Solver_ampl, Solver_mz

class SolverComparisonTest(unittest.TestCase):

    def test_solver_comparison_inst1(self):
        ampl_solver = Solver_ampl('tp2_new_inst1.dat')
        ampl_solution = ampl_solver.solve_ampl()

        mz_solver = Solver_mz('inst1.dzn.txt')
        mz_solution = mz_solver.solve_mz()

        # Comparaison des résultats
        self.assertEqual(ampl_solution, mz_solution)

        # Comparaison des temps d'exécution
        temps_exec_ampl = ampl_solver.temps_exec_ampl
        temps_exec_mz = mz_solver.temps_exec_mz
        print("Temps d'exécution AMPL:", temps_exec_ampl)
        print("Temps d'exécution MiniZinc:", temps_exec_mz)
        
        self.assertLess(temps_exec_ampl, temps_exec_mz)

    def test_solver_comparison_inst2(self):
        ampl_solver = Solver_ampl('tp2_new_inst2.dat')
        ampl_solution = ampl_solver.solve_ampl()

        mz_solver = Solver_mz('inst2.dzn.txt')
        mz_solution = mz_solver.solve_mz()

        # Comparaison des résultats
        self.assertEqual(ampl_solution, mz_solution)

        # Comparaison des temps d'exécution
        temps_exec_ampl = ampl_solver.temps_exec_ampl
        temps_exec_mz = mz_solver.temps_exec_mz
        print("Temps d'exécution AMPL:", temps_exec_ampl)
        print("Temps d'exécution MiniZinc:", temps_exec_mz)
        
        self.assertLess(temps_exec_ampl, temps_exec_mz)
    
    def test_solver_comparison_inst3(self):
        ampl_solver = Solver_ampl('tp2_new_inst3.dat')
        ampl_solution = ampl_solver.solve_ampl()

        mz_solver = Solver_mz('inst3.dzn.txt')
        mz_solution = mz_solver.solve_mz()

        # Comparaison des résultats
        self.assertEqual(ampl_solution, mz_solution)

        # Comparaison des temps d'exécution
        temps_exec_ampl = ampl_solver.temps_exec_ampl
        temps_exec_mz = mz_solver.temps_exec_mz
        print("Temps d'exécution AMPL:", temps_exec_ampl)
        print("Temps d'exécution MiniZinc:", temps_exec_mz)
        
        self.assertLess(temps_exec_ampl, temps_exec_mz)

if __name__ == '__main__':
    unittest.main()