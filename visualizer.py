import tkinter as tk
import random
import time

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")

        self.canvas = tk.Canvas(self.root, width=700, height=400, bg="black")
        self.canvas.pack()
        self.time_label = tk.Label(self.root, text="Tempo: --")
        self.time_label.pack()
        self.data = []
        self.generate_data()
        self.root.after(100, self.bubble_sort)


    def generate_data(self):
        self.data = [random.randint(10, 380) for _ in range(50)]
        self.draw_data(self.data)
        self.time_label.config(text="Time: --")

    def draw_data(self, data, color="blue"):
        self.canvas.delete("all")
        c_width = 800 / len(data)

        for i, value in enumerate(data):
            x0 = i * c_width
            y0 = 400 - value
            x1 = (i + 1) * c_width
            y1 = 400
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        
        self.root.update()

    def bubble_sort(self):
        data = self.data.copy()

        # Tempo real (sem animação)
        from algorithms.bubble import bubble_sort as pure_bubble_sort
        start_real = time.perf_counter()
        pure_bubble_sort(self.data.copy())
        end_real = time.perf_counter()
        real_time = end_real - start_real

        # Tempo animado (visual)
        start_anim = time.perf_counter()
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    self.draw_data(data, color="blue")
        end_anim = time.perf_counter()
        anim_time = end_anim - start_anim

        self.draw_data(data, color="blue")

        self.time_label.config(
            text=f"Real time: {real_time:.4f} s | Animation time: {anim_time:.4f} s"
        )

