import matplotlib
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]
nombre_linea = "mi linea"
plt.plot(x,y, label=nombre_linea, color="blue")

plt.title("primer gráfico")
plt.xlabel("Datos eje x")
plt.ylabel("Datos eje y")
plt.legend()
plt.show()