import matplotlib.pyplot as plt
import numpy as np

# 1. Configurando a fonte para o estilo acadêmico (Serif)
plt.rcParams['font.family'] = 'serif'

applications = ("Zip", "Core", "Sha", "Jpeg", "Linear", "Loops", "Nnet", "Parser", "Radix", "Ndp", 
              "Ec", "P2i", "Ep", "Ft", "Sp", "Fio",
                "Cubic", "Isqrt", "Lsqrt", "Deg2rad", "Rad2ded", "Susan", "Geomean")

performance_values = {
    'Full cores(E-->P)' : (0.95, 1.00, 0.99, 1.00, 1.06, 1.02, 0.97, 0.99, 1.02, 1.06, 1.24, 1.09, 1.00, 1.05, 0.98, 0.98, 1.04, 1.06, 1.01, 1.00, 1.02, 1.01, 1.02),
    'Full_P' : (1.15, 1.27, 0.78, 1.34, 1.12, 1.56, 1.29, 2.20,1.79, 0.89, 0.93, 0.89, 1.92, 1.09, 0.87, 0.42, 2.01, 1.58, 1.32, 2.08, 1.84, 1.18, 1.25),
    'Full_E' : (3.08, 2.51, 1.66, 2.88, 3.45, 8.17, 3.52, 7.12, 14.19, 0.49, 0.60, 0.56, 2.37, 1.16, 0.23, 0.07, 3.23, 2.00, 1.65, 3.80, 3.86, 2.31, 1.88),
    'Caipiratuning' : (0.97, 1.02, 0.82, 1.02, 1.01, 0.95, 0.98, 1.03, 1.07, 0.48, 0.59, 0.43, 0.95, 0.95, 0.22, 0.0035, 1.02, 0.99, 1.00, 0.98, 0.97, 1.09, 0.65),
    'Exhaustive Search' : (0.95, 1.00, 0.78, 1.00, 0.99, 1.00, 0.97, 0.99, 1.00, 0.48, 0.60, 0.42, 1.00, 0.86, 0.21, 0.0038, 1.00, 1.00, 1.00, 1.00, 0.97, 1.00, 0.64)
}

x = np.arange(len(applications))
width = 0.17
multiplier = 0


fig, ax = plt.subplots(figsize=(20, 6), layout='constrained')
ax.grid(axis='y')
ax.set_axisbelow(True)

ymax_limit = 2.5 

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


ax.set_ylabel('Normalized EDP', fontsize=16)
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

plt.savefig('graphic_edp.png')
plt.savefig('graphic_edp.pdf')