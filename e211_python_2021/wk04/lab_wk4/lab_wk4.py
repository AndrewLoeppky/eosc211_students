# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Lab Week 4
#
# ## EOSC 211
#
# ### Learning Objectives:
#
# 1. Do math with python! 
#
# 2. Write structured code following input-process-output format\
#
# 3. Develop code with the scaffolding technique (source: HTTLACS?)
#
# 4. More plots!
#
#
# ### Intro
#
#
# ### Themes
#
# computer math + - * / **
#
# logical operators > < == !=
#
# ```and``` and ```or```
#
# order of operations

# %%
from e211_lib import e211
import numpy as np
from matplotlib import pyplot as plt 

# %% [markdown]
# What does this do?

# %%
z = 2
x = round(np.exp(np.sqrt(z / 3)))

# %% [markdown]
# ### Clausius-Clapeyron equation and the atmospheric equation of state
#
# Over large spatial scales in the atmosphere (and ocean) we can attempt to predict the winds (or currents) by looking at spatial changes in the DENSITY. In air the density is a function of pressure, temperature, and the amount of water
# vapour present - i.e.  the THERMODYNAMIC STATE*. Moist air is less dense than dry air, because H$_2$O gas is lighter than either N$_2$ or O$_2$ gas (which makes up most of the atmosphere). We often hear water vapour measurements given as a RELATIVE HUMIDITY (RH) which is the the ratio of the vapor pressure relative to the SATURATION LEVEL for a particular temperature.  The saturation level is the maximum amount of water vapour that air can hold in equilibrium (say, inside a closed bottle containing air and water, which you let sit for a long time).  A RH of 100% means it is foggy (saturated) and 0% means you are coughing and generating sparks every time you walk across a carpet! How do we get from RH to density?
#
# First, define the following quantities:
#
#
# | Symbol      | Variable  | SI Units   |
# |:-------------|:-----------|:------------|
# | $\rho$  | Density       | $kg/m^3$   |
# | $P$     | Pressure      | $Pa$   |
# | $T$     | Temperature   | $K$ |
# | $RH$    | Relative Humidity | $\%$ |
# | $r$     | Mixing Ratio  | $\frac{kg \space water \space vapor}{kg \space dry \space air}$|
# | $e$     | Vapor Pressure | $Pa$   |
# | $e_s$   | Saturation Vapor Pressure |
#
