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

def Check_Hw1Q7(truth_table:pd.DataFrame)->bool:
    """
    This function checks the output of the circuit for the truth table and returns 
    weather the output is correct or not.
    """
    for i,row in truth_table.iterrows():
        month=int(row.M,2)
        if month in  range(1,13):
            if  bool(int(row.Y))!=(monthrange(2022, month)[1]==31):
                return False
    return True

def Check_Hw2Q3(truth_table:pd.DataFrame)->bool:
    """
    This function checks the output of the circuit for the truth table and returns 
    weather the output is correct or not.
    """
    for i,row in truth_table.iterrows():
        A=row.A
        X=[int(row[f"X{i}"],16) for i in range(4)]
        i=int(A[:2],2)
        val=2**int(A[2:],2)
        for j in range(4):
            if j!=i:
                if X[j]!=0:
                    return False
        if X[i]!=val:
            return False
    return True

def Check_Hw2Q4(truth_table:pd.DataFrame)->bool:
    """
    This function checks the output of the circuit for the truth table and returns 
    weather the output is correct or not.
    """
    for i,row in truth_table.iterrows():
        if np.median([int(row[c],2) for c in ["A","B","C"]])!=int(row.M,2):
            return False
    return True

def Check_Hw2Q5(truth_table:pd.DataFrame)->bool:
    """
    This function checks the output of the circuit for the truth table and returns 
    weather the output is correct or not.
    """
    for i,row in truth_table.iterrows():
        P=int(row.P,2)
        K=int(row.K,2)
        C=int(row.C,2)
        if P<26 and K<26:
            if C!=(P+K)%26:
                print()
                print(f"P={P}")
                print(f"K={K}")
                print(f"C={C}")
                print(f"expected C={(P+K)%26}")
                return False
    return True

def Check_Hw2Q6(truth_table:pd.DataFrame)->bool:
    """
    This function checks the output of the circuit for the truth table and returns 
    weather the output is correct or not.
    """
    for i,row in truth_table.iterrows():
        D1=int(row.D1,2)
        D0=int(row.D0,2)
        Z=int(row.Z,16)
        if D1<10 and D0<10:
            if Z!=D1*10+D0:
                print("Z=",Z)
                print("D1=",D1)
                print("D0=",D0)
                return False
    return True


if __name__=="__main__":
    logisim_jar="../logisim-evolution.jar"

    #check HW1Q7
    circuit="Logisim/HW1Q7.circ"
    print("Checking HW1Q7...",end="")
    truth_table=RunCircuit(logisim_jar,circuit)
    if Check_Hw1Q7(truth_table):
        print("PASSED")
    else:
        print("FAILED")

    #check HW2Q3
    circuit="Logisim/HW2Q3.circ"
    print("Checking HW2Q3...",end="")
    truth_table=RunCircuit(logisim_jar,circuit)
    if Check_Hw2Q3(truth_table):
        print("PASSED")
    else:
        print("FAILED")

    #check HW2Q4
    circuit="Logisim/HW2Q4.circ"
    print("Checking HW2Q4...",end="")
    truth_table=RunCircuit(logisim_jar,circuit)
    if Check_Hw2Q4(truth_table):
        print("PASSED")
    else:
        print("FAILED")

    #check HW2Q5
    circuit="Logisim/HW2Q5.circ"
    print("Checking HW2Q5...",end="")
    truth_table=RunCircuit(logisim_jar,circuit)
    if Check_Hw2Q5(truth_table):
        print("PASSED")
    else:
        print("FAILED")
    
    #check HW2Q6
    circuit="Logisim/HW2Q6.circ"
    print("Checking HW2Q6...",end="")
    truth_table=RunCircuit(logisim_jar,circuit)
    if Check_Hw2Q6(truth_table):
        print("PASSED")
    else:
        print("FAILED")