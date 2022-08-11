import numpy as np
import pandas as pd
import os
from calendar import monthrange

def RunCircuit(logisim_jar  : str, circuit : str):
    """
    This function runs the logisim simulator and returns the output of the circuit as
    a  pandas dataframe.
    """
    output=os.popen(f"java -jar {logisim_jar} {circuit} -tty table").read()
    output=[o.split() for o in output.split("\n")[:-1]]
    return pd.DataFrame(output[1:],columns=output[0])

def checkQ2(truth_table:pd.DataFrame)->bool:
    """
    This function checks the output of the circuit for the truth table and returns 
    weather the output is correct or not.
    """
    #convert hex to binary
    truth_table['i']=truth_table['i'].apply(lambda x: f'{int(x,16):0>8b}')
    for i,row in truth_table.iterrows():
        c=int(row.C,2)
        i=row.i 
        a=row.a
        #calculate a expected
        a_expected=i[c*2:c*2+2]
        #check if a is equal to a_expected
        if a!=a_expected:
            print("error!")
            print(f"at c={row.C}")
            print(f"expected a={a_expected}")
            print(f"got a={a}")
            print(f"i={row.i}")
            return False
    return True

if __name__=="__main__":
    truth_table=RunCircuit("../logisim-evolution.jar","logisim/FinalQ3.circ")
    if checkQ2(truth_table):
        print("Q2 passed!")