import amplpy
import os

ampl_env = amplpy.Environment()
ampl = amplpy.AMPL(ampl_env)

ampl.setOption('solver', 'gurobi')

model_dir = os.path.normpath('/Users/victorialemay/Documents/ecole/Genie_industriel/Session_6/SIAD/TP2')
ampl.read(os.path.join(model_dir, 'tp2_new.mod'))

