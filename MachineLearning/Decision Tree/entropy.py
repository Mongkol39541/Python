# Entropy
# 31/10/2022
# Copyright (C) 2022

from matplotlib import pyplot as plt
import numpy as np

Ph = np.arange(0.0, 1.01, .01)
Pt = 1 - Ph
E = -Ph * np.log2(Ph) - Pt * np.log2(Pt)
E[np.isnan(E)] = 0
plt.plot(Ph, E)
plt.title('Toss a coin')
plt.xlabel('Probability')
plt.ylabel('Entropy')
plt.grid('on')
plt.show()