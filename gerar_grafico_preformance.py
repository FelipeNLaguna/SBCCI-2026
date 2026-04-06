import matplotlib.pyplot as plt
import numpy as np

# 1. Configurando a fonte para o estilo acadêmico (Serif)
plt.rcParams['font.family'] = 'serif'

applications = ("Zip", "Core", "Sha", "Jpeg", "Linear", "Loops", "Nnet", "Parser", "Radix", "Ndp", 
              "Ec", "P2i", "Ep", "Ft", "Sp", "Fio",
                "Cubic", "Isqrt", "Lsqrt", "Deg2rad", "Rad2ded", "Susan", "Geomean")

performance_values = {
    'Full cores(E-->P)' : (1.04, 0.99, 0.99, 0.99, 0.97, 0.99, 1.08, 1.00, 1.00, 1.22, 1.18, 1.32, 1.00, 1.08, 0.99, 0.98, 1.00, 1.00, 0.99, 1.00, 1.04, 1.00, 1.04),
    'Full_P' : (1.06, 1.11, 0.87, 1.14, 1.02, 1.25, 1.12, 1.52, 1.30, 0.95, 0.97, 0.95, 1.45, 1.16, 0.94, 0.67, 1.41, 1.29, 1.16, 1.45, 1.40, 1.08, 1.13),
    'Full_E' : (2.91, 2.38, 2.09, 2.69, 2.79, 5.00, 3.01, 5.12, 6.47, 1.22, 1.33, 1.32, 2.87, 1.81, 0.87, 0.33, 3.46, 2.64, 2.36, 3.75, 3.88,2.34, 2.33),
    'Caipiratuning' : (1.02, 0.96, 0.86, 0.98, 0.99, 1.04, 1.08, 0.99, 0.98, 0.94, 0.97, 0.87, 1.00, 1.00, 0.81, 0.04, 1.00, 0.98, 0.99, 0.99, 1.00, 0.97, 0.84),
    'Exhaustive Search' : (1.00, 0.99, 0.87, 0.99, 0.96, 0.99, 1.00, 1.00, 1.00, 0.97, 0.97, 0.87, 1.00, 1.00, 0.81, 0.04, 1.00, 1.00, 0.99, 1.00, 1.00, 1.00, 0.84)
}

x = np.arange(len(applications))
width = 0.17
multiplier = 0


fig, ax = plt.subplots(figsize=(20, 6), layout='constrained')

ymax_limit = 2.0 

ax.grid(axis='y')
ax.set_axisbelow(True) 

for attribute, measurement in performance_values.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    
    for rect in rects:
        height = rect.get_height()
        
        if height > ymax_limit:
            # 2. Configurando o texto extrapolado igual à imagem
            ax.text(
                rect.get_x() + rect.get_width() + 0.01,     
                ymax_limit - 0.05,       # Posição Y levemente abaixo do teto
                f'{height:.2f}',         
                ha='left',               
                va='top',                
                fontsize=14,             
                rotation=0,              # Texto na horizontal
                color='black'
            )
            
    multiplier +=1


ax.axhline(y=1, color='black', linestyle='--', linewidth=2, label='Full cores(P-->E)')


ax.set_ylabel('Normalized Execution Time', fontsize=16)
ax.set_ylim(0, ymax_limit)
ax.tick_params(axis='y', labelsize=14)


ax.set_xticks(x + width * 1.5, applications, fontsize=14, rotation=45)


ax.legend(
    loc='upper center', 
    bbox_to_anchor=(0.5, -0.15),
    ncols=6,                   
    fontsize=12, 
    frameon=True
)

plt.savefig('graphic_performance.png')
plt.savefig('graphic_performance.pdf')
