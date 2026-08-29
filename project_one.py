import pandas as pd
import numpy as np

def do_stuff():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]
    }
    df = pd.DataFrame(data)
    
    # Perform some operations
    df['D'] = df['A'] + df['B']
    df['E'] = np.log(df['C'])


    
    return print("yes i am done")


if __name__ == "__main__":
    do_stuff()