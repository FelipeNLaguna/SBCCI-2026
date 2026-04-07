import matplotlib.pyplot as plt
import numpy as np

# 1. Configurando a fonte para o estilo acadêmico (Serif)
plt.rcParams['font.family'] = 'serif'

applications = ("Zip", "Core", "Sha", "Jpeg", "Linear", "Loops", "Nnet", "Parser", "Radix", "Ndp", 
              "Ec", "P2i", "Ep", "Ft", "Sp", "Fio",
                "Cubic", "Isqrt", "Lsqrt", "Deg2rad", "Rad2ded", "Susan", "Geomean")

performance_values = {
    'Full cores(E-->P)' : (0.92, 1.01, 1.00, 1.01, 1.09, 1.02, 0.90, 0.99, 1.02, 0.86, 1.05, 0.82, 1.00, 0.97, 0.99, 1.00, 1.05, 1.05, 1.02, 1.01, 0.98, 1.01, 0.99),
    'Full_P' : (1.08, 1.14, 0.89, 1.17, 1.09, 1.25, 1.15, 1.44, 1.37, 0.93, 0.96, 0.95, 1.32, 0.94, 0.92, 0.63, 1.43, 1.22, 1.14, 1.43, 1.31, 1.09, 1.11),
    'Full_E' : (1.06, 1.05, 0.80, 1.07, 1.24, 1.63, 1.17, 1.39, 2.19, 0.40, 0.45, 0.42, 0.82, 0.64, 0.27, 0.23, 0.93, 0.76, 0.70, 1.01, 0.99, 0.99, 0.80),
    'Caipiratuning' : (1.05, 1.01, 0.79, 1.05, 1.02, 0.94, 1.14, 1.35, 2.97, 0.38, 0.44, 0.35, 0.81, 0.75, 0.23, 0.08, 0.90, 0.75, 0.68, 0.97, 0.99, 0.97, 0.73),
    'Exhaustive Search' : (0.92, 1.00, 0.89, 1.00, 0.99, 1.00, 0.90, 0.99, 1.00, 0.38, 0.44, 0.36, 0.82, 0.64, 0.23, 0.09, 0.93, 0.76, 0.70, 1.00, 0.96, 0.99, 0.68)
}

x = np.arange(len(applications))
width = 0.17
multiplier = 0


fig, ax = plt.subplots(figsize=(14, 3), layout='constrained')
ax.grid(axis='y')
ax.set_axisbelow(True)

ymax_limit = 2.0
# Usado para printar nos lados corretos do grafico quando value>ymax_limit 
inverter = True
right_or_left = 0

for attribute, measurement in performance_values.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    
    for rect in rects:
        height = rect.get_height()
        
        if height > ymax_limit:
            if(inverter):
                right_or_left = -0.95
                inverter = False
            
            else:
                right_or_left = 0.01
                inverter = True
            
            # 2. Configurando o texto extrapolado igual à imagem
            ax.text(
                rect.get_x() + rect.get_width() + right_or_left,     
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


ax.set_ylabel('Normalized Energy', fontsize=16)
ax.set_ylim(0, ymax_limit)
ax.tick_params(axis='y', labelsize=14)


ax.set_xticks(x + width * 1.5, applications, fontsize=11, rotation=20)


ax.legend(
    loc='upper center', 
    bbox_to_anchor=(0.5, -0.15),
    ncols=6,                   
    fontsize=8, 
    frameon=True
)

plt.savefig('graphic_energy.png')
plt.savefig('graphic_energy.pdf')