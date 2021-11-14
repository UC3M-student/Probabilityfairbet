import pandas as pd
import numpy as np

def variables (file):
    df = pd.read_excel(file)
    matrix = np.array([[0,0],[0,0]])
    size = len(df)
    results = df.iloc[0:size,7]
    n = 0
     
    try:
        while n < size: 
            n += 1
            t = n - 1
            if results[n] == "W" and results[t] == "L":
                a = np.array([[0,1],[0,0]])
                matrix = matrix + a
            elif results[n] == "L" and results[t] == "W":
                b = np.array([[0,0],[1,0]])
                matrix = matrix + b
            elif results[n] == results[t] == "W":
                c = np.array([[1,0],[0,0]])
                matrix = matrix + c
            elif results[n] == results[t] == "L":
                d = np.array([[0,0],[0,1]])
                matrix = matrix + d
            else:
                continue 
    except KeyError:
        print("value error")
    
    return matrix
        
    
first = variables("D:\VSCODE projects\Golden State Warriors\Excell data\Wolden State Warriors.xls")
print(first) 
