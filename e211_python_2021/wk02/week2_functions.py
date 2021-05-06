# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
from matplotlib import pyplot as plt


def show_earthquake_data():
    df = pd.read_csv("EQCanOB_20190907_2020_0906.txt", sep="|")
    pd.options.display.max_columns = None
    display(df)


