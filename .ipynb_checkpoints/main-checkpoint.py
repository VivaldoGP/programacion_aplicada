import pandas as pd
import matplotlib.pyplot as plt

def make_graph(countries, data, index):


    df = pd.read_csv(data)

    if type(countries) == list:
        print(df[df[index].isin(countries)])

        fig, ax = plt.subplots(figsize=(10,10))
    elif type(countries) == str:
        print("uno SOLO")

