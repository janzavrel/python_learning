import numpy as np

#plot graph of sin(x) and cos(x)
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of sin(x) and cos(x)')
plt.legend()
plt.grid(True)
plt.show()


#plot graph of tan(x)
x = np.linspace(-10, 10, 100)
y = np.tan(x)
plt.plot(x, y, label='tan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of tan(x)')
plt.ylim(-10, 10)  # Limit y-axis to avoid extreme values
plt.legend()
plt.grid(True)
plt.show()





