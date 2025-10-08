import pandas as pd



def get_local_mapping_data(index):
    x_list = [3000, 4000, 5000]
    y_list = [500, 1000, 1500, 2000, 2500]
    y_list = [index * i for i in y_list]
    return x_list, y_list

def get_remote_mapping_data(index1, index2):
    df_happy = pd.read_csv("data/happy.csv")
    match index1:
        case 'Happiness':
            x_array = df_happy['happiness']
        case 'Generosity':
            x_array = df_happy['generosity']
        case 'GDP':
            x_array = df_happy['gdp']

    match index2:
        case 'Happiness':
            y_array = df_happy['happiness']
        case 'Generosity':
            y_array = df_happy['generosity']
        case 'GDP':
            y_array = df_happy['gdp']
    print(f"x_array {x_array}")
    print(f"y_array {y_array}")
    return x_array, y_array




