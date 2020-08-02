#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:09:24 2020

@author: kareem
"""

import strawberryfields as sf
from strawberryfields.ops import *

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


print(sf.hbar)
prog = sf.Program(1)

weight = np.load('./downloads/weights_per_epoch.npy')[363]

def layer(v):

    Rgate(v[0]) | q[0]
    Sgate(v[1]) | q[0]
    Rgate(v[2]) | q[0]
    Dgate(v[3]) | q[0]
    Kgate(v[4]) | q[0]

# sf.hbar = 2
# with prog.context as q:
#     Sgate(r=0.8) | q[0]
#     Dgate(a=-1.)| q[0]
# #    DisplacedSqueezed(alpha=-0.5,r=0.7)
# #    for x in weight:
#  #       layer(x)
# sf.hbar = 2
# eng = sf.Engine('fock',backend_options={'cutoff_dim':18})
# state = eng.run(prog).state
# prog.draw_circuit()

# X = np.linspace(-7.5, 7.5, 350)
# P = np.linspace(-7.5, 7.5, 350)
# Z = state.wigner(0, X, P)
# X, P = np.meshgrid(X, P)


# fig = plt.figure()
# ax = fig.add_subplot(2,1,1, projection="3d")

# surf = ax.plot_surface(X, P, Z, cmap='RdYlBu')
# fig.colorbar(surf)
# #ax.plot_surface(X, P, Z, cmap="RdYlBu", lw=0.5, rstride=1, cstride=1)
# #fig.set_size_inches(4.8, 5)
# ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
# ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
# ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
# # make the grid lines transparent
# ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,1)
# ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,1)
# ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,1)

# ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

# # Get rid of the spines
# ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
# ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
# ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

# # Get rid of the ticks
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])


# # ax.set_zlabel('Z')
# ax.set_xlabel('X')
# ax.set_ylabel('P')

# # ax.set_axis_off()
# plt.gca().axes.get_yaxis().set_visible(False)


prog = sf.Program(1)
with prog.context as q:
    Sgate(r=0.8) | q[0]
    Dgate(a=-1.)| q[0]
#    DisplacedSqueezed(alpha=-0.5,r=0.7)
    for x in weight:
        layer(x)
sf.hbar = 2
eng = sf.Engine('fock',backend_options={'cutoff_dim':18})
state = eng.run(prog).state

# # fig = plt.figure()
# X = np.linspace(-7.5, 7.5, 350)
# P = np.linspace(-7.5, 7.5, 350)
# Z = state.wigner(0, X, P)
# X, P = np.meshgrid(X, P)



# ax = fig.add_subplot(2,1,2, projection="3d")

# surf = ax.plot_surface(X, P, Z, cmap='RdYlBu')
# fig.colorbar(surf)
# ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# # make the grid lines transparent
# ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
# ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
# ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)

# ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

# # Get rid of the spines
# ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
# ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
# ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

# # Get rid of the ticks
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])


# # ax.set_zlabel('Z')
# ax.set_xlabel('X')
# ax.set_ylabel('P')
# #ax.plot_surface(X, P, Z, cmap="RdYlBu", lw=0.5, rstride=1, cstride=1)
# #fig.set_size_inches(4.8, 5)
# # ax.set_axis_off()
