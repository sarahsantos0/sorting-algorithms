import time
from algorithms.bubble import bubble_sort
from visualizer import SortingVisualizer
import tkinter as tk

data = [64, 25, 12, 22, 11]
print("Original:", data)

start = time.perf_counter()
sorted_data = bubble_sort(data)
end = time.perf_counter()
elapsed = end - start

print("Ordenado:", sorted_data)
print(f"Tempo de execução: {elapsed:.6f} s")

root = tk.Tk()
app = SortingVisualizer(root)
root.mainloop()