import pandas as pd
s=pd.Series([1,2,3,4,5,None])
print(s.median())
print(
    None or True,
    None or False,
    #None == None,
    None is None,
    #None + 1,
    #type(None),
    sep="\n"
)