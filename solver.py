import amplpy
import os
import numpy as np


class Solver():

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



#MAIN
solver = Solver('tp2_new_inst1.dat')
solver.solve_ampl()


