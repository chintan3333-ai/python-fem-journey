import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, color='blue', linewidth=2)
plt.title("My First Engineering Plot - Chintan")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()