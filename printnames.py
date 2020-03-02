from randomnames import names
import numpy as np

import random


namearray = []

x = np.random.randint(1, 100)

for name in names:

    newname = "{"+name+"}" + "," + {str(x[0])}
    namearray.append(newname)
    print(newname)
print(namearray)
