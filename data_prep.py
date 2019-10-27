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
        """
         responsável: suto
         data: 04/05/19
         objetivo: essa função retorna uma tupla com:
                 (1) contendo uma pd.series com os atributos com maior proporção de nulos; e
                 (2) uma string indicando quantos atributos estão com uma proporção de nulos acima do corte dado.
         argumentos: são necessários 2 argumentos:
                 (1) dataframe df - base que se deseja verificar quantos nulos têm; e
                 (2) float corte - número entre 0 e 100 para indicar o valor mínimo da proporção de nulos. 
        """
        serie = (df.isnull().sum().sort_values(ascending=False)/len(df))*100
        return (serie[serie > corte], ("-> {} atributos/features/campos possuem mais de {}% de valores nulos.".
                format(len(serie[serie > corte]),corte)))
    
    def cardinalidade(df):
        """
        responsável: suto
        data: 27/10/19
        objetivo:   essa função retorna um dataframe com os atributos não
                    numéricos e sua respectiva cardinalidade em ordem crescente. 
        argumentos: somente 01 (um) argumento, o DataFrame que se deseja
                    analisar.
        """
        import pandas as pd
        
        df_temporario = df.select_dtypes(exclude=["int64", "float64"])

        matriz_cardialidade = []

        for i, coluna in df_temporario.items():
            matriz_cardialidade.append([i, len(df_temporario[i].unique()), df_temporario[i].unique()])
            
        matriz_cardialidade = pd.DataFrame(matriz_cardialidade, columns=["Atributo", "Cardinalidade", "Valores"])
        matriz_cardialidade.sort_values(by="Cardinalidade", inplace=True, ascending=True)
        
        return matriz_cardialidade
    
    def cardinalidadeComDescricao(df):
        """
        responsável: suto
        data: 27/10/19
        objetivo: essa função retorna dois dataframes.
            (1) O primeiro com a descrição dos atributos numéricos (int ou
            float); e
            (2) O segundo com os atributos não numéricos e sua respectiva
            cardinalidade em ordem crescente. 
        argumentos: somente 01 (um) argumento, o DataFrame que se deseja
                    analisar.
        """
        import pandas as pd
        
        df_temporario = df.select_dtypes(exclude=["int64", "float64"])

        matriz_cardialidade = []

        for i, coluna in df_temporario.items():
            matriz_cardialidade.append([i, len(df_temporario[i].unique())])
            
        matriz_cardialidade = pd.DataFrame(matriz_cardialidade, columns=["Atributo", "Cardinalidade"])
        matriz_cardialidade.sort_values(by="Cardinalidade", inplace=True, ascending=True)
        
        return matriz_cardialidade.T, df.describe()