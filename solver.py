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

        #appel du modèle
        model_path = os.path.normpath('/Users/victorialemay/Documents/ecole/Genie_industriel/Session_6/SIAD/TP2/tp2.mzn')
        problem = minizinc.Model(model_path)

        #création des data        
        data_path = os.path.normpath('/Users/victorialemay/Documents/ecole/Genie_industriel/Session_6/SIAD/TP2')
        data_path_inst = os.path.join(data_path, self.inst)

        instance = minizinc.Instance(solver, problem)
        S = enum.Enum('S', ['soir1', 'soir2', 'soir3', 'soir4', 'soir5', 'soir6', 'soir7', 'soir8', 'soir9', 'soir10', 'soir11'])
        instance['S'] = S
        Z = enum.Enum('Z', ['zone1', 'zone2', 'zone3', 'zone4', 'zone5'])
        
        #if self.inst == 'inst1_dzn.txt':
            #Z = enum.Enum('Z', ['zone1', 'zone2', 'zone3', 'zone4', 'zone5'])
            
        
        with open(data_path_inst, 'r') as text_file:
            for line in text_file.readlines():
                line = line.strip()
                param_name, param_value = line.split('=')

                param_name = param_name.strip()
                param_value = param_value.strip(';')
                param_value = param_value.strip(']')

                if param_name == 'placedispo':
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
        print('Solution:\n' + str(result['NBUS']))
""""
        instance = minizinc.Instance(solver, problem)
        S = enum.Enum('S', ['soir1', 'soir2', 'soir3', 'soir4', 'soir5', 'soir6', 'soir7', 'soir8', 'soir9', 'soir10', 'soir11'])
        instance['S'] = S
        
        if self.inst == 'inst1_dzn':
            Z = enum.Enum('Z', ['zone1', 'zone2', 'zone3', 'zone4', 'zone5'])
            instance['Z'] = Z
        
        
        
        data = pd.read_csv(data_path_inst, delimiter='=', header=None, names=['param', 'value'])

        placedispo = data.loc[data['param'] == 'placedispo', 'value'].values[0]
        cfixe = data.loc[data['param'] == 'cfixe', 'value'].values[0]
        salaire = data.loc[data['param'] == 'salaire', 'value'].values[0]
        esssence = data.loc[data['param'] == 'essence', 'value'].values[0]
        vitbus = data.loc[data['param'] == 'vitbus', 'value'].values[0]
        maxbus = data.loc[data['param'] == 'maxbus', 'value'].values[0]
        pers = data.loc[data['param'] == 'pers', 'value'].values[0]
        pourcentage = data.loc[data['param'] == 'pourcentage', 'value'].values[0]
        distancet = data.loc[data['param'] == 'distancet', 'value'].values[0]

        instance['placedispo'] = placedispo
        instance['cfixe'] = cfixe
        instance['salaire'] = salaire
        instance['essence'] = esssence
        instance['vitbus'] = vitbus
        instance['maxbus'] = maxbus
        instance['pers'] = pers
        instance['pourcentage'] = pourcentage
        instance['distancet'] = distancet
"""

        
        #print(result.status)
        #print(result.statistics)
        #if result.status is minizinc.Status.SATISFIED:
            #print(result['NBUS'])
        #else:
            #print('Aucune solution trouvée')


