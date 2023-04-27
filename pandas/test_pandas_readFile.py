import pandas as pd

pf = pd.read_csv(r'examples\ex1.csv');
print(pf);
bi = pd.read_pickle('textbinary');
print(bi);
