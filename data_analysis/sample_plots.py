# ****************************************************************************
# Sample Plots
# Examples of plots using Python libraries
#
# File: sample_plots.py
# Author: Haley Kong
# Email: haley.kong15@gmail.com
# Date: July 04, 2024
# License: MIT License
#
# Copyright (c) 2024, Haley Kong
#
# Version History
# ---------------
# 04-07-2024 Initial Version
#
# *****************************************************************************
""" One-line Description:

"""
# Standard imports


# 3rd Party package imports
from matplotlib import pyplot as plt
import numpy as np

# Local imports

# -----------------------------------------------------------------------------
# CONSTANTS

# -----------------------------------------------------------------------------
# CLASSES

# -----------------------------------------------------------------------------
# FUNCTIONS

# -----------------------------------------------------------------------------

n = np.arange(1, 100)
f = np.sqrt((n ** 2) + (3 * n ** 3)) * (np.log(n) ** (np.log(n)))
g = n

fh, ax = plt.subplots(figsize=(12, 12))
ax.plot(n, f, label="Function I am trying to bound: log(n)**log(n)")
ax.plot(n, g, label="Is it a lower bound? n")
ax.set_xlabel("n")
ax.set_ylabel("Value")
ax.grid()
ax.legend()
plt.show()
