#import benchmarking as Ben #Alias Ben
from benchmarking import Benchmarking #Importa solo lo que quiero
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt
#main
if __name__ == "__main__":
    print("Funciona")
    #Ben.Benchmarking()#Archivo.clases
    metodosOrden = MetodosOrdenamiento()
    benchmark = Benchmarking()
    
    #tam = 10000
    tamanios = [500,1000,2000]
    resultados = []
    
    for tam in tamanios:
        arreglo_base = benchmark.build_arreglo(tam)
        metodos = {
            "burbuja":metodosOrden.sortByBubble, 
            "seleccion":metodosOrden.sort_selecction
            }
        for nombre, metodo in metodos.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
            tuplaResultado = (tam,nombre,tiempo)
            resultados.append(tuplaResultado)
            
        for resultado in resultados:
            tam, nombre, tiempo = resultado
            print(f"Tamaño:{tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")
    
    tiempos_by_metodo = {
        "burbuja":[], 
        "seleccion":[]
    }
    #Clasificar los tiempos según el método
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)
        #Crear una gráfica
    fig = plt.figure(figsize=(10,6))
    #graficar una línea de tiempo para cada método
    # el x sean los tiempos obtenidos
    # el y sea el tamaño del arreglo
    
    
    for nombre, tiempos, in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label = nombre, marker='o')
        
    plt.grid()
    plt.legend()
    plt.title("Comparativa Métodos \n Pedro Pesántez - 2025-05-07 9:00")
    fig.canvas.manager.set_window_title("Pedro Pesántez - 2025-05-07 9:00")
    plt.xlabel("Tiempos obtenidos")
    plt.ylabel("Tamaños arreglo")
    plt.show()