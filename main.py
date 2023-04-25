import pandas as pd
mydata=pd.read_csv("nato_phonetic_alphabet.csv")
Code_dict={r["letter"]:r["code"] for i,r in mydata.iterrows()}

print(Code_dict)

name="Sasha"



NATO_mynamecode=[Code_dict.get(str.upper()) for str in name]

print(NATO_mynamecode)