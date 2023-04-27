import pandas as pd
import numpy as np
from pandas import Series,DataFrame  #两种数据结构，类似于键值对和C#的DataTable

def main1():
	points = pd.Series([5,9,-3,14,44,32]);
	print(points);
	print(pd.isnull(points));
	
	data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
			'year': [2000, 2001, 2002, 2001, 2002, 2003],
			'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]};
	frame = pd.DataFrame(data);
	print(frame);
	print(frame.year);

# 测试pandas的分组能力
def main2():
	df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
		'key2' : ['one', 'two', 'one', 'two', 'one'],
		'data1' : np.random.randn(5),
		'data2' : np.random.randn(5)})
	grouped = df['data1'].groupby(df['key1'])
	print(grouped.mean())
	print(df.groupby('key1').mean())
	print(df.groupby(['key1','key2']).mean())
	
	for name,group in df.groupby('key1'):  #迭代 GroupBy 对象
		print(name)
		print(group)
	
if __name__ == '__main__':
	main2();