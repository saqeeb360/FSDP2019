# -*- coding: utf-8 -*-
"""
created on date

This is a temporary script file.
"""
from random import shuffle
import matplotlib.pyplot as plt
import numpy as np

slices = [1,2,3] * 4 + [20, 25, 30] * 2
shuffle(slices)

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

cmap = plt.cm.prism
colors = cmap(np.linspace(0., 1., len(slices)))

labels = ["Some text"] * len(slices)

ax.pie(slices, colors=colors, labels=labels, labeldistance=1.05)
ax.set_title("Figure 1")

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

pie_wedge_collection = ax.pie(slices, colors=colors, labels=labels, labeldistance=1.05);

for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')

ax.set_title("Figure 2")

slices = sorted(slices)

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

pie_wedge_collection = ax.pie(slices, colors=colors, labels=labels, labeldistance=1.05);

for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')

ax.set_title("Figure 3")

large = slices[0:int(len(slices) / 2)]
small = slices[int(len(slices) / 2):]

reordered = large[::2] + small[::2] + large[1::2] + small[1::2]

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

pie_wedge_collection = ax.pie(reordered, colors=colors, labels=labels, labeldistance=1.05);

for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')

ax.set_title("Figure 4")

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

angle = 180 + float(sum(small[::2])) / sum(reordered) * 360

pie_wedge_collection = ax.pie(reordered, colors=colors, labels=labels, labeldistance=1.05, startangle=angle);

for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')

ax.set_title("Figure 5")



