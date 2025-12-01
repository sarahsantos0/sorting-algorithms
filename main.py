# Esse é um projeto universitario de visualização de algoritmos de ordenação voltado para estudo em Python usando Tkinter.
# Algoritmos criados até o momento: Bubble Sort
# Caso queira contribuir, fique à vontade para abrir um pull request.


import time
from visualizer import SortingVisualizer
import tkinter as tk


root = tk.Tk()
app = SortingVisualizer(root)
root.mainloop()