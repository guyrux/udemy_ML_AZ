# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:36:39 2019

@author: user
"""
class data_prep():
    def breveDescricao(df):
        df.dropna(axis=1, how="all", inplace=True)
    
        print("O data set possui: \n- {} atributos/campos; e \n- {} registros.\n".
          format(df.shape[1], df.shape[0]))
        df.info()
    
    def serieNulos(df, corte = 50):
    #     Responsável: Suto
    #     Data: 04/05/19
    #     Objetivo: Essa função retorna uma tupla com:
    #             (1) contendo uma pd.Series com os atributos com maior proporção de nulos; e
    #             (2) uma string indicando quantos atributos estão com uma proporção de nulos acima do corte dado.
    #     Argumentos: São necessários 2 argumentos:
    #             (1) dataframe df - base que se deseja verificar quantos nulos têm; e
    #             (2) float corte - número entre 0 e 100 para indicar o valor mínimo da proporção de nulos. 
        
        serie = (df.isnull().sum().sort_values(ascending=False)/len(df))*100
    #     print("-> {} atributos/features/campos possuem mais de {}% de valores nulos.\n".
    #       format(len(serie[serie > corte]),corte))
        return (serie[serie > corte], ("-> {} atributos/features/campos possuem mais de {}% de valores nulos.".
                                              format(len(serie[serie > corte]),corte)))