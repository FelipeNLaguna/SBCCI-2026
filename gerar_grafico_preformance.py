import matplotlib.pyplot as plt
import numpy as np

applications = ("Zip", "Core", "Sha", "Jpeg", "Linear", "Loops", "Nnet", "Parser", "Radix", "Ndp", 
              "Euclidean Cluster", "Points2Image", "Ep", "Ft", "Sp", "Fio",
                "Cubic", "Isqrt", "Lsqrt", "Deg2rad", "Rad2ded", "Susan", "Geomean")

performance_values = {
    'Full_P' : (1.06, 1.11, 0.87, 1.14, 1.02, 1.25, 1.12, 1.52, 1.30, 0.95, 0.97, 0.95, 1.45, 1.16, 0.94, 0.67, 1.41, 1.29, 1.16, 1.45, 1.40, 1.08, 1.13),
    'Full_E' : (2.91, 2.38, 2.09, 2.69, 2.79, 5.00, 3.01, 5.12, 6.47, 1.22, 1.33, 1.32, 2.87, 1.81, 0.87, 0.33, 3.46, 2.64, 2.36, 3.75, 3.88,2.34, 2.33),
    'Caipiratuning' : (1.02, 0.96, 0.86, 0.98, 0.99, 1.04, 1.08, 0.99, 0.98, 0.94, 0.97, 0.87, 1.00, 1.00, 0.81, 0.04, 1.00, 0.98, 0.99, 0.99, 1.00, 0.97, 0.84),
    'Exhaustive Search' : (1.00, 1.00, 0.87, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.97, 0.97, 0.87, 1.00, 1.00, 0.81, 0.04, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.84)
}

x = np.arange(len(applications))
width = 0.20
multiplier = 0

fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')


for attribute, measurement in performance_values.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    #ax.bar_label(rects, padding=3)
    multiplier +=1

ax.set_ylabel('Normalized Execution Time')
ax.set_title('Execution Time')
ax.set_xticks(x + width, applications, fontsize = 9, rotation = 90)
ax.legend(loc='upper left', ncols=4)
ax.set_ylim(0, 2)

plt.savefig('graphic_performance.png')