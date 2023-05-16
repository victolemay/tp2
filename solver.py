import amplpy
import os
import numpy as np
import minizinc

class Solver_ampl():

    def __init__(self, inst):
        self.inst = inst

    def __str__(self):
        return str('Instance etudiee = ' + str(self.inst))


    def solve_ampl(self):

        ampl_env = amplpy.Environment('/Applications/ampl_macos643')
        ampl = amplpy.AMPL(ampl_env)

        model_dir = os.path.normpath('/Users/rosaliedesmeules/Desktop/AMPLSIAD')
        data1_dir = os.path.normpath('/Users/rosaliedesmeules/Desktop/AMPLSIAD')
        ampl.read(os.path.join(model_dir, 'tp2_new.mod'))

        #ampl.read(os.path.join(data1_dir, 'tp2_new_inst1.dat'))
        ampl.readData(os.path.join(data1_dir, self.inst))


        ampl.solve()

        print('Objective : {}'.format(ampl.getObjective('couttotal').value()))
        solution = ampl.getVariable('NBUS').getValues()
        print('Solution :\n' + str(solution))


class Solver_mz():

    def __init__(self, inst):
        self.inst = inst

    def __str__(self):
        return str('Instance etudiee = ' + str(self.inst))

    def solve_mz(self):

        solver = minizinc.Solver.lookup('gecode')

        model_path = os.path.normpath('C:/equipe8_TP1/modelefinal.mzn')
        problem = minizinc.Model(model_path)

        # code
        data_path = os.path.normpath('C:/equipe8_TP1/instance1final.dzn')
        instance = minizinc.Instance(data_path)

        #instance = Instance(solver, problem)
        #instance['maxbus'] = 5000

        result = solver.solve_all(problem, instance)

        print(result.status)
        print(result.statistics)
        if result.status is minizinc.Status.SATISFIED:
            print(result['NBUS'])
        else:
            print('Aucune solution trouvée')