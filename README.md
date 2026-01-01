## 📊 Sorting Algorithms Visualizer

Esse projeto foi desenvolvido como parte da disciplina de algoritmos e estrutura de dados da minha faculdade. 
Ele permite visualizar o funcionamento de algoritmos de ordenação, nesse caso o bubble sort, em tempo real e de forma animada.


## 🚀 Funcionalidades

- Visualização gráfica dos algoritmos
- Animação passo a passo da ordenação
- Cálculo de tempo real do algoritmo (execução pura, sem animação)
- Cálculo do tempo da animação (execução visual com delays e redraw)


## 🛠️ Tecnologias Utilizadas

| Tecnologia   | Função                       |
| ------------ | ---------------------------- |
| **Python 3** | Linguagem principal          |
| **Tkinter**  | Interface gráfica            |
| **time**     | Cálculo do tempo de execução |
| **random**   | Geração de dados aleatórios  |


## 📁 Estrutura do Projeto

```markdown
sorting-algorithms-visualizer/
│
├── algorithms/
│   └── bubble.py        # Implementação do algoritmo Bubble Sort
|   └── selection.py     # Implementação do algoritmo Selection Sort
│
├── utils/
│   └── timer.py         # Utilitário para medição de tempo
│
├── visualizer.py        # Classe responsável pela interface gráfica e visualização
├── main.py              # Arquivo principal para execução do programa
├── .gitignore           # Ignora caches e arquivos desnecessários
└── README.md
```

## 🔍 Como Funciona

- Ao iniciar o programa, um conjunto de valores aleatórios é gerado.
- O usuário visualiza cada etapa do algoritmo enquanto os elementos são comparados e trocados.
- O tempo de execução real e o de animação são exibidos na parte inferior da tela.
- O programa utiliza ```time.perf_counter()``` para calcular a duração total da execução do algoritmo, permitindo análises comparativas futuras.


## Desenvolvedor 👩‍💻

**Sarah Santos**  
- [LinkedIn](https://www.linkedin.com/in/sarah-santos-1977b5279/) 🌐



