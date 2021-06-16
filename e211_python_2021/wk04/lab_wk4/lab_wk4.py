# -*- coding: utf-8 -*-
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

# %%

# %% [markdown]
# What does this do?

# %%
z = 2
x = round(np.exp(np.sqrt(z / 3)))

# %% [markdown]
# ### Demo: S

# %%

# %% [markdown]
# ### Clausius-Clapeyron equation and the atmospheric equation of state
#
# Over large spatial scales in the atmosphere (and ocean) we can attempt to predict the winds (or currents) by looking at spatial changes in the DENSITY. In air the density is a function of pressure, temperature, and the amount of water
# vapour present - i.e.  the THERMODYNAMIC STATE*. Moist air is less dense than dry air, because H$_2$O gas is lighter than either N$_2$ or O$_2$ gas (which makes up most of the atmosphere). We often hear water vapour measurements given as a RELATIVE HUMIDITY (RH) which is the the ratio of the vapor pressure relative to the SATURATION LEVEL for a particular temperature.  The saturation level is the maximum amount of water vapour that air can hold in equilibrium (say, inside a closed bottle containing air and water, which you let sit for a long time).  A RH of 100% means it is foggy (saturated) and 0% means you are coughing and generating sparks every time you walk across a carpet! How do we get from RH to density?
#
# First, define the following quantities:
#
#
# | Symbol  | Variable      | SI Units   |
# |:--------|:--------------|:------------|
# | $\rho$  | Density       | $kg/m^3$   |
# | $P$     | Pressure      | $Pa$   |
# | $T$     | Temperature   | $K$ |
# | $RH$    | Relative Humidity | $\%$ |
# | $r$     | Mixing Ratio  | $\frac{kg \space water \space vapor}{kg \space dry \space air}$|
# | $e$     | Vapor Pressure | $Pa$   |
# | $e_s$   | Saturation Vapor Pressure | $Pa$ |
#
# Now,  it  would  be  nice  to  have  (say)  a  single,  perhaps  complicated, equation of state for density (as oceanographers do), but in fact atmospheric scientists define things using a chain of temporary variables†. It all begins with the CLAUSIUS-CLAPEYRON equation which relates the temperature andthe saturation vapour pressure:
#
# $$
# e_s = e_0\cdot exp \left[ \frac{L}{R_v}\frac{1}{T_0}-\frac{1}{T}\right]\tag{Clausius-Clapeyron Eqn}
# $$
#
# where $e_0 = 611Pa$, $L= 2.5\cdot10^6J/kg$ is the latent heat of evaporation, $T_0= 273K$ is a constant (NOT $273.15K$), and $R_v= 461J/K/kg$ (Joules per kelvin per kilogram) is the gas constant for pure water vapour. Next we have
#
# $$
# e = e_s\frac{RH}{100}
# $$
#
# and then 
#
# $$
# r = \frac{\varepsilon e}{P - e}
# $$
#
# where $\varepsilon= 0.622\frac{kg_{vapour}}{kg_{dry\space air}} \space (=R_d/R_v)$, and finally
#
# $$
# \rho = \frac{P}{R_dT(1 + 0.61r)}
# $$
#
# where $R_d = 287J/K/kg$ is  the  ideal  gas  constant  for  dry  air.‡ To  check  units,  remember  that  $1\space Pa  =1\space kg/m/s^2$, and $1\space J=1\space kg m^2/s^2$.
#
# ---
# ---
# \* For oceanographers, density is a function of pressure, temperature, and salinity, and for geologists the density of (say) molten rock willdepend on pressure, temperature, and its chemical composition. For this lab you just have to know that thereareequations to figure out!
#
# † See *Meteorology Today for Scientists and Engineers*, R. Stull
#
# ‡ You may recognize some similarity between this last equation and the IDEAL GAS LAW $P V=nRT$ which is no coincidence - in fact the $0.61r$ is a correction for the non-ideal nature of moist air.

# %% [markdown]
# ### Implementing the CC Equation in Python
#
# #### Four important points about programming style:
#
# * Be very careful with unit conversion.  Humans usually like to express temperature in Celsius, but the thermodynamic equations require temperatures in Kelvin.  That means that you need to distinguish between two temperatures with names like `Tk` and `Tc`, where `Tk = Tc + 273.15`. Make sure that you convert to Kelvin as soon as you can. Do it only once at the start and (if necessary for output) once at the end.
#
# * Choose good variable names. Don’t use single letters like `T`, `e` and `P` for variable names in a script. It makes it very hard to do search and replace with your editor when you want to change them, and the names aren’t very meaningful to others who might read your code. Also remember that Python is *case sensitive* so `P` and `p` are two different variables.
#
# * Just like the week 3 lab, we will endeavor to keep our code organized and readable. As much as you can, separate your script into 4 parts IN THIS ORDER:
#
# **1.  INPUTS:**  These  are  variables  whose  values  you  might  want  to  change  if  you  run  the  programmultiple times.
#
# **2.  INTERNAL DEFINITIONS or CONSTANTS:** These are variables that are defined as constantswhich you will never change, or some simple conversions (e.g. Celcius to Kelvin)
#
# **3.  CALCULATIONS:** This is where the complicated parts of the procedure go
#
# **4.  the OUTPUTS:** What you do once the math is finished (e.g. plotting).
#
# Also, It is useful to separate the parts by white space, and liberally comment your code. Note that not all tasks in 2 and 3 are easily separated, and sometimes plotting happens earlier than the end of the program, but it’s a good idea to always approach problems this way initially.

# %%
