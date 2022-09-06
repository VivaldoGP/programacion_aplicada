import random
import pandas as pd
import matplotlib.pyplot as plt


def millions(x, pos):
    return '{:1.1f}M'.format(x*1e-6)


def plot_graph(data, year, identifier= "Country Code"):

    fig, ax = plt.subplots(figsize=(10,10))
    ax.yaxis.set_major_formatter(millions)
    ax.set_title("Población total")
    ax.set_xlabel("País")
    ax.set_ylabel("Millones de personas")
    ax.grid()
    ax.bar(x= data[identifier], height=data[year])
    plt.show()





def countries_data(raw_data, identifier="Country Code", countries_list=None, number_of_elements= 7):

    df = pd.read_csv(raw_data)

    filter = str(input("L for a given list of countries, R for random choice of countries: "))

    if filter == "L":
        new_df = df[df[identifier].isin(countries_list)]
        #print(new_df)
    elif filter == "R":
        options = df[identifier].tolist()
        selected = random.sample(options, number_of_elements)
        new_df = df[df[identifier].isin(selected)]
        print(selected)
        #print(new_df)
    else:
        print("Try again")
    
    return new_df