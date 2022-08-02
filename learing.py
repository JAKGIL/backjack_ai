import numpy as np 
import pandas as pd


weights_and_baias = pd.read_csv("w_and_b.csv")

print(weights_and_baias)

weigths = weights_and_baias["weight"].values

weights_and_baias.to_csv("data.csv", index=0)

print(weigths)

data_dict = {
            'Distance': [0], # Distance to nearest Snake tail 
            'Score': [0],
            "Rotation" : [0]# Rotatnion (in angles) of Snake head
          }

df = pd.DataFrame(data_dict)

df["Distance"][0] = 13
df.loc[1] = [0,0,0] 

print(df)