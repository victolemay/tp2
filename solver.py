import amplpy
import os
import numpy as np

class Solver():

    def __init__(self, inst = 'tp2_new_inst1.dat'):
        self.inst = inst

    def __str__(self):
        return str('Instance etudiee = ' + str(self.inst))


    def solve_ampl(self):


        ampl_env = amplpy.Environment()
        ampl = amplpy.AMPL(ampl_env)

        model_dir = os.path.normpath('/Users/victorialemay/Documents/ecole/Genie_industriel/Session_6/SIAD/TP2')
        data1_dir = os.path.normpath('/Users/victorialemay/Documents/ecole/Genie_industriel/Session_6/SIAD/TP2')
        ampl.read(os.path.join(model_dir, 'tp2_new.mod'))
        ampl.read(os.path.join(data1_dir, self.inst))

#importer les data

        ampl.solve()

        print('Objective : {}'.format(ampl.getObjective('couttotal').value()))
        solution = ampl.getVariable('NBUS').getValues()
        print('Solution :\n' + str(solution))

