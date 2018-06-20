import pandas as pd
from pandas import Series,DataFrame  #两种数据结构，类似于键值对和C#的DataTable

points = pd.Series([5,9,-3,14,44,32]);
print(points);
print(pd.isnull(points));

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]};
frame = pd.DataFrame(data);
print(frame);
print(frame.year);