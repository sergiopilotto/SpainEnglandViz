import mplsoccer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr




pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize=(15, 10))
fig.set_facecolor('black')

pitch.lines(xstart=0, xend=105, ystart=54, yend=54, ax=ax, lw=4, color='green')
pitch.lines(xstart=0, xend=105, ystart=13.8, yend=13.8, ax=ax, lw=4, color='green')
pitch.lines(xstart=16.5, xend=88.5, ystart=43.2, yend=43.2, ax=ax, lw=4, color='green')
pitch.lines(xstart=16.5, xend=88.5, ystart=24.8, yend=24.8, ax=ax, lw=4, color='green')
pitch.lines(xstart=16.5, xend=16.5, ystart=0, yend=68, ax=ax, lw=4, color='green')
pitch.lines(xstart=88.5, xend=88.5, ystart=0, yend=68, ax=ax, lw=4, color='green')
pitch.lines(xstart=34.5, xend=34.5, ystart=0, yend=13.8, ax=ax, lw=4, color='green')
pitch.lines(xstart=34.5, xend=34.5, ystart=68, yend=54, ax=ax, lw=4, color='green')
pitch.lines(xstart=70.5, xend=70.5, ystart=0, yend=13.8, ax=ax, lw=4, color='green')
pitch.lines(xstart=70.5, xend=70.5, ystart=68, yend=54, ax=ax, lw=4, color='green')
pitch.lines(xstart=52.5, xend=52.5, ystart=0, yend=68, ax=ax, lw=4, color='green')

pitch.annotate('1', (8.25, 60), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('2', (8.25, 33), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('3', (8.25, 6), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('4', (25.5, 60), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('5', (44, 60), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('6', (34.5, 47), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('7', (34.5, 33), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('8', (34.5, 18), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('9', (25.5, 6), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('10', (44, 6), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('11', (61.5, 60), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('12', (79.5, 60), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('13', (70.5, 47), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('14', (70.5, 33), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('15', (70.5, 18), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('16', (61.5, 6), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('17', (79.5, 6), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('18', (96.5, 60), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('19', (96.5, 33), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')
pitch.annotate('20', (96.5, 6), ax=ax, c='green', fontweight='bold', fontsize=30, ha='center')


plt.title('Positional 20 zone layout or Juego de Posición', color='white', fontweight='bold', fontsize=30)

plt.show()
