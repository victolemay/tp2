import unittest
import sys

##Tester si le code est correct

class TestMaFonction(unittest.TestCase):
    def test_ma_fonction(self):
        self.assertEqual(ma_fonction(2), 4) ## remplacer ma_fonction par la fonction qu'on veut tester
        self.assertEqual(ma_fonction(0), 0) ## remplacer ma_fonction par la fonction qu'on veut tester
        self.assertEqual(ma_fonction(-2), -4) ## remplacer ma_fonction par la fonction qu'on veut tester

if __name__ == 'main':
    unittest.main()
##L'exécution de ce code affichera le résultat des tests exécutés. Si tous les tests réussissent, vous verrez "OK" à la fin de la sortie. 
# Si des tests échouent, vous verrez des messages d'erreur décrivant ce qui a échoué.

##Tester si le code est efficace

# verifier si le temps de résolution est résonable (en bas de 10s)

import numpy as np
from solver import minimize
import time

# Définir la limite de temps
time_limit = 5 # 5 secondes

# Définir les options du solver
options = {'maxiter': 1000}

# Définir les contraintes et les bornes
constraints = {'type': 'ineq', 'fun': constraint}

# Définir les valeurs initiales
x0 = np.array([0.5, 0.5])

# Résoudre le problème en mesurant le temps
start_time = time.time()
res = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints, options=options)
end_time = time.time()

# Afficher la solution et le temps de résolution
if res.success:
    print("Solution optimale trouvée en {} secondes".format(end_time - start_time))
else:
    print("Aucune solution optimale trouvée dans la limite de temps imparti")


