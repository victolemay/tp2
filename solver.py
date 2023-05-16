import amplpy
import os
import numpy as np
import minizinc
import pandas as pd
import enum

class Solver_ampl():

    def __init__(self, inst):
        self.inst = inst

    def __str__(self):
        return str('Instance etudiee = ' + str(self.inst))

    def solve_ampl(self):

        ampl_env = amplpy.Environment('/Users/victorialemay/Desktop/ampl_macos64_1')
        ampl = amplpy.AMPL(ampl_env)

        model_dir = os.path.normpath('/Users/victorialemay/Documents/ecole/Genie_industriel/Session_6/SIAD/TP2')
        data1_dir = os.path.normpath('/Users/victorialemay/Documents/ecole/Genie_industriel/Session_6/SIAD/TP2')
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

        #appel du modèle
        model_path = os.path.normpath('/Users/victorialemay/Documents/ecole/Genie_industriel/Session_6/SIAD/TP2/tp2.mzn')
        problem = minizinc.Model(model_path)

        #création des data        
        data_path = os.path.normpath('/Users/victorialemay/Documents/ecole/Genie_industriel/Session_6/SIAD/TP2')
        data_path_inst = os.path.join(data_path, self.inst)

        instance = minizinc.Instance(solver, problem)
        
        with open(data_path_inst, 'r') as text_file:
            for line in text_file.readlines():
                line = line.strip()
                param_name, param_value = line.split('=')

                param_name = param_name.strip()
                param_value = param_value.strip(';')
                param_value = param_value.strip(']')

                if param_name == 'S':
                    S = param_value.replace('[', '').split(',')
                    S = [(s.strip()) for s in S]
                    S = enum.Enum('S', S)
                elif param_name == 'Z':
                    Z = param_value.replace('[', '').split(',')
                    Z = [(z.strip()) for z in Z]
                    Z = enum.Enum('Z', Z)

                elif param_name == 'placedispo':
                    placedispo = int(param_value)

                elif param_name == 'cfixe':
                    cfixe = int(param_value)

                elif param_name == 'salaire':
                    salaire = float(param_value)

                elif param_name == 'essence':
                    essence = float(param_value)

                elif param_name == 'vitbus':
                    vitbus = float(param_value)

                elif param_name == 'maxbus':
                    maxbus = int(param_value)

                elif param_name == 'pers':
                    pers = param_value.replace('[', '').split(',')
                    pers = [int(p.strip()) for p in pers]

                elif param_name == 'pourcentage':
                    pourcentage = param_value.replace('[', '').split(',')
                    pourcentage = [float(p.strip()) for p in pourcentage]

                elif param_name == 'distancet':
                    distancet = param_value.replace('[', '').split(',')
                    distancet = [float(d.strip()) for d in distancet]
        
        instance['S'] = S
        instance['Z'] = Z
        instance['placedispo'] = placedispo
        instance['cfixe'] = cfixe
        instance['salaire'] = salaire
        instance['essence'] = essence
        instance['vitbus'] = vitbus
        instance['maxbus'] = maxbus
        instance['pers'] = pers
        instance['pourcentage'] = pourcentage
        instance['distancet'] = distancet


        result = instance.solve()

        print('Objectif: ' + str(result['couttotal'])) 
        #print('Solution:\n' + str(result['NBUS']))

        
        print(result.status)
        print(result.statistics)
        if result.status is minizinc.Status.OPTIMAL_SOLUTION:
            print(result['NBUS'])
        else:
            print('Aucune solution trouvée')


