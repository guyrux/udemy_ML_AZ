# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:02:07 2019

@author: user
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
from plotting import (multiple_histograms_plot,
                      bar_plot_with_categorical,
                      plot_confusion_matrix,
                      plot_roc)
from bokeh.plotting import figure
from bokeh.io import show, output_notebook
from data_prep import data_prep as dp
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

#pd.set_option('display.max_columns', None)  
#pd.set_option('display.max_colwidth', -1)
#pd.set_option('display.max_rows', 500)

nomeDaBase = "../bases/credit-data.csv"
df = pd.read_csv(nomeDaBase, encoding="utf-8")

imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)