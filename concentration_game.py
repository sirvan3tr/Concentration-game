# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:54:30 2018

@author: Sirvan
"""

import csv, random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


file = open('table.csv', 'w', newline='')
writer = csv.writer(file)
line = []

#nums = random.sample(range(1, 101), 100)

pp = PdfPages('multipagess.pdf')
for j in range(0,10):
    nums = random.sample(range(1, 101), 100)
    arr = np.array(random.sample(range(1, 11), 10))
    t = 0;
    for i in range(0,10):
        row = nums[t:t+10]
        print(row)
        arr = np.vstack([arr, row])
        writer.writerow(row)
        t += 10
    
    fig, ax = plt.subplots()
    # Hide axes
    ax.xaxis.set_visible(False) 
    ax.yaxis.set_visible(False)
    ax.table(cellText=arr,loc='center')
    
    pp.savefig()
    writer.writerow([])
    
file.close()
pp.close()



nums = random.sample(range(1, 101), 100)
t = 0;
arr = np.array(random.sample(range(1, 11), 10))
for i in range(0,10):
    row = nums[t:t+10]
    arr = np.vstack([arr, row])
    print(row)
    t += 10


pp = PdfPages('multipage.pdf')

fig, ax = plt.subplots()
# Hide axes
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False)
ax.table(cellText=arr,loc='center', bbox=None)

pp.savefig()
pp.close()